from PyQt4 import QtGui, QtCore, uic
from bp.Compiler import *

class BPPostProcessorThread(QtCore.QThread, Benchmarkable):
	
	def __init__(self, bpIDE):
		super().__init__(bpIDE)
		self.bpIDE = bpIDE
		self.processor = bpIDE.processor
		self.finished.connect(self.bpIDE.postProcessorFinished)
		
	def startWith(self, codeEdit):
		self.codeEdit = codeEdit
		self.start()
		
	def run(self):
		try:
			self.startBenchmark("[%s] PostProcessor" % stripDir(self.codeEdit.getFilePath()))
			self.processor.resetDTreesForFile(self.codeEdit.getFilePath())
			self.bpIDE.processorOutFile = self.processor.process(self.codeEdit.root, self.codeEdit.getFilePath())
			self.endBenchmark()
		except PostProcessorException as e:
			errorMessage = e.getMsg()
			self.bpIDE.msgView.addMessage(errorMessage)