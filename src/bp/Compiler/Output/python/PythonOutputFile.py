####################################################################
# Header
####################################################################
# Target:   Python 3 Code
# Author:   Eduard Urbach

####################################################################
# License
####################################################################
# (C) 2012  Eduard Urbach
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
from bp.Compiler.Output.BaseOutputFile import *
from bp.Compiler.Output.python.PythonClass import *
from bp.Compiler.Output.python.PythonFunction import *
from bp.Compiler.Output.python.PythonVariable import *
from bp.Compiler.Output.python.PythonClassImplementation import *
from bp.Compiler.Output.python.PythonFunctionImplementation import *

####################################################################
# Classes
####################################################################
class PythonOutputFile(BaseOutputFile):
	
	def __init__(self, compiler, file, root):
		self.currentTabLevel = 0
		
		BaseOutputFile.__init__(self, compiler, file, root)
		
		# XML tag : C++ keyword, condition tag name, code tag name
		self.paramBlocks = {
			"if" : ["if", "condition", "code"],
			"else-if" : ["elif", "condition", "code"],
			"while" : ["while", "condition", "code"]
		}
		
		# Header
		self.functionsHeader = "# Functions\n"
		self.varsHeader = "\n# Variables\n"
		self.classesHeader = ""
		self.prototypesHeader = "\n# Prototypes\n"
		
		# Syntax
		self.lineLimiter = "\n"
		self.myself = "self"
		self.trySyntax = "try\n%s\n\t"
		self.catchSyntax = "except %s\n%s\n\t"
		self.returnSyntax = "return %s"
		self.memberAccessSyntax = "self."
		self.singleParameterSyntax = "%s"
		self.newObjectSyntax = "%s(%s)"
		self.binaryOperatorDivideSyntax = "%s%s%s%s%s"
		self.pointerDerefAssignSyntax = "%s = %s"
		self.declareUnmanagedSyntax = "%s(%s)"
		self.constAssignSyntax = "%s = %s"
		self.elseSyntax = " else\n%s%s"
		self.ptrMemberAccessChar = "."
	
	def compile(self):
		print("Compiling: " + self.file)
		
		# Check whether string class has been defined or not
		# NOTE: This has to be called before self.scanAhead is executed.
		self.stringClassDefined = self.classExists("UTF8String")
		
		# Scan
		self.scanAhead(self.codeNode)
		
		# String class init
		self.checkStringClass()
		
		# Header
		self.header = "# Imports\n"
		self.header += "from bp_decls import *\n"
		for node in self.dependencies.childNodes:
			if isElemNode(node) and node.tagName == "import":
				self.header += self.handleImport(node)
		
		# Strings
		self.stringsHeader = "\n# Strings\n"
		for node in self.strings.childNodes:
			self.stringsHeader += self.handleString(node)
		
		# Code
		self.currentTabLevel = 0
		self.code = self.parseChilds(self.codeNode, "\t" * self.currentTabLevel, self.lineLimiter)
	
	def createVariable(self, name, type, value, isConst, isPointer, isPublic):
		return PythonVariable(name, type, value, isConst, isPointer, isPublic)
	
	def createNamespace(self, name):
		return PythonNamespace(name)
		
	def createClass(self, name, node):
		return PythonClass(name, node)
	
	def createFunction(self, node):
		return PythonFunction(self, node)
		
	def buildThreadFunc(self, funcName, paramTypes):
		pass
		
	def adjustDataType(self, typeName, adjustOuterAsWell = True):
		return adjustDataTypePY(typeName, adjustOuterAsWell)
	
	def buildThreadJoin(self, threadID, tabs):
		return ""
	
	def buildForLoop(self, varDefs, typeInit, iterExpr, fromExpr, operator, toExpr, code, tabs):
		# TODO: Is there another Python range object for that?
		if operator == "<=":
			toExpr += " + 1"
		
		return "%sfor %s in range(%s, %s):\n%s%s" % (varDefs, iterExpr, fromExpr, toExpr, tabs, code)
		#return "%sfor(%s%s = %s; %s %s %s; ++%s) {\n%s%s}" % (varDefs, typeInit, iterExpr, fromExpr, iterExpr, operator, toExpr, iterExpr, code, tabs)
	
	def buildVarDeclaration(self, typeName, name):
		return "%s = None" % name
	
	def buildTypeDeclaration(self, typeName, varName):
		return varName
		
	def buildTypeDeclarationNameOnly(self, varName):
		return varName
	
	def buildTemplateCall(self, op1, op2):
		return op1 + "<" + op2 + ">"
	
	def buildDivByZeroCheck(self, op):
		return 'if (%s) == 0: raise BPDivisionByZeroException()' % op
	
	def buildDivByZeroThrow(self, op):
		return 'raise BPDivisionByZeroException()'
	
	def buildString(self, id, value):
		return id + " = BPUTF8String(b\"" + value + "\")\n"
	
	def buildUndefinedString(self, id, value):
		return id + " = b\"" + value + "\"\n"
	
	def buildModuleImport(self, importedModule):
		path = (extractDir(importedModule) + stripAll(importedModule))[len(self.compiler.modDir):]
		return "from " + normalizeModPath(path) + " import *\n"
	
	def buildDeleteMemPointer(self, caller):
		return "del %s" % (caller)
	
	def buildThreadCreation(self, threadID, threadFuncID, paramTypes, paramsString, tabs):
		return ""
	
	def buildNonPointerCall(self, caller, fullName, paramsString):
		return "%s%s%s%s%s" % (["", caller + "."][caller != ""], fullName, "(", paramsString, ")")
	
	def buildCall(self, caller, fullName, paramsString):
		return "%s%s%s%s%s" % (["", caller + "."][caller != ""], fullName, "(", paramsString, ")")
	
	def buildSingleParameter(self, typeName, name):
		return self.singleParameterSyntax % (name)
	
	def castToNativeNumeric(self, variableType, value):
		return value
	
	def writeClasses(self):
		prefix = "BP"
		
		for classObj in self.localClasses:
			if not classObj.isExtern:
				for classImplId, classImpl in classObj.implementations.items():
					code = ""
					
					# Functions
					for funcImpl in classImpl.funcImplementations.values():
						code += "\t"
						
						if funcImpl.getFuncName() == "init":
							code += funcImpl.getConstructorCode()
						elif funcImpl.getFuncName() == "finalize":
							code += funcImpl.getDestructorCode()
						else:
							code += funcImpl.getFullCode()
						
						code += "\n"
					
					if code == "":
						code = "\tpass\n"
					
					code += "\t\n"
					
					# Templates
					templatePrefix = ""
					templatePostfix = ""
					if classObj.templateNames:
						templatePrefix += "template <>\n"
						templatePostfix = classImpl.getTemplateValuesString(True)
						#self.classesHeader += "template <typename %s>\n" % (", typename ".join(classObj.templateParams))
					
					# Comment
					self.classesHeader += "# %s\n" % (prefix + classObj.name + templatePostfix)
					self.classesHeader += templatePrefix
					
					# Add code to classes header
					finalClassName = prefix + classObj.name + templatePostfix
					
					# Memory management
					if self.useGC:
						# TODO: Ensure destructor call?
						if classObj.ensureDestructorCall:
							pass
						else:
							pass
						
						self.classesHeader += "class %s:" % (finalClassName)
					
					# For debugging the GC add this commented line to the string:
					# ~%s(){std::cout << \"Destroying %s\" << std::endl;}\n
					self.classesHeader += "\n" + code + "\n"
	
	def getCode(self):
		self.writeFunctions()
		self.writeClasses()
		return self.header + self.stringsHeader + self.varsHeader + self.functionsHeader + "\n" + self.classesHeader + "\n# Code\n%s" % self.code