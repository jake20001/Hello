#coding=UTF-8
#-------------------------------------------------------------------------------
#Title:                 Preconfig
#Precondition:          clear mtk log
#Description:           Used for Yaris_3.5_ATT
#Platform:              4.2.2
#Resolution:            320x480
#Version:               
#Auther:                jianke.zhang
#-------------------------------------------------------------------------------
from __future__ import division
import os
import sys
import string
import random
import traceback
import ConfigParser
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from com.android.monkeyrunner.easy import By


scriptpath=sys.path[0][sys.path[0].find(':')+1:]+"\\..\\common"
crrentpath = sys.path[0][sys.path[0].find(':')+1:]
contactDatapath = crrentpath + '\\contactData.txt'
sys.path.append(scriptpath)
import common
from common import ConnectClientDevice


cdevice,chierarchyviewer,ceasy_device=ConnectClientDevice()

MTKLog_ID = 'com.mediatek.mtklogger/com.mediatek.mtklogger.MainActivity'
folder_act  = 'com.mediatek.mtklogger/com.mediatek.mtklogger.LogFolderListActivity'

SucTimes = 0

def EnterMTKLog(device = cdevice,easy_device = ceasy_device,hierarchyviewer = chierarchyviewer):
    print "Launch MTKLog And Wait"
    if common.isEnterApp(easy_device,MTKLog_ID) or common.startapp(device,easy_device,MTKLog_ID):
        MonkeyRunner.sleep(1)
        return True
    return False

def getTimeShow():
    time_view_node = common.GetNode(cdevice,chierarchyviewer,'id/timeTextView')
    if time_view_node is None:
        raise TypeError,"Get Node FAIL"
    time_view_text = chierarchyviewer.getText(time_view_node)
    print 'time_view_text ' + str(time_view_text)
    return str(time_view_text)

def justClear():
    #test begin
    clear_node = common.GetNode(cdevice,chierarchyviewer,'id/split_action_bar')
    if clear_node is None:
        raise TypeError,"Get Node FAIL"
    clear_action = clear_node.children[0].children[1]
    clear_text = chierarchyviewer.getText(clear_action)
    print 'clear_text ' + str(clear_text)
    #test end
        
    clear_itemPos = chierarchyviewer.getAbsoluteCenterOfView(clear_action)
    cdevice.touch(clear_itemPos.x,clear_itemPos.y,MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    '''
    ceasy_device.touchtext(By.id('id/0xc'),str(clear_text),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    '''
    ceasy_device.touchtext(By.id('id/button1'),'OK',MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    timeclear = 0
    while chierarchyviewer.getFocusedWindowName() != MTKLog_ID:
        print '0000000000'
        MonkeyRunner.sleep(1)
        timeclear = timeclear + 1
    print 'timeclear ' + str(timeclear)
    if chierarchyviewer.getFocusedWindowName() == MTKLog_ID:
        ceasy_device.touch(By.id('id/startStopToggleButton'),MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    timestartagain = 0
    while chierarchyviewer.getFocusedWindowName() != MTKLog_ID:
        MonkeyRunner.sleep(1)
        timestartagain = timestartagain + 1
    print 'timestartagain ' + str(timestartagain)

def justStart():
    global SucTimes
    if chierarchyviewer.getFocusedWindowName() == MTKLog_ID:
        ceasy_device.touch(By.id('id/startStopToggleButton'),MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        SucTimes = SucTimes + 1
    timestartagain2 = 0
    while chierarchyviewer.getFocusedWindowName() != MTKLog_ID:
        MonkeyRunner.sleep(1)
        timestartagain2 = timestartagain2 + 1
    print 'timestartagain2 ' + str(timestartagain2)
    
def clearStartAction():
    ceasy_device.touch(By.id('id/clearLogImageButton'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    if chierarchyviewer.getFocusedWindowName() == folder_act:
        print 'justClear --------- '
        justClear()
    else:
        print 'justStart -------- '
        justStart()

def setCardMemo(title_a=None,title_b=None):
    ceasy_device.touchtext(By.id('id/title'),title_a,MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    ceasy_device.touchtext(By.id('id/title'),title_b,MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    input_node = common.GetNode(cdevice,chierarchyviewer,'id/edit')
    if input_node is None:
        raise TypeError,"Get Node FAIL"
    input_node_itemPos = chierarchyviewer.getAbsoluteCenterOfView(input_node)
    cdevice.touch(input_node_itemPos.x,input_node_itemPos.y,MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.5)
    for loop in range(6):
        cdevice.touch(288,408,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(0.5) 
    ceasy_device.type(By.id('id/edit'),'30000')
    MonkeyRunner.sleep(1)
    ceasy_device.touchtext(By.id('id/button1'),'OK',MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.5)
    
def setMomeAndClear():
    bar_node = common.GetNode(cdevice,chierarchyviewer,'id/action_bar')
    if bar_node is None:
        raise TypeError,"Get Node FAIL"
    right_bar_node = bar_node.children[1]
    right_bar_itemPos = chierarchyviewer.getAbsoluteCenterOfView(right_bar_node)
    cdevice.touch(right_bar_itemPos.x,right_bar_itemPos.y,MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    #1
    ceasy_device.touchtext(By.id('id/title'),'Log storage location',MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    ceasy_device.touchtext(By.id('id/text1'),'SD Card',MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    #2
    setCardMemo('MobileLog','Limit Log Size(MB)')
    #3
    setCardMemo('ModemLog','Limit Log Size(MB)')
    #4
    setCardMemo('NetworkLog','Limit Log Size(MB)')
    #clear and open
    cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.5)
    #Clear and Start
    clearStartAction()
    
def clearMtkLog():
    time1 = getTimeShow()
    MonkeyRunner.sleep(2)
    time2 = getTimeShow()
    if time1 != time2:
        print 'already logging begin'
        ceasy_device.touch(By.id('id/startStopToggleButton'),MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        timestop = 0
        while chierarchyviewer.getFocusedWindowName() != MTKLog_ID:
            MonkeyRunner.sleep(1)
            timestop = timestop + 1
        print 'timestop ' + str(timestop)
        clearStartAction()
    else:
        print 'no start logging begin'
        setMomeAndClear()
    #back
    print 'Clear Over and Start Logging!'
    common.BackToHome(cdevice)

def showMtkFile():
    content = cdevice.shell("ls /storage/sdcard0/")
    num = content.count("mtklog")
    print "mtklog num is",num
    return num

def rmTtkLogFile():
    global SucTimes
    numa = showMtkFile()
    if numa>0:
        for i in range(numa+1):
            cdevice.shell("rm -rf /storage/sdcard0/mtklog")
    numb = showMtkFile()
    if numb == 0:
        print "Trace Success Loop "
        print 'rm mtklog File'
        SucTimes = SucTimes + 1
    else:
        print 'failed delete'
        
def main():
    global SucTimes
    print '------------Start preconfig------------'
    common.ShowDeviceMemoryInfo(cdevice)
    common.BackToHome(cdevice)
    #-----enter mtkLog--------
    '''
    if EnterMTKLog():
        clearMtkLog()
    '''
    '''
    #for first time
    if EnterMTKLog():
        setMomeAndClear()
    '''
    rmTtkLogFile()
    print '---------------------'
    MonkeyRunner.sleep(10)
    
    if EnterMTKLog():
        justStart()
    #back below is not nessary,because next loop also run this line code
    print 'Clear Over and Start Logging!'
    common.BackToHome(cdevice)
    Rate = SucTimes/2*100
    if Rate != 100 :
        print 'Result Fail Success Rate Is ' + str(Rate) + '%'
    else:
        print 'Result Pass Success Rate Is ' + str(Rate) + '%'
    

if __name__ == "__main__":
    main()
# Scrpit End
