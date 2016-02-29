import os
import sys


def require(key):
	if not key in os.environ:
		print "Required environment variable not set: %s." % (key);
		sys.exit(1)
	return os.environ

