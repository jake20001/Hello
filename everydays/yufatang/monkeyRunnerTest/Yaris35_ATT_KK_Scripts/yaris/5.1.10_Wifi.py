#*****************************************************************************
# Title:        5.1.10_Wifi
# Precondition: 1.Wifi is clsed and no wifi spot saved
#               2.Make Sure The Spot You Want To Connect Is The First Item
#                 Put Phone With Wifi Hotspot Opened Next To The Device
# Description:  Used for Yaris-3.5-att
# Platform:     4.2.2
# version:      SWC6D
# Resolution:   320x480
# Modify:       Jake
#*****************************************************************************
from __future__ import division
import os
import re
import sys
import string
import traceback
import subprocess
import ConfigParser
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from com.android.monkeyrunner.easy import By
scriptpath = sys.path[0][sys.path[0].find(':')+1:] + "\\..\\common"
sys.path.append(scriptpath)
import common

# Need tool support
environ = os.environ
#mdevice_id = environ.get('MDEVICE')
mdevice,mhierarchyviewer,easy_mdevice = common.ConnectClientDevice()

# Change Depend On Real Condition
config = ConfigParser.ConfigParser()
config.read(scriptpath + "\\config.ini")
SSID = config.get("Wifi","wifi_name")
psw = config.get("Wifi","wifi_password")
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
SucTimes = 0
if testtype == "mini":
    SwitchTimes = 2 #20
    ConnectTimes = 2 #20
else:
    SwitchTimes = 20 #20
    ConnectTimes = 20 #20

TestTimes = SwitchTimes + ConnectTimes
print 'Trace Total Times ' + str(TestTimes)


# Create Folders To Save Imgs Of Result
ImagePath = common.CreateFolder('5.1.10')

def EnterWifi():
    if common.isEnterApp(easy_mdevice,id_name.SubSETTING_ID):
        print "Enter Wifi"
        return True
    print "Enter Settings And Wait 3 Seconds"
    # Launch Settings And Wait
    if common.startapp(mdevice,easy_mdevice,id_name.SETTING_ID):
        # Enter Wifi
        MonkeyRunner.sleep(1)
        List_Node = common.GetNode(mdevice,mhierarchyviewer,'id/list')       
        if List_Node is None:
            raise TypeError,"Get Node FAIL"
        #add by jianke 07/16
        number = List_Node.children.size()
        print 'number ',number
        for lp in range(number):
            lst_node_name = List_Node.children[lp].name
            print 'lst_node_name ',lst_node_name
            if lst_node_name.find('LinearLayout') > -1:
                text_Node = common.GetNode(mdevice,mhierarchyviewer,'id/title',List_Node.children[lp])
                if text_Node is None:
                    raise TypeError,"Get Node FAIL"
                if mhierarchyviewer.getText(text_Node).find('Wi-Fi') > -1:
                    WIFI_Node = mhierarchyviewer.getAbsoluteCenterOfView(List_Node.children[lp])
                    mdevice.touch(WIFI_Node.x,WIFI_Node.y,MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(3)
        #end
        if common.isEnterApp(easy_mdevice,id_name.SubSETTING_ID):
            print "Enter Wifi"
            return True
    return False
    
def BackToWifi():
    for i in range(5):
        if common.isEnterApp(easy_mdevice,id_name.SubSETTING_ID):
            break
        mdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)

def OpenCloseWifi():
    bar_node = common.GetNode(mdevice,mhierarchyviewer,'id/action_bar')
    if bar_node is None:
        raise TypeError,"Get Node FAIL"
    Switch_Node = bar_node.children[1]
    Switch_Pos = mhierarchyviewer.getAbsoluteCenterOfView(Switch_Node)
    mdevice.touch(Switch_Pos.x,Switch_Pos.y,MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(8)
    return True

def ConfirmWifiStatus(b_ex_open):
    Maxtime = 0
    while True:
        if b_ex_open == easy_mdevice.visible(By.id('id/empty')):
            OpenCloseWifi()
            Maxtime = Maxtime + 1
            if (Maxtime) > 3:
                return False
        else:
            return True

def SwitchWifi(times):
    global SucTimes
    
    for loop in range(times):
        if EnterWifi():
            # Make wifi close at first
            if not ConfirmWifiStatus(False):
                print "Wifi Can not close at first"
                continue
            try:
                # Open Wifi And Wait 10 seconds
                print "Open Wifi And Wait 10 seconds"
                OpenCloseWifi()
                if easy_mdevice.visible(By.id('id/empty')):
                    shotpath = ImagePath + "\\Fail_OpenWifi_" + str(loop+1) + ".png"
                    common.SaveFailImg(mdevice,shotpath)
                    continue
                else:
                    print "Open Wifi Successfully"
                # Close Wifi And Wait 10 seconds
                OpenCloseWifi()
                if not easy_mdevice.visible(By.id('id/empty')):
                    shotpath = ImagePath + "\\Fail_CloseWifi_" + str(loop+1) + ".png"
                    common.SaveFailImg(mdevice,shotpath)
                else:
                    SucTimes += 1
                    print "Close Wifi Successfully"
                    print "Trace Success Loop " + str(loop+1)
            except Exception,e:
                shotpath = ImagePath + "\\switchWifi_exc_" + str(loop+1) + ".png"
                common.SaveFailImg(mdevice,shotpath)
                print "SwitchWifi Exception Error: " ,e
                traceback.print_exc()
                #BackToWifi()
        else:
            print "Can not enter Wifi"

def GetConnectionStatus(device = mdevice):
    status = device.shell("ifconfig wlan0")
    m = re.search(r'wlan0:\sip\s[\d\.]+\smask.*\[up', status)
    if m is not None:
        return True
    return False

def Addwifi(SSID):
    # Add Wifi
    print 'Add Wifi'
    easy_mdevice.touch(By.id('0x4'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    mdevice.type(SSID)
    MonkeyRunner.sleep(1)
    mdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    # Save Wifi
    easy_mdevice.touch(By.id('id/button1'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    print 'Connecting...'
    Maxtime = 0
    while not GetConnectionStatus():
        MonkeyRunner.sleep(2)
        Maxtime = Maxtime + 1
        if (Maxtime) > 30:
            return False
    return True

def Selectwifi(SSID):
    print "Select wifi"
    width_w = int(str(width))
    width_w = width_w/2
    height_w = int(str(height))
    height_w = height_w/4
    width_w = int(width_w)
    print 'width_w 2222 ',width_w
    height_w = int(height_w)
    print 'height_w 2222 ',height_w
    
    for loop_i in range(2):
        mdevice.drag((width_w,height_w),(width_w,height_w*3),0.5,10)
        MonkeyRunner.sleep(0.5)
    
    for attempt in range(3):
        flag = False
        prefs_node = common.GetNode(mdevice,mhierarchyviewer,'id/prefs')
        if prefs_node is None:
            raise TypeError,"Get Node FAIL"
        list_node = common.GetNode(mdevice,mhierarchyviewer,'id/list',prefs_node.children[0])
        if list_node is None:
            raise TypeError,"Get Node FAIL"
        item_number = list_node.children.size()
        print 'item_number ',item_number
        for order in range(item_number-1):
            title_node =  common.GetNode(mdevice,mhierarchyviewer,'id/title',list_node.children[order])
            if title_node is None:
                raise TypeError,"Get Node FAIL"
            #add by jianke 08/01
            print 'title_node',mhierarchyviewer.getText(title_node)
            if SSID == mhierarchyviewer.getText(title_node):
                print 'touch to get pwd input'
                ssid_times = 0
                title_Pos = mhierarchyviewer.getAbsoluteCenterOfView(title_node)
                mdevice.touch(title_Pos.x,title_Pos.y,MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(3)
                while not easy_mdevice.visible(By.id('id/customPanel')):
                    mdevice.touch(title_Pos.x,title_Pos.y,MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(2)
                    ssid_times = ssid_times + 1
                    print 'ssid_times ',ssid_times
                    if ssid_times > 2:
                        break
                if ssid_times < 3:
                    flag = True
                break
        if flag:
            if psw != "":
                MonkeyRunner.sleep(1)
                #add by jianke 08/04
                alertTitle_node=common.GetNode(mdevice,mhierarchyviewer,'id/alertTitle')
                if SSID == mhierarchyviewer.getText(alertTitle_node):
                    common.Get_keyBoard_wind(mdevice,mhierarchyviewer,'id/parentPanel',250)
                    easy_mdevice.type(By.id('id/password'),psw)
                    MonkeyRunner.sleep(2)
                    print 'password ',psw
                    #add by jianke 08/04
                    password_node = common.GetNode(mdevice,mhierarchyviewer,'id/password')
                    if password_node is None:
                        raise TypeError,"Get Node FAIL"
                    password_node_Name = mhierarchyviewer.getText(password_node)
                    print 'password_node_Name ',password_node_Name
                    #end
                    # Save Wifi
                    '''
                    mdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(1)
                    '''
                    easy_mdevice.touch(By.id('id/button1'),MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(2)
                    break
                else:
                    print 'Miss touched SSID'
                    easy_mdevice.touch(By.id('id/button2'),MonkeyDevice.DOWN_AND_UP)
                    flag = False
                    MonkeyRunner.sleep(0.5)
        else:
            shotpath = ImagePath + "\\Fail_findspot_" + str(attempt) + ".png"
            common.SaveFailImg(mdevice,shotpath)
            mdevice.drag((width_w,height_w*2),(width_w,height_w),0.5,10)
            MonkeyRunner.sleep(1)
    #add by jianke 08/09 for fresh wifi
    if not flag:
        for loop_i in range(2):
            mdevice.drag((width_w,height_w),(width_w,height_w*3),0.5,10)
            MonkeyRunner.sleep(0.5)
        Selectwifi(SSID)
    #end
    if flag:
        for loop_i in range(3):
            mdevice.drag((width_w,height_w),(width_w,height_w*3),0.5,10)
            MonkeyRunner.sleep(0.5)
        print 'Connecting...'
        Maxtime = 0
        while not GetConnectionStatus():
            MonkeyRunner.sleep(2)
            Maxtime = Maxtime + 1
            if (Maxtime) > 30:
                return False
        return True
    else:
        shotpath = ImagePath + "\\Fail_Select_Wifi.png"
        common.SaveFailImg(mdevice,shotpath)
    return False

def ForgetWifi():
    FailTestTimes = 0
    
    if GetConnectionStatus():   
        # Disconnect Wifi
        print 'Select the first item'
        prefs_node = common.GetNode(mdevice,mhierarchyviewer,'id/prefs')
        if prefs_node is None:
            raise TypeError,"Get Node FAIL"
        list_node = common.GetNode(mdevice,mhierarchyviewer,'id/list',prefs_node)
        if list_node is None:
            raise TypeError,"Get Node FAIL"
        #add by jianke 0218 begin
        MonkeyRunner.sleep(5)
        number = list_node.children.size()
        print 'number ' + str(number)
        while number==0:
            FailTestTimes = FailTestTimes + 1
            MonkeyRunner.sleep(3)
            prefs_node = common.GetNode(mdevice,mhierarchyviewer,'id/prefs')
            if prefs_node is None:
                raise TypeError,"Get Node FAIL"
            list_node = common.GetNode(mdevice,mhierarchyviewer,'id/list',prefs_node)
            if list_node is None:
                raise TypeError,"Get Node FAIL"
            number = list_node.children.size()
            print 'number2 ' + str(number)
            if FailTestTimes > 3:
                return False
        #end
        FirstItem_node = list_node.children[0]     #0218
        #add by jianke 04/27 for test
        Node_Title = common.GetNode(mdevice,mhierarchyviewer,'id/title',FirstItem_node.children[1])
        if Node_Title is None:
                raise TypeError,"Get Node FAIL"
        Node_Title_Name = mhierarchyviewer.getText(Node_Title)
        print 'Node_Title_Name ',Node_Title_Name
        Node_Summary = common.GetNode(mdevice,mhierarchyviewer,'id/summary',FirstItem_node.children[1])
        if Node_Summary is None:
                raise TypeError,"Get Node FAIL"
        Node_Summary_Name = mhierarchyviewer.getText(Node_Summary)
        print 'Node_Summary_Name ',Node_Summary_Name
        #end
        if common.GetWind_Id(mhierarchyviewer,easy_mdevice,id_name.SubSETTING_ID,'id/prefs',1,3,1,4) and Node_Summary_Name == 'Connected':
            FirstItemPos = mhierarchyviewer.getAbsoluteCenterOfView(FirstItem_node)
            print 'FirstItemPos 001',FirstItemPos
            mdevice.touch(FirstItemPos.x,FirstItemPos.y,MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(2)
        # Forget Wifi 07/26 add by jianke 
            touch_times = 0
            while not easy_mdevice.visible(By.id('id/parentPanel')):
                MonkeyRunner.sleep(1)
                touch_times = touch_times + 1
                if touch_times > 2:
                    break
            else:
                if easy_mdevice.visible(By.id('id/button3')):
                    easy_mdevice.touch(By.id('id/button3'),MonkeyDevice.DOWN_AND_UP)  
            MonkeyRunner.sleep(8)
        if GetConnectionStatus():
            print 'Forget Wifi Failed'
            return False
        print 'Forget Wifi Success'
        return True
    else:
        print 'Already Forget.'
        return False

def ConectWifi(times):
    global SucTimes
    
    if EnterWifi():
        # Make wifi open at first
        if ConfirmWifiStatus(True):
            print "Wifi open successfully"
        else:
            print "Wifi can not open at first. End test ConectWifi"
            return False        
    for loop in range(times):
        if EnterWifi():
            flag = True
            try:
                Max_time = 0
                while GetConnectionStatus():
                    Max_time = Max_time + 1
                    print 'Max_time ',Max_time
                    ForgetWifi()
                    MonkeyRunner.sleep(20)
                    if Max_time > 5:
                        shotpath = ImagePath+"\\Fail_DisconnectWifi.png"
                        common.SaveFailImg(mdevice,shotpath)
                        break
                if Selectwifi(SSID):
                    print 'Connect Wifi Successfully And Stay Connected For 20s'
                    MonkeyRunner.sleep(20)
                else:
                    flag = False
                    shotpath = ImagePath + "\\Fail_ConnectWifi_" + str(loop+1) + ".png"
                    common.SaveFailImg(mdevice,shotpath)
                if ForgetWifi():
                    #forget window appears then forgetwifi, else do nothing
                    print 'Disconnect Wifi Successfully'
                else:
                    flag = False
                    shotpath = ImagePath + "\\Fail_DisconnectWifi_" + str(loop+1) + ".png"
                    common.SaveFailImg(mdevice,shotpath)
                if flag:
                    SucTimes += 1
                    print "Trace Success Loop " + str(loop+1)
            except Exception,e:
                shotpath = ImagePath + "\\ConectWifi_exc" + str(loop+1) + ".png"
                common.SaveFailImg(mdevice,shotpath)
                print "ConectWifi Exception Error: " ,e
                traceback.print_exc()
                #BackToWifi()
                ConfirmWifiStatus(True)
        else:
            print "Open Wifi Failed. End ConectWifi Test"

def main():
    time_Start = common.timeCalc()
    
    print 'Start Wifi Test'
    common.ShowDeviceMemoryInfo(mdevice)
    common.BackToHome(mdevice)

    # Closewifi
    EnterWifi()
    # Make wifi close at first
    if not ConfirmWifiStatus(False):
        print "Wifi Can not close"

    if True:
        print "Switch Wifi " + str(SwitchTimes) + " Times"
        SwitchWifi(SwitchTimes)
    
    print "Dis/Connect Wifi " + str(ConnectTimes) + " Times"
    ConectWifi(ConnectTimes)

    common.BackToHome(mdevice)
    print "Finished Wifi Test"
    common.ShowDeviceMemoryInfo(mdevice)
    print "Success Times: ", SucTimes
    Rate = SucTimes/TestTimes*100
    
    if Rate < 99:
        print 'Result Fail Success Rate Is ' + str(Rate) + '%'
    else:
        print 'Result Pass Success Rate Is ' + str(Rate) + '%'
    timeEnd = common.timeCalc()
    totalTime = timeEnd - time_Start
    print '5.1.10_Wifi time = ' + str(totalTime) + 'mins'
    
# Script End
if __name__ == "__main__":
    main()
#  Scrpit End
