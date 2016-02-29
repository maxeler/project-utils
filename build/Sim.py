#!/usr/bin/env python

import os
import sys
import getpass

try:
	import Environment
	import Executor
except ImportError, e:
	print "Couldn't find project-utils modules."
	sys.exit(1)


network_config = [ 
				{ 'NAME' : 'QSFP_TOP_10G_PORT1', 'DFE': '172.16.50.1', 'TAP': '172.16.50.10', 'NETMASK' : '255.255.255.0' }, 
				{ 'NAME' : 'QSFP_BOT_10G_PORT1', 'DFE': '172.16.60.1', 'TAP': '172.16.60.10', 'NETMASK' : '255.255.255.0' }
			] 

class MaxCompilerSim(Executor):
	def __init__(self, dfeModel):
		super(MaxCompilerSim, self).__init__(logPrefix="[MaxCompilerSim] ")
		self.MAXCOMPILERDIR = Environment.require("MAXCOMPILERDIR")
		self.dfeModel = dfeModel

	def getSimName():
		return getpass.getuser() + 'Sim'

	def getSimDeviceName():
		return '%s0:%s' % (getSimName(), getSimName())

	def getSimNameParam():
		return ['-n', getSimName()] 

	def getMaxCompilerSim():
		return ['%s/bin/maxcompilersim' % self.MAXCOMPILERDIR]

	def getDfeModelParam():
		return ['-c', self.dfeModel]

	def getNetSimParams(config):
		params = [] 
		for p in config:
			params += ['-e', p['NAME'] + '%s:%s' % (p['TAP'], p['NETMASK'])]
			params += ['-p', p['NAME'] + '%s.pcap' % (p['NAME'])]
		return cmd
	
	def getSimParams(netConfig):
		return getMaxCompilerSim() + getSimNameParam() + getDfeModelParam() + getNetSimParams(netConfig)

	def start(netConfig=network_config):
		if self.isRunning():
			print "Cannot start another instance of the simulator. Please stop the previous one."
			return 
		self.execCommand(getSimParams(netConfig))	

	def stop():
		self.kill()

