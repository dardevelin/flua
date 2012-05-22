from PyQt4 import QtGui, QtCore, uic
from bp.Tools.IDE.Syntax.BPCSyntax import *
from bp.Tools.IDE.Threads import *
from bp.Compiler import *
import collections
#import yappi

# Auto Completion
class BPCAutoCompleterModel(QtGui.QStringListModel):
	
	def __init__(self, parent = None):
		self.shortCuts = dict()
		self.shortCutList = list(self.shortCuts)
		
		self.funcListLen = 0
		self.functionList = []
		self.keywordList = []
		
		super().__init__([], parent)
		self.keywordIcon = QtGui.QIcon("images/icons/autocomplete/keyword.png")
		self.functionIcon = QtGui.QIcon("images/icons/autocomplete/function.png")
		self.shortcutFunctionIcon = QtGui.QIcon("images/icons/autocomplete/shortcut-function.png")
		#self.index(0, 0).setData(QtCore.Qt.DecorationRole, self.icon)
		
	def setKeywordList(self, keywordList):
		self.keywordList = keywordList
		self.updateStringList()
		
	def setFunctionList(self, functionList, shortCuts):
		self.functionList = functionList
		self.funcListLen = len(functionList)
		
		self.shortCuts = shortCuts
		self.shortCutList = list(shortCuts)
		
		self.updateStringList()
		
	#def setShortCutDict(self, shortCuts):
	#	self.shortCuts = shortCuts
	#	self.shortCutList = list(shortCuts)
	#	self.updateStringList()
		
	def updateStringList(self):
		self.setStringList(self.keywordList + self.functionList + self.shortCutList)
		
	def data(self, index, role):
		if role == QtCore.Qt.DecorationRole:
			text = super().data(index, QtCore.Qt.DisplayRole)
			if text in self.keywordList:
				return self.keywordIcon
			elif text in self.shortCutList:
				return self.shortcutFunctionIcon
			elif text in self.functionList:
				return self.functionIcon
		
		# TODO: Auto completion for shortcuts
		if role == QtCore.Qt.DisplayRole:
			shortCut = super().data(index, role)
			if shortCut in self.shortCuts:
				fullCompletion = self.shortCuts[shortCut]
				return fullCompletion
			else:
				return shortCut
		
		return super().data(index, role)

class BPCAutoCompleter(QtGui.QCompleter):
	
	def __init__(self, parent = None):
		self.bpcModel = BPCAutoCompleterModel()
		QtGui.QCompleter.__init__(self, self.bpcModel, parent)

# Code Edit
class BPCodeEdit(QtGui.QPlainTextEdit, Benchmarkable):
	
	def __init__(self, bpIDE = None, parent = None):
		super().__init__(parent)
		
		self.threaded = True
		
		self.bpIDE = bpIDE
		currentTheme = self.bpIDE.getCurrentTheme()
		
		self.openingFile = False
		self.isTextFile = False
		self.hoveringFileName = ""
		self.updateQueue = collections.deque()
		self.qdoc = self.document()
		self.highlighter = BPCHighlighter(self.qdoc, self.bpIDE)
		self.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
		self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		self.setFont(self.bpIDE.config.monospaceFont)
		self.lastCompletionTime = 0
		self.autoCompleteOpenedAuto = True
		
		self.autoSuggestion = True
		self.autoSuggestionMinChars = 3
		self.autoSuggestionMinCompleteChars = 1
		
		#self.setCurrentCharFormat(self.bpIDE.config.theme["default"])
		
		#bgStyle = bpIDE.currentTheme["default-background"]
		#if bgStyle != "#ffffff":
		#	self.setStyleSheet("background-color: %s" % bgStyle);
		
		#p = self.palette()
		#p.setColor(QtGui.QPalette.Base, QtCore.Qt.red)
		#p.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
		#self.setPalette(p)
		#self.setTextColor(QtCore.QColor.white)
		
		self.autoIndentKeywords = {
			"if",
			"elif",
			"else",
			"try",
			"catch",
			"while",
			"for",
			"in",
			"switch",
			"case",
			"target",
			"extends",
			"pattern",
			"extern",
			"compilerflags",
			"template",
			"get",
			"set",
			"private",
			"operator",
			"to",
			"require",
			"ensure",
			"test",
			"parallel",
			
			# A dirty hack so that C++ gets some auto indent
			'inline',
			'case',
			'default',
		}
		
		self.qdoc.contentsChange.connect(self.onTextChange)
		self.lineNumberArea = None
		
		self.completer = None
		#self.completer.setWidget(self)
		
		#self.initLineNumberArea()
	
	def clear(self):
		self.doc = None
		self.root = None
		self.filePath = ""
		self.lines = []
		self.bpcFile = None
		
		self.disableUpdatesFlag = True
		self.updater = None
		super().clear()
		self.updater = BPCodeUpdater(self)
		self.disableUpdatesFlag = False
		
		self.timer = QtCore.QTimer(self)
		self.timer.timeout.connect(self.onUpdateTimeout)
		self.timer.start(self.bpIDE.config.updateInterval)
	
	#def setBackgroundColor(self, bgColor):
	#	p = self.palette()
	#	p.setColor(QtGui.QPalette.Base, bgColor)
	#	p.setColor(QtGui.QPalette.Window, bgColor)
	#	self.setPalette(p)
	#	self.setBackgroundVisible(True)
	
	def mousePressEvent(self, event):
		if self.bpIDE.ctrlPressed and self.hasMouseTracking() and self.hoveringFileName:
			
			# Create file if it doesn't exist
			if not os.path.exists(self.hoveringFileName):
				with open(self.hoveringFileName, "w") as out:
					out.write("\n")
			
			self.bpIDE.openFile(self.hoveringFileName)
			self.hoveringFileName = ""
			self.setMouseTracking(False)
		
		super().mousePressEvent(event)
	
	def mouseMoveEvent(self, event):
		self.hoveringFileName = ""
		
		if self.bpIDE.ctrlPressed:
			p = event.pos()
			cursor = self.cursorForPosition(p)
			block = cursor.block()
			text = block.text().strip()
			
			#cursor.movePosition(QtGui.QTextCursor.StartOfWord)
			#cursor.select(QtGui.QTextCursor.WordUnderCursor)
			
			if text.startswith("include "):
				self.hoveringFileName = extractDir(self.getFilePath()) + text[len("include "):]
			elif text.startswith("import "):
				importedMod = text[len("import "):]
				self.hoveringFileName = self.bpIDE.getModulePath(importedMod)
		
		super().mouseMoveEvent(event)
	
	def setFont(self, font):
		super().setFont(font)
		self.setTabWidth(self.bpIDE.config.tabWidth)
	
	def setTabWidth(self, value):
		if os.name == "nt":
			self.setTabStopWidth(value * self.fontMetrics().width("9"))
		else:
			self.setTabStopWidth(value * self.fontMetrics().maxWidth())
	
	def setCompleter(self, completer):
		signal = QtCore.SIGNAL("activated(const QString&)")
		
		if self.completer:
			self.disconnect(self.completer, signal, self.insertCompletion)
		
		if not completer:
			return
		
		completer.setWidget(self)
		self.completer = completer
		completer.disconnect(self.completer, signal, self.insertCompletion)
		self.connect(self.completer, signal, self.insertCompletion)
	
	def insertCompletion(self, completion):
		if self.bpIDE.codeEdit != self:
			return
		
		tc = self.textCursor()
		
		if completion in self.completer.bpcModel.shortCuts:
			#tc.movePosition(QtGui.QTextCursor.Left)
			tc.movePosition(QtGui.QTextCursor.StartOfWord)
			tc.select(QtGui.QTextCursor.WordUnderCursor)
			tc.removeSelectedText()
			tc.insertText(self.completer.bpcModel.shortCuts[completion])
		else:
			extra = (len(completion) - len(self.completer.completionPrefix()))
			tc.movePosition(QtGui.QTextCursor.EndOfWord)
			tc.insertText(completion[len(completion) - extra:])
			
		# Functions
		if completion in self.completer.bpcModel.functionList:
			beforeCompletion = tc.block().text()[:-len(completion)]
			functionHasParameters = False
			if beforeCompletion.isspace() or not beforeCompletion and functionHasParameters:
				tc.insertText(" ")
			else:
				tc.insertText("()")
				tc.movePosition(QtGui.QTextCursor.Left)
		# Expr blocks
		#elif completion in xmlToBPCExprBlock.keys() or completion in xmlToBPCSingleLineExpr.values():
		#	pass#tc.insertText(" ")
		# Blocks
		elif completion in xmlToBPCBlock.values():
			tc.insertText("\n" + ("\t" * (countTabs(tc.block().text()) + 1)))
			
		self.lastCompletionTime = time.time()
		self.setTextCursor(tc)
	
	def textUnderCursor(self):
		tc = self.textCursor()
		tc.select(QtGui.QTextCursor.WordUnderCursor)
		return tc.selectedText()

	def focusInEvent(self, event):
		if self.completer:
			self.completer.setWidget(self)
		QtGui.QPlainTextEdit.focusInEvent(self, event)
	
	def getImportedModulesByCode(self):
		importedMods = []
		lines = self.toPlainText().split("\n")
		for line in lines:
			line = line.strip()
			if line.startswith("import") and len(line) >= 8 and line[6].isspace():
				mod = line[7:].strip()
				if mod:
					importedMods.append(mod)
		return importedMods
	
	def keyReleaseEvent(self, event):
		#if event.modifiers() & QtCore.Qt.ControlModifier:
		if self.bpIDE.ctrlPressed and self.hasMouseTracking():
			self.setMouseTracking(False)
		
		self.bpIDE.ctrlPressed = False
		super().keyReleaseEvent(event)
	
	def focusInEvent(self, event):
		# To fix switching workspaces on GNOME/KDE
		self.bpIDE.ctrlPressed = False
		super().focusInEvent(event)
	
	def keyPressEvent(self, event, dontAutoComplete = False):
		if self.bpIDE.codeEdit is None:
			return
		
		# Auto Complete
		isShortcut = (event.modifiers() == QtCore.Qt.ControlModifier and event.key() == QtCore.Qt.Key_Space)
		
		# Ctrl + Mouse click
		if event.modifiers() == QtCore.Qt.ControlModifier:
			self.bpIDE.ctrlPressed = True
			self.setMouseTracking(True)
		
		# Auto Complete
		if (not dontAutoComplete) and self.completer and self.bpIDE.codeEdit == self and (isShortcut or self.completer.popup().isVisible() or self.autoSuggestion):
			if self.completer.popup().isVisible() and event.key() in (
					QtCore.Qt.Key_Enter,
					QtCore.Qt.Key_Return,
					QtCore.Qt.Key_Escape,
					QtCore.Qt.Key_Tab,
					QtCore.Qt.Key_Backtab):
				event.ignore()
				return
			
			# Has ctrl + space been pressed?
			if (not self.completer or not isShortcut):
				self.keyPressEvent(event, True)

			## ctrl or shift key on it's own??
			ctrlOrShift = event.modifiers() in (QtCore.Qt.ControlModifier, QtCore.Qt.ShiftModifier)
			if ctrlOrShift and not event.text():
				# ctrl or shift key on it's own
				return
			
			eow = "~!@#$%^&*()_+{}|:\"<>?,./;'[]\\-=" #end of word
			
			hasModifier = ((event.modifiers() != QtCore.Qt.NoModifier) and not ctrlOrShift)
			
			completionPrefix = self.textUnderCursor()
			
			if (not isShortcut and (hasModifier or not event.text() or event.text()[-1] in eow)):
				self.completer.popup().hide()
				return
			
			popup = self.completer.popup()
			if (completionPrefix != self.completer.completionPrefix()):
				self.completer.setCompletionPrefix(completionPrefix)
				popup.setCurrentIndex(self.completer.completionModel().index(0, 0))
			
			if self.autoCompleteOpenedAuto:
				autoCompleteAintWorthIt = (
					len(completionPrefix) < self.autoSuggestionMinChars
					or
					(
						len(self.completer.currentCompletion()) - len(completionPrefix) < self.autoSuggestionMinCompleteChars
						and
						not completionPrefix in self.completer.bpcModel.shortCuts
					)
				)
				if (not isShortcut) and autoCompleteAintWorthIt:
					self.completer.popup().hide()
					return
			
			# Insert directly if it's just 1 possibility
			enableACInstant = True
			if enableACInstant and isShortcut:
				if self.completer.completionCount() == 1:
					self.insertCompletion(self.completer.currentCompletion())
					self.completer.popup().hide()
					return
			
			cr = self.cursorRect()
			cr.setWidth(self.completer.popup().sizeHintForColumn(0) + self.completer.popup().verticalScrollBar().sizeHint().width())
			
			if popup.isHidden():
				if isShortcut:
					self.autoCompleteOpenedAuto = False
				elif self.autoSuggestion:
					self.autoCompleteOpenedAuto = True
			else:
				if not completionPrefix:
					self.autoCompleteOpenedAuto = True
					popup.hide()
					return
			
			self.completer.complete(cr) ## pop it up!
			
			#if isShortcut:
			#	self.completer.popup().show()
		# Unindent
		elif event.key() == QtCore.Qt.Key_Backtab: # Seriously f*** *** whoever invented Backtab instead of shift modifier + tab
			self.unIndentSelection()
			
		# Disable wrong indentation
		elif event.key() == QtCore.Qt.Key_Tab:
			if self.textCursor().hasSelection():
				if event.modifiers() == QtCore.Qt.ShiftModifier:
					self.unIndentSelection()
				else:
					self.indentSelection()
			else:
				cursor = self.textCursor()
				pos = cursor.position()
				block = self.qdoc.findBlock(pos)
				prevBlock = block.previous()
				
				line = block.text()
				tabLevel = countTabs(line)
				prevLine = prevBlock.text()
				prevTabLevel = countTabs(prevLine)
				
				if not prevLine or tabLevel <= prevTabLevel or not line[:pos - block.position()].isspace():
					super().keyPressEvent(event)
		
		# Auto Indent
		elif event.key() == QtCore.Qt.Key_Return:
			cursor = self.textCursor()
			
			pos = cursor.position()
			block = self.qdoc.findBlock(pos)
			blockPos = block.position()
			lineInfo = block.userData()
			line = block.text()
			tabLevel = countTabs(line)
			
			isAtEndOfLine = (blockPos + len(line) == pos)
			
			nodeName = ""
			if lineInfo:
				node = lineInfo.node
				if node and node.nodeType != Node.TEXT_NODE:
					nodeName = node.tagName
			else:
				node = None
			
			# Retrieve the keyword from the line
			pureLine = line[tabLevel:]
			keyword = ""
			i = 0
			for c in pureLine:
				if not c.isalnum() and not c == '_' or i == (pos - blockPos):
					keyword = pureLine[:i]
					break
				i += 1
			
			# Whole line
			wasFullLine = False
			if not keyword:
				keyword = pureLine
				wasFullLine = True
			
			keywordStaysAfterNewline = (pos >= blockPos + len(keyword)) #isAtEndOfLine
			
			if keyword and keywordStaysAfterNewline and not keyword[0] == '#' and nodeName != "extern-function":
				# Indent it?
				if keyword in self.autoIndentKeywords:
					tabLevel += 1
				elif nodeName == "function" or nodeName == "class" or nodeName == "new":
					tabLevel += 1
				elif keyword == "init" and tabLevel == 1:
					tabLevel += 1
				#else:
				#	topLevelFuncExists = self.bpIDE.processor.getFirstDTreeByFunctionName(keyword)
				#	if not topLevelFuncExists:
				#		tabLevel += 1
					# isTopLevelFuncDefinition = (node is not None and node.parentNode.parentNode.tagName == "module")
					# isClassFunction = (self.updater is not None) and (self.updater.lastException is not None)
					# topLevelFuncExists = self.bpIDE.processor.getFirstDTreeByFunctionName(keyword)
					# if (
						# (wasFullLine or addBrackets(pureLine)[-1] == ')')
						# and tabLevel <= 1
						# and isAtEndOfLine
						# and line and line[-1] != ')'
						# and (isTopLevelFuncDefinition or isClassFunction)
						# and (not topLevelFuncExists) or (isClassFunction)
						# ):
						
					# TODO: Check whether parameters hold variable names only
					# If the parameters have numbers then this won't be a function definition
						# tabLevel += 1
					
			# Add the text
			cursor.beginEditBlock()
			cursor.insertText("\n" + "\t" * tabLevel)
			cursor.endEditBlock()
			
			event.accept()
		# TODO: Binary and ?
		#elif event.key() == QtCore.Qt.Key_Space and event.modifiers() == QtCore.Qt.ControlModifier:
		#	print("Yo!")
		else:
			super().keyPressEvent(event)
	
	def indentSelection(self):
		tab = "\t"
		tabLen = 1
		
		cursor = self.textCursor()
		cursor.beginEditBlock()
		
		# Previous selection
		selStart = cursor.selectionStart()
		selEnd = cursor.selectionEnd()
		cursor.setPosition(selEnd, QtGui.QTextCursor.MoveAnchor)
		blockEnd = cursor.blockNumber()
		
		# First block
		selStartBlockPosition = self.qdoc.findBlock(selStart).position()
		cursor.setPosition(selStartBlockPosition, QtGui.QTextCursor.MoveAnchor)
		cursor.insertText(tab)
		selEnd += tabLen
		
		# All selected blocks
		while cursor.blockNumber() < blockEnd:
			cursor.movePosition(QtGui.QTextCursor.NextBlock, QtGui.QTextCursor.MoveAnchor)
			cursor.movePosition(QtGui.QTextCursor.StartOfBlock, QtGui.QTextCursor.MoveAnchor)
			cursor.insertText(tab)
			selEnd += tabLen
		
		# Restore old selection
		cursor.setPosition(selStart + 1, QtGui.QTextCursor.MoveAnchor)
		cursor.setPosition(selEnd, QtGui.QTextCursor.KeepAnchor)
		
		cursor.endEditBlock()
		self.setTextCursor(cursor)
	
	def unIndentSelection(self):
		tab = "\t"
		tabLen = 1
		
		cursor = self.textCursor()
		cursor.beginEditBlock()
		
		selStart = cursor.selectionStart()
		selEnd = cursor.selectionEnd()
		
		selStartBlockPosition = self.qdoc.findBlock(selStart).position()
		
		cursor.setPosition(selEnd, QtGui.QTextCursor.MoveAnchor)
		blockEnd = cursor.blockNumber()
		
		# First block
		cursor.setPosition(selStartBlockPosition, QtGui.QTextCursor.MoveAnchor)
		line = cursor.block().text()
		if line and line[0].isspace():
			cursor.deleteChar()
			selStart -= tabLen
			selEnd -= tabLen
		
		# All selected blocks
		while cursor.blockNumber() < blockEnd:
			cursor.movePosition(QtGui.QTextCursor.NextBlock, QtGui.QTextCursor.MoveAnchor)
			cursor.movePosition(QtGui.QTextCursor.StartOfBlock, QtGui.QTextCursor.MoveAnchor)
			line = cursor.block().text()
			if line and line[0].isspace():
				cursor.deleteChar()
				selEnd -= tabLen
			
		# Restore old selection
		cursor.setPosition(selStart, QtGui.QTextCursor.MoveAnchor)
		cursor.setPosition(selEnd, QtGui.QTextCursor.KeepAnchor)
			
		cursor.endEditBlock()
		self.setTextCursor(cursor)
	
	def clearHighlights(self):
		self.setExtraSelections([])
	
	def getCurrentTheme(self):
		return self.bpIDE.getCurrentTheme()
	
	def rehighlightFunctionUsage(self):
		if self.isTextFile:
			return
		
		# TODO: Only highlight blocks where the function is used
		self.startBenchmark("[%s] Syntax Highlighter" % (stripDir(self.filePath)))
		self.highlighter.rehighlight()
		self.endBenchmark()
		
	def rehighlightCurrentLine(self):
		self.highlighter.rehighlightBlock(self.textCursor().block())
	
	def save(self, newPath = ""):
		oldPath = self.getFilePath()
		
		try:
			if newPath:
				if self.isTextFile:
					self.setFilePath(newPath)
				else:
					if not newPath.endswith(".bp"):
						newPath = stripExt(newPath) + ".bp"
					self.setFilePath(newPath)
					
					if oldPath != newPath and self.bpIDE.processor:
						self.bpIDE.processor.changeCompiledFilePath(oldPath, newPath)
			
			if self.isTextFile:
				with codecs.open(self.getFilePath(), "w", encoding="utf-8") as outStream:
					outStream.write(self.toPlainText())
			else:
				if self.bpcFile:
					self.bpcFile.writeToFS()
				else:
					raise "No bpc data"
			
			# Success
			self.qdoc.setModified(False)
			self.bpIDE.statusBar.showMessage("Saved " + self.getFilePath() + " successfully.", 1000)
		except:
			self.setFilePath(oldPath)
			self.bpIDE.statusBar.showMessage("Error saving " + newPath, 3000)
	
	def setFilePath(self, filePath):
		self.filePath = fixPath(filePath)
		if self.bpcFile:
			self.bpcFile.setFilePath(self.filePath)
		
	def getFilePath(self):
		return self.filePath
		
	#def setLineNode(self, index, newNode):
	#	block = self.qdoc.findBlockByNumber(index)
	#	
	#	oldNode = None
	#	oldData = block.userData()
	#	if oldData:
	#		oldNode = oldData.node
	#	
	#	block.setUserData(BPLineInformation(newNode, False, oldNode))
	
	# def setLineEdited(self, index, edited):
		# block = self.qdoc.findBlockByNumber(index)
		# lineInfo = block.userData()
		# if lineInfo:
			# block.setUserData(BPLineInformation(lineInfo.node, True, lineInfo.oldNode))
		
	def onTextChange(self, position, charsRemoved, charsAdded):
		# blockStart = self.qdoc.findBlock(position)
		# blockEnd = self.qdoc.findBlock(position + charsAdded)
		# for i in range(blockStart.blockNumber(), blockEnd.blockNumber() + 1):
			# #print("Update user data for line: " + str(block.text()))
			# self.setLineEdited(i, True)
		
		# Run bpc -> xml updater
		#print(self.disableUpdatesFlag)
		
		if self.updater and not self.disableUpdatesFlag:
			self.runUpdater()
		
	def runUpdater(self):
		if self.isTextFile:
			return
		
		self.updateQueue.append(1)
		if self.openingFile:
			self.onUpdateTimeout()
		
	def onUpdateTimeout(self):
		if self.isTextFile:
			return
		
		if self.updateQueue:
			self.updateQueue.clear()
			self.updater.setDocument(self.qdoc)
			
			if self.threaded:
				self.updater.start(QtCore.QThread.IdlePriority)
			else:
				self.updater.run()
				self.updater.finished.emit()
		
	def getLineIndex(self):
		return self.textCursor().blockNumber()
		
	def getLineNumber(self):
		return self.getLineIndex() + 1
		
	def getNodeByLineIndex(self, lineIndex):
		lineInfo = self.qdoc.findBlockByNumber(lineIndex).userData()
		
		if lineInfo:
			#if lineInfo.edited == False:
			return lineInfo.node
		
		return None
		
	def getOldNodeByLineIndex(self, lineIndex):
		lineInfo = self.qdoc.findBlockByNumber(lineIndex).userData()
		
		if lineInfo:
			#if lineInfo.edited == False:
			return lineInfo.oldNode
		
		return None
		
	def compilerFinished(self):
		del self.bpcFile
		self.bpcFile = self.updater.bpcFile
		self.updater.bpcFile = None
		
		#self.disableUpdatesFlag = True
		
		if self.bpcFile:
			self.doc = self.bpcFile.doc
			#self.bpIDE.startBenchmark("UpdateRootSafely")
			self.updateRootSafely()
			#self.bpIDE.endBenchmark()
			
			self.bpIDE.runPostProcessor(self)
		
		# Any work in the queue left?
		interval = self.updater.executionTime + self.bpIDE.config.updateInterval
		if self.updateQueue and abs(self.timer.interval() - interval) > 300:
			print("Setting new update interval: %d ms" % (interval))
			self.timer.setInterval(interval)
		
	def getCurrentLine(self):
		lineIndex = self.getLineIndex()
		return self.qdoc.findBlockByNumber(lineIndex).text()
		
	def updateRootSafely(self):
		lineIndex = -1 # -1 because of bp.Core
		for node in self.bpcFile.nodes:
			#print("[%d] %s" % (lineIndex, node))
			if lineIndex >= 0:
				block = self.qdoc.findBlockByNumber(lineIndex)
				
				oldNode = None
				oldData = block.userData()
				if oldData:
					oldNode = oldData.node
					# Meta data
					if oldNode:
						metaNode = getElementByTagName(oldNode, "meta")
						if metaNode and node:
							node.appendChild(metaNode)
					
					#oldData.oldNode = oldData.node
					#oldData.node = node
				#else:
				del oldData
				block.setUserData(BPLineInformation(node, False, oldNode))
				#self.setLineNode(lineIndex, node)
			lineIndex += 1
		
		del self.root
		self.root = self.bpcFile.root
		
		#del self.bpcFile.root
		#del self.bpcFile.doc
		#del self.bpcFile.nodeToOriginalLine
		#del self.bpcFile.nodes
		
	def setRoot(self, newRoot):
		self.root = newRoot
		#header = getElementByTagName(self.root, "header")
		codeNode = getElementByTagName(self.root, "code")
		
		converter = LineToNodeConverter()
		bpcCode = nodeToBPC(self.root, 0, converter).strip()
		self.lines = bpcCode.split("\n")
		
		# Set new text
		self.disableUpdatesFlag = True
		code = "\n".join(self.lines) + "\n"
		
		# Fixes a bug in QTextDocument for the modification state
		#if not code:
		#	code = "\n"
		
		self.setPlainText(code)
		
		# Set user data
		lineToNodeLen = len(converter.lineToNode)
		for i in range(len(self.lines)):
			if i < lineToNodeLen:
				userData = BPLineInformation(converter.lineToNode[i])
			else:
				userData = BPLineInformation()
			self.qdoc.findBlockByNumber(i).setUserData(userData)
		
		self.runUpdater()
		
	def setXML(self, xmlCode):
		self.disableUpdatesFlag = True
		
		self.doc = parseString(xmlCode.encode("utf-8"))
		
		self.setRoot(self.doc.documentElement)
		
	def goToLine(self, lineNum):
		cursor = self.textCursor()
		cursor.setPosition(self.qdoc.findBlockByLineNumber(max(lineNum - 1, 0)).position())
		self.setTextCursor(cursor)
		
	def goToLineEnd(self, lineNum):
		cursor = self.textCursor()
		block = self.qdoc.findBlockByLineNumber(lineNum - 1)
		cursor.setPosition(block.position() + len(block.text()))
		self.setTextCursor(cursor)
	
	# LineNumberArea functions
	
	def initLineNumberArea(self):
		self.lineNumberArea = LineNumberArea(self)
		
		self.blockCountChanged.connect(self.updateLineNumberAreaWidth)
		self.updateRequest.connect(self.updateLineNumberArea)
		self.cursorPositionChanged.connect(self.highlightCurrentLine)
		
		self.updateLineNumberAreaWidth(0)
		#self.highlightLine()
	
	def highlightLine(self, lineIndex = 0, lineColor = None):
		if not lineColor:
			lineColor = self.getCurrentTheme()["current-line"]
		
		if lineColor:
			extraSelections = []
			
			if(not self.isReadOnly()):
				selection = QtGui.QTextEdit.ExtraSelection()
				selection.format.setBackground(lineColor)
				selection.format.setProperty(QtGui.QTextFormat.FullWidthSelection, True)
				selection.cursor = self.textCursor()
				if lineIndex:
					selection.cursor.setPosition(self.qdoc.findBlockByLineNumber(lineIndex).position())
				selection.cursor.clearSelection()
				extraSelections.append(selection)
			
			self.setExtraSelections(extraSelections)
		
	def getLineNumberAreaWidth(self):
		digits = 1
		maxBlocks = max(1, self.blockCount())
		while maxBlocks >= 10:
			maxBlocks //= 10
			digits += 1
			
		space = 3 + self.fontMetrics().width('9') * digits
		return space
		
	def updateLineNumberArea(self, rect, dy):
		if dy:
			self.lineNumberArea.scroll(0, dy)
		else:
			self.lineNumberArea.update(0, rect.y(), self.lineNumberArea.width(), rect.height())
			
		if rect.contains(self.viewport().rect()):
			self.updateLineNumberAreaWidth(0)
		
	def updateLineNumberAreaWidth(self, newBlockCount):
		self.setViewportMargins(self.getLineNumberAreaWidth(), 0, 0, 0)
		
	def resizeEvent(self, event):
		super().resizeEvent(event)
		
		if self.lineNumberArea:
			cr = self.contentsRect()
			self.lineNumberArea.setGeometry(QtCore.QRect(cr.left(), cr.top(), self.getLineNumberAreaWidth(), cr.height()))
		
	def lineNumberAreaPaintEvent(self, event):
		painter = QtGui.QPainter(self.lineNumberArea)
		painter.fillRect(event.rect(), QtCore.Qt.lightGray)
		
		block = self.firstVisibleBlock()
		blockNumber = block.blockNumber()
		top = self.blockBoundingGeometry(block).translated(self.contentOffset()).top()
		bottom = top + self.blockBoundingRect(block).height()
		
		while block.isValid() and top <= event.rect().bottom():
			if block.isVisible() and bottom >= event.rect().top():
				number = str(blockNumber + 1)
				painter.setPen(QtCore.Qt.black)
				painter.drawText(0, top, self.lineNumberArea.width(), self.fontMetrics().height(), QtCore.Qt.AlignRight, number)
			
			block = block.next()
			top = bottom
			bottom = top + int(self.blockBoundingRect(block).height())
			blockNumber += 1

# Information stored per line
class BPLineInformation(QtGui.QTextBlockUserData):
	
	def __init__(self, xmlNode = None, edited = False, previousNode = None):
		super().__init__()
		self.node = xmlNode
		self.oldNode = previousNode
		self.edited = edited

# Useless line numbers
class LineNumberArea(QtGui.QWidget):
	
	def __init__(self, codeEdit):
		super().__init__(codeEdit)
		self.codeEdit = codeEdit
		
	def sizeHint(self):
		return QtCore.QSize(self.codeEdit.getLineNumberAreaWidth(), 0)
		
	def paintEvent(self, event):
		self.codeEdit.lineNumberAreaPaintEvent(event)
