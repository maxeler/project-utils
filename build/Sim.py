#!/usr/bin/env python

import os
import sys
import getpass

MAXCOMPILERDIR = os.environ['MAXCOMPILERDIR']

network_config = [ 
				{ 'NAME' : 'QSFP_TOP_10G_PORT1', 'DFE': '172.16.50.1', 'TAP': '172.16.50.10', 'NETMASK' : '255.255.255.0' }, 
				{ 'NAME' : 'QSFP_BOT_10G_PORT1', 'DFE': '172.16.60.1', 'TAP': '172.16.60.10', 'NETMASK' : '255.255.255.0' }
			] 

class MaxCompilerSim(Executor):
	def __init__(self):
		super(MaxCompilerSim, self).__init__(logPrefix="[MaxCompilerSim] ")

	def getSimName():
		return getpass.getuser() + 'Sim'

	def getSimDeviceName():
		return '%s0:%s' % (getSimName(), getSimName())

	def getSimNameParam():
		return ['-n', getSimName()] 

	def getMaxCompilerSim():
		return ['%s/bin/maxcompilersim' % MAXCOMPILERDIR]

	def getDfeModelParam(dfeModel):
		return ['-c', dfeModel]

	def getNetSimParams(config):
		params = [] 
		for p in config:
			params += ['-e', p['NAME'] + '%s:%s' % (p['TAP'], p['NETMASK'])]
			params += ['-p', p['NAME'] + '%s.pcap' % (p['NAME'])]
		return cmd
	
	def getSimParams(dfeModel, netConfig):
		return getMaxCompilerSim() + getSimNameParam() + getDfeModelParam(dfeModel) + getNetSimParams(netConfig)

	def start(dfeModel="ISCA", netConfig=network_config):
		if self.isRunning():
			print "Cannot start another instance of the simulator. Please stop the previous one."
			return 
		self.execCommand(getSimParams(dfeModel, netConfig))	

	def stop():
		self.kill()

