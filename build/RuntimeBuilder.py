import os
import sys

try:
	from fabricate import *
	import Environment
	import Executor
except ImportError, e:
	print "Couldn't find project-utils modules."
	sys.exit(1)


class MaxRuntimeBuilder(Executor):
	def __init__(self, cc='gcc', maxfile):
		super(MaxRuntimeBuilder, self).__init__(logPrefix="[MaxRuntimeBuilder] ")
		if not os.path.isfile(maxfile):
			print "Maxfile doesn't exist: '%s'" % (maxfile)
			exit(1)
 
		if not maxfile.endswith('.max'):
			print "Maxfile doesn't end with .max: '%s'" % (maxfile)
			exit(1)

		self.maxfile = maxfile
		self.designName = maxfile.replace('.max', '')
		
		self.MAXELEROSDIR = Environment.require("MAXELEROSDIR")
		self.MAXCOMPILERDIR = Environment.require("MAXCOMPILERDIR")
		self.MAXNETDIR = Environment.require("MAXNETDIR")
		self.cc = cc

	def getMaxelerOsInc():
		"""return the include paths for MaxelerOS."""
		return ['-I%s/include' % self.MAXELEROSDIR]

	def getMaxelerOsLibs():
		"""Return the MaxelerOS libraries to be used in linking."""
		return ['-L%s/lib' % self.MAXELEROSDIR, '-lmaxeleros']

	def getSlicInc():
		"""Return the SLiC include paths."""
		return ['-I%s/include/slic' % self.MAXCOMPILERDIR]

	def getSlicLibs():
		"""Return the SLiC libraries to be used in linking."""
		return ['-L%s/lib' % self.MAXCOMPILERDIR, '-lslic']

	def getMaxNetInc():
		"""Return the include paths for Networking."""
		return ['-I%s/include/slicnet' % self.MAXNETDIR]

	def getMaxNetLibs():
		"""Return the Networking libraries to be used in linking."""
		return ['-L%s/lib' % self.MAXNETDIR, '-lslicnet']

	def getMaxfileLibs():
		"""Return the Maxfile object to be used in linking."""
		return [maxfile.replace('.max', '.o')]

	def getCompileFlags():
		"""Return all runtime include paths"""
		return ['-DDESIGN_NAME=%s' % (self.designName)] + getMaxelerOsInc() + getSlicInc() + getMaxNetInc()

	def getLinkFlags():
		"""Returns the libraries to be used for linking."""
		return getMaxfileLibs() + getMaxelerOsLibs() + getSlicLibs() + getMaxNetLibs() + getMaxfileLibs() + ['-lpthread'] 

	def slicCompile():
		"""Compiles a maxfile in to a .o file"""
		run("%s/bin/sliccompile" % (self.MAXCOMPILERDIR), maxfile, self.maxfile.replace('.max', '.o'))

	def compile(sources):
		for source in sources:
			run(cc, getCompileFlags(), '-c', source, source.replace('.c', '.o'))

	def link(sources, target):
		objects = [s.replace('.c', '.o') for s in sources]
		run(cc, objects, getLinkFlags(), '-o', target)

	def clean():
		autoclean()


