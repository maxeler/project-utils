import os
import sys

MAXOSDIR = os.environ['MAXELEROSDIR']
MAXCOMPILERDIR = os.environ['MAXCOMPILERDIR']
MAXNETDIR = os.environ['MAXCOMPILERNETDIR']


def slicCompile(maxfile):
	"""Compiles a maxfile in to a .o file"""
	run("%s/bin/sliccompile" % (MAXCOMPILERDIR), maxfile, maxfile.replace('.max', '.o'))


def getMaxelerOsInc():
	"""return the include paths for MaxelerOS."""
	return ['-I%s/include' % MAXOSDIR]

def getMaxelerOsLibs():
	"""Return the MaxelerOS libraries to be used in linking."""
	return ['-L%s/lib' % MAXOSDIR, '-lmaxeleros']

def getSlicInc():
	"""Return the SLiC include paths."""
	return ['-I%s/include/slic' % MAXCOMPILERDIR]

def getSlicLibs():
	"""Return the SLiC libraries to be used in linking."""
	return ['-L%s/lib' % MAXCOMPILERDIR, '-lslic']

def getMaxNetInc():
	"""Return the include paths for Networking."""
	return ['-I%s/include/slicnet' % MAXNETDIR]

def getMaxNetLibs():
	"""Return the Networking libraries to be used in linking."""
	return ['-L%s/lib' % MAXNETDIR, '-lslicnet']

def getMaxfileLibs(maxfile):
	"""Return the Maxfile object to be used in linking."""
	return [maxfile.replace('.max', '.o')]

def getMaxRuntimeCflags(maxfile):
	"""Return all runtime include paths"""
	DESIGN_NAME = maxfile.replace('.max', '')
	return ['-DDESIGN_NAME=%s' % (DESIGN_NAME)] + getMaxelerOsInc() + getSlicInc() + getMaxNetInc()

def getMaxRuntimeLdflags(maxfile):
	"""Returns the libraries to be used for linking."""
	return getMaxfileLibs(maxfile) + getMaxelerOsLibs() + getSlicLibs() + getMaxNetLibs() + getMaxfileLibs() + ['-lpthread'] 


