####################################################################
# Header
####################################################################
# Blitzprog Compiler
# 
# Website: www.blitzprog.com
# Started: 19.07.2008 (Sat, Jul 19 2008)

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
from Input import *
from Generic import *
from Output import *

####################################################################
# Main
####################################################################
if __name__ == '__main__':
	try:
		print("Starting:")
		start = time.clock()
		
		# Compile
		start = time.clock()
		
		bpc = BPCCompiler("../../")
		bpc.compile("Test/Input/main.bpc")
		
		elapsedTime = time.clock() - start
		print("CompileTime:  " + str(elapsedTime * 1000) + " ms")
		
		# Post-processing
		start = time.clock()
		
		bp = BPPostProcessor(bpc)
		bp.process(bpc.getCompiledFiles()[0])
		
		elapsedTime = time.clock() - start
		print("PostProcessTime:  " + str(elapsedTime * 1000) + " ms")
		
		# Generate
		start = time.clock()
		
		cpp = CPPOutputCompiler(bpc)
		cpp.compile(bpc.getCompiledFiles()[0])
		cpp.writeToFS("Test/Output/")
		
		elapsedTime = time.clock() - start
		print("GenerateTime:  " + str(elapsedTime * 1000) + " ms")
		
		# Build
		start = time.clock()
		
		exe = cpp.build()
		
		elapsedTime = time.clock() - start
		print("BuildTime:    " + str(elapsedTime * 1000) + " ms")
		
		# Exec
		print("\nOutput:")
		cpp.execute(exe)
	except:
		printTraceback()