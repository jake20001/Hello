#coding=UTF-8
#*****************************************************************************
# Title:        5.1.05_Store_Front_Download
# Precondition: 
# Description:  Used for Yaris-3.5-att
# Platform:     4.2.2
# version:      SWC68
# Resolution:   320x480
# Modify :      Jake
#*****************************************************************************
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
sys.path.append(scriptpath)
import common
from common import ConnectClientDevice
#from common import ConnectServerDevice


cdevice,chierarchyviewer,ceasy_device=ConnectClientDevice()
#sdevice,shierarchyviewer,seasy_device=ConnectServerDevice()

# Change Depend On Real Condition
config = ConfigParser.ConfigParser()
config.read(scriptpath+"\\config.ini")

supportedNetworkType = config.get("Common", "SUPPORTED_NETWORK_TYPE")
testtype = config.get("Default", "TEST_TYPE")
#add by jianke 07/08/2014
project_name = config.get("Project", "project_name")
print 'project_name ',project_name
config_pixel = ConfigParser.ConfigParser()
if project_name == 'yaris35_ATT':
    config_pixel.read(scriptpath + "\\yaris35_att.ini")
    import yaris35_att_id
    id_name = yaris35_att_id
else:
    print 'other project may add'
#end
#add by jianke 07/04/2014
width = config_pixel.get("Pixel", "width")
height = config_pixel.get("Pixel", "height")
width = width.strip()
height = height.strip()
print 'width ',width
print 'height ',height
#end

#add by jianke 14/06/10 for test
Flag_mini = True
#end

if supportedNetworkType == "2G3GLTE":
    if testtype == "mini":
        OPENCLOSE = 2
        DOWNLOAD2G = 2
        DOWNLOAD3G = 2
        DOWNLOADLTE = 2
        OPENAPP = 6
        DELETETIMES = 6
    else:
        OPENCLOSE = 20
        DOWNLOAD2G = 1
        DOWNLOAD3G = 4
        DOWNLOADLTE = 5
        OPENAPP = 10
        DELETETIMES = 10
    TestTimes = OPENCLOSE + DOWNLOAD2G + DOWNLOAD3G + DOWNLOADLTE + OPENAPP + DELETETIMES
if supportedNetworkType == "2G3G":
    if testtype == "mini":
        if Flag_mini:
            OPENCLOSE = 2 #20
            DOWNLOAD2G = 1 #2
            DOWNLOAD3G = 1 #8
        else:
            OPENCLOSE = 2 #20
            DOWNLOAD2G = 1 #2
            DOWNLOAD3G = 4 #8
    else:
        OPENCLOSE = 20 #20
        DOWNLOAD2G = 0 #2
        DOWNLOAD3G = 10 #8
    TestTimes = OPENCLOSE + (DOWNLOAD2G + DOWNLOAD3G)*3

print 'Trace Total Times ' + str(TestTimes)

SucTimes = 0

Appname = ["TCTTemperature"]

# Create Folders To Save Imgs Of Result
ImagePath = common.CreateFolder('5.1.5')

def func(obj):   
    str2 = obj[6:]
    str3 = ''
    flag = False
    for c in str2:
        if c.isdigit():
            str3 = str3 + c
            flag = True    
        else:
            if flag:
                break
    return str3

#add by jianke 04/18
def message_pop():
    if ceasy_device.visible(By.id('id/message')):
        if ceasy_device.getText(By.id('id/message')).find('Enjoy your app') > -1:
            if ceasy_device.visible(By.id('id/button1')):
                ceasy_device.touch(By.id('id/button1'), MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
            if ceasy_device.visible(By.id('id/yes')):
                ceasy_device.touch(By.id('id/yes'), MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
            if ceasy_device.visible(By.id('id/done')):
                ceasy_device.touch(By.id('id/done'), MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(3)
        return True
    return False

#end    
def EnterStore():
    print "Lauch Store And Wait"
    '''
    obj = cdevice.shell('ps | grep com.android.vending')
    #print 'obj ' + str(obj)
    strb = func(obj)
    #print 'strb ' + str(strb)
    obj = cdevice.shell('kill ' + strb)
    #print 'obj1 ' + str(obj) 
    obj = cdevice.shell('ps | grep com.android.vending')
    #print 'obj2 ' + str(obj)
    '''
    
    #add by jianke 04/30 002
    progress_time = 0
    if common.isEnterApp(ceasy_device,id_name.GSTORE_ID) or common.startapp(cdevice,ceasy_device,id_name.GSTORE_ID):
        while ceasy_device.visible(By.id('id/placeholder_loading')):
            progress_time = progress_time + 1
            print 'progress_time ',progress_time
        else:
            print 'progress_time MAX ',progress_time
            return True
    return False

def OpenCloseStore(times):
    global SucTimes
    
    for loop in range(times):
        common.BackToHome(cdevice)
        if EnterStore():
            MonkeyRunner.sleep(10)
            SucTimes = SucTimes + 1
            print "Trace Success Loop " + str(loop+1)
    common.BackToHome(cdevice)

#-----------------------------------------------------------
def EnterMenu(stritem):
    action_bar_node =  common.GetNode(cdevice,chierarchyviewer,"id/action_bar")
    if action_bar_node is None:
        raise TypeError,"Get Node FAIL"
    menu_node = action_bar_node.children[2].children[1]
    menu_pos = chierarchyviewer.getAbsoluteCenterOfView(menu_node)
    cdevice.touch(menu_pos.x,menu_pos.y, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    ceasy_device.touchtext(By.id('id/title'),stritem,MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(20)


def InstallApp(loop):
    max_time = 0
    wait_continue_Time = 0
    print 'Download And Install The APP'
    install_Flag = True
    if common.GetWind_Id(chierarchyviewer,ceasy_device,id_name.GSTORE_ID,'id/buy_button',1,10,1,10):
        print 'go to ooooooooooooooo'
        ceasy_device.touch(By.id('id/buy_button'),MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)
    else:
        install_Flag = False
    if install_Flag:
        if message_pop():
            DownloadApp(1,loop)
        ErrorPop()
        #continue_button
        while not ceasy_device.visible(By.id('id/positive_button')) and not ceasy_device.visible(By.id('id/continue_button')):
            print 'positive_button ... ',wait_continue_Time
            MonkeyRunner.sleep(2)
            ErrorPop()
            wait_continue_Time += 1
            if ceasy_device.visible(By.id('id/buy_button')):
                print 'buy_button ',wait_continue_Time
                ErrorPop()
                ceasy_device.touch(By.id('id/buy_button'),MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(2)
            if wait_continue_Time > 10:
                print "Couldn't fresh out the contuine button."
                return False
        touch_Times = 0    
        while ceasy_device.visible(By.id('id/positive_button')) or ceasy_device.visible(By.id('id/continue_button')):
            print 'enter continue_button ' ,touch_Times
            if ceasy_device.visible(By.id('id/positive_button')):
                print 'positive_button ............... 07/22'
                ceasy_device.touch(By.id('id/positive_button'), MonkeyDevice.DOWN_AND_UP)
            elif ceasy_device.visible(By.id('id/continue_button')):
                print 'continue_button ............... 07/22'
                ceasy_device.touch(By.id('id/continue_button'), MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(2)
            touch_Times = touch_Times + 1
            if touch_Times > 2:
                return False
        #add by jianke 07/09
        message_pop()
        #end  
        while not ceasy_device.visible(By.id('id/progress_bar')):
            max_time += 1
            if max_time > 10:  
                print "Can not install the app"
                return False
            MonkeyRunner.sleep(max_time)
        print "Start loading..."
        return True
    return False
    
def CloseApp():
    MaxTimes = 0

    while True:
        MaxTimes = MaxTimes + 1
        cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(0.5)
        if ceasy_device.visible(By.id('id/button1')):
            ceasy_device.touch(By.id('id/button1'),MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(2)
            return True
        elif id_name.GSTORE_ID == chierarchyviewer.getFocusedWindowName():
            return True
        if MaxTimes > 3:
            return False

def OpenMyApp(times):
    global SucTimes
    
    if EnterStore():
        #add by jianke 04/30 003
        if isFree_Exist():
            print 'Exist open app Idle '
        else:
            SearchApp()
        #end
        if not isFree(True):
            try:
                print 'Select The Installed APP'
                ceasy_device.touch(By.id('id/launch_button'),MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(2)
                #add by jianke
                if ceasy_device.visible(By.id("id/message")):
                    ceasy_device.touch(By.id('id/button1'),MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(1)
                    if ceasy_device.visible(By.id("id/message")):
                        ceasy_device.touch(By.id('id/button1'),MonkeyDevice.DOWN_AND_UP)
                        MonkeyRunner.sleep(1)
                if chierarchyviewer.getFocusedWindowName() == id_name.GSTORE_ID:
                    return False
                else:
                    print "Open APP Successfully"
                    if not CloseApp():
                        return False
                    else:
                        print "Close APP Successfully"
                        print "Trace Success OpenClose APP Loop " + str(times+1)
                        return True
            except Exception,e:
                shotpath = ImagePath + "\\OpenMyApp_exc_" + str(times+1) + ".png"
                common.SaveFailImg(cdevice,shotpath)
                print "OpenMyApp Exception Error:",e
                traceback.print_exc()
                return False


def isFree(b_free):
    #add by jianke 04/30 001
    index = 0
    while index < 10:
        print 'isFree buy_button 04/30 .... ',ceasy_device.visible(By.id('id/buy_button'))
        print 'isFree launch_button ',ceasy_device.visible(By.id('id/launch_button'))
        if common.GetWind_Id(chierarchyviewer,ceasy_device,id_name.GSTORE_ID,'id/buy_button',1,2,1,3):
            return True
        if common.GetWind_Id(chierarchyviewer,ceasy_device,id_name.GSTORE_ID,'id/launch_button',1,2,1,3):
            if ceasy_device.visible(By.id('id/uninstall_button')) == b_free or ceasy_device.visible(By.id('id/launch_button')) == b_free:
                return False
        index += 1
        print 'index waiting ... ',index

def SearchApp():
    #add by jianke 04/16 001
    if common.Get_keyType(ceasy_device,chierarchyviewer,'id/search_voice_btn',1):
        cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    if common.Get_keyType(ceasy_device,chierarchyviewer,'id/search_button',4):
    #end
        ceasy_device.touch(By.id('id/search_button'),MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)
        for i in range(3):
            print 'i --> ',i
            ceasy_device.type(By.id("id/search_plate"),Appname[0]) #TCTTemperature
            #raw_input()
            MonkeyRunner.sleep(2)
            text_node = common.GetNode(cdevice,chierarchyviewer,'id/search_src_text')
            if text_node is None:
                raise TypeError,"Get Node FAIL"
            text =  chierarchyviewer.getText(text_node)
            if text != None:
                print 'The app name has been input.'
                break
        cdevice.press('KEYCODE_ENTER',MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        MaxTime = 0
        while not ceasy_device.visible(By.id('id/section_corpus_spinner')): 
            MonkeyRunner.sleep(2)
            MaxTime = MaxTime + 1
            if MaxTime > 10:
                break
        if MaxTime > 10:
            print "Search app More Than 20s"
            return False 
        else:
            print 'The app shows.'
            MonkeyRunner.sleep(5)
            #add by jianke 03/20 bucket_list_view
            bucket_list = common.GetNode(cdevice,chierarchyviewer,'id/bucket_list_view')
            if bucket_list is None:
                raise TypeError,"Get Node FAIL"
            ch_num = bucket_list.children.size()
            print 'ch_num ',ch_num
            for index in range(ch_num):
                if str(bucket_list.children[index].id).find('id/bucket_items') > -1:
                    the_num_node = bucket_list.children[index].children[0]
                    list_txt_node = common.GetNode(cdevice,chierarchyviewer,'id/li_title',the_num_node)
                    if list_txt_node is None:
                        raise TypeError,"Get Node FAIL"
                    if chierarchyviewer.getText(list_txt_node).find(Appname[0]) > -1:
                        search_node = chierarchyviewer.getAbsoluteCenterOfView(the_num_node)
                        cdevice.touch(search_node.x,search_node.y,MonkeyDevice.DOWN_AND_UP)
                        MonkeyRunner.sleep(3)
                        return True
            #end
    else:
        print 'it is not seen the search_button'
    return False

#add by jianke 07/17
def ErrorPop():
    #id/alertTitle
    print 'exist error popup from app'
    if ceasy_device.visible(By.id('id/alertTitle')):
        print 'come out error pop!'
        ceasy_device.touchtext(By.id('id/button1'),'OK',MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
#end

#add by jianke 04/30 004
def isFree_Exist():
    ErrorPop()
    #add by jianke 04/30 001
    index = 0
    while index < 1:
        print 'isFree buy_button 04/30 004 .... ',ceasy_device.visible(By.id('id/buy_button'))
        print 'isFree launch_button ',ceasy_device.visible(By.id('id/launch_button'))
        if common.GetWind_Id(chierarchyviewer,ceasy_device,id_name.GSTORE_ID,'id/buy_button',1,2,1,3):
            return True
        if common.GetWind_Id(chierarchyviewer,ceasy_device,id_name.GSTORE_ID,'id/launch_button',1,2,1,3):
            if ceasy_device.visible(By.id('id/uninstall_button')) or ceasy_device.visible(By.id('id/launch_button')):
                return True
        index += 1
    return False
#end

def DownloadApp(times,loop_parent):
    global SucTimes
    
    for loop in range(times):
        try:
            if EnterStore():
                if common.GetWind_Id(chierarchyviewer,ceasy_device,id_name.GSTORE_ID,'id/main_container',1,5,1,6):
                    #add by jianke 04/30 003
                    if isFree_Exist():
                        print 'Exist download Idle'
                    else:
                        SearchApp()
                    #end
                if isFree(True):
                    print '0330 ......... '
                    #modify by jianke 03/30 002
                    if InstallApp(loop_parent):
                        Maxtimes = 0
                        #add by jianke 04/05 001
                        message_pop()
                        #end
                        while not ceasy_device.visible(By.id('id/uninstall_button')):
                            Maxtimes = Maxtimes + 1
                            MonkeyRunner.sleep(10)
                            print 'Maxtimes ',Maxtimes*10
                            message_pop()
                            ErrorPop()
                            if Maxtimes > 60:
                                print "Download APP More Than 10 mins"
                                return False
                        else:
                            print "Download APP Successfully"
                            print "Trace Success Download APP Loop " + str(loop_parent+1)
                            return True
                    elif ceasy_device.visible(By.id('id/uninstall_button')):
                        print "Download APP Successfully"
                        print "Trace Success Download APP Loop " + str(loop_parent+1)
                        return True
                    #end
                else:
                    print "App installed"
                    print "Trace Success Download APP Loop " + str(loop+1)
                    return True
                cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(2)
        except Exception,e:
            shotpath = ImagePath + "\\DownloadApp_exc_" + NetWork_type + "_" + str(loop_parent+1) + ".png"
            common.SaveFailImg(cdevice,shotpath)
            print "DownloadApp Exception Error:",e
            traceback.print_exc()

def DelAllApps(times):
    global SucTimes
    
    if EnterStore():
        #add by jianke 04/30 003
        if isFree_Exist():
            print 'Exist delete app Idle'
        else:
            SearchApp()
        #end
        try:
            if ceasy_device.visible(By.id('id/uninstall_button')):
                ceasy_device.touch(By.id('id/uninstall_button'),MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(2)
                ceasy_device.touch(By.id('id/button1'),MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(10)
                if ceasy_device.visible(By.id('id/buy_button')):
                    print "Delete APP Successfully"
                    print "Trace Success Delete APP Loop " + str(times+1)
                    return True
                else:
                    return False
            else:
                return False
        except Exception,e:
            shotpath = ImagePath + "\\DelAllApps_exc_" + str(times+1) + ".png"
            common.SaveFailImg(cdevice,shotpath)
            print "DelAllApps Exception Error:",e
            traceback.print_exc()
            return False

def DoWholeLoop(times,NetWork_type):
    global SucTimes
    
    for loop in range(times):
        if DownloadApp(1,loop):
            SucTimes = SucTimes + 1  
            if OpenMyApp(loop):
                SucTimes = SucTimes + 1
            else:
                shotpath = ImagePath + "\\Fail_OpenClose_APP_" + str(loop+1) + NetWork_type + ".png"
                common.SaveFailImg(cdevice,shotpath)
            if DelAllApps(loop):
                SucTimes = SucTimes + 1
            else:
                shotpath = ImagePath + "\\Fail_Delete_APP_" + str(loop+1) + NetWork_type + ".png"
                common.SaveFailImg(cdevice,shotpath)
        else:
            shotpath = ImagePath + "\\Fail_Download_APP_" + NetWork_type + '_' + str(loop+1) + ".png"
            common.SaveFailImg(cdevice,shotpath)
            if ceasy_device.visible(By.id('id/cancel_download')):
                ceasy_device.touch(By.id('id/cancel_download'),MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(3)

def main():
    global NetWork_type

    time_Start = common.timeCalc()
    
    print 'Start Store Front Download Test'
    common.ShowDeviceMemoryInfo(cdevice)
    # Return to idle
    common.BackToHome(cdevice)

    #---1------------
    if True:
        print 'Open and close store ' + str(OPENCLOSE)+' Times'
        OpenCloseStore(OPENCLOSE)

    #---2------------

    #---3------------
    if True:
        NetWork_type = '3G'
        print NetWork_type + ' _Do the whole loop ' + str(DOWNLOAD3G) + ' Times'
        DoWholeLoop(DOWNLOAD3G,NetWork_type)
    
    common.BackToHome(cdevice)
    print "Finished Store_Front_Download Test"
    
    common.ShowDeviceMemoryInfo(cdevice)
    print "Success Times:",SucTimes

    Rate = SucTimes/TestTimes*100
    if Rate < 95:
        print 'Result Fail Success Rate Is ' + str(Rate) + '%'
    else:
        print 'Result Pass Success Rate Is ' + str(Rate) + '%'
    timeEnd = common.timeCalc()
    totalTime = timeEnd - time_Start
    print '5.1.05_Store_Front_Download time = ' + str(totalTime) + 'mins'
    
if __name__ == "__main__":
    main()
#  Scrpit End











