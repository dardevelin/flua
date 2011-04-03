####################################################################
# Header
####################################################################
# Syntax:   Blitzprog Code
# Author:   Eduard Urbach

####################################################################
# License
####################################################################
# (C) 2008  Eduard Urbach
# 
# This file is part of Blitzprog.
# 
# Blitzprog is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Blitzprog is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Blitzprog.  If not, see <http://www.gnu.org/licenses/>.

####################################################################
# Imports
####################################################################
from ExpressionParser import *
from Utils import *
import codecs

####################################################################
# Classes
####################################################################
class CompilerException(Exception):
	
	def __init__(self, reason):
		self.reason = reason
		
	def __str__(self):
		return repr(self.reason)

class BPCCompiler:
	
	def __init__(self, modDir):
		self.compiledFiles = dict()
		self.compiledFilesList = []
		self.projectDir = ""
		self.modDir = fixPath(os.path.abspath(modDir)) + "/"
		self.initExprParser()
		
		#print("Mods: " + self.modDir)
	
	def getCompiledFiles(self):
		return self.compiledFilesList
	
	def getFileInstanceByPath(self, path):
		return self.compiledFiles[path]
	
	def initExprParser(self):
		self.parser = ExpressionParser()
		
		# See http://www.cppreference.com/wiki/operator_precedence
		
		# 1: Function calls
		operators = OperatorLevel()
		operators.addOperator(Operator("(", "call.unused", Operator.BINARY))
		operators.addOperator(Operator("§", "template-call", Operator.BINARY))
		self.parser.addOperatorLevel(operators)
		
		# 2: Access
		operators = OperatorLevel()
		operators.addOperator(Operator(".", "access", Operator.BINARY))
		operators.addOperator(Operator("[", "index.unused", Operator.BINARY))
		operators.addOperator(Operator("#", "call", Operator.BINARY))
		operators.addOperator(Operator("@", "index", Operator.BINARY))
		operators.addOperator(Operator(":", "declare-type", Operator.BINARY))
		self.parser.addOperatorLevel(operators)
		
		# Loose pointer
		operators = OperatorLevel()
		operators.addOperator(Operator("~", "loose-reference", Operator.UNARY))
		self.parser.addOperatorLevel(operators)
		
		# 3: Unary
		operators = OperatorLevel()
		operators.addOperator(Operator("!", "not", Operator.UNARY))
		operators.addOperator(Operator("-", "negative", Operator.UNARY))
		self.parser.addOperatorLevel(operators)
		
		# 5: Mul, Div
		operators = OperatorLevel()
		operators.addOperator(Operator("*", "multiply", Operator.BINARY))
		operators.addOperator(Operator("/", "divide", Operator.BINARY))
		operators.addOperator(Operator("\\", "divide-floor", Operator.BINARY))
		operators.addOperator(Operator("%", "modulo", Operator.BINARY))
		self.parser.addOperatorLevel(operators)
		
		# 6: Add, Sub
		operators = OperatorLevel()
		operators.addOperator(Operator("+", "add", Operator.BINARY))
		operators.addOperator(Operator("-", "subtract", Operator.BINARY))
		self.parser.addOperatorLevel(operators)
		
		# 8: GT, LT
		operators = OperatorLevel()
		operators.addOperator(Operator(">=", "greater-or-equal", Operator.BINARY))
		operators.addOperator(Operator(">", "greater", Operator.BINARY))
		operators.addOperator(Operator("<=", "less-or-equal", Operator.BINARY))
		operators.addOperator(Operator("<", "less", Operator.BINARY))
		self.parser.addOperatorLevel(operators)
		
		# 9: Comparison
		operators = OperatorLevel()
		operators.addOperator(Operator("==", "equal", Operator.BINARY))
		operators.addOperator(Operator("!=", "not-equal", Operator.BINARY))
		self.parser.addOperatorLevel(operators)
		
		# 13: Logical AND
		operators = OperatorLevel()
		operators.addOperator(Operator("&&", "and", Operator.BINARY))
		self.parser.addOperatorLevel(operators)
		
		# 14: Logical OR
		operators = OperatorLevel()
		operators.addOperator(Operator("||", "or", Operator.BINARY))
		self.parser.addOperatorLevel(operators)
		
		# 15: Ternary operator
#		operators = OperatorLevel()
#		operators.addOperator(Operator(":", "ternary-code", Operator.BINARY))
#		self.parser.addOperatorLevel(operators)
#		
#		operators = OperatorLevel()
#		operators.addOperator(Operator("?", "ternary-condition", Operator.BINARY))
#		self.parser.addOperatorLevel(operators)
		
		# 16: Assign
		operators = OperatorLevel()
		operators.addOperator(Operator("+=", "assign-add", Operator.BINARY))
		operators.addOperator(Operator("-=", "assign-subtract", Operator.BINARY))
		operators.addOperator(Operator("*=", "assign-multiply", Operator.BINARY))
		operators.addOperator(Operator("/=", "assign-divide", Operator.BINARY))
		#operators.addOperator(Operator("}=", "assign-each-in", Operator.BINARY))
		operators.addOperator(Operator("=", "assign", Operator.BINARY))
		operators.addOperator(Operator("->", "flows-to", Operator.BINARY))
		operators.addOperator(Operator("<-", "flows-from", Operator.BINARY))
		self.parser.addOperatorLevel(operators)
		
		# Comma
		operators = OperatorLevel()
		operators.addOperator(Operator(",", "separate", Operator.BINARY))
		self.parser.addOperatorLevel(operators)
	
	def compile(self, mainFile):
		fileIn = fixPath(os.path.abspath(mainFile))
		
		isMainFile = not self.compiledFiles
		
		if isMainFile:
			self.projectDir = os.path.dirname(fileIn) + "/"
		
		bpcFile = self.spawnFileCompiler(fileIn, isMainFile)
		
		self.compiledFiles[fileIn] = bpcFile
		self.compiledFilesList.append(bpcFile)
		
		for file in bpcFile.importedFiles:
			if not file in self.compiledFiles:
				# TODO: Change directory
				self.compile(file)
		
	def spawnFileCompiler(self, fileIn, isMainFile):
		myFile = BPCFile(self, fileIn, isMainFile)
		myFile.compile()
		return myFile
	
	def writeToFS(self, dirOut):
		dirOut = os.path.abspath(dirOut) + "/"
		
		for bpcFile in self.compiledFiles.values():
			fileOut = dirOut + stripExt(bpcFile.file[len(self.projectDir):]) + ".bp"
			
			# Directory structure
			concreteDirOut = os.path.dirname(fileOut)
			if not os.path.isdir(concreteDirOut):
				os.makedirs(concreteDirOut)
			
			with open(fileOut, "w") as outStream:
				outStream.write(bpcFile.root.toprettyxml())
		
class BPCFile(ScopeController):
	
	def __init__(self, compiler, fileIn, isMainFile):
		ScopeController.__init__(self)
		
		self.compiler = compiler
		self.file = fileIn
		self.dir = os.path.dirname(fileIn) + "/"
		self.stringCount = 0
		self.importedFiles = []
		self.nextLineIndented = False
		self.savedNextNode = 0
		self.inSwitch = 0
		self.inCase = 0
		self.inExtern = 0
		self.inTemplate = 0
		self.inGetter = 0
		self.inSetter = 0
		self.parser = self.compiler.parser
		self.isMainFile = isMainFile
		self.doc = parseString("<module><header><title/><dependencies/><strings/></header><code></code></module>")
		self.root = self.doc.documentElement
		self.header = getElementByTagName(self.root, "header")
		self.dependencies = getElementByTagName(self.header, "dependencies")
		self.strings = getElementByTagName(self.header, "strings")
		
		# XML tags which can follow another tag
		
		# 2 levels
		self.blocks = {
			"if-block" : ["else-if", "else"],
			"try-block" : ["catch"]
		}
		
		# 1 level
		self.simpleBlocks = {
			"class" : [],
			"function" : [],
			"while" : [],
			"for" : [],
			"in" : [],
			"switch" : [],
			"case" : [],
			"target" : [],
			"extern" : [],
			"template" : [],
			"get" : [],
			"set" : [],
			"getter" : [],
			"setter" : []
		}
		
		# This is used for xml tags which have a "code" node
		self.nextNode = 0
		
		# parseExpr
		self.parseExpr = self.parser.buildXMLTree
		
	def getRoot(self):
		return self.root
		
	def compile(self):
		print("Compiling: " + self.file)
		
		self.currentNode = getElementByTagName(self.root, "code")
		self.lastNode = None
		
		# Read
		with codecs.open(self.file, "r", "utf-8") as inStream:
			codeText = inStream.read()
		
		lines = ["import bp.Core"] + codeText.split('\n') + [""]
		tabCount = 0
		prevTabCount = 0
		
		# Go through every line -> build the structure
		for lineIndex in range(0, len(lines)):
			line = lines[lineIndex].rstrip()
			tabCount = self.countTabs(line)
			line = line.lstrip()
			line = self.removeStrings(line)
			line = self.removeComments(line)
			
			if line == "":
				continue
			
			# pi
			line = line.replace("π", "pi")
			
			self.nextLineIndented = False
			if lineIndex < len(lines) - 1:
				tabCountNextLine = self.countTabs(lines[lineIndex + 1])
				if tabCountNextLine == tabCount + 1:
					self.nextLineIndented = True
			
			# Remove whitespaces
			line = line.replace("\t", " ")
			while line.find("  ") != -1:
				line = line.replace("  ", " ")
			
			if tabCount < prevTabCount:
				savedCurrentNode = self.currentNode
				self.tabBack(currentLine, prevTabCount, tabCount, True)
				self.currentNode = savedCurrentNode
			
			currentLine = self.processLine(line)
			
			# Tab level hierarchy
			if tabCount > prevTabCount:
				if self.savedNextNode:
					self.currentNode = self.savedNextNode
					self.savedNextNode = 0
				else:
					self.currentNode = self.lastNode
			elif tabCount < prevTabCount:
				self.tabBack(currentLine, prevTabCount, tabCount, False)
			
			self.savedNextNode = self.nextNode
			
			if currentLine:
				if not isTextNode(currentLine) and currentLine.tagName == "assign":
					variableNode = currentLine.childNodes[0].childNodes[0]
					if isTextNode(variableNode):
						variable = variableNode.nodeValue
						if not variable in self.getCurrentScope().variables:
							self.getCurrentScope().variables[variable] = currentLine
				
				self.lastNode = self.currentNode.appendChild(currentLine)
			prevTabCount = tabCount
		
	def tabBack(self, currentLine, prevTabCount, tabCount, countIns):
		atTab = prevTabCount
		while atTab > tabCount:
			if countIns:
				if self.currentNode.tagName == "switch":
					self.inSwitch -= 1
				elif self.currentNode.tagName == "extern":
					self.inExtern -= 1
				elif self.currentNode.tagName == "template":
					self.inTemplate -= 1
				elif self.currentNode.tagName == "get":
					self.inGetter -= 1
				elif self.currentNode.tagName == "set":
					self.inSetter -= 1
			
			self.currentNode = self.currentNode.parentNode
			
			if countIns:
				if self.currentNode.tagName == "case":
					self.inCase -= 1
			
			# XML elements with "code" tags need special treatment
			if self.currentNode.parentNode.tagName in self.blocks:
				tagsAllowed = self.blocks[self.currentNode.parentNode.tagName]
				if atTab != tabCount + 1 or isTextNode(currentLine) or (not currentLine.tagName in tagsAllowed):
					self.currentNode = self.currentNode.parentNode.parentNode
				else:
					self.currentNode = self.currentNode.parentNode
			elif self.currentNode.tagName in self.simpleBlocks:
				tagsAllowed = self.simpleBlocks[self.currentNode.tagName]
				if atTab != tabCount + 1 or isTextNode(currentLine) or not currentLine.tagName in tagsAllowed:
					self.currentNode = self.currentNode.parentNode
			atTab -= 1
		
	def processLine(self, line):
		if self.inExtern:
			return self.handleExternLine(line)
		elif startsWith(line, "import"):
			return self.handleImport(line)
		elif startsWith(line, "while"):
			return self.handleWhile(line)
		elif startsWith(line, "for"):
			return self.handleFor(line)
		elif startsWith(line, "try"):
			return self.handleTry(line)
		elif startsWith(line, "catch"):
			return self.handleCatch(line)
		elif startsWith(line, "if"):
			return self.handleIf(line)
		elif startsWith(line, "elif"):
			return self.handleElif(line)
		elif startsWith(line, "else"):
			return self.handleElse(line)
		elif startsWith(line, "throw"):
			return self.handleThrow(line)
		elif startsWith(line, "return"):
			return self.handleReturn(line)
		elif startsWith(line, "const"):
			return self.handleConst(line)
		elif startsWith(line, "break"):
			return self.handleBreak(line)
		elif startsWith(line, "continue"):
			return self.handleContinue(line)
		elif startsWith(line, "private"):
			return self.handlePrivate(line)
		elif startsWith(line, "in"):
			return self.handleIn(line)
		elif startsWith(line, "switch"):
			return self.handleSwitch(line)
		elif startsWith(line, "target"):
			return self.handleTarget(line)
		elif startsWith(line, "extern"):
			return self.handleExtern(line)
		elif startsWith(line, "include"):
			return self.handleInclude(line)
		elif startsWith(line, "template"):
			return self.handleTemplate(line)
		elif startsWith(line, "get"):
			return self.handleGet(line)
		elif startsWith(line, "set"):
			return self.handleSet(line)
		elif line == "...":
			return self.handleNOOP(line)
		elif self.nextLineIndented:
			if self.inSwitch > 0:
				return self.handleCase(line)
			elif line[0].islower():
				return self.handleFunction(line)
			else:
				return self.handleClass(line)
		else:
			if self.inTemplate:
				return self.handleTemplateParameter(line)
			
			line = self.addBrackets(line)
			line = self.addGenerics(line)
			node = self.parseExpr(line)
			return node
	
	def addGenerics(self, line):
		bracketCounter = 0
		char = ''
		startGeneric = -1
		#oldLine = line
		
		for i in range(len(line)):
			char = line[i]
			
			if char == '<':
				bracketCounter += 1
				if bracketCounter == 1:
					startGeneric = i
			elif char == '>':
				bracketCounter -= 1
				
				# End of template parameter
				if bracketCounter == 0:
					templateParam = self.addGenerics(line[startGeneric+1:i])
					line = line[:startGeneric] + "§(" + templateParam + ")" + line[i+1:]
					
			elif bracketCounter > 0 and char != ',' and (not char.isspace()) and ((not isVarChar(char)) or char == '.'):
				break
		
#		if oldLine != line:
#			print("Start: " + oldLine)
#			print("End: " + line)
		return line
		
	def addBrackets(self, line):
		bracketCounter = 0
		char = ''
		
		for i in range(len(line)):
			char = line[i]
			
			if char == '(' or char == '[':
				bracketCounter += 1
			elif char == ')' or char == ']':
				bracketCounter -= 1
			elif (not isVarChar(char)) and char != '.' and bracketCounter == 0:
				break
		
		if i < len(line) - 1:
			nextChar = line[i+1]
			
			if char.isspace() and (isVarChar(nextChar)):
				line = "%s(%s)" % (line[:i], line[i+1:])
		elif line[-1] != ')':
			line += "()"
		
		return line
		
	def handleCase(self, line):
		node = self.doc.createElement("case")
		values = self.compiler.parser.getParametersNode(self.parseExpr(line))
		code = self.doc.createElement("code")
		
		values.tagName = "values"
		for value in values.childNodes:
			value.tagName = "value"
	
		node.appendChild(values)
		node.appendChild(code)
		
		self.inCase += 1
		self.nextNode = code
		return node
		
	def handleSwitch(self, line):
		node = self.doc.createElement("switch")
		value = self.doc.createElement("value")
		value.appendChild(self.parseExpr(line[len("switch")+1:]))
		
		node.appendChild(value)
		
		self.inSwitch += 1
		self.nextNode = node
		return node
		
	def handleGet(self, line):
		node = self.doc.createElement("get")
		
		self.inGetter = 1
		self.nextNode = node
		return node
	
	def handleSet(self, line):
		node = self.doc.createElement("set")
		
		self.inSetter = 1
		self.nextNode = node
		return node
		
	def handleTemplate(self, line):
		node = self.doc.createElement("template")
		
		self.inTemplate = 1
		self.nextNode = node
		return node
		
	def handleTemplateParameter(self, line):
		node = self.doc.createElement("parameter")
		node.appendChild(self.doc.createTextNode(line))
		
		return node
		
	def handleIn(self, line):
		node = self.doc.createElement("in")
		expr = self.doc.createElement("expression")
		code = self.doc.createElement("code")
		expr.appendChild(self.parseExpr(line[len("in")+1:]))
		
		node.appendChild(expr)
		node.appendChild(code)
		
		self.nextNode = code
		return node
		
	def handleFor(self, line):
		node = self.doc.createElement("for")
		
		pos = line.find(" to ")
		if pos == -1:
			node.tagName = "foreach"
			# TODO: Foreach
			return None
		else:
			initExpr = self.parseExpr(line[len("for")+1:pos])
			toExpr = self.parseExpr(line[pos+len(" to "):])
			
			iterNode = self.doc.createElement("iterator")
			iterNode.appendChild(initExpr.childNodes[0].childNodes[0])
			
			fromNode = self.doc.createElement("from")
			fromNode.appendChild(initExpr.childNodes[1].childNodes[0])
			
			toNode = self.doc.createElement("to")
			toNode.appendChild(toExpr)
			
			codeNode = self.doc.createElement("code")
			
			node.appendChild(iterNode)
			node.appendChild(fromNode)
			node.appendChild(toNode)
			node.appendChild(codeNode)
			
			self.nextNode = codeNode
		
		return node
		
	def handlePrivate(self, line):
		node = self.doc.createElement("private")
		self.nextNode = node
		return node
		
	def handleNOOP(self, line):
		return self.doc.createElement("noop")
		
	def handleWhile(self, line):
		node = self.doc.createElement("while")
		condition = self.doc.createElement("condition")
		code = self.doc.createElement("code")
		condition.appendChild(self.parseExpr(line[len("while")+1:]))
		
		node.appendChild(condition)
		node.appendChild(code)
		
		self.nextNode = code
		return node
	
	def handleTarget(self, line):
		node = self.doc.createElement("target")
		condition = self.doc.createElement("name")
		code = self.doc.createElement("code")
		condition.appendChild(self.doc.createTextNode(line[len("target")+1:]))
		
		node.appendChild(condition)
		node.appendChild(code)
		
		self.nextNode = code
		return node
	
	def handleExtern(self, line):
		node = self.doc.createElement("extern")
		self.inExtern += 1
		
		self.nextNode = node
		return node
	
	def handleExternLine(self, line):
		node = self.doc.createElement("extern-function")
		name = self.doc.createElement("name")
		node.appendChild(name)
		
		pos = line.find(":")
		
		if pos == -1:
			name.appendChild(self.doc.createTextNode(line))
		else:
			funcName = line[:pos].rstrip()
			funcType = line[pos+1:].lstrip()
			
			type = self.doc.createElement("type")
			node.appendChild(type)
			
			name.appendChild(self.doc.createTextNode(funcName))
			type.appendChild(self.doc.createTextNode(funcType))
		
		return node
		
	def handleContinue(self, line):
		return self.doc.createElement("continue")
		
	def handleBreak(self, line):
		return self.doc.createElement("break")
		
	def handleConst(self, line):
		node = self.doc.createElement("const")
		param = self.parseExpr(line[len("const")+1:])
		if param.hasChildNodes() and param.tagName == "assign":
			node.appendChild(param)
		else:
			raise CompilerException("#const keyword expects a variable assignment")
		return node
		
	def handleReturn(self, line):
		node = self.doc.createElement("return")
		param = self.parseExpr(line[len("return")+1:])
		if param.nodeValue or param.hasChildNodes():
			node.appendChild(param)
		return node
	
	def handleThrow(self, line):
		node = self.doc.createElement("throw")
		param = self.parseExpr(line[len("throw")+1:])
		if param.nodeValue or param.hasChildNodes():
			node.appendChild(param)
		else:
			raise CompilerException("#throw keyword expects a parameter (e.g. an exception object)")
		return node
	
	def handleInclude(self, line):
		node = self.doc.createElement("include")
		param = self.doc.createTextNode(line[len("include")+1:])
		if param.nodeValue:
			node.appendChild(param)
		else:
			raise CompilerException("#include keyword expects a file name")
		return node
		
	def handleFunction(self, line):
		# Check for function
		funcName = ""
		pos = 0
		lineLen = len(line)
		while pos < lineLen and isVarChar(line[pos]):
			pos += 1
		if pos is len(line):
			funcName = line
		elif line[pos] == ' ':
			funcName = line[:pos]
		else:
			whiteSpace = line.find(' ')
			if whiteSpace is not -1:
				funcName = line[:whiteSpace]
			else:
				funcName = line
			raise CompilerException("Invalid function name '" + funcName + "'")
		
		#print(" belongs to " + self.currentNode.tagName)
		
		if self.inSetter:
			node = self.doc.createElement("setter")
		elif self.inGetter:
			node = self.doc.createElement("getter")
		else:
			node = self.doc.createElement("function")
		
		params = self.parseExpr(line[len(funcName)+1:])
		
		nameNode = self.doc.createElement("name")
		nameNode.appendChild(self.doc.createTextNode(funcName))
		paramsNode = self.parser.getParametersNode(params)
		codeNode = self.doc.createElement("code")
		
		node.appendChild(nameNode)
		node.appendChild(paramsNode)
		node.appendChild(codeNode)
		
		#self.inFunction = True
		self.nextNode = codeNode
		return node
		
	def handleClass(self, line):
		className = line
		
		node = self.doc.createElement("class")
		
		nameNode = self.doc.createElement("name")
		nameNode.appendChild(self.doc.createTextNode(className))
		#publicNode = self.doc.createElement("public")
		#privateNode = self.doc.createElement("private")
		code = self.doc.createElement("code")
		
		node.appendChild(nameNode)
		#node.appendChild(publicNode)
		#node.appendChild(privateNode)
		node.appendChild(code)
		
		self.nextNode = code
		return node
		
	def handleTry(self, line):
		node = self.doc.createElement("try-block")
		
		tryNode = self.doc.createElement("try")
		code = self.doc.createElement("code")
		
		tryNode.appendChild(code)
		
		node.appendChild(tryNode)
		self.nextNode = code
		return node
	
	def handleCatch(self, line):
		node = self.doc.createElement("catch")
		exceptionType = self.doc.createElement("variable")
		code = self.doc.createElement("code")
		
		varNode = self.parseExpr(line[len("catch")+1:])
		if nodeIsValid(varNode):
			exceptionType.appendChild(varNode)
		
		node.appendChild(exceptionType)
		node.appendChild(code)
		self.nextNode = code
		return node
		
	def handleIf(self, line):
		node = self.doc.createElement("if-block")
		
		ifNode = self.doc.createElement("if")
		condition = self.doc.createElement("condition")
		code = self.doc.createElement("code")
		
		condition.appendChild(self.parseExpr(line[len("if")+1:]))
		
		ifNode.appendChild(condition)
		ifNode.appendChild(code)
		
		node.appendChild(ifNode)
		
		self.nextNode = code
		return node
	
	def handleElif(self, line):
		node = self.doc.createElement("else-if")
		condition = self.doc.createElement("condition")
		code = self.doc.createElement("code")
		
		condition.appendChild(self.parseExpr(line[len("elif")+1:]))
		
		node.appendChild(condition)
		node.appendChild(code)
		
		self.nextNode = code
		return node
		
	def handleElse(self, line):
		node = self.doc.createElement("else")
		code = self.doc.createElement("code")
		
		node.appendChild(code)
		self.nextNode = code
		return node
		
	def handleImport(self, line):
		# Priority for module search:
		# ########################### #
		# 1. Local    # 4. Project    # 7. Global     #
		# ########################### ############### #
		# 2. File     # 5.  File      # 8.  File      #
		# 3. Dir      # 6.  Dir       # 9.  Dir       #
		
		importedModule = line[len("import"):].strip()
		importedModulePath = importedModule.replace(".", "/")
		
		# Local
		importedFile = self.dir + importedModulePath + ".bpc"
		
		importedInFolder = self.dir + importedModulePath
		importedInFolder += "/" + stripAll(importedInFolder) + ".bpc"
		
		# Project
		pImportedFile = self.compiler.projectDir + importedModulePath + ".bpc"
		
		pImportedInFolder = self.compiler.projectDir + importedModulePath
		pImportedInFolder += "/" + stripAll(pImportedInFolder) + ".bpc"
		
		# Global
		gImportedFile = self.compiler.modDir + importedModulePath + ".bpc"
		
		gImportedInFolder = self.compiler.modDir + importedModulePath
		gImportedInFolder += "/" + stripAll(pImportedInFolder) + ".bpc"
		
		# TODO: Implement global variant
		
		if os.path.isfile(importedFile):
			self.importedFiles.append(importedFile)
		elif os.path.isfile(importedInFolder):
			self.importedFiles.append(importedInFolder)
		elif os.path.isfile(pImportedFile):
			self.importedFiles.append(pImportedFile)
		elif os.path.isfile(pImportedInFolder):
			self.importedFiles.append(pImportedInFolder)
		elif os.path.isfile(gImportedFile):
			self.importedFiles.append(gImportedFile)
		elif os.path.isfile(gImportedInFolder):
			self.importedFiles.append(gImportedInFolder)
		else:
			raise CompilerException("Module not found: " + importedModule)
		
		element = self.doc.createElement("import")
		element.appendChild(self.doc.createTextNode(importedModule))
		self.dependencies.appendChild(element)
		
		return None
	
	def countTabs(self, line):
		tabCount = 0
		while tabCount < len(line) and line[tabCount] == '\t':
			tabCount += 1
		
		return tabCount
	
	def removeStrings(self, line):
		i = 0
		while i < len(line):
			if line[i] == '"':
				h = i + 1
				while h < len(line) and line[h] != '"':
					h += 1
				# TODO: Add string to string list
				identifier = "bp_string_" + str(self.stringCount) #.zfill(9)
				
				# Create XML node
				stringNode = self.doc.createElement("string")
				stringNode.setAttribute("id", identifier)
				stringNode.appendChild(self.doc.createTextNode(line[i+1:h]))
				self.strings.appendChild(stringNode)
				
				line = line[:i] + identifier + line[h+1:]
				self.stringCount += 1
				i += len(identifier)
			i += 1
		return line
	
	def removeComments(self, line):
		pos = line.find('#')
		if pos is not -1:
			return line[:pos].rstrip()
		else:
			return line
	
####################################################################
# Functions
####################################################################
def compileWarning(msg):
	print("[Warning] " + msg)

####################################################################
# Main
####################################################################
if __name__ == '__main__':
	try:
		print("Starting:")
		start = time.clock()
		
		bpc = BPCCompiler("../../../")
		bpc.compile("../Test/Input/main.bpc")
		#bpc.writeToFS("../Test/Output/")
		
		elapsedTime = time.clock() - start
		print("Time:    " + str(elapsedTime * 1000) + " ms")
		print("Done.")
	except:
		printTraceback()