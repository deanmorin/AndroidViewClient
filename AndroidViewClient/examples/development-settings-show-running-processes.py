#! /usr/bin/env monkeyrunner
'''
Created on Feb 3, 2012

@author: diego
'''


import re
import sys
import os

# this must be imported before MonkeyRunner and MonkeyDevice,
# otherwise the import fails
try:
    ANDROID_VIEW_CLIENT_HOME = os.environ['ANDROID_VIEW_CLIENT_HOME']
except KeyError:
    print >>sys.stderr, "%s: ERROR: ANDROID_VIEW_CLIENT_HOME not set in environment" % __file__
    sys.exit(1)
sys.path.append(ANDROID_VIEW_CLIENT_HOME + '/src')
from com.dtmilano.android.viewclient import ViewClient

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

STATUS_BAR = 38
TITLE = 40
CHECK_BOX = 50

# 01-04 18:23:42.000: I/ActivityManager(4288): Displayed com.android.development/.DevelopmentSettings: +379ms
package = 'com.android.development'                                          
activity = '.DevelopmentSetting'                           
componentName = package + "/" + activity                        
device = MonkeyRunner.waitForConnection(60)
if not device:
	raise Exception('Cannot connect to device')

device.startActivity(component=componentName)
vc = ViewClient(device)
vc.dump()
print vc.getViewIds().keys()

showCpu = vc.findViewById("id/show_cpu")
showLoad = vc.findViewById("id/show_load")
alwaysFinish = vc.findViewById("id/always_finish")

if showLoad.isChecked() == 'false':
    showLoad.touch()

if alwaysFinish['isChecked()'] == 'false':
    alwaysFinish.touch()
