#coding=UTF-8
#-------------------------------------------------------------------------------
#Title:                 5.1.03_Email
#Precondition:          1.One devices connected
#                       2.Sim Card Exist
#Description:           Used for Yaris_3.5_ATT
#Platform:              4.2.2
#Resolution:            320x480
#Version:               C65
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
scriptpath=sys.path[0][sys.path[0].find(':')+1:] + "\\..\\common"
sys.path.append(scriptpath)
import common
from common import ConnectClientDevice
#from common import ConnectServerDevice


cdevice,chierarchyviewer,ceasy_device=ConnectClientDevice()
#sdevice,shierarchyviewer,seasy_device=ConnectServerDevice()

# Change Depend On Real Condition
config = ConfigParser.ConfigParser()
config.read(scriptpath+"\\config.ini")
strEmail = config.get("Email","Email_receiver")
RECEIVERLIST = strEmail.split(",")

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
        SendBy2G = 2
        SendBy3G = 2
        SendByLTE = 2
        opentimes = 2
    else:
        SendBy2G = 5
        SendBy3G = 20
        SendByLTE = 25
        opentimes = 50
    TestTimes = (SendBy2G+SendBy3G+SendByLTE)*2+opentimes
if supportedNetworkType == "2G3G":
    if testtype == "mini":
        if Flag_mini:
            SendBy2G = 0 #10
            SendBy3G = 1 #40
            opentimes = 2 #50
        else:
            SendBy2G = 1 #10
            SendBy3G = 4 #40
            opentimes = 5 #50
    else:
        SendBy2G = 0 #10
        SendBy3G = 50 #40
        opentimes = 50 #50
    TestTimes = (SendBy2G+SendBy3G)*2+opentimes

print 'Trace Total Times ' + str(TestTimes)
SucTimes = 0

# Image Path
ImagePath = common.CreateFolder('5.1.3')

def DelSentMail():
    if not EnterMailBox("Sent"):
        print 'Enter Sentbox Failed'
        return False
    if GetNumberofMail("Sent") > 0:
        DelAllMail("Sent")
    return True

def GetEnterTitile():
    action_bar_title_node_test =common.GetNode(cdevice,chierarchyviewer,'id/action_bar_title')
    if action_bar_title_node_test is None:
        raise TypeError,"Get Node FAIL"
    title_node_text = chierarchyviewer.getText(action_bar_title_node_test)
    print 'action_bar_title_test 08/20 ',title_node_text
    return title_node_text

def EnterEmail():
    common.BackToHome(cdevice)
    print 'Launch Email And Wait'
    if common.isEnterApp(ceasy_device,(id_name.EMAIL_APPID,id_name.EMAIL_WINID)) or common.startapp(cdevice,ceasy_device,id_name.EMAIL_APPID):
        print 'start activity'
        #add by jianke 08/20
        if common.GetWind_Id(chierarchyviewer,ceasy_device,id_name.EMAIL_APPID,'id/action_bar_title',1,3,1,5):
            delay_time = 0
            while GetEnterTitile() == 'Email':
                MonkeyRunner.sleep(2)
                delay_time = delay_time + 1
                print 'enter delay 08/20 ',delay_time*2
                if delay_time > 5:
                    return False
        #end
        return True
    return False

def GetListName(box_name):
    drawer_pullout_node = common.GetNode(cdevice,chierarchyviewer,'id/drawer_pullout')
    if drawer_pullout_node is None:
        raise TypeError,"Get Node FAIL"
    drawer_pullout_list = common.GetNode(cdevice,chierarchyviewer,'id/list',drawer_pullout_node)
    if drawer_pullout_list is None:
        raise TypeError,"Get Node FAIL"
    drawer_pullout_list_size = drawer_pullout_list.children.size()
    print 'drawer_pullout_list_size ',drawer_pullout_list_size
    for child_node in range(drawer_pullout_list_size):
        drawer_pullout_list_child_node = drawer_pullout_list.children[child_node]
        drawer_pullout_list_child_node_name = drawer_pullout_list_child_node.name
        if str(drawer_pullout_list_child_node_name).find('FolderItemView') > -1:
            folder_node = common.GetNode(cdevice,chierarchyviewer,'id/name',drawer_pullout_list_child_node)
            if folder_node is None:
                raise TypeError,"Get Node FAIL"
            if chierarchyviewer.getText(folder_node).find(box_name) > -1:
                print 'box_name 88888 ',box_name
                MonkeyRunner.sleep(2)
                ceasy_device.touchtext(By.id('id/name'),box_name,MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(5)
                return True
    return False
            
def EnterMailBox(box_name):
    #add by jianke 04/01 001
    try:
        #add by jianke 03/29 001
        box_times = 0
        while not ceasy_device.visible(By.id('id/action_bar')):
            MonkeyRunner.sleep(1)
            print 'go toooooo box_times ',box_times
            box_times = box_times + 1
            if box_times > 10:
                print 'gooooooooooooooo'
                break
        print 'box_times ',box_times
        #add by jianke 14/06/05 for att_kk
        action_bar_node = common.GetNode(cdevice,chierarchyviewer,'id/action_bar')
        if action_bar_node is None:
            raise TypeError,"Get Node FAIL"
        #For check 14/06/05
        action_bar_node_children = action_bar_node.children.size()
        print 'action_bar_node_children ',action_bar_node_children
        #end
        action_bar_child_node = action_bar_node.children[0]
        action_bar_child_node_point =chierarchyviewer.getAbsoluteCenterOfView(action_bar_child_node)
        cdevice.touch(action_bar_child_node_point.x,action_bar_child_node_point.y,MonkeyDevice.DOWN_AND_UP)
        print 'refresh switch interface'
        MonkeyRunner.sleep(2)
        #add by jianke 07/09
        width_w = int(str(width))
        width_w = width_w/2
        width_w = int(width_w)
        height_w = int(str(height))
        height_w = height_w/4
        print 'height_w ',height_w
        height_w = int(height_w)
        print 'height_w 2222 ',height_w
        if project_name == 'yaris35_ATT':
            cdevice.drag((width_w,height_w),(width_w,height_w*2),0.5,10)
            MonkeyRunner.sleep(0.5)
        #end
        #add by jianke 07/11
        if GetListName(box_name):
            print 'First get the ',box_name
            #add by jianke 07/17
            refresh_times = 0
            while box_name == 'Inbox' and GetNumberofMail(box_name) < 2:
                print '111111111111111111 jk'
                MonkeyRunner.sleep(3)
                refresh_times = refresh_times + 1
                if refresh_times > 3:
                    break
            #end
            return True
        else:
            if project_name == 'yaris35_ATT':
                cdevice.drag((width_w,height_w*2),(width_w,height_w),0.5,10)
                MonkeyRunner.sleep(0.5)
                if GetListName(box_name):
                    print 'Second get the ',box_name
                    #add by jianke 07/17
                    refresh_times = 0
                    while box_name == 'Inbox' and GetNumberofMail(box_name) < 2:
                        print '2222222222222222 jk'
                        MonkeyRunner.sleep(3)
                        refresh_times = refresh_times + 1
                        if refresh_times > 3:
                            break
                    #end
                    return True
        #end
        return False
        #end
    except Exception,e:
        shotpath = ImagePath + "\\enter_" + str(box_name) + "_exc_with" + '_Attachment_By_' + NetWork_type + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print "EnterMailBox Exception Error:",e
        traceback.print_exc()
    #end

def GetNumberofMail(box_name):
    #CheckWarning()
    #add by jianke 14/06/05
    conversation_list_child_node = GetListNode()
    #end
    #add by jianke 07/09
    if project_name == 'yaris35_ATT': 
        if box_name == "Sent" or box_name == "Trash" or box_name == "Inbox" or box_name == "Outbox":
            #add by jianke 08/02
            if box_name == "Outbox":
                num = conversation_list_child_node.children.size()
            else:
                num = conversation_list_child_node.children.size() - 1
            #add by jianke 07/12  
            if ceasy_device.visible(By.id('id/network_error')):
                num = num - 1 
            if ceasy_device.visible(By.id('id/dismiss_separator')):
                num = num - 1
            if ceasy_device.visible(By.id('id/loading')):
                num = num - 1
            if ceasy_device.visible(By.id('id/load_more')):
                num = num - 1
            if ceasy_device.visible(By.id('id/remote_search')):
                num = num - 1
            #end   
    else:
        print 'other projects come here!'
        num = conversation_list_child_node.children.size()
    #end
    print("number is " + str(num))
    return num

def GetListNode():
    #add by jianke 14/06/05
    conversation_list_node = common.GetNode(cdevice,chierarchyviewer,'id/conversation_list')
    if conversation_list_node is None:
        raise TypeError,"Get Node FAIL"
    conversation_list_child_node = common.GetNode(cdevice,chierarchyviewer,'id/list',conversation_list_node)
    if conversation_list_child_node is None:
        raise TypeError,"Get Node FAIL"    
    #end
    return conversation_list_child_node

def DelAllMail(box_name):
    print("Delete All Email")
    
    #add by jianke 14/06/05  07/29
    print 'if delete inbox important ',box_name
    action_bar_title_node_test =common.GetNode(cdevice,chierarchyviewer,'id/action_bar_title')
    if action_bar_title_node_test is None:
        raise TypeError,"Get Node FAIL"
    title_node_text = chierarchyviewer.getText(action_bar_title_node_test)
    print 'action_bar_title_test ',title_node_text
    
    #add by jianke 07/29
    if box_name == title_node_text:
        try:
            num = GetNumberofMail(box_name)
            while num > 0:
                conversation_list_child_node = GetListNode()
                if project_name == 'yaris35_ATT':
                    a = 1
                    #add by jianke 08/03 
                    if ceasy_device.visible(By.id('id/dismiss_separator')):
                        a = a + 1
                    '''
                    if ceasy_device.visible(By.id('id/loading')):
                        a = a + 1
                        
                    if ceasy_device.visible(By.id('id/load_more')):
                        a = a + 1
                    '''
                    if ceasy_device.visible(By.id('id/remote_search')):
                        a = a + 1
                    #end
                    print 'a ----------> ',a
                else:
                    a = 0
                for del_time in range(a,num+a):
                    conversation_list_child_node_point = chierarchyviewer.getAbsoluteCenterOfView(conversation_list_child_node.children[del_time])
                    print 'conversation_list_child_node_point.y ',conversation_list_child_node_point.y
                    #add by jianke 07/09
                    width_w = int(str(width))
                    width_w = width_w/8
                    print 'width_w ',width_w
                    width_w = int(width_w)
                    cdevice.touch(width_w,conversation_list_child_node_point.y,MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(0.5)
                    #add by jianke 07/29
                    if box_name == 'Trash' or box_name == 'Outbox':
                        print 'enter to trash'
                        action_context_bar_node = common.GetNode(cdevice,chierarchyviewer,'id/action_context_bar')
                        if action_context_bar_node is None:
                            raise TypeError,"Get Node FAIL"
                        choose_node = action_context_bar_node.children[2].children[2]
                        choose_node_pos =  chierarchyviewer.getAbsoluteCenterOfView(choose_node)
                        cdevice.touch(choose_node_pos.x,choose_node_pos.y,MonkeyDevice.DOWN_AND_UP)
                        MonkeyRunner.sleep(1)
                        ceasy_device.touchtext(By.id('id/title'), 'Select all', MonkeyDevice.DOWN_AND_UP)
                        MonkeyRunner.sleep(5)
                        break
                    #end
                    #end
                #add by jianke 08/06
                wait_delete_times = 0
                while not ceasy_device.visible(By.id('id/delete')):
                    MonkeyRunner.sleep(2)
                    wait_delete_times = wait_delete_times + 1
                    print 'wait delete time ',wait_delete_times*2
                    if wait_delete_times > 2:
                        break
                if ceasy_device.visible(By.id('id/delete')):
                    print 'touch delete All trash!!!'
                    ceasy_device.touch(By.id('id/delete'), MonkeyDevice.DOWN_AND_UP)
                    if box_name == 'Sent' or box_name == 'Outbox':
                        MonkeyRunner.sleep(2)
                    if box_name == 'Trash':
                        MonkeyRunner.sleep(8)
                    #add by jianke 08/06
                    if box_name == 'Trash':
                        cdevice.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
                        MonkeyRunner.sleep(2)
                        if common.Get_keyType(ceasy_device,chierarchyviewer,'id/title',6):
                            print 'go to refresh in trash'
                            ceasy_device.touchtext(By.id('id/title'), 'Refresh', MonkeyDevice.DOWN_AND_UP)
                            MonkeyRunner.sleep(3)
                        else:
                            print 'refresh failed!!!'
                    #end
                else:
                    print 'delete Fail!!!'
                    shotpath = ImagePath + "\\" + str(common.timeCalc()) + "_delete_fail.png"
                    common.SaveFailImg(cdevice,shotpath)
                if box_name != 'Trash' and box_name != 'Outbox':
                    num = GetNumberofMail(box_name)
                else:
                    break
        except:
            print 'delete next time!!!'
            shotpath = ImagePath + "\\"+ str(common.timeCalc()) + '_delete_next_time.png'
            common.SaveFailImg(cdevice,shotpath)
            return False
    else:
        print 'get wrong point!!!!!'
        shotpath = ImagePath + "\\"+ str(common.timeCalc()) + ".png"
        common.SaveFailImg(cdevice,shotpath)
        return False
    return True
#end

def SendEmail(times,att_Flag):
    global SucTimes

    height_w = int(str(height))
    if height_w == 480:
        height_w = 202
    
    for loop in range (times):
        #changed by jianke 0206
        if EnterEmail():
            try:
                DelSentMail()
                EnterMailBox("Inbox")
                print 'Select an Email'
                # If att_Flag Is 1 ,Select Email Without Attachment
                # If att_Flag Is 0 ,Select Email With Attachment
                #add by jianke 07/11 07/25
                if common.GetWind_Id(chierarchyviewer,ceasy_device,id_name.EMAIL_APPID,'id/content_pane',1,3,1,4):
                    if SelectMail(att_Flag,offset = 2):
                        EnterForward(att_Flag)
                        #add by jianke 07/17
                        print 'height_w 07/17 ',height_w
                        common.Get_keyBoard_wind(cdevice,chierarchyviewer,'id/compose',height_w)
                        InputTo()
                        #end
                        PressSendEmail()
                        # Check Sent Success
                        EnterMailBox("Sent")
                        # Check in Sent box
                        if CkeckInSentBox(15):
                            print "successful send email loop: " + str(loop+1)
                            SucTimes = SucTimes + 1
                            print "Trace Success Loop " + str(loop + 1)
                        else:
                            print "fail send email loop: " + str(loop+1)
                            shotpath = ImagePath + "\\Fail_Sent_with_" + str(att_Flag) + '_Attachment_By_' + NetWork_type + '_' + str(loop+1) + ".png"
                            common.SaveFailImg(cdevice,shotpath)
                    else:
                        print 'select no email, no email record refresh out!'
                        shotpath = ImagePath + "\\select_no_email_" + str(att_Flag) + '_Attachment_By_' + NetWork_type + '_' + str(loop+1) + ".png"
                        common.SaveFailImg(cdevice,shotpath)
            except Exception,e:
                shotpath = ImagePath + "\\Sent_exc_with_" + str(att_Flag) + '_Attachment_By_' + NetWork_type + '_' + str(loop+1) + ".png"
                common.SaveFailImg(cdevice,shotpath)
                print "SendEmail Exception Error:",e
                traceback.print_exc()
        else:
            print 'fail start email'
            shotpath = ImagePath + "\\NotEnter_Sent_with_" + str(att_Flag) + '_Attachment_By_' + NetWork_type + '_' + str(loop+1) + ".png"
            common.SaveFailImg(cdevice,shotpath)
    #add by jianke 02/29
    if EnterMailBox("Trash") and GetNumberofMail("Trash")>0:
        DelAllMail("Trash")
    #end
    print 'Send Email Test complete'
    
def SendEmail_old(times,att_Flag):
    global SucTimes
    if EnterEmail():
        for loop in range (times):
            try:
                EnterMailBox("Inbox")
                print 'Select an Email'
                # If att_Flag Is 1 ,Select Email Without Attachment
                # If att_Flag Is 0 ,Select Email With Attachment
                SelectMail(att_Flag,offset = 2)
                EnterForward()
                InputTo()
                PressSendEmail()
                # Check Sent Success
                print 'Enter Out Box To Check'
                EnterMailBox("Outbox")           
                if CheckInOutBox():
                    print 'Check eamil in Sentbox'
                    EnterMailBox("Sent")
                    MonkeyRunner.sleep(10)
                    SentDelFlag = DelAllMail()
                    EnterMailBox("Trash")
                    TrashFlag = DelAllMail()
                    if SentDelFlag and TrashFlag:
                        print 'Delete Email Success'
                        SucTimes = SucTimes + 1
                        print "Trace Success Loop "+ str(loop + 1)
                    else:
                        shotpath = ImagePath+"\\Fail_Del_with_"+str(att_Flag)+'_Attachment_By_'+NetWork_type+'_'+str(loop+1)+".png"
                        common.SaveFailImg(cdevice,shotpath)
                else :
                    shotpath = ImagePath+"\\Fail_Sent_with_"+str(att_Flag)+'_Attachment_By_'+NetWork_type+'_'+str(loop+1)+".png"
                    common.SaveFailImg(cdevice,shotpath)
                    #DelAllMail()
            except Exception,e:
                shotpath = ImagePath+"\\Sent_exc_with_"+str(att_Flag)+\
                           '_Attachment_By_'+NetWork_type+'_'+str(loop+1)+".png"
                common.SaveFailImg(cdevice,shotpath)
                print "SendEmail Exception Error:",e
                traceback.print_exc()
        print 'Send Email Test complete'

def SelectMail(index,offset = None):
    MonkeyRunner.sleep(2)
    #add by jianke 14/06/05  07/25
    conversation_list_child_node = GetListNode()
    #end
    list_num = conversation_list_child_node.children.size()
    print 'list_num 07/09 ',list_num
    if project_name == 'yaris35_ATT':
        #add by jianke 07/17
        refresh_inbox_times = 0
        while list_num < 3:
            #add by jianke 14/07/26
            cdevice.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            if common.Get_keyType(ceasy_device,chierarchyviewer,'id/title',1):
                print 'go to refresh'
                ceasy_device.touchtext(By.id('id/title'), 'Refresh', MonkeyDevice.DOWN_AND_UP)
            #end
            MonkeyRunner.sleep(5)
            refresh_inbox_times = refresh_inbox_times + 1
            conversation_list_child_node = GetListNode()
            list_num = conversation_list_child_node.children.size()
            print 'list_num ' + str(refresh_inbox_times) + '  ' + str(list_num)
            #so slow refresh!!!!!!!!!!!!!!!!!!!!!!!!!!!
            print 'so slow refresh!!!!!!!!!'
            print 'refresh_inbox_times ',refresh_inbox_times*2
            if refresh_inbox_times > 10:
                break
        #end
        if list_num > 3 and index == 1:
            index = list_num - 2
        elif list_num > 3 and index == 0:
            index = list_num - 3
        elif list_num == 3 and index == 1:
            index = 2
        elif list_num == 3 and index == 0:
            index = 1
        else:
            return False
    else:
        if index == 1:
            index = list_num - 1
        elif index == 0:
            index = list_num - 2
        elif list_num > 3: 
            index = index    
        else:
            return False
    mail_pos =  chierarchyviewer.getAbsoluteCenterOfView(conversation_list_child_node.children[index])
    cdevice.touch(mail_pos.x,mail_pos.y,MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    return True

def EnterForward(att_Flag):
    print 'Forward The Email'
    width_w = int(str(width))
    width_w = int(width_w)
    print 'width_w 2222 ',width_w
    height_w = int(str(height))
    height_w = height_w/4
    height_w = int(height_w)
    print 'height_w 2222 ',height_w
    #add by jianke 14/07/09 001 id/conversation_pane
    conversation_pane_node = common.GetNode(cdevice,chierarchyviewer,'id/conversation_pane')
    if conversation_pane_node is None:
        raise TypeError,"Get Node FAIL"
    print 'conversation_pane_node ',conversation_pane_node.children.size()
    child_pane_node = conversation_pane_node.children[att_Flag]
    overflow_node = common.GetNode(cdevice,chierarchyviewer,'id/overflow',child_pane_node)
    if overflow_node is None:
        raise TypeError,"Get Node FAIL"
    overflow_node_point =chierarchyviewer.getAbsoluteCenterOfView(overflow_node)
    print 'overflow_node_point ',overflow_node_point
    #add by jianke test 07/09
    while overflow_node_point.x < 0 or overflow_node_point.x > width_w:
        if att_Flag == 1:
            att_Flag = 0
        else:
            att_Flag = 1
        child_pane_node = conversation_pane_node.children[att_Flag]
        overflow_node = common.GetNode(cdevice,chierarchyviewer,'id/overflow',child_pane_node)
        if overflow_node is None:
            raise TypeError,"Get Node FAIL"
        overflow_node_point =chierarchyviewer.getAbsoluteCenterOfView(overflow_node)
        print 'overflow_node_point ',overflow_node_point
    #end
    cdevice.touch(overflow_node_point.x,overflow_node_point.y,MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    #end
    ceasy_device.touchtext(By.id('id/title'),'Forward',MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    MaxTime = 0
    text = chierarchyviewer.getFocusedWindowName()
    print 'text begin ... ',text
    #add by jianke 07/09
    while text != id_name.EMAIL_FWD:
        MonkeyRunner.sleep(1)
        text = chierarchyviewer.getFocusedWindowName()
        print 'text after ... ',text
        MaxTime = MaxTime + 1
        if MaxTime > 5:
            print 'Enter Forward Failed'
            break

def InputTo():
    print 'Type Address'
    Receiver = random.choice(RECEIVERLIST)
    Receiver = Receiver.strip()
    ceasy_device.type(By.id('id/to_content'),Receiver)
    MonkeyRunner.sleep(2)
    #add by jianke test 07/14 id/to
    reto_node = common.GetNode(cdevice,chierarchyviewer,'id/to')
    if reto_node is None:
        raise TypeError,"Get Node FAIL"
    MonkeyRunner.sleep(2)
    check_name = chierarchyviewer.getText(reto_node)
    print 'check_name ',check_name
    #end

def PressSendEmail():
    print 'Send The Email'
    #add by jianke 07/09
    ceasy_device.touch(By.id('id/send'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    print 'send ..... 07/09'
    cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

def CkeckInSentBox(send_times):
    MaxTime = 0
    while not (GetNumberofMail("Sent") > 0):
        print "the num of email in sent box is: " + str(GetNumberofMail("Sent"))
        print "Send Email wait " + str(MaxTime) + " by 15s"
        #add by jianke 14/06/05
        cdevice.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        if common.Get_keyType(ceasy_device,chierarchyviewer,'id/title',1):
            print 'go to refresh'
            ceasy_device.touchtext(By.id('id/title'), 'Refresh', MonkeyDevice.DOWN_AND_UP)
        #end
        MonkeyRunner.sleep(10)
        #add by jianke 07/22
        conversation_list_child_node = GetListNode()
        send_number = conversation_list_child_node.children.size()
        print 'conversation_list_child_node 07/22 email in outbox ',send_number
        if send_number == 2:
            #add by jianke 07/26
            try:
                swipeable_content_node = common.GetNode(cdevice,chierarchyviewer,'id/swipeable_content',conversation_list_child_node.children[0])
                if swipeable_content_node is None:
                    raise TypeError,"Get Node FAIL"
                outbox_node = common.GetNode(cdevice,chierarchyviewer,'id/outbox',swipeable_content_node)
                if outbox_node is None:
                    raise TypeError,"Get Node FAIL"
                if chierarchyviewer.getText(outbox_node).find('Outbox') > -1:
                    #test
                    '''
                    outbox_node_pos =  chierarchyviewer.getAbsoluteCenterOfView(outbox_node)
                    cdevice.touch(outbox_node_pos.x,outbox_node_pos.y,MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(2)
                    '''
                    #end
                    ceasy_device.touch(By.id('id/outbox'),MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(2)
                    #add by jianke maybe need more excactly 07/22
                    cdevice.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(1)
                    if common.Get_keyType(ceasy_device,chierarchyviewer,'id/title',1):
                        print 'go to refresh outbox'
                        ceasy_device.touchtext(By.id('id/title'), 'Refresh', MonkeyDevice.DOWN_AND_UP)
                        MonkeyRunner.sleep(10)
                        #add by jianke 08/02
                        if GetNumberofMail("Outbox") > 1:
                            print 'enter here!!!'
                            DelAllMail('Outbox')
                        #end
                EnterMailBox("Sent")
            except: 
                cdevice.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                if common.Get_keyType(ceasy_device,chierarchyviewer,'id/title',1):
                    print 'go to refresh'
                    ceasy_device.touchtext(By.id('id/title'), 'Refresh', MonkeyDevice.DOWN_AND_UP)
                    print '22222222222222222222 jk'
                    MonkeyRunner.sleep(3)
            #end
        MaxTime = MaxTime + 1
        if MaxTime > send_times:  #30
            break
    if MaxTime <= send_times:
        print "Send Email with in " + str(15*send_times) + " seconds successful"
        return True
    elif MaxTime > send_times:
        print "Send Email More Than " + str(15*send_times) + " seconds"
        return False 

def CheckInOutBox():
    MaxTime = 0
    while (GetNumberofMail() > 0):  
        MonkeyRunner.sleep(5)#10
        MaxTime = MaxTime + 1
        if MaxTime > 60:#30
            break
    if MaxTime > 60:
        print "Send Email More Than 5 mins"
        return False 
    else:
        print 'The eamil leave outbox'   
        return True

def BackToInbox():
    for loop_time in range(5):
        if ceasy_device.visible(By.id('id/spinner_line_1')):
            if ceasy_device.getText(By.id("id/spinner_line_1")) == "Inbox":
                break
        cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)

def OpenEmail(times):
    global SucTimes
    
    for loop in range (times):
        if EnterEmail():
            EnterMailBox("Inbox")
            try:
                # open Email
                SelectMail(0,offset = 2)
                if ceasy_device.visible(By.id('id/list')):
                    shotpath = ImagePath+"\\Fail_Open_"+str(loop+1)+".png"
                    common.SaveFailImg(cdevice,shotpath)
                else:
                    SucTimes = SucTimes + 1
                    print "Trace Success Loop "+ str(loop + 1)
                    cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
            except Exception,e:
                shotpath = ImagePath+"\\Open_exc_"+str(loop+1)+".png"
                common.SaveFailImg(cdevice,shotpath)
                print "OpenEmail Exception Error:",e
                traceback.print_exc()
                try:
                    BackToInbox()
                except Exception,e:
                    traceback.print_exc()
        else:
            print 'fail start email'
            shotpath = ImagePath+"\\NotEnter_Email_"+str(loop+1)+".png"
            common.SaveFailImg(cdevice,shotpath)
        print 'Open Email Test complete'
        
def main():
    global NetWork_type

    time_Start = common.timeCalc()
    
    print 'Email Start Test'
    common.BackToHome(cdevice)
    common.ShowDeviceMemoryInfo(cdevice)

    if True:
        NetWork_type = '3G'
        print 'Send an Email with no attachment by ' + NetWork_type + ' NetWork'
        SendEmail(SendBy3G,1)

    if True:
        NetWork_type = '3G'
        print 'Send an Email with attachment by ' + NetWork_type + ' NetWork'
        SendEmail(SendBy3G,0)
    
    OpenEmail(opentimes)
    
    common.BackToHome(cdevice)
    print "Finished Email Test"
    
    common.ShowDeviceMemoryInfo(cdevice)
    print "Success Times:", SucTimes
    Rate = SucTimes/TestTimes*100
    if Rate < 95:
        print 'Result Fail Success Rate Is ' + str(Rate) + '%'
    else:
        print 'Result Pass Success Rate Is ' + str(Rate) + '%'
    timeEnd = common.timeCalc()
    totalTime = timeEnd-time_Start
    print '5.1.03_Email time = ' + str(totalTime) + 'mins'
    
if __name__ == "__main__":
    main()
# Scrpit End
