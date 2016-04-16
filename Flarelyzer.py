#!/usr/bin/python2.7

#Requirements: libnotify-bin (notify-send), pypy

#TODO: general revamp needed!
#TODO: Qt UI
#TODO: improve exit execution paths

import os
import sys
import time
import signal
from subprocess import Popen, check_call


agent = None
scanner = None
sockfile = '/tmp/flarelyzer.sock'
try:
	os.unlink(sockfile)  #Make sure the socket does not already exist
except OSError, e:
	pass

sudo = ''


def quit():
	global agent
	if agent:
		agent.terminate()
	print '==Terminated=='
	sys.exit(0)
signal.signal(signal.SIGTERM, lambda x, y: quit())


def check_installed(binary):
	try:
		check_call('which ' + binary + ' > /dev/null 2>&1', shell=True)
		return True
	except:
		print 'Could not find ' + binary + ' executable, please install before running Flarelyzer'
		return False

if sys.stdin.isatty():  # Running from terminal
	sudo = 'sudo'
else:
	#select sudo frontend
	sudo = filter(check_installed,['gksu','kdesudo'])[0]
if not sudo or not all(map(check_installed, ['pypy', 'notify-send'])):
	quit()  #if the requirements are not met

try:
	agent = Popen(['pypy', 'agent.py'])
	while not os.path.exists(sockfile):
		time.sleep(0.05)  #probably a hack
	scanner = Popen([sudo, 'pypy', 'memscan.py'])
	scanerror = scanner.wait()
	if not scanerror:
		agent.wait()
	else:
		agent.terminate()
except KeyboardInterrupt:
	print '\nKeyboard Interrupt, closing...'
	quit()

