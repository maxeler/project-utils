import os
import sys


def require(key):
	if not key in os.environ:
		print "[ERROR] Required environment variable not set: %s" % (key)
		sys.exit(1)
	val = os.environ.get(key)
	print "[INFO] Required Environment variable: %s = %s" % (key, val)
	return val


def optional(key):
	if not key in os.environ:
		print "[WARN] Optional environment variable not set: %s" % (key)
		return ""
	
	val = os.environ.get(key)
	print "[INFO] Optional Environment variable: %s = %s" % (key, val)
	return val 


def set(key, value):
	if value:
		print "[INFO] Setting environment %s <-- %s" % (key, value)
		os.environ[key] = value
	else:
		print "[INFO] Unsetting environment variable %s" % (key)
		del os.environ[key]

