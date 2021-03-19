#coding=UTF-8
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
from common import ConnectServerDevice

cdevice,chierarchyviewer,ceasy_device=ConnectClientDevice()
sdevice,shierarchyviewer,seasy_device=ConnectServerDevice()

# Change Depend On Real Condition
config = ConfigParser.ConfigParser()
config.read(scriptpath+"\\config.ini")

strnumber = config.get("Telephony","sdevice_num")
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

if testtype == "mini":
    ITERATIONS = 5 #50
else:
    ITERATIONS = 50 #50
SucTimes = 0

TestTimes = ITERATIONS*2 + 4

print 'Trace Total Times ' + str(TestTimes)

ID_arr = [id_name.Contact_ID,id_name.Message_ID,id_name.Phone_ID,id_name.Browser_ID,id_name.Camera_ID,id_name.Gstore_ID]

def RemoveActivity():
    print "Remove applications"
    width_w = int(str(width))
    width_w = width_w/4
    height_w = int(str(height))
    height_w = height_w/4
    width_w = int(width_w)
    print 'width_w 2222 ',width_w
    height_w = int(height_w)
    print 'height_w 2222 ',height_w
    try:
        common.startapp(cdevice,ceasy_device,id_name.Remove_ID)
        MonkeyRunner.sleep(2)
        rm_index = 0
        if project_name == 'yaris35_ATT':
            if not ceasy_device.visible(By.id('id/recents_no_apps')):
                while chierarchyviewer.getFocusedWindowName() != id_name.Launcher_ID:
                    rm_index = rm_index + 1
                    print 'rm_index --> ',rm_index
                    cdevice.drag((width_w,height_w*3),(width_w*3,height_w*3),0.2,10, MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(2)
        else:
            print 'other project come here!!!'
            if chierarchyviewer.getFocusedWindowName() != id_name.Launcher_Jrd_ID:
                container_Node = common.GetNode(cdevice,chierarchyviewer,'id/recents_linear_layout')
                if container_Node is None:
                    raise TypeError,"Get Node FAIL"
                number_child_node = container_Node.children.size()
                print 'number_child_node ',number_child_node
                if ceasy_device.visible(By.id('id/recents_clear_button')) and number_child_node > 0:
                    print '6666666666666666'
                    ceasy_device.touchtext(By.id('id/recents_clear_button'),'Clear all',MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(1)
    except Exception,e:
        shotpath = ImagePath + "\\RemoveActivity_exc_" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'RemoveActivity Exception Error: ',e
        traceback.print_exc()
        common.BackToHome(cdevice)
                      
def StartActivity():
    print "Start Some Activities"
    # Start Some Activities
    print 'length ...  ',len(ID_arr)
    for add_index in range(len(ID_arr)):
        common.startapp(cdevice,ceasy_device,ID_arr[add_index])
        if common.isEnterApp(ceasy_device,ID_arr[add_index]):
            add_index = add_index + 1
            print 'add_index ---> ',add_index
        cdevice.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)
    print 'add_index start total ',add_index

def MackeCall(dailtimes):
    global SucTimes
    
    print "Clean up battery full popup before make call"
    common.BatteryFull(ceasy_device)
    common.BatteryFull(seasy_device)
    if EnterDial():
        try:
            DialNumber(strnumber)
            if isReceived(shierarchyviewer):
                MonkeyRunner.sleep(2)
                sdevice.press('KEYCODE_CALL',MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                SucTimes = SucTimes + 1
                print "Trace Success Make Call"
                #add by jianke 08/06
                common.BackToHome(cdevice)
                #end
                return True
            else:
                shotpath = ImagePath + "\\Fail_MCall_" + str(dailtimes) + ".png"
                common.SaveFailImg(cdevice,shotpath)
                shotpath1 = ImagePath + "\\Fail_SCall" + str(dailtimes) + ".png"
                common.SaveFailImg(sdevice,shotpath1)
                #add by jianke 07/14
                if ceasy_device.visible(By.id('id/endButton')):
                    ceasy_device.touch(By.id('id/endButton'),MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(2)
                #end
        except Exception,e:
            shotpath = ImagePath + "\\MackeCall_exc.png"
            common.SaveFailImg(cdevice,shotpath)
            print 'MackeCall Exception Error: ',e
            traceback.print_exc()
            return False

def EnterDial():
    print "First make sure clean up battery full popup"
    common.BatteryFull(ceasy_device)
    common.BatteryFull(seasy_device)
    
    print "Enter Telephony And Wait"
    #jianke 07/10
    if common.startapp(cdevice,ceasy_device,id_name.Phone_ID):
        bar = common.GetNode(cdevice,chierarchyviewer,'id/action_bar_container')
        if bar is None:
            raise TypeError,"Get Node FAIL"
        dial =  chierarchyviewer.getAbsoluteCenterOfView(bar.children[2].children[0].children[0])
        cdevice.touch(dial.x,dial.y,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        return True
    return False

def DialNumber(strnum):
    print "Dial Number"
    #add by jianke 07/27
    #test
    Digit_Node = common.GetNode(cdevice,chierarchyviewer,'id/digits')
    if Digit_Node is None:
        raise TypeError,"Get Node FAIL"
    #end
    numbers = ''
    try:
        numbers = ceasy_device.getText(By.id('id/digits'))
        if numbers == None:
            numbers = ''
        print 'numbers ',numbers
    except:
        print 'numbers is null'
    if numbers <> '':
        for deltetime in range(len(numbers)):
            ceasy_device.touch(By.id('id/deleteButton'),MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(0.5)
    #end
    cdevice.type(strnum)
    MonkeyRunner.sleep(1)
    ceasy_device.touch(By.id('id/dialButton'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(3)

def isReceived(hierarchyviewer = chierarchyviewer):
    wait_time = 0
    while id_name.CALLSCREEN_ID != hierarchyviewer.getFocusedWindowName():
        wait_time = wait_time + 1
        MonkeyRunner.sleep(1)
        print 'wait_time ',wait_time
        if wait_time > 24:
            print "Fail Accept The incoming call"
            return False
    print "Accept The incoming call"
    return True

def interaction(times):
    global SucTimes
    
    width_w = int(str(width))
    width_w = width_w/2
    height_w = int(str(height))
    height_w = height_w/2
    width_w = int(width_w)
    print 'width_w 2222 ',width_w
    height_w = int(height_w)
    print 'height_w 2222 ',height_w
    
    print "Switch applications"
    for loop in range(times):
        try:
            #common.startapp(cdevice,ceasy_device,id_name.Remove_ID)
            #cdevice.press('KEYCODE_BUTTON_SELECT', MonkeyDevice.DOWN_AND_UP)
            #add by jianke 07/25
            Flag_rem = True
            remove_start_times = 0
            remove_wind = chierarchyviewer.getFocusedWindowName()
            while id_name.Remove_ID != remove_wind:
                print 'start Remove_ID ',remove_start_times
                remove_start_times = remove_start_times + 1
                if remove_start_times > 2:
                    Flag_rem = False
                    break
                common.startapp(cdevice,ceasy_device,id_name.Remove_ID)
                remove_wind = chierarchyviewer.getFocusedWindowName()
                MonkeyRunner.sleep(2)
                
            if id_name.Remove_ID != chierarchyviewer.getFocusedWindowName():
                print 'send command!!!'
                cdevice.shell('sendevent /dev/input/event3 1 330 1')
                cdevice.shell('sendevent /dev/input/event3 3 53 270')
                cdevice.shell('sendevent /dev/input/event3 3 54 510')
                cdevice.shell('sendevent /dev/input/event3 0 2 0')
                cdevice.shell('sendevent /dev/input/event3 0 0 0')
                cdevice.shell('sendevent /dev/input/event3 3 48 128')
                cdevice.shell('sendevent /dev/input/event3 3 24 0')
                cdevice.shell('sendevent /dev/input/event3 1 330 0')
                MonkeyRunner.sleep(2)
                if chierarchyviewer.getFocusedWindowName() == id_name.Remove_ID:
                    print 'get with command !!!! '
                    Flag_rem = True
            #end
            if Flag_rem:
                for loop_times in range(3):
                    cdevice.drag((width_w,height_w),(width_w,height_w*2),0.1,10)
                MonkeyRunner.sleep(1)
                tempid = chierarchyviewer.getFocusedWindowName()
                List_Node = common.GetNode(cdevice,chierarchyviewer,'id/recents_linear_layout')
                while List_Node is None:
                    #add by jianke 07/17 For refresh slow
                    MonkeyRunner.sleep(3)
                    refresh_node_times = 0
                    List_Node = common.GetNode(cdevice,chierarchyviewer,'id/recents_linear_layout')
                    refresh_node_times = refresh_node_times + 1
                    if refresh_node_times > 1:
                        print 'don not get the node!'
                        break
                    #end
                FirstItemPos = chierarchyviewer.getAbsoluteCenterOfView(List_Node.children[0])
                cdevice.touch(FirstItemPos.x,FirstItemPos.y, MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(3)
                cunrrentid = chierarchyviewer.getFocusedWindowName()
                if tempid == cunrrentid:
                    shotpath = ImagePath + "\\Fail_Interaction_" + str(loop+1) + ".png"
                    common.SaveFailImg(cdevice,shotpath)
                else:
                    SucTimes = SucTimes + 1
                    print "Trace Success Loop " + str(loop+1)
                    #add by jianke 03/25
                    cdevice.press('KEYCODE_BACK',MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(0.5)
                    #end
        except Exception,e:
            shotpath = ImagePath + "\\Interaction_exc_" + str(loop+1) + ".png"
            common.SaveFailImg(cdevice,shotpath)
            print 'interaction Exception Error: ',e
            traceback.print_exc()
            common.BackToHome(cdevice)

def EndCall():
    global SucTimes
    
    try:
        if HangUpCall():
            SucTimes = SucTimes + 1
            print "Trace Success End Call"
            return True
        else:
            seasy_device.touch(By.id('id/endButton'),MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(2)
    except Exception,e:
        shotpath = ImagePath + "\\EndCall_exc.png"
        common.SaveFailImg(cdevice,shotpath)
        print 'EndCall Exception Error: ',e
        traceback.print_exc()
        return False

def ReturnToCall():
    List_Node = common.GetNode(cdevice,chierarchyviewer,'id/dialpadChooser')
    if List_Node is None:
        raise TypeError,"Get Node FAIL"
    RETURNPOS = chierarchyviewer.getAbsoluteCenterOfView(List_Node.children[1]) 
    cdevice.touch(RETURNPOS.x,RETURNPOS.y, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(3)

def GetDialIconLoc():
    try:
        layout_node = common.GetNode(cdevice,chierarchyviewer,'id/layout')
        if layout_node is None:
            raise TypeError,"Get Node FAIL"
        layout_dial_node = layout_node.children[0].children[1]
        layout_dial_node_point = chierarchyviewer.getAbsoluteCenterOfView(layout_dial_node)
        print 'layout_dial_node_point ',layout_dial_node_point
    except:
        layout_dial_node_point = [32,449]
    return layout_dial_node_point
    
def HangUpCall():
    #jianke 07/10
    TELEPHONYPOS = GetDialIconLoc()
    print 'TELEPHONYPOS ',TELEPHONYPOS
    common.BackToHome(cdevice)
    try:
        cdevice.touch(TELEPHONYPOS.x,TELEPHONYPOS.y,MonkeyDevice.DOWN_AND_UP)
    except:
        cdevice.touch(TELEPHONYPOS[0],TELEPHONYPOS[1],MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    ReturnToCall()
    # Hang up
    ceasy_device.touch(By.id('id/endButton'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    if id_name.Launcher_Andr_ID == chierarchyviewer.getFocusedWindowName():
        print '_____sucess______'
        return True
    else:
        print '_____fail______'
        shotpath = ImagePath + "\\Fail_EndCall.png"
        common.SaveFailImg(cdevice,shotpath)
        return False

def EnterBrowser():
    print "Lauch Browser And Wait"
    #add by jianke 03/20
    if common.isEnterApp(ceasy_device,id_name.Browser_ID) or common.startapp(cdevice,ceasy_device,id_name.Browser_ID):
        text = chierarchyviewer.getFocusedWindowName()
        br_times = 0
        while text != id_name.Browser_ID:
            br_times = br_times + 1
            MonkeyRunner.sleep(2)
            print 'br_times ',br_times*2
            text = chierarchyviewer.getFocusedWindowName()
            if br_times > 2:
                print '1111111111111111111'
                return False
        return True
    return False
    #end

def RefreshPage():
    print 'Refresh Page'
    width_w = int(str(width))
    width_w = width_w/2
    height_w = int(str(height))
    height_w = height_w/2
    width_w = int(width_w)
    print 'width_w 2222 ',width_w
    height_w = int(height_w)
    print 'height_w 2222 ',height_w
    
    cdevice.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    #add by jianke 04/08
    text = chierarchyviewer.getFocusedWindowName()
    print 'text ',text
    br_times = 0
    while text != id_name.BROWSER_DLG_APPID:
        br_times = br_times + 1
        cdevice.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)
        text = chierarchyviewer.getFocusedWindowName()
        print 'text22 ',text
        if br_times > 2:
            return False
    if text == id_name.BROWSER_DLG_APPID:
        cdevice.drag((width_w,height_w),(width_w,height_w*2),0.1,10) 
        MonkeyRunner.sleep(0.5) 
        ceasy_device.touchtext(By.id('id/title'),'Refresh',MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    return True
    #end
        
def StartBrowser():
    global SucTimes
    
    try:
        if EnterBrowser():
            RefreshPage()
            SucTimes = SucTimes + 1
            print "Trace Success Start Browser"
            #add by jianke 08/06
            common.BackToHome(cdevice)
            #end
            return True
        shotpath = ImagePath + "\\Fail_StartBrowser.png"
        common.SaveFailImg(cdevice,shotpath)
        return False
    except Exception,e:
        shotpath = ImagePath + "\\StartBrowser_exc.png"
        common.SaveFailImg(cdevice,shotpath)
        print "StartBrowser Exception Error:",e
        traceback.print_exc()

def IsMainCotent():
    maxtimes = 0
    print 'IsMainCotent '
    while not ceasy_device.visible(By.id('id/main_content')):
        maxtimes = maxtimes + 1
        cdevice.press('KEYCODE_BACK',MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        if maxtimes > 3:
            return False
    return True


def CloseBrowser():
    global SucTimes
    
    try:
        if EnterBrowser() and IsMainCotent():
            cdevice.press('KEYCODE_MENU',MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(2)
            ceasy_device.touchtext(By.id('id/title'),'Close',MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            maxtimes_close = 0
            while True:
                maxtimes_close = maxtimes_close + 1
                print 'maxtimes_close ',maxtimes_close
                if ceasy_device.visible(By.id('id/parentPanel')):
                    MonkeyRunner.sleep(2)
                    ceasy_device.touchtext(By.id('id/text1'),'Quit',MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(1)
                    winid = chierarchyviewer.getFocusedWindowName()
                    if winid == id_name.Launcher_ID:
                        SucTimes = SucTimes +1
                        print 'Trace Success Close Browser'
                        return True
                if maxtimes_close > 5:
                    break
        shotpath = ImagePath + "\\Fail_CloseBrowser.png"
        common.SaveFailImg(cdevice,shotpath)
        return False
    except Exception,e:
        shotpath = ImagePath + "\\CloseBrowser_exc_.png"
        common.SaveFailImg(cdevice,shotpath)
        print "CloseBrowser Exception Error:",e
        traceback.print_exc()

def main():
    global ImagePath

    time_Start = common.timeCalc()
    print 'Start Multi tasking Test'
    # Create Folders To Save Imgs Of Result
    ImagePath = common.CreateFolder('5.1.8')
    common.ShowDeviceMemoryInfo(cdevice)
    common.BackToHome(cdevice)
    
    print "First make sure clean up battery full popup"
    common.BatteryFull(ceasy_device)
    common.BatteryFull(seasy_device)

    # remove applications run
    if True:
        RemoveActivity()
    # some applications shall be running
    if True:
        StartActivity()
    
    #------------1---------------
    if True:
        dailtimes = 1
        while dailtimes < 4:
            if (MackeCall(dailtimes)):
                interaction(ITERATIONS)
                EndCall()
                break
            else:
                dailtimes = dailtimes + 1
                print 'dial again! ',dailtimes
                continue

    #------------2-----------------
    if True:
        if StartBrowser():
            interaction(ITERATIONS)
            CloseBrowser()

    common.BackToHome(cdevice)
    print "Finished Multi-Tasking Test"
    common.ShowDeviceMemoryInfo(cdevice)
    print "Success Times: ", SucTimes
    Rate = SucTimes/TestTimes*100
    if Rate < 99:
        print 'Result Fail Success Rate Is ' + str(Rate) + '%'
    else:
        print 'Result Pass Success Rate Is ' + str(Rate) + '%'
    timeEnd = common.timeCalc()
    totalTime = timeEnd - time_Start
    print '5.1.08_Multi_Tasking time = ' + str(totalTime) + 'mins'

# Scrpit End
if __name__ == "__main__":
    main()
#  Scrpit End







