#coding=UTF-8
#-------------------------------------------------------------------------------
#Title:                 5.1.1_Telephony
#Precondition:          1.Two devices connected
#                       2.Sim Card Exist
#Description:           Used for Yaris_3.5_ATT_KK
#Platform:              4.2.2
#Resolution:            320x480
#Version:               C98
#Modify:                Jake
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
sys.path.append(scriptpath)
import common
from common import ConnectClientDevice
from common import ConnectServerDevice


cdevice,chierarchyviewer,ceasy_device=ConnectClientDevice()
sdevice,shierarchyviewer,seasy_device=ConnectServerDevice()

# Change Depend On Real Condition
config = ConfigParser.ConfigParser()
config.read(scriptpath + "\\config.ini")
cdevicenumber = config.get("Telephony","cdevice_num")
sdevicenumber = config.get("Telephony","sdevice_num")
supportedNetworkType = config.get("Common","SUPPORTED_NETWORK_TYPE")
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

strname = '1AutoTest'
numseed = "0123456789"
Flag_mini = True

if supportedNetworkType == "2G3GLTE":
    if testtype == "mini":
        Contact2G = 5
        Contact3G = 5
        ContactLTE = 5 
        CallLog2G = 5
        CallLog3G = 5
        CallLogLTE = 5
        ReceiveCall = 1 #100
        DelTimes = 1 #20
        AddTimes = 1 #20
    else:
        Contact2G = 20
        Contact3G = 20
        ContactLTE = 60
        CallLog2G = 20
        CallLog3G = 20
        CallLogLTE = 60
        ReceiveCall = 100 #100
        DelTimes = 20 #20
        AddTimes = 20 #20
    TestTimes = (Contact2G+Contact3G+ContactLTE+CallLog2G+CallLog3G+CallLogLTE+ReceiveCall+DelTimes+AddTimes)
if supportedNetworkType == "2G3G":
    if testtype == "mini":
        if Flag_mini:
            Contact2G = 1 # 50
            Contact3G = 1
            CallLog2G = 1 # 50
            CallLog3G = 1
            ReceiveCall = 1 #100
            DelTimes = 1
            AddTimes = 1 #20
        else:
            Contact2G = 10 # 50
            Contact3G = 0
            CallLog2G = 10 # 50
            CallLog3G = 0
            ReceiveCall = 10 #100
            DelTimes = 5
            AddTimes = 5 #20
    else:
        Contact2G = 0
        Contact3G = 50
        CallLog2G = 0
        CallLog3G = 50
        ReceiveCall = 100 #100
        DelTimes = 20
        AddTimes = 20 #20
    TestTimes = (Contact2G+Contact3G+CallLog2G+CallLog3G+ReceiveCall+DelTimes+AddTimes)
    
SucTimes = 0
print 'Trace Total Times ' + str(TestTimes)


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
    print 'pid --> ',str3
    return str3

def EnterContact(device = cdevice,easy_device = ceasy_device,hierarchyviewer = chierarchyviewer):
    print "Launch Contacts And Wait"
    #add by jianke 07/27
    '''
    obj = device.shell('ps | grep com.android.contacts')
    print 'obj ' + str(obj)
    strb = func(obj)
    print 'strb ' + str(strb)
    obj = device.shell('kill ' + strb)
    print 'obj1 ' + str(obj) 
    obj = device.shell('ps | grep com.android.contacts')
    print 'obj2 ' + str(obj)
    '''
    #end
    #jianke test 07/08
    print 'test 07/08 --> ',id_name.Contact_ID
    if common.isEnterApp(easy_device,id_name.Contact_ID) or common.startapp(device,easy_device,id_name.Contact_ID):
        print 'Launch ...... Contacts '
        if project_name == 'yaris35_ATT': 
            bar = hierarchyviewer.findViewById('id/action_bar_container')
            if bar is None:
                return False
            cont =  hierarchyviewer.getAbsoluteCenterOfView(bar.children[2].children[0].children[1])
            device.touch(cont.x,cont.y,MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            return True
        else:
            print 'other project may come here!!!!!!!!!!!!!!!!!'
    return False

def SelectAnItembytouch(index):
    print 'Select A Contact'
    #jianke 0218 begin
    MonkeyRunner.sleep(1)
    #jianke 0218 end
    if project_name == 'yaris35_ATT':
        contact_tab_node = common.GetNode(cdevice,chierarchyviewer,'id/pinned_header_list_layout')
        if contact_tab_node is None:
            raise TypeError,"Get Node FAIL"
        list = common.GetNode(cdevice,chierarchyviewer,'id/list',contact_tab_node)
        if list is None:
            raise TypeError,"Get Node FAIL"
        contact_nameid =  chierarchyviewer.getAbsoluteCenterOfView(list.children[index + 3])
        #test begin 0228
        print 'contact_nameid ' + str(contact_nameid)
        #test end 0228
        #maybe problem , touch no reaction by jianke 0214 / 0228
        text = chierarchyviewer.getFocusedWindowName()
        print 'SelectAnItembytouch text ' + str(text)
        time_1 = 0
        while text != id_name.Contact_ID:
            print 'sleep to wait id'
            MonkeyRunner.sleep(1)
            text = chierarchyviewer.getFocusedWindowName()
            time_1 = time_1 + 1
            if time_1 > 2:
                break
        cdevice.touch(contact_nameid.x,contact_nameid.y,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        time_2 = 0
        text2 = chierarchyviewer.getFocusedWindowName()
        while id_name.PhoneNumber_ID != text2:
            cdevice.touch(contact_nameid.x,contact_nameid.y,MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            text2 = chierarchyviewer.getFocusedWindowName()
            time_2 = time_2 + 1
            if time_2 > 2:
                break
    MonkeyRunner.sleep(1)
        
def Contact_MOC():
    print 'MOC'
    txtimes = 0
    text_1 = chierarchyviewer.getFocusedWindowName()
    #add by jianke 07/08
    if project_name == 'yaris35_ATT': 
        while text_1 != id_name.PhoneNumber_ID:
            MonkeyRunner.sleep(1)
            text_1 = chierarchyviewer.getFocusedWindowName()
            txtimes = txtimes + 1
            if txtimes > 2:
                break
        MaxTime = 0
        text = chierarchyviewer.getFocusedWindowName()
        print 'text ' + str(text)
        while text != id_name.CALLSCREEN_ID:
            MaxTime = MaxTime + 1
            #add by jianke 0218 begin 
            if ceasy_device.visible(By.id('id/primary_action_view')):
                ceasy_device.touch(By.id('id/primary_action_view'),MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                print 'touch ' + str(MaxTime) + ' times'
                MonkeyRunner.sleep(3)
                break
            #Test switch
            text = chierarchyviewer.getFocusedWindowName()
            print str(MaxTime) + ' text ' + str(text)
            if MaxTime > 4:
                return False
        #add by jianke For no coming call 07/30
        '''
        if common.GetWind_Id(chierarchyviewer,ceasy_device,id_name.CALLSCREEN_ID,'id/audioButton',1,2,1,3):
            ceasy_device.touch(By.id('id/audioButton'),MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
        '''
        #end
    else:
        print 'other project come here!!!!!!!!!'
    return True

def WaitingCall(hierarchyviewer,easy_device):   #jianke 0214
    print "Waiting incoming call"
    #add by jianke 2014/04/01 001 
    common.BatteryFull(easy_device)
    #end
    wait_time = 0
    #add by jianke 0214 begin
    text_income = hierarchyviewer.getFocusedWindowName()
    #add by jianke 0214 end
    while id_name.CALLSCREEN_ID != text_income:
        #add by jianke 2014/04/01 005 
        common.BatteryFull(easy_device)
        #end
        wait_time = wait_time + 1
        MonkeyRunner.sleep(1)
        #add by jianke 0214 begin
        text_income = hierarchyviewer.getFocusedWindowName()
        #add by jianke 0214 end
        print 'wait_time ',wait_time
        if wait_time > 23:
            print "No incoming call"
            return False
    MonkeyRunner.sleep(3)
    return True

def AnswerCall(snappath,device,hierarchyviewer,easy_device):
    common.BatteryFull(easy_device)
    if WaitingCall(hierarchyviewer,easy_device):           
        print "Accept The incoming call"
        MonkeyRunner.sleep(1)
        device.press('KEYCODE_CALL',MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(5)
        return True
    common.SaveFailImg(device,snappath)
    print 'network is poor'
    if device == cdevice:
        if seasy_device.visible(By.id('id/endButton')):  
            seasy_device.touch(By.id('id/endButton'),MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(0.5)
        else:
            print 'cdevice,the communication is not connencted!'
    else:
        if ceasy_device.visible(By.id('id/endButton')):
            ceasy_device.touch(By.id('id/endButton'),MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(0.5)
        else:
            print 'sdevice,the communication is not connencted!'
    return False

def BackToContact(device = cdevice,easy_device = ceasy_device,hierarchyviewer = chierarchyviewer):
    if easy_device.visible(By.id('id/endButton')):
        easy_device.touch(By.id('id/endButton'),MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(3)
    for i in range(5):
        # modify by gqding for make sure back to contact 2014-02-01
        if common.isEnterApp(easy_device,Contact_ID) or common.startapp(device,easy_device,Contact_ID):
            bar = hierarchyviewer.findViewById('id/action_bar_container')
            if bar is None:
                raise TypeError,"Get Node FAIL"
            cont =  hierarchyviewer.getAbsoluteCenterOfView(bar.children[2].children[0].children[1])
            device.touch(cont.x,cont.y,MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)           
            break
        device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)


def isBacktoLTE():
    observedMode = common.getDataServiceState(cdevice)
    j = 0
    # Try to wait for 20 sec at most if state is unknown
    while observedMode != 'LTE' and j < 10:
        MonkeyRunner.sleep(2)
        j += 1
        observedMode = common.getDataServiceState(cdevice)
    if observedMode == 'LTE':
        print "Change to LTE"
        return True
    else:
        print "Can not change to LTE"
        return False

def Voice_Call_From_Contact(times,NetWork_type):
    global SucTimes

    width_w = int(str(width))
    width_w = width_w/2
    height_w = int(str(height))
    height_w = height_w/4
    width_w = int(width_w)
    print 'width_w 2222 ',width_w
    height_w = int(height_w)
    print 'height_w 2222 ',height_w
    
    for loop in range(times):
        if EnterContact():
            try:
                print "First make sure clean up battery full popup"
                common.BatteryFull(ceasy_device)
                common.BatteryFull(seasy_device)
                cdevice.drag((width_w,height_w),(width_w,height_w*2),0.1,10)
                MonkeyRunner.sleep(0.5)
                SelectAnItembytouch(0)
                shotpath = ImagePath + "\\Fail_Answercall_contact_" + NetWork_type + '_' + str(loop+1) + ".png"
                if Contact_MOC():
                    if AnswerCall(shotpath,sdevice,shierarchyviewer,seasy_device):    
                        print 'Answer Call From Contact'
                        if ceasy_device.visible(By.id('id/message')) and ceasy_device.getText(By.id('id/message')).find('Call not sent') > -1:
                            ceasy_device.touch(By.id('id/button1'),MonkeyDevice.DOWN_AND_UP)
                            MonkeyRunner.sleep(0.5)
                        #end
                        ceasy_device.touch(By.id('id/endButton'),MonkeyDevice.DOWN_AND_UP)
                        '''
                        MonkeyRunner.sleep(1.5)
                        txt_get = chierarchyviewer.getFocusedWindowName()
                        state_Flag = True
                        if txt_get == "com.android.phone/com.android.phone.InCallScreen" and ceasy_device.visible(By.id('id/callStateLabel')):
                            #add by jianke 03/26
                            state_node = common.GetNode(cdevice,chierarchyviewer,'id/callStateLabel')
                            if state_node is None:
                                state_Flag = False
                            if state_Flag:
                                call_time_txt = ceasy_device.getText(By.id('id/callStateLabel'))
                                print 'call_time_txt ',call_time_txt
                                for num in call_time_txt:
                                    if num.isdigit():
                                        print 'num ',num
                                        ceasy_device.touch(By.id('id/endButton'),MonkeyDevice.DOWN_AND_UP)
                            #end
                        '''
                        SucTimes = SucTimes + 1
                        
                        print "Trace Success Loop " + str(loop+1)
                    else:
                        print "sdevice can not pick up from contact,Can Not To Establish The Connection"
                else:
                    print "Can Not Dial from Contact"
                    cshotpath = ImagePath + "\\Fail_Dial_contact" + NetWork_type + '_' + str(loop+1) + ".png"
                    common.SaveFailImg(cdevice,cshotpath)
                #avoid the second call 07/24
                MonkeyRunner.sleep(3)
                cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
            except Exception,e:
                shotpath = ImagePath + "\\Contact_exc_" + NetWork_type + '_' + str(loop+1) + '_cdevice' + ".png"
                common.SaveFailImg(cdevice,shotpath)
                print 'Voice_Call_From_Contact Exception Error: ' + str(loop+1),e
                traceback.print_exc()
                #BackToContact()
    print 'Voice_Call Test complete'

def EnterCallLog(device = cdevice,easy_device = ceasy_device,hierarchyviewer = chierarchyviewer):
    print "Launch CallLog And Wait"

    if common.isEnterApp(easy_device,id_name.Phone_ID) or common.startapp(device,easy_device,id_name.Phone_ID):
        print 'Launch ..... CallLog'
        bar = hierarchyviewer.findViewById('id/action_bar_container')
        if bar is None:
            return False
        #jianke 0310 modify
        try:
            cont =  hierarchyviewer.getAbsoluteCenterOfView(bar.children[2].children[0].children[1])
            print 'cont for test ',cont
            device.touch(cont.x,cont.y,MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            #modify by jianke 04/02 001
            if easy_device == ceasy_device:
                easy_device.touch(By.id('id/call_out'),MonkeyDevice.DOWN_AND_UP)
            else:
                easy_device.touch(By.id('id/call_in'),MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            #end
        except:
            return False
        print 'EnterCallLog'
        return True
    return False

def IfChar(chstr):
    for ch in chstr:
        if ch.isdigit():
            return False
    return True

def CallLog_MOC(strnum,device = cdevice,easy_device = ceasy_device,hierarchyviewer = chierarchyviewer):
    common.BatteryFull(easy_device)
    print 'MOC'
    dialNum = strnum.strip()
    print 'strnum --------- ' + str(strnum)
    if len(dialNum) < 4 :
        print "Number should be bigger than 4 digits"
        return False
    lastFourDigits = dialNum[-4:]
    print 'lastFourDigits ' + str(lastFourDigits)
    num = 0
    fail_times = 0
    while num==0:
        fail_times = fail_times + 1
        MonkeyRunner.sleep(2)
        pager_node = common.GetNode(device,hierarchyviewer,'id/pager')
        if pager_node is None:
            raise TypeError,"Get Node FAIL"
        list_node = common.GetNode(device,hierarchyviewer,'id/list',pager_node.children[1])
        if list_node is None:
            print 'list_node is None'
            list_node = common.GetNode(device,hierarchyviewer,'id/list',pager_node.children[0])
            if list_node is None:
                raise TypeError,"Get Node FAIL"
        num = list_node.children.size()
        print "Exist ",num,"Call logs"
        if fail_times > 2:
            return False
    for i in range(num):
        itemNode = list_node.children[i]
        number_node = common.GetNode(device,hierarchyviewer,'id/number',itemNode)
        if number_node is None:
            raise TypeError,"Get Node FAIL"
        if easy_device.visible(By.id('id/number')):
            callLogNum = hierarchyviewer.getText(number_node)
            print 'callLogNum ',callLogNum
            if easy_device == seasy_device:
                if callLogNum == '' or IfChar(callLogNum):
                    number_node = common.GetNode(device,hierarchyviewer,'id/name',itemNode)
                    callLogNum = hierarchyviewer.getText(number_node)
                    print 'callLogNum name ',callLogNum
            print "Expected Number: " + str(lastFourDigits) + "  Call Log Number: " + callLogNum.strip().encode('utf-8')
            if callLogNum.find(lastFourDigits) < 0 :
                print "can't find"
                print "Expected Number: " + str(lastFourDigits) + "  Call Log Number: " + str(callLogNum.encode('utf-8'))
            else:
                MonkeyRunner.sleep(1)
                if common.GetWind_Id(hierarchyviewer,easy_device,id_name.Phone_ID,'id/secondary_action_icon',1,2,1,2):
                    dial_line_node = common.GetNode(device,hierarchyviewer,'id/secondary_action_icon',itemNode)
                    if dial_line_node is None:
                        raise TypeError,"Get Node FAIL"
                    itemPos = hierarchyviewer.getAbsoluteCenterOfView(dial_line_node)
                    device.touch(itemPos.x,itemPos.y,MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(1)      
    MaxTime = 0
    text = hierarchyviewer.getFocusedWindowName()
    while text != id_name.CALLSCREEN_ID: #07/08
        MaxTime = MaxTime + 1
        text = hierarchyviewer.getFocusedWindowName()
        MonkeyRunner.sleep(1)
        if MaxTime > 10:
            print 'go to oooooooooo'
            return False
    MonkeyRunner.sleep(1)
    print 'go to kkkkkkkkkkk'
    #add by jianke For test 07/30
    '''
    if common.GetWind_Id(hierarchyviewer,easy_device,id_name.CALLSCREEN_ID,'id/audioButton',1,2,1,3):
        easy_device.touch(By.id('id/audioButton'),MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    '''
    #end
    return True

def BackToCallLog(device = cdevice,easy_device = ceasy_device,hierarchyviewer = chierarchyviewer):
    if ceasy_device.visible(By.id('id/endButton')):
        ceasy_device.touch(By.id('id/endButton'),MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(3)
    if seasy_device.visible(By.id('id/endButton')):
        seasy_device.touch(By.id('id/endButton'),MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(3)
    for i in range(5):
        # modify by gqding for make sure back to call log and call all log tab 2014-02-01
        if common.isEnterApp(easy_device,Phone_ID) or common.startapp(device,easy_device,Phone_ID):
            bar = hierarchyviewer.findViewById('id/action_bar_container')
            if bar is None:
                raise TypeError,"Get Node FAIL"
            cont =  hierarchyviewer.getAbsoluteCenterOfView(bar.children[2].children[0].children[1])
            device.touch(cont.x,cont.y,MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            easy_device.touch(By.id('id/call_all'),MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)            
            break
        device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        
def Voice_Call_From_CallLog(times,NetWork_type):
    global SucTimes
    
    for loop in range (times):
        #add by jianke 0303
        if EnterCallLog():
            try:
                print "First make sure clean up battery full popup"
                common.BatteryFull(ceasy_device)
                common.BatteryFull(seasy_device)
                shotpath = ImagePath + "\\Fail_AnswerCall_CallLog_" + NetWork_type + '_' + str(loop+1) + ".png"
                if CallLog_MOC(sdevicenumber):
                    if AnswerCall(shotpath,sdevice,shierarchyviewer,seasy_device):
                        print 'Answer Call From CallLog'
                        #add by jianke 03/25
                        if ceasy_device.visible(By.id('id/message')) and ceasy_device.getText(By.id('id/message')).find('Call not sent') > -1:
                            ceasy_device.touch(By.id('id/button1'),MonkeyDevice.DOWN_AND_UP)
                            MonkeyRunner.sleep(0.5)
                        #end
                        ceasy_device.touch(By.id('id/endButton'),MonkeyDevice.DOWN_AND_UP)
                        #add by jianke 03/25
                        '''
                        MonkeyRunner.sleep(1.5)
                        txt_get = chierarchyviewer.getFocusedWindowName()
                        state_Flag = True
                        if txt_get == "com.android.phone/com.android.phone.InCallScreen" and ceasy_device.visible(By.id('id/callStateLabel')):
                            #add by jianke 03/26
                            state_node = common.GetNode(cdevice,chierarchyviewer,'id/callStateLabel')
                            if state_node is None:
                                state_Flag = False
                            if state_Flag:
                                call_time_txt = ceasy_device.getText(By.id('id/callStateLabel'))
                                print 'call_time_txt ',call_time_txt
                                for num in call_time_txt:
                                    if num.isdigit():
                                        print 'num ',num
                                        ceasy_device.touch(By.id('id/endButton'),MonkeyDevice.DOWN_AND_UP)
                            #end
                        '''
                        #end
                        
                        SucTimes = SucTimes + 1
                        print "Trace Success Loop " + str(loop+1)
                    else:
                        print "sdevice can not pick up from call log,Can Not To Establish The Connection"
                else:
                    print "Can not Dial from Call log"
                    cshotpath = ImagePath + "\\Fail_Dialing_CallLog_" + NetWork_type + '_' + str(loop+1) + ".png"
                    common.SaveFailImg(cdevice,cshotpath)
                #avoid the second call 07/24
                MonkeyRunner.sleep(3)
            except Exception,e:
                shotpath = ImagePath + "\\CallLog_exc_" + str(loop+1) + ".png"
                common.SaveFailImg(cdevice,shotpath)
                print 'Voice_Call_From_CallLog Exception Error: ' + str(loop+1),e
                traceback.print_exc()
                #BackToCallLog()
    print 'Voice_Call Test complete'

def Receive_Voice_Call(times,NetWork_type): 
    global SucTimes
    
    for loop in range (times):
        #add by jianke 0303
        if EnterCallLog(sdevice,seasy_device,shierarchyviewer):
            print "Waiting For Incoming Call"
            try:
                print "First make sure clean up battery full popup"
                common.BatteryFull(ceasy_device)
                common.BatteryFull(seasy_device)
                shotpath = ImagePath + "\\Fail_ReceiveCall_" + NetWork_type + '_' + str(loop+1) + ".png"
                print 'cdevicenumber:',cdevicenumber
                if CallLog_MOC(cdevicenumber,sdevice,seasy_device,shierarchyviewer):
                    if AnswerCall(shotpath,cdevice,chierarchyviewer,ceasy_device):
                        print 'Answer Receive Voice Call'
                        #add by jianke 03/25
                        if ceasy_device.visible(By.id('id/message')) and ceasy_device.getText(By.id('id/message')).find('Call not sent') > -1:
                            ceasy_device.touch(By.id('id/button1'),MonkeyDevice.DOWN_AND_UP)
                            MonkeyRunner.sleep(0.5)
                        #end
                        ceasy_device.touch(By.id('id/endButton'),MonkeyDevice.DOWN_AND_UP)
                        #add by jianke 03/25
                        '''
                        MonkeyRunner.sleep(1.5)
                        state_Flag = True
                        txt_get = chierarchyviewer.getFocusedWindowName()
                        if txt_get == "com.android.phone/com.android.phone.InCallScreen" and ceasy_device.visible(By.id('id/callStateLabel')):
                            #add by jianke 03/26
                            state_node = common.GetNode(cdevice,chierarchyviewer,'id/callStateLabel')
                            if state_node is None:
                                state_Flag = False
                            if state_Flag:
                                call_time_txt = ceasy_device.getText(By.id('id/callStateLabel'))
                                print 'call_time_txt ',call_time_txt
                                for num in call_time_txt:
                                    if num.isdigit():
                                        print 'num ',num
                                        ceasy_device.touch(By.id('id/endButton'),MonkeyDevice.DOWN_AND_UP)
                            #end
                        '''
                        #end
                        SucTimes = SucTimes + 1
                        print "Trace Success Loop " + str(loop+1)
                    else:
                        print "mdevice can not pick up,Can Not To Establish The Connection 3G!"
                else:
                    #add by jianke 0218 begin
                    print "Can Not Dial from sdevice in 3G"
                    sshotpath = ImagePath + "\\Fail_sDial_" + NetWork_type + '_' + str(loop+1) + ".png"
                    common.SaveFailImg(sdevice,sshotpath)
                    #end
                #avoid the second call 07/24
                MonkeyRunner.sleep(3)
            except Exception,e:
                shotpath = ImagePath + "\\Receive_exc_" + str(loop+1) + ".png"
                common.SaveFailImg(cdevice,shotpath)
                print 'Receive_Voice_Call Exception Error: ' + str(loop+1),e
                traceback.print_exc()
                #BackToCallLog(sdevice,seasy_device,shierarchyviewer)
    print 'Voice_Call Test complete'

def GetContactName(index):
    contact_tab_node = common.GetNode(cdevice,chierarchyviewer,'id/pinned_header_list_layout')#contact_list
    if contact_tab_node is None:
        raise TypeError,"Get Node FAIL"
    list = common.GetNode(cdevice,chierarchyviewer,'id/list',contact_tab_node)
    if list is None:
        raise TypeError,"Get Node FAIL"
    print index
    if index==0:
        contact_name = list.children[index + 3].children[3]
    elif index==1:
        contact_name = list.children[index + 3].children[1]
    return chierarchyviewer.getText(contact_name)

def DeleteItem():
    print "Delete one Contact"
    cdevice.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    ceasy_device.touchtext(By.id('id/title'), 'Delete',MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    ceasy_device.touch(By.id('id/button1'), MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)

def OnlyCharNum(s,oth=''): 
    s2  = s.lower() 
    fomart  = '0123456789' 
    for c in  s2:
        if not c in fomart: 
            s = s.replace(c,'')
    return s

def GetContactNum():
    contact_num_node = common.GetNode(cdevice,chierarchyviewer,'id/contacts_count')
    if contact_num_node is None:
        raise TypeError,"Get Node FAIL"
    Num = chierarchyviewer.getText(contact_num_node)
    Num2 = OnlyCharNum(Num)
    return int(Num2)
                               
def Delete_contact(times):
    global SucTimes

    width_w = int(str(width))
    width_w = width_w/2
    height_w = int(str(height))
    height_w = height_w/4
    width_w = int(width_w)
    print 'width_w 2222 ',width_w
    height_w = int(height_w)
    print 'height_w 2222 ',height_w
    
    #jianke modify 2014/03/13
    for loop in range (times):
        if EnterContact():
            for i in range(3):
                cdevice.drag((width_w,height_w),(width_w,height_w*3),0.1,10)
                MonkeyRunner.sleep(0.5)
            try:
                NumOfContacts_old = GetContactNum()
                print 'get Num of Contacts before delete',NumOfContacts_old
                SelectAnItembytouch(1)
                DeleteItem()
                NumOfContacts_new = GetContactNum()
                print 'get Num of Contacts after delete',NumOfContacts_new
                print NumOfContacts_old - NumOfContacts_new
                if (NumOfContacts_old - NumOfContacts_new) == 1:
                    SucTimes = SucTimes + 1
                    print '----------------Delete Contact-------',(loop+1)
                    print "Trace Success Loop" + str(loop+1)
                else:
                    shotpath = ImagePath + "\\Fail_Delete_" + str(loop+1) + ".png"
                    common.SaveFailImg(cdevice,shotpath)
                MonkeyRunner.sleep(1)
            except Exception,e:
                shotpath = ImagePath + "\\Delete_exc_" + str(loop+1) + ".png"
                common.SaveFailImg(cdevice,shotpath)
                print 'Delete_contact Exception Error: ' + str(loop+1),e
                traceback.print_exc()
                #BackToContact()

def Add_contact(times):
    global SucTimes

    width_w = int(str(width))
    width_w = width_w/2
    height_w = int(str(height))
    height_w = height_w/4
    width_w = int(width_w)
    print 'width_w 2222 ',width_w
    height_w = int(height_w)
    print 'height_w 2222 ',height_w
    
    #jianke modify 2014/03/13
    for loop in range (times):
        if EnterContact():
            for i in range(3):
                cdevice.drag((width_w,height_w),(width_w,height_w*3),0.1,10)
                MonkeyRunner.sleep(0.5)
            try:
                NumOfContacts_old = GetContactNum()
                print 'get Num of Contacts before ADD',NumOfContacts_old
                print "Add one contact"
                AddAContact(loop,times)
                NumOfContacts_new = GetContactNum()
                print 'get Num of Contacts after ADD',NumOfContacts_new
                print 'add contact num: ',NumOfContacts_new - NumOfContacts_old
                if (NumOfContacts_new - NumOfContacts_old) == 1:
                    SucTimes = SucTimes + 1
                    print '----------------ADD Contact-------',(loop+1)
                    print "Trace Success Loop"+ str(loop+1)
                else:
                    shotpath = ImagePath+"\\Fail_Add_"+str(loop+1)+".png"
                    common.SaveFailImg(cdevice,shotpath)
                MonkeyRunner.sleep(1)
            except Exception,e:
                shotpath = ImagePath + "\\Add_exc_" + str(loop+1) + ".png"
                common.SaveFailImg(cdevice,shotpath)
                print 'Add_contact Exception Error: ',e
                traceback.print_exc()
                #BackToContact()

def AddAContact(loop,times):
    print 'Create A Contact'
    ceasy_device.touch(By.id('id/menu_add_contact'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    screen = chierarchyviewer.getFocusedWindowName()
    if screen == id_name.Account_Wind_ID:
        print 'must can not be enter here'
        ceasy_device.touchtext(By.id('id/text1'),"Phone contact",MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    # Edit Contact
    if (times-loop) < 10:
        name = strname + str(0) + str(times-loop)
    else:
        name = strname + str(times-loop)
    sa = []
    for i in range(5):
        sa.append(random.choice(numseed))
    stamp = ''.join(sa)
    name = name + '_' + str(stamp)
    #Add by jianke 04/25 002
    if common.GetWind_Id(chierarchyviewer,ceasy_device,id_name.Contact_Wind_ID,'id/content',1,3,1,4):  #07/08
        print 'go to name ... '
        height_w = int(str(height))
        print '07/14 ... ',height_w
        common.Get_keyBoard_wind(cdevice,chierarchyviewer,'id/content',height_w)
        ceasy_device.type(By.id('0x3'),name)
        MonkeyRunner.sleep(1)
    else:
        print 'not prepare to enter contact name.'
    #end
    cdevice.press('KEYCODE_BACK',MonkeyDevice.DOWN_AND_UP)
    #add by jianke 0218 begin
    MonkeyRunner.sleep(1)
    #end
    #input server number
    '''
    ceasy_device.touch(By.id('id/editors'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    '''
    ceasy_device.type(By.id('0x11'),sdevicenumber)
    MonkeyRunner.sleep(2)
    # Save
    ceasy_device.touch(By.id('id/save_menu_item'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    #Contact_ID
    #add by jianke 07/14
    contact_times = 0
    while chierarchyviewer.getFocusedWindowName() != id_name.Contact_ID:
        cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        contact_times = contact_times + 1
        print 'contact_times ',contact_times
        if contact_times > 3:
            break
    #end

def main():
    global SucTimes
    global ImagePath

    time_Start = common.timeCalc()
    
    print 'Start Telephony Test'
    common.ShowDeviceMemoryInfo(cdevice)
    ImagePath = common.CreateFolder('5.1.1')

    common.BackToHome(cdevice)
    common.BackToHome(sdevice)  
    
    #-------1------------------
    if True:
        NetWork_type = '3G'
        print 'Make ' + NetWork_type + ' Voice Call from Contact ' + str(Contact3G) + ' Times'    
        Voice_Call_From_Contact(Contact3G,NetWork_type)
    #-------------------------------------------------------------------
    #------------2-------------
    if True:
        NetWork_type = '3G'
        print 'Make ' + NetWork_type + ' Voice Call from CallLog ' + str(CallLog3G) + ' Times'
        Voice_Call_From_CallLog(CallLog3G,NetWork_type)
    #-------------------Receive a voice call on 3G-----------------------
    #-------------3-----------------
    if True:
        NetWork_type = '3G'
        print 'Receive ' + NetWork_type + ' Voice Call ' + str(ReceiveCall) + ' Times'
        Receive_Voice_Call(ReceiveCall,NetWork_type)
    
    #--------------------------------------------------------------------------
    #---------------4---------------
    print 'Delete a contact from the Contacts ' + str(DelTimes) + ' Times'
    Delete_contact(DelTimes)
    #---------------5---------------
    print 'Add a contact To the Contacts ' + str(AddTimes) + ' Times'
    Add_contact(AddTimes)
    
    common.BackToHome(cdevice)
    common.BackToHome(sdevice)

    common.ShowDeviceMemoryInfo(cdevice)
    print 'Telephony Mission Complete'
    print "Success Times:", SucTimes
    Rate = SucTimes/TestTimes*100
    if Rate < 95:
        print 'Result Fail Success Rate Is ' + str(Rate) + '%'
    else:
        print 'Result Pass Success Rate Is ' + str(Rate) + '%'
    timeEnd = common.timeCalc()
    totalTime = timeEnd-time_Start
    print '5.1.01_Telephony time = ' + str(totalTime) + 'mins'
    
if __name__ == "__main__":
    main()
# Scrpit End
