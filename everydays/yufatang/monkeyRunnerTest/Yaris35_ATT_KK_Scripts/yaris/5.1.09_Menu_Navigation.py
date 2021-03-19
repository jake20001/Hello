#coding=UTF-8
#-------------------------------------------------------------------------------
# Title:        5.1.9_Menu_Navigation
# Precondition: 
# Description:  Used for Yaris_3.5_ATT
# Platform:     4.2.2
# Resolution:   320x480
# Version:      C19
# Created:      Jake
#-------------------------------------------------------------------------------
from __future__ import division
import os
import sys
import string
import random
import traceback
import ConfigParser
from datetime import *
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from com.android.monkeyrunner.easy import By
#\\.. road back one time
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


isAABSupported = config.get("Menu","AAB_ENABLED")
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
'''
if isAABSupported == "TRUE":
    print 'Trace Total Times 29'
else:
    print 'Trace Total Times 28'
'''

SucTimes = 0
FailTimes = 0
flag = 1
#mobile TV add by jianke 08/21
Flag_TV = config.get("MobleTV","Flag_TV")
if Flag_TV == 'ON':
    Flag_NoTV = False
else:
    Flag_NoTV = True
#end

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


def SwithWorkSpace(start,end): #1->2
    if start > end:
        for times in range(start - end):
            cdevice.drag((20,250),(300,250),0.2,10)
    else:
        for times in range(end - start):
            cdevice.drag((300,250),(20,250),0.2,10)
    MonkeyRunner.sleep(1)

#--------------worksapce 1 ----------------#
def enterGoogleSearchBox():
    global SucTimes
    global FailTimes
    global ImagePath

    try:
        cdevice.touch(145,100,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        a = [GoogleSearchBox_ID,GoogleSearchBox2_ID]
        gb_id = a[1]
            
        if common.isEnterApp(ceasy_device,gb_id):
            MonkeyRunner.sleep(1)
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter GoogleSearchBox"
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Can not Enter GoogleSearchBox"
        shotpath = ImagePath+"\\Interaction_exc_GoogleSearchBox" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()    
    common.BackToIdle(cdevice)

def DeactivateAlarm():
    list_node = common.GetNode(cdevice,chierarchyviewer,'id/alarms_list')
    if list_node is None:
        raise TypeError,"Get Node FAIL"
    alarm_num = list_node.children.size()-1
    print alarm_num
    for index in range(alarm_num):
        alarm_node = list_node.children[index]
        slipbtn_node = common.GetNode(cdevice,chierarchyviewer,'id/slipbtn',alarm_node)
        if slipbtn_node is None:
            raise TypeError,"Get Node FAIL"
        if slipbtn_node.namedProperties.get("isChecked").value == "false":
            slipbtn_pos = chierarchyviewer.getAbsoluteCenterOfView(slipbtn_node)
            cdevice.touch(slipbtn_pos.x,slipbtn_pos.y,MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            
def enterDeskClock():
    global SucTimes    
    global FailTimes
    global ImagePath

    try:
        cdevice.touch(161,138,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    
        if common.isEnterApp(ceasy_device,DeskClock_ID):
            #set
            ceasy_device.touch(By.id('id/set_alarm'),MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP) 
            MonkeyRunner.sleep(1)
            #delete all
            if ceasy_device.visible(By.id('id/del_alarm')):
                ceasy_device.touch(By.id('id/del_alarm'),MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                List_Node = common.GetNode(cdevice,chierarchyviewer,'id/alarm_list')
                if List_Node is None:
                    raise TypeError,"Get Node FAIL"
                num = List_Node.children.size()
                for loop in range(num):
                    alarm_Node = chierarchyviewer.getAbsoluteCenterOfView(List_Node.children[loop])
                    cdevice.touch(alarm_Node.x,alarm_Node.y,MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(0.5)
                ceasy_device.touch(By.id('id/alarm_delete'),MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                ceasy_device.touch(By.id('id/button1'),MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
            #add one
            ceasy_device.touch(By.id('id/add_alarm'),MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            ceasy_device.touch(By.id('id/label'),MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(0.5)
            #cdevice.type('Add One Alarm')
            #cdevice.press('Add One Alarm')
            #MonkeyRunner.sleep(1)
            cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP) 
            MonkeyRunner.sleep(0.5)
            #ceasy_device.type(By.id('id/label'),'Add One Alarm')
            #MonkeyRunner.sleep(1)
            ceasy_device.touch(By.id('id/alarm_save'),MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            DeactivateAlarm()
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter DeskClock"
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter DeskClock"
            shotpath = ImagePath+"\\Fail_enter_DeskClock" + ".png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Exception,Can not Enter DeskClock"
        shotpath = ImagePath+"\\Interaction_exc_DeskClock" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()    
    common.BackToIdle(cdevice)

def enterDeskWeather():
    global SucTimes    
    global FailTimes
    global ImagePath

    id_items = [DeskWeather_ID,DeskWeather_C1J_ID]
    id_item = id_items[1]
    try:
        cdevice.touch(156,244,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    
        if common.isEnterApp(ceasy_device,id_item):
            MonkeyRunner.sleep(1)
            SucTimes = SucTimes + 1
            
            print "Trace Success Enter DeskWeather"
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter DeskWeather"
            shotpath = ImagePath+"\\Interaction_exc_DeskWeather0" + ".png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Can not Enter DeskWeather"
        shotpath = ImagePath+"\\Interaction_exc_DeskWeather" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()    
    common.BackToIdle(cdevice)

def enterFeaturedApps():
    global SucTimes    
    global FailTimes
    global ImagePath

    try:
        cdevice.touch(122,193,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    
        if common.isEnterApp(ceasy_device,FeaturedApps2_ID):
            MonkeyRunner.sleep(1)
            SucTimes = SucTimes + 1
            
            print "Trace Success Enter FeaturedApps"
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Can not Enter FeaturedApps"
        shotpath = ImagePath+"\\Interaction_exc_FeaturedApps" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()    
    common.BackToIdle(cdevice)
    
def showSubPeopleMenu(text=None):
        cdevice.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        print 'text ' + str(text)
        ceasy_device.touchtext(By.id('id/title'),text,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        if text == 'Edit':   
            cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)            
        cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        #add by jianke 08/01
        if text == 'Accounts':
            if ceasy_device.visible(By.id('id/prefs_frame')):
                cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
        #end
    
def enterPeople():
    global SucTimes 
    global FailTimes
    global ImagePath

    width_w = int(str(width))
    width_w = width_w/4
    height_w = int(str(height))
    height_w = height_w/2
    width_w = int(width_w)
    print 'width_w 2222 ',width_w
    height_w = int(height_w)
    print 'height_w 2222 ',height_w
    
    try:
        cdevice.touch(46,340,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        if common.isEnterApp(ceasy_device,id_name.Contact_ATT_ID) or common.isEnterApp(ceasy_device,id_name.Contact_ID):
            MonkeyRunner.sleep(1)
            if isAABSupported == "TRUE":
                delay = 0
                print str(ceasy_device.visible(By.id('id/left_button'))),str(ceasy_device.visible(By.id('id/action_bar_container'))),\
                    str(ceasy_device.visible(By.id('id/middle_button')))
                while ceasy_device.visible(By.id('id/left_button'))==False and ceasy_device.visible(By.id('id/middle_button'))==False:
                    print 'delay -> ' + str(delay)  
                    MonkeyRunner.sleep(1)
                    delay = delay + 1
                if ceasy_device.visible(By.id('id/left_button')):
                    ceasy_device.touch(By.id('id/left_button'),MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(0.5)
                    ceasy_device.touch(By.id('id/middle_button'),MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(0.5)
                if ceasy_device.visible(By.id('id/middle_button')):
                    ceasy_device.touch(By.id('id/middle_button'),MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(3)
            List_Node = common.GetNode(cdevice,chierarchyviewer,'id/action_bar_container')
            if List_Node is None:
                raise TypeError,"Get Node FAIL"
            #middle
            People_Middle_Node = chierarchyviewer.getAbsoluteCenterOfView(List_Node.children[2].children[0].children[1])
            print 'People_Middle_Node ' + str(People_Middle_Node)
            cdevice.touch(People_Middle_Node.x,People_Middle_Node.y,MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(0.5)

            a = ['Contacts to display','Import contacts','Export contacts','Delete','Accounts','Revert AT&T Address Book','Show contacts type']#,'Settings'
            for loop2 in range(len(a)):
                showSubPeopleMenu(a[loop2])
            #enter setting
            people_set_inner_id = 'com.android.contacts/com.android.contacts.preference.ContactsPreferenceActivity'
            people_set_id = 'com.android.contacts/com.android.contacts.preference.ContactsSettingsPreferenceActivity'
            cdevice.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            wind_pop_Flag = common.GetWind_Pop_KeyWord(chierarchyviewer,cdevice,ceasy_device,'PopupWindow',None,1,3,True)
            if wind_pop_Flag:
                ceasy_device.touchtext(By.id('id/title'),'Settings',MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                wind_set_people_Flag = common.GetWind_Keyword(chierarchyviewer,ceasy_device,cdevice,people_set_id,'id/action_bar_title','Settings',0.5,3)
                if wind_set_people_Flag:
                    ceasy_device.touchtext(By.id('id/title'),'Display options',MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(0.5)
                    if chierarchyviewer.getFocusedWindowName() == people_set_inner_id:
                        for loop1 in range(2):
                            cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                            MonkeyRunner.sleep(1)
                    else:
                        cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                        MonkeyRunner.sleep(1)
            wind_add_Flag = common.GetWind_Id(chierarchyviewer,ceasy_device,id_name.Contact_ID,'id/menu_add_contact',0.5,3,0.5,3)
            if wind_add_Flag:
                ceasy_device.touch(By.id('id/menu_add_contact'),MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(0.5)
                Flag_keyBoard = True
                while Flag_keyBoard:
                    print 'go 222222222222'
                    lay_node = common.GetNode(cdevice,chierarchyviewer,'id/content')
                    print 'lay_node ... ',lay_node
                    if lay_node is None:
                        raise TypeError,"Get Node FAIL"
                    lay_height = lay_node.height
                    print 'lay_height ',lay_height
                    if lay_height < 10 or lay_height > 240:
                        MonkeyRunner.sleep(1)
                        continue
                    else:
                        Flag_keyBoard = False
                        break
                print 'go to here 2'
                for loop in range(2):
                    cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(1)
            People_Left_Node = chierarchyviewer.getAbsoluteCenterOfView(List_Node.children[2].children[0].children[0])
            cdevice.touch(People_Left_Node.x,People_Left_Node.y,MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(0.5)
            wind_times = 0
            wind_Flag = True
            while not ceasy_device.visible(By.id('id/menu_add_group')):
                MonkeyRunner.sleep(0.5)
                wind_times = wind_times + 1
                if wind_times > 2:
                    wind_Flag = False
                    break
            #end
            if wind_Flag:
                ceasy_device.touch(By.id('id/menu_add_group'),MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                text_pop = chierarchyviewer.getFocusedWindowName()
                if text_pop != id_name.Contact_ID:
                    cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(1)
            b = ['Import contacts','Export contacts','Delete','Accounts','Revert AT&T Address Book','Settings']
            for loop3 in range(len(b)):
                showSubPeopleMenu(b[loop3])
            #Right
            People_Right_Node = chierarchyviewer.getAbsoluteCenterOfView(List_Node.children[2].children[0].children[2])
            cdevice.touch(People_Right_Node.x,People_Right_Node.y,MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(0.5)
            ceasy_device.touch(By.id('id/menu_add_favor'),MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(0.5)
            cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            c = ['Edit','Import contacts','Export contacts','Accounts','Revert AT&T Address Book','Settings']
            for loop4 in range(len(c)):
                showSubPeopleMenu(c[loop4])
            #Search node
            ceasy_device.touch(By.id('id/menu_search'),MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(0.5)
            common.Get_keyBoard_wind(cdevice,chierarchyviewer,'id/content',height_w*2)
            for loop in range(2):
                cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter People"
            print '111111111111111111111111111111'
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter People"
            shotpath = ImagePath+"\\Fail_enter_People" + ".png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Exception,Can not Enter People"
        shotpath = ImagePath+"\\Interaction_exc_People" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()     
    common.BackToIdle(cdevice)

def showSubCalendarMenu(text=None):
    wind_pop_Flag = common.GetWind_Pop_KeyWord(chierarchyviewer,cdevice,ceasy_device,'PopupWindow','id/top_button_date',1,3,False)
    if wind_pop_Flag:
        ceasy_device.touchtext(By.id('id/button_view'),text,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(0.5)
        
def showSubCalendarMenu2(text=None):
    wind_pop_Flag = common.GetWind_Pop_KeyWord(chierarchyviewer,cdevice,ceasy_device,'PopupWindow',None,1,3,True)
    if wind_pop_Flag:
        ceasy_device.touchtext(By.id('id/title'),text,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    if text=='New event' or text=='Search':
        MonkeyRunner.sleep(0.5)
        for loop1 in range(2):
            cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(0.5)
            if text=='Search':
                MonkeyRunner.sleep(0.5)
    elif text=='Refresh':
        MonkeyRunner.sleep(0.5)
    elif text=='Calendars to display' or text=='Clear events' or text=='Go to' or text=='Settings':
        cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(0.5)
        if text=='Go to':
            MonkeyRunner.sleep(0.5)
        
def enterCalendar():
    global SucTimes 
    global FailTimes
    global ImagePath
    
    try:
        cdevice.touch(114,340,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    
        if common.isEnterApp(ceasy_device,Calendar_ID):
            MonkeyRunner.sleep(1)
            a = ['Day','Week','Month','Agenda']
            for loop in range(len(a)):
                showSubCalendarMenu(a[loop])
            b = ['New event','Refresh','Search','Calendars to display','Clear events','Go to']#,'Settings'
            for loop2 in range(len(b)):
                showSubCalendarMenu2(b[loop2])
            #enter setting
            cdevice.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1.5)
            ceasy_device.touchtext(By.id('id/title'),'Settings',MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1.5)
            #enter submenu General in setting
            print 'test General settings'
            calendar_set_id = 'com.android.calendar/com.android.calendar.CalendarSettingsActivity'
            txt_outer_wind_get = chierarchyviewer.getFocusedWindowName()
            wind_outer_times = 0
            wind_outer_Flag = True
            while calendar_set_id != txt_outer_wind_get:
                MonkeyRunner.sleep(1)
                txt_outer_wind_get = chierarchyviewer.getFocusedWindowName()
                wind_outer_times = wind_outer_times + 1
                if wind_outer_times > 3:
                    wind_outer_Flag = False
                    break
            if calendar_set_id == txt_outer_wind_get:
                if ceasy_device.getText(By.id('id/action_bar_title')).find('Settings') > -1:
                    wind_outer_Flag = True
            if wind_outer_Flag:
                ceasy_device.touchtext(By.id('id/title'),'General settings',MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                #enter Week starts on
                print 'test Week starts on'
                txt_wind_get = chierarchyviewer.getFocusedWindowName()
                wind_times = 0
                wind_Flag = True
                while calendar_set_id != txt_wind_get:
                    MonkeyRunner.sleep(1)
                    txt_wind_get = chierarchyviewer.getFocusedWindowName()
                    wind_times = wind_times + 1
                    if wind_times > 3:
                        wind_Flag = False
                        break
                if calendar_set_id == txt_wind_get:
                    if ceasy_device.getText(By.id('id/action_bar_title')).find('General settings') > -1:
                        wind_Flag = True
                if wind_Flag:
                    ceasy_device.touchtext(By.id('id/title'),'Week starts on',MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(1)
                    cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(0.5)
                for loop in range(3):
                    cdevice.drag((50,300),(50,100),0.5,10, MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(0.5)
                #enter Select ringtone
                print 'test Select ringtone'
                ceasy_device.touchtext(By.id('id/title'),'Select ringtone',MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(0.5)
                #enter Default reminder time
                print 'test Default reminder time'
                wind_set_Flag = common.GetWind_Keyword(chierarchyviewer,ceasy_device,cdevice,calendar_set_id,'id/action_bar_title','General settings',0.5,3)
                if wind_set_Flag:
                    print 'test common function'
                    ceasy_device.touchtext(By.id('id/title'),'Default reminder time',MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(1)
                    cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(0.5)
                #enter Quick responses
                print 'test Quick responses'
                ceasy_device.touchtext(By.id('id/title'),'Quick responses',MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(0.5)
                #back to clendar setting
                cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(0.5)
            #enter About Calendar
            print 'test About Calendar'
            ceasy_device.touchtext(By.id('id/title'),'About Calendar',MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(0.5)
                
            SucTimes = SucTimes + 1
            print "Trace Success Enter Calendar"
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter Calendar"
            shotpath = ImagePath+"\\Fail_enter_Calendar" + ".png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Exception,Can not Enter Calendar"
        shotpath = ImagePath+"\\Interaction_exc_Calendar" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()   
    common.BackToIdle(cdevice)

def showAddSubMenuson(text=None):
    if common.GetWind_Pop_KeyWord(chierarchyviewer,cdevice,ceasy_device,'PopupWindow',None,1,3,True):
        ceasy_device.touchtext(By.id('id/title'),text,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    print 'text ',text
    if text=='Insert quick text':
        cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    if text=='Discard': 
        wind_msg_Flag = common.GetWind_Keyword(chierarchyviewer,ceasy_device,cdevice,id_name.Message_ID,'id/action_bar_title','Messaging',0.5,3)
        if wind_msg_Flag:
            ceasy_device.touch(By.id('id/action_compose_new'),MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(2)
        
    
def showAddSubMenu():
    ceasy_device.touch(By.id('id/action_compose_new'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    msg_set_id = "com.android.mms/com.android.mms.ui.ComposeMessageActivity"
    wind_set_Flag = common.GetWind_Keyword(chierarchyviewer,ceasy_device,cdevice,msg_set_id,'id/tv_top_title','New message',0.5,3)
    #end
    if wind_set_Flag:
        a = ['Insert quick text','Discard']
        for loop in range(len(a)):
            showAddSubMenuson(a[loop])
        msgtxt_get_in = chierarchyviewer.getFocusedWindowName()
        if msg_set_id == msgtxt_get_in:
            ceasy_device.touch(By.id('id/recipients_picker'),MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(2)
            for loop_b in range(2):
                cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
    
def showSearchSubMenu():
    width_w = int(str(width))
    width_w = width_w/4
    height_w = int(str(height))
    height_w = height_w/2
    width_w = int(width_w)
    print 'width_w 2222 ',width_w
    height_w = int(height_w)
    print 'height_w 2222 ',height_w
    ceasy_device.touch(By.id('id/search'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    #search menu
    common.Get_keyBoard_wind(cdevice,chierarchyviewer,'id/content',height_w*2)
    for loop in range(2):
        cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)

    
def messageSettingSubMenu(text=None):
    print 'text2 ' + str(text)
    txt_set_ui = 'com.android.mms/com.android.mms.ui.SettingListActivity'
    txt_get = chierarchyviewer.getFocusedWindowName()
    print 'txt_get ',txt_get
    times = 0
    Flag_back = False
    Flag_ReadBack = True
  
    while Flag_ReadBack:
        if txt_get == txt_set_ui:
            lst_node = common.GetNode(cdevice,chierarchyviewer,'id/list')
            if lst_node is None:
                raise TypeError,"Get Node FAIL"
            num_lst = lst_node.children.size()
            print 'num_lst ',num_lst
            for index in range(num_lst):
                text_child = chierarchyviewer.getText(lst_node.children[index])
                print 'text_child ',text_child
                print '3333333333333 ',str(text_child).find(text)
                if str(text_child).find(text) > -1:
                    print 'times ',times
                    Flag_back = True
                    Flag_ReadBack = False
                    break
                else:
                    MonkeyRunner.sleep(1)
                    txt_get = chierarchyviewer.getFocusedWindowName()
                    print 'txt_get3 ',txt_get
                    times = times + 1
                    if times > 5:
                        Flag_back = False
                        Flag_ReadBack = False
                        break
        else:
            MonkeyRunner.sleep(1)
            txt_get = chierarchyviewer.getFocusedWindowName()
            print 'txt_get2 ',txt_get
            times = times + 1
            if times > 2:
                Flag_back = False
                Flag_ReadBack = False
                break
    print 'Flag_back ',Flag_back
    if Flag_back:
        ceasy_device.touchtext(By.id('id/text1'),text,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)  
    
def showSubtextMenu(text=None):
    if common.GetWind_Pop_KeyWord(chierarchyviewer,cdevice,ceasy_device,'PopupWindow',None,1,3,True):
        ceasy_device.touchtext(By.id('id/title'),text,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    if text == 'Settings':
        a = ['Text messages (SMS)','Multimedia messages (MMS)','Notifications','General']
        for loop in range(len(a)):
            messageSettingSubMenu(a[loop])
    cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
        
def showSubMenu():
    a = ['Settings','Delete all threads','Wap push messages','Emergency Alerts']
    for loop in range(len(a)):
        showSubtextMenu(a[loop])
        
def enterMessage():
    global SucTimes
    global FailTimes
    global ImagePath
    
    try:
        cdevice.touch(50,350,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        txt_show = chierarchyviewer.getFocusedWindowName()
        if txt_show != id_name.Message_ID:
            print 'txt_show touch again'
            cdevice.touch(204,340,MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
    
        if common.isEnterApp(ceasy_device,id_name.Message_ID):
            MonkeyRunner.sleep(1)
            #add key
            showAddSubMenu()
            #search
            txt_msg = "com.android.mms/com.android.mms.ui.ConversationList"
            txt_msg_cl = chierarchyviewer.getFocusedWindowName()
            if txt_msg == txt_msg_cl:
                showSearchSubMenu()
            #menu
            showSubMenu()

            SucTimes = SucTimes + 1
            print "Trace Success Enter Message"
            print '111111111111111111111111111111'
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter Message"
            shotpath = ImagePath+"\\Fail_enter_Message" + ".png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Exception,Can not Enter Message"
        shotpath = ImagePath+"\\Interaction_exc_Message" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()    
    common.BackToIdle(cdevice)

def showReminderExistImage():
    ceasy_device.touch(By.id('id/grid_item_image'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    
def showReminderAddmenuItemText(text=None):
    cdevice.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.5)
    print 'text ' + str(text)
    wind_pop_Flag = common.GetWind_Pop_KeyWord(chierarchyviewer,cdevice,ceasy_device,'PopupWindow',None,1,3,True)
    #end
    if wind_pop_Flag:
        ceasy_device.touchtext(By.id('id/title'),text,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        if text=='Background':
            print 'text -> ' + str(text)
            cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
        
def showReminderAddmenuItem():
    ceasy_device.touch(By.id('id/add_menu_item'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    edit_txt = "com.tcl.memo/com.tcl.memo.activity.NoteEditor"
    edit_txt_get = chierarchyviewer.getFocusedWindowName()
    a = ['Background']#'Create new note'
    if edit_txt == edit_txt_get:
        for loop1 in range(len(a)):
            showReminderAddmenuItemText(a[loop1])
        cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    else:
        cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    #end
    
def showReminderMenuDelete():
    ceasy_device.touch(By.id('id/menu_delete'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.5)
     
def showReminderMenuSearch():
    ceasy_device.touch(By.id('id/menu_search'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.5)
    for loop in range(2):
        cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)

def showReminderMenuSort():
    ceasy_device.touch(By.id('id/switch_order'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    if not ceasy_device.visible(By.id('id/select_dialog_listview')):
        MonkeyRunner.sleep(1)
    if ceasy_device.visible(By.id('id/select_dialog_listview')):
        cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    '''
    a = ['Date updated','Date created','Title','Text','Containing voice']
    for loop in range(len(a)):
        ceasy_device.touch(By.id('id/switch_order'),MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(0.5)
        ceasy_device.touchtext(By.id('id/text1'),a[loop],MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(0.5)
    '''
    
def showReminderMenuSwitchMode():
    for loop in range(2):
        ceasy_device.touch(By.id('id/switch_display_mode'),MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(0.5)
        
def showMenuMoreItem(Version=None,text=None):
    ceasy_device.touch(By.id('id/menu_more'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.5)
    ceasy_device.touchtext(By.id('id/title'),text,MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.5)
    if Version=='C1K':
        if text=='Sort by':
            cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
    else:
        if text=='Mini Memo':
            ceasy_device.touch(By.id('id/menu_more'),MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(0.5)
            ceasy_device.touchtext(By.id('id/title'),text,MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(0.5)
    if text=='Search':
        for loop in range(2):
            cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
    
def showReminderMenuMore():
    #maybe add some menu code
    if Version=='C1K':
        b = ['View by list','Sort by','Search']
    else:
        b = ['View by list','Search','Mini Memo']
    for loop in range(len(b)):
        showMenuMoreItem(Version,b[loop])
    cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
        
def enterReminder():
    global SucTimes
    global FailTimes
    global ImagePath

    try:
        cdevice.touch(286,340,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    
        if common.isEnterApp(ceasy_device,id_name.Reminder_ID):
            MonkeyRunner.sleep(2)
            #exist image
            showReminderExistImage()
            note_txt = "com.tcl.memo/com.tcl.memo.activity.NoteList"
            note_txt_get = chierarchyviewer.getFocusedWindowName()
            if note_txt == note_txt_get:
                showReminderAddmenuItem()
            #four icons
            #showReminderMenuDelete()
            showReminderMenuSwitchMode()
            showReminderMenuSort()
            showReminderMenuSearch()
            #menu more
            #showReminderMenuMore()

            SucTimes = SucTimes + 1
            print "Trace Success Enter Reminder"
            print '111111111111111111111111111111'
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter Reminder"
            shotpath = ImagePath+"\\Fail_enter_Reminder" + ".png"
            common.SaveFailImg(cdevice,shotpath) 
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Exception,Can not Enter Reminder"
        shotpath = ImagePath+"\\Interaction_exc_Reminder" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()    
    common.BackToIdle(cdevice)

def showDialMiddleMapText(text=None):
    ceasy_device.touch(By.id('id/overflow_menu'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    ceasy_device.touchtext(By.id('id/title'),text,MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
        
def showDialMiddleMap():
    ceasy_device.touch(By.id('id/call_all'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    ceasy_device.touch(By.id('id/call_in'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    ceasy_device.touch(By.id('id/call_out'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    ceasy_device.touch(By.id('id/call_miss'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    #search jianke 0103
    ceasy_device.touch(By.id('id/searchButton'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    for loop in range(2):
        cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    #menu
    a = ['Clear call log','Settings']
    for loop in range(len(a)):
        showDialMiddleMapText(a[loop])

def showDialLeftMapItem(text=None):
    ceasy_device.touch(By.id('id/overflow_menu'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    ceasy_device.touchtext(By.id('id/title'),text,MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    
def showDialLeftMap():
    #menu
    a = ['Settings']
    for loop in range(len(a)):
        showDialLeftMapItem(a[loop])
    #search
    wind_times = 0
    wind_Flag = True
    while not ceasy_device.visible(By.id('id/searchButton')):
        MonkeyRunner.sleep(0.5)
        wind_times = wind_times + 1
        if wind_times > 2:
            wind_Flag = False
            break
    #end
    if wind_Flag:
        ceasy_device.touch(By.id('id/searchButton'),MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        for loop2 in range(2):
            cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
    
def showDialRightMapItem(text=None):
    print 'test: ' + str(text)
    MonkeyRunner.sleep(1)
    cdevice.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    ceasy_device.touchtext(By.id('id/title'),text,MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    
def showDialRightMap():
    #search
    ceasy_device.touch(By.id('id/searchButton'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    for loop in range(2):
        cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    #add contact
    ceasy_device.touch(By.id('id/add_contact'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    editxt = "com.android.contacts/com.android.contacts.activities.ContactEditorActivity"
    editxt_sh = chierarchyviewer.getFocusedWindowName()
    txt_times = 0
    Flag = True
    while editxt_sh != editxt:
        MonkeyRunner.sleep(1)
        editxt_sh = chierarchyviewer.getFocusedWindowName()
        txt_times = txt_times + 1
        if txt_times > 2:
            Flag = False
            break
    if Flag:
        print 'back ... 0324 ... '
        for loop2 in range(2):
            cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
    #menu
    a = ['Contacts to display','Import contacts','Export contacts','Accounts','Settings']#remove 'Clear frequents' for not sync
    for loop in range(len(a)):
        showDialRightMapItem(a[loop]) 
    #maybe add some more menu code
    cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    
def enterDialtacts():
    global SucTimes
    global FailTimes
    global ImagePath
    
    try:
        cdevice.touch(28,460,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        if common.isEnterApp(ceasy_device,id_name.Dialtact_ID):
            MonkeyRunner.sleep(1)
            List_Node = common.GetNode(cdevice,chierarchyviewer,'id/action_bar_container')
            if List_Node is None:
                raise TypeError,"Get Node FAIL"
            Dial_Node2 = chierarchyviewer.getAbsoluteCenterOfView(List_Node.children[2].children[0].children[1])
            print (Dial_Node2.x,Dial_Node2.y)
            cdevice.touch(Dial_Node2.x,Dial_Node2.y,MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            #show middle map
            print 'MiddleMap'
            showDialMiddleMap()
            #show left map
            print 'left Map'
            Dial_Node1 = chierarchyviewer.getAbsoluteCenterOfView(List_Node.children[2].children[0].children[0])
            cdevice.touch(Dial_Node1.x,Dial_Node1.y,MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            showDialLeftMap()
            #show Right map
            print 'RightMap'
            Dial_Node3 = chierarchyviewer.getAbsoluteCenterOfView(List_Node.children[2].children[0].children[2])
            cdevice.touch(Dial_Node3.x,Dial_Node3.y,MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            showDialRightMap()
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter Dialtacts"
            print '111111111111111111111111111111'
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter Dialtacts"
            shotpath = ImagePath+"\\Fail_enter_Dialtacts" + ".png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Exception,Can not Enter Dialtacts"
        shotpath = ImagePath+"\\Interaction_exc_Dialtacts" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()    
    common.BackToIdle(cdevice)
    
def enterMailBox(text=None):  
    ceasy_device.touchtext(By.id('id/name'),text,MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(3)
    cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    
def enterEmail():
    global SucTimes
    global FailTimes
    global ImagePath
    
    id_emails = [id_name.Email_ID,id_name.Email2_ID,id_name.Email3_ID]
    id_email = id_emails[2]

    try:
        cdevice.touch(100,460,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(3)
        if common.isEnterApp(ceasy_device,id_email):
            MonkeyRunner.sleep(1)
            print 'test: show_all_mailboxes'
            wind_times = 0
            wind_Flag = True
            while not ceasy_device.visible(By.id('id/up')):
                MonkeyRunner.sleep(0.5)
                wind_times = wind_times + 1
                if wind_times > 2:
                    wind_Flag = False
                    break
            #end
            if wind_Flag:
                a = ['Starred','Unread','VIP','Drafts','Outbox','Sent','Trash']
                for loop3 in range(len(a)):
                    print 'test: '+str(a[loop3])
                    ceasy_device.touch(By.id('id/up'),MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(1)  
                    if loop3 < 4 :
                        cdevice.drag((100,150),(100,350),0.1,10)
                        MonkeyRunner.sleep(1)
                    if loop3 >= 4 :
                        cdevice.drag((100,350),(100,150),0.1,10)
                        MonkeyRunner.sleep(1)                        
                    enterMailBox(a[loop3])
                #cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                #MonkeyRunner.sleep(1)
            b = ['Compose','Settings','Sort by']
            for loop4 in range(len(b)):
                print 'test: '+str(b[loop4])
                cdevice.touch(285,50,MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(0.5)
                text = chierarchyviewer.getFocusedWindowName()
                print str(text).find('PopupWindow')
                if not str(text).find('PopupWindow') < 0:
                    ceasy_device.touchtext(By.id('id/title'),b[loop4],MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(2)
                    if loop4 == 2:
                        cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                        MonkeyRunner.sleep(2)
                    else:
                        ceasy_device.touch(By.id('id/home'),MonkeyDevice.DOWN_AND_UP)
                        MonkeyRunner.sleep(2)                    
            ceasy_device.touch(By.id('id/search'),MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(2)
            print 'back to email home screen'
            ceasy_device.touch(By.id('id/home'),MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(2)
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter Email"
            print '111111111111111111111111111111'
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter Email"
            shotpath = ImagePath+"\\Fail_enter_Email" + ".png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Exception,Can not Enter Email"
        shotpath = ImagePath+"\\Interaction_exc_Email" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()    
    common.BackToIdle(cdevice)

def enterLauncher2():
    global SucTimes
    global FailTimes
    global ImagePath
    
    try:
        cdevice.touch(160,460,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        if common.isEnterApp(ceasy_device,id_name.Launcher2_ID):
            MonkeyRunner.sleep(1)
            List_Node = common.GetNode(cdevice,chierarchyviewer,'id/tabs')
            if List_Node is None:
                raise TypeError,"Get Node FAIL"
            for loop in range(2):
                Tab_Node = chierarchyviewer.getAbsoluteCenterOfView(List_Node.children[loop])
                print (Tab_Node.x,Tab_Node.y)
                cdevice.touch(Tab_Node.x,Tab_Node.y,MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(0.5)
                #some more menu code
                
            SucTimes = SucTimes + 1
            print "Trace Success Enter Launcher2"
            print '111111111111111111111111111111'
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter Launcher2"
            shotpath = ImagePath+"\\Fail_enter_Launcher2" + ".png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Exception,Can not Enter Launcher2"
        shotpath = ImagePath+"\\Interaction_exc_Launcher2" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()    
    common.BackToIdle(cdevice)

def enterBrowser():
    global SucTimes
    global FailTimes
    global ImagePath
    
    try:
        cdevice.touch(220,460,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(3)
        if common.isEnterApp(ceasy_device,id_name.Browser_ID):
            MonkeyRunner.sleep(1)
            #menu remove action menu 'Refresh','Stop','Home page','Save to bookmarks','Request desktop site','Save for offline reading'
            a = ['Close','Find on page','Bookmarks/History','Settings','Browser bar']
            print 'a = ' + str(len(a))
            for loop in range(len(a)):
                cdevice.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1.5)
                if loop >= 2:
                    cdevice.drag((174,381),(174,92),0.5,10, MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(1)
                ceasy_device.touchtext(By.id('id/title'),a[loop],MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                #0105
                if a[loop]=='Save to bookmarks':
                    ceasy_device.touch(By.id('id/cancel'),MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(0.5)
                if a[loop]=='Find on page':
                    for loop2 in range(2):
                        cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                        MonkeyRunner.sleep(1)
                if a[loop]=='Close' or a[loop]=='Request desktop site' or a[loop]=='Save for offline reading'\
                            or a[loop]=='Share page' or a[loop]=='Bookmarks/History' or a[loop] == 'Browser bar':
                    cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(1)
                if a[loop]=='Settings':
                    #modify by jianke 2014/04/05 the sw Version always change the text show
                    b = ['General','Privacy & security','Accessibility','Advanced','Bandwidth Management','Labs']
                    for loop2 in range(len(b)):
                        print 'test: '+str(b[loop2])
                        ceasy_device.touchtext(By.id('id/title'),b[loop2],MonkeyDevice.DOWN_AND_UP)
                        MonkeyRunner.sleep(1)
                        cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                        MonkeyRunner.sleep(1)
                    cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(1)
            #return the status before
            print 'loop ' + str(loop)
            if loop==(len(a)-1):
                cdevice.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                cdevice.drag((174,92),(174,381),0.5,10, MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
            #some more menu code
            cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter Browser"
            print '111111111111111111111111111111'
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter Browser"
            shotpath = ImagePath+"\\Fail_enter_Browser" + ".png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Exception,Can not Enter Browser"
        shotpath = ImagePath+"\\Interaction_exc_Browser" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()    
    common.BackToHome(cdevice)

def enterCamera():
    global SucTimes
    global FailTimes
    global ImagePath
    
    try:
        cdevice.touch(295,460,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        text = chierarchyviewer.getFocusedWindowName()
        print 'enterCamera text ' + str(text)
        #jianke 07/10 
        while not ceasy_device.visible(By.id('id/shutter_button_photo')):
            MonkeyRunner.sleep(1)
        #end
        
        if common.isEnterApp(ceasy_device,id_name.Camera_ID):
            MonkeyRunner.sleep(1)
            #menu  id/setting_indicator
            #cdevice.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
            ceasy_device.touch(By.id('id/setting_indicator'),MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            List_Node = common.GetNode(cdevice,chierarchyviewer,'id/mode_picker')
            if List_Node is None:
                raise TypeError,"Get Node FAIL"
            #add 0103
            num = List_Node.children.size()
            #print 'num ' + str(num)
            for loop in range(num):
                Tab_Node = chierarchyviewer.getAbsoluteCenterOfView(List_Node.children[loop])
                print (Tab_Node.x,Tab_Node.y)
                cdevice.touch(Tab_Node.x,Tab_Node.y,MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                #some more menu code
            for loop1 in range(2):
                cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter Camera"
            print '111111111111111111111111111111'
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter Camera"
            shotpath = ImagePath+"\\Fail_enter_Camera" + ".png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Exception,Can not Enter Camera"
        shotpath = ImagePath+"\\Interaction_exc_Camera" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)

#--------------worksapce 2 ----------------#
def enterYellowpageSearch():
    global SucTimes    
    global FailTimes
    global ImagePath

    try:
        if flag==2:
            cdevice.touch(159,157,MonkeyDevice.DOWN_AND_UP)
        elif flag==3:
            cdevice.touch(159,123,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        if common.startapp(cdevice,ceasy_device,YellowPageSearh_ID):
            MonkeyRunner.sleep(1)
            SucTimes = SucTimes + 1
            print "Trace Success Enter YellowpageSearch"
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Can not Enter YellowpageSearch"
        shotpath = ImagePath+"\\Interaction_exc_YellowpageSearch" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)

def enterYellowpageLocation():
    global SucTimes    
    global FailTimes
    global ImagePath

    try:
        if flag==2:
            cdevice.touch(159,190,MonkeyDevice.DOWN_AND_UP)
        elif flag==3:
            cdevice.touch(159,160,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    
        if common.startapp(cdevice,ceasy_device,YellowPageLocation_ID):
            MonkeyRunner.sleep(1)
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter YellowpageLocation"
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Can not Enter YellowpageLocation"
        shotpath = ImagePath+"\\Interaction_exc_YellowpageLocation" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)

def enterYellowpageOOBEIntro():
    global SucTimes    
    global FailTimes
    global ImagePath

    try:
        if flag==2:
            cdevice.touch(33,157,MonkeyDevice.DOWN_AND_UP)
        elif flag==3:
            cdevice.touch(33,143,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)
    
        if common.startapp(cdevice,ceasy_device,YellowPageOOBEIntro_ID):
            MonkeyRunner.sleep(1)
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter YellowpageOOBEIntro"
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Can not Enter YellowpageOOBEIntro"
        shotpath = ImagePath+"\\Interaction_exc_YellowpageOOBEIntro" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)

def enterYellowpageGasSRP():
    global SucTimes    
    global FailTimes
    global ImagePath

    try:
        if flag==2:
            cdevice.touch(35,240,MonkeyDevice.DOWN_AND_UP)
        elif flag==3:
            cdevice.touch(35,217,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)
    
        if common.startapp(cdevice,ceasy_device,YellowPageGasSRP_ID):
            MonkeyRunner.sleep(1)
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter YellowpageGasSRP"
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Can not Enter YellowpageGasSRP"
        shotpath = ImagePath+"\\Interaction_exc_YellowpageGasSRP" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)

def enterYellowpageRestaurantWizard():
    global SucTimes    
    global FailTimes
    global ImagePath

    try:
        if flag==2:
            cdevice.touch(103,240,MonkeyDevice.DOWN_AND_UP)
        elif flag==3:
            cdevice.touch(103,217,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)
    
        if common.startapp(cdevice,ceasy_device,YellowPageRestaurantWizard_ID):
            MonkeyRunner.sleep(1)
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter YellowpageRestaurantWizard"
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Can not Enter YellowpageRestaurantWizard"
        shotpath = ImagePath+"\\Interaction_exc_YellowpageRestaurantWizard" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)

def enterYellowpageBusinessSRP():
    global SucTimes    
    global FailTimes
    global ImagePath
    
    try:
        if flag==2:
            cdevice.touch(157,240,MonkeyDevice.DOWN_AND_UP)
        elif flag==3:
            cdevice.touch(157,217,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)
        if common.startapp(cdevice,ceasy_device,YellowPageBusinessSRP_ID):
            MonkeyRunner.sleep(1)
            SucTimes = SucTimes + 1
            print "Trace Success Enter YellowpageBusinessSRP"
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Can not Enter YellowpageBusinessSRP"
        shotpath = ImagePath+"\\Interaction_exc_YellowpageBusinessSRP" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)

def enterYellowpageBusiness2SRP():
    global SucTimes    
    global FailTimes
    global ImagePath

    try:
        if flag==2:
            cdevice.touch(216,240,MonkeyDevice.DOWN_AND_UP)
        elif flag==3:
            cdevice.touch(216,217,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)
        if common.startapp(cdevice,ceasy_device,YellowPageBusinessSRP_ID):
            MonkeyRunner.sleep(1)
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter YellowpageBusiness2SRP"
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Can not Enter YellowpageBusiness2SRP"
        shotpath = ImagePath+"\\Interaction_exc_YellowpageBusiness2SRP" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)
    
def enterYellowpageMyBookLanding():
    global SucTimes    
    global FailTimes
    global ImagePath
    try:
        if flag==2:
            cdevice.touch(279,240,MonkeyDevice.DOWN_AND_UP)
        elif flag==3:
            cdevice.touch(279,217,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)
    
        if common.startapp(cdevice,ceasy_device,YellowPageMyBookLanding_ID):
            MonkeyRunner.sleep(1)
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter YellowpageMyBookLanding"
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Can not Enter YellowpageMyBookLanding"
        shotpath = ImagePath+"\\Interaction_exc_YellowpageMyBookLanding" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)
    
def enterGoogleVoiceSearch():
    global SucTimes    
    global FailTimes
    global ImagePath

    try:
        cdevice.touch(274,152,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)
    
        if common.startapp(cdevice,ceasy_device,GoogleVoiceSearch_ID):
            MonkeyRunner.sleep(1)
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter GoogleVoiceSearch"
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Can not Enter GoogleVoiceSearch"
        shotpath = ImagePath+"\\Interaction_exc_GoogleVoiceSearch" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)

def enterGooglePlay():
    global SucTimes 
    global FailTimes
    global ImagePath
    
    try:
        cdevice.touch(120,350,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1.5)
    
        if common.isEnterApp(ceasy_device,id_name.GSTORE_ID):
            MonkeyRunner.sleep(1)
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter GooglePlay"
            print '111111111111111111111111111111'
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter GooglePlay"
            shotpath = ImagePath+"\\Fail_enter_GooglePlay" + ".png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Exception,Can not Enter GooglePlay"
        shotpath = ImagePath+"\\Interaction_exc_GooglePlay" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)

def showGallerySubMenu(text=None):
    print 'text ' + str(text)
    ceasy_device.touchtext(By.id('id/item_name'),text,MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    
def showGallerySubMenu_II(text=None):
    print 'text ' + str(text)
    MonkeyRunner.sleep(1)
    ceasy_device.touchtext(By.id('id/title'),text,MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(3)
    cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    
def enterGallery():
    global SucTimes
    global FailTimes
    global ImagePath
    Flag_ga = True
    
    try:
        cdevice.touch(120,350,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)    
        if common.isEnterApp(ceasy_device,id_name.Gallery_ID):
            MonkeyRunner.sleep(1)
            #check some more menu
            a = ['Albums','Locations','Times']
            for loop in range(len(a)):
                print 'a[loop] ' + str(a[loop])                
                ceasy_device.touch(By.id('id/item_name'),MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(2)
                if loop==0 or loop==1:
                    txt_get = chierarchyviewer.getFocusedWindowName()
                    print 'txt_get ',txt_get
                    times = 0
                    Flag_txt = True
                    while str(txt_get).find('PopupWindow') == -1:
                        MonkeyRunner.sleep(1)
                        times = times + 1
                        txt_get = chierarchyviewer.getFocusedWindowName()
                        print 'txt_get2 ',txt_get
                        if times > 2:
                            Flag_txt = False
                            break
                    #end
                    if Flag_txt:
                        showGallerySubMenu(a[loop+1])
                else:
                    showGallerySubMenu(a[0])

            '''
            #camera
            ceasy_device.touch(By.id('id/action_camera'),MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(2)
            #add by jianke 03/20
            time_pre = 0
            while not ceasy_device.visible(By.id('id/shutter_button_video')):
                MonkeyRunner.sleep(1)
                time_pre = time_pre + 1
                if time_pre > 3:
                    break
            if ceasy_device.visible(By.id('id/shutter_button_video')):
                cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(2)
            #end
            '''
            #menu
            cdevice.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            #modify
            '''
            delay = 0
            while ceasy_device.visible(By.id('id/action_camera')):
                delay = delay + 1
                cdevice.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                if delay>3:
                    FailTimes = FailTimes + 1
                    print "Can not Enter Gallery00"
                    Flag_ga = False
                    break
            if Flag_ga==True:
            '''
            if True:
                ceasy_device.touchtext(By.id('id/title'),'Select album',MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                
                SucTimes = SucTimes + 1
                print "Trace Success Enter Gallery"
                print '111111111111111111111111111111'
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter Gallery"
            shotpath = ImagePath+"\\Fail_enter_Gallery" + ".png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Exception,Can not Enter Gallery"
        shotpath = ImagePath+"\\Interaction_exc_Gallery" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)

def enterDriveMode():
    global SucTimes 
    global FailTimes
    global ImagePath
    
    try:
        cdevice.touch(205,350,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(3)
    
        if common.isEnterApp(ceasy_device,id_name.DriveMode2_ID):
            MonkeyRunner.sleep(2)
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter DriveMode"
            print '111111111111111111111111111111'
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter DriveMode"
            shotpath = ImagePath+"\\Fail_enter_DriveMode" + ".png"
            common.SaveFailImg(cdevice,shotpath) 
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Exception,Can not Enter DriveMode"
        shotpath = ImagePath+"\\Interaction_exc_DriveMode" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)

def enterDriveMode2():
    global SucTimes    
    global FailTimes
    global ImagePath
    try:
        cdevice.touch(275,210,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    
        if common.startapp(cdevice,ceasy_device,DriveMode_ID):
            MonkeyRunner.sleep(1)
        
            SucTimes = SucTimes + 1
            print "Trace Success Enter DriveMode2"
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter DriveMode20"
            shotpath = ImagePath+"\\Interaction_exc_DriveMode20" + ".png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Can not Enter DriveMode2"
        shotpath = ImagePath+"\\Interaction_exc_DriveMode2" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)
    
def enterCodeScanner():
    global SucTimes    
    global FailTimes
    global ImagePath
    
    try:
        if flag==2:
            cdevice.touch(204,210,MonkeyDevice.DOWN_AND_UP)
        elif flag==3:
            cdevice.touch(48,260,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    
        if common.startapp(cdevice,ceasy_device,CodeScanner_ID):
            MonkeyRunner.sleep(1)
        
            SucTimes = SucTimes + 1
            print "Trace Success Enter CodeScanner"
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter CodeScanner0"
            shotpath = ImagePath+"\\Interaction_exc_CodeScanner0" + ".png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Can not Enter CodeScanner"
        shotpath = ImagePath+"\\Interaction_exc_CodeScanner" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)

def enterDigtallocker():
    global SucTimes
    global FailTimes
    global ImagePath
    
    try:
        if Flag_NoTV:
            cdevice.touch(120,364,MonkeyDevice.DOWN_AND_UP)
        else:
            cdevice.touch(120,282,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)
        text_wind = wait_time(5)
        #common.isEnterApp(ceasy_device,id_name.DigtalLocker2_ID) or common.isEnterApp(ceasy_device,id_name.DigtalLocker_ID)
        if str(text_wind).find(id_name.Package_DigtalLocker_ID) > -1:
            MonkeyRunner.sleep(1)
            #add 08/19
            cdevice.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            #end
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter Digtallocker"
            print '111111111111111111111111111111'
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter Digtallocker"
            shotpath = ImagePath+"\\Fail_enter_Digtallocker.png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Exception,Can not Enter Digtallocker"
        shotpath = ImagePath+"\\Interaction_exc_Digtallocker.png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)

def enterTeleNav():
    global SucTimes
    global FailTimes
    global ImagePath
    
    try:
        if Flag_NoTV:
            cdevice.touch(40,364,MonkeyDevice.DOWN_AND_UP)
        else:
            cdevice.touch(40,282,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)
        text_wind = wait_time(5)
        #common.startapp(cdevice,ceasy_device,id_name.TeleNav_ID)
        if str(text_wind).find(id_name.Package_TeleNav_ID) > -1:
            MonkeyRunner.sleep(2)
            cdevice.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter TeleNav"
            print '111111111111111111111111111111'
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter TeleNav"
            shotpath = ImagePath+"\\Fail_enter_TeleNav.png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Exception,Can not Enter TeleNav"
        shotpath = ImagePath+"\\Interaction_exc_TeleNav.png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)

def enterBatteryManager():
    global SucTimes 
    global FailTimes
    global ImagePath
    
    try:
        #for 5
        cdevice.touch(115,292,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        #print BatManager_ID
        if common.isEnterApp(ceasy_device,BatManager_ID):  #SettingsSub_ID
            MonkeyRunner.sleep(1)
            #ceasy_device.touchtext(By.id('id/title'),'Battery',MonkeyDevice.DOWN_AND_UP)
            #MonkeyRunner.sleep(1)
            ListParent_Node = common.GetNode(cdevice,chierarchyviewer,'id/prefs')
            if ListParent_Node is None:
                raise TypeError,"Get Node FAIL"
            List_Node = common.GetNode(cdevice,chierarchyviewer,'id/list',ListParent_Node)
            if List_Node is None:
                raise TypeError,"Get Node FAIL"
            Battery_Node = chierarchyviewer.getAbsoluteCenterOfView(List_Node.children[2])
            cdevice.touch(Battery_Node.x,Battery_Node.y,MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)

            SucTimes = SucTimes + 1
            print "Trace Success Enter BatteryManager"
        else:
            print "Can not Enter BatteryManager0"
            FailTimes = FailTimes + 1
            shotpath = ImagePath+"\\Interaction_exc_BatteryManager0" + ".png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Can not Enter BatteryManager"
        shotpath = ImagePath+"\\Interaction_exc_BatteryManager" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)

def enterDeviceHelp():
    global SucTimes    
    global FailTimes
    global ImagePath
    
    try:   #40,364
        if Flag_NoTV:
            cdevice.touch(280,364,MonkeyDevice.DOWN_AND_UP)
        else:
            cdevice.touch(40,364,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)
        text_wind = wait_time(5)
        #common.isEnterApp(ceasy_device,id_name.Browser_ID)
        if str(text_wind).find(id_name.Package_Browser_ID) > -1:
            MonkeyRunner.sleep(1)

            SucTimes = SucTimes + 1
            print "Trace Success Enter DeviceHelp"
            print '111111111111111111111111111111'
        else:
            print "Can not Enter DeviceHelp"
            FailTimes = FailTimes + 1
            shotpath = ImagePath+"\\Fail_enter_DeviceHelp.png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Exception,Can not Enter DeviceHelp"
        shotpath = ImagePath+"\\Interaction_exc_DeviceHelp.png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)
    
def enterDataManager():
    global SucTimes    
    global FailTimes
    global ImagePath
    
    try:
        #for 5
        cdevice.touch(200,292,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    
        if common.isEnterApp(ceasy_device,DataManager_ID):
            MonkeyRunner.sleep(1)
            cdevice.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            ceasy_device.touchtext(By.id('id/title'),'Mobile hotspots',MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter DataManager"
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter DataManager0"
            shotpath = ImagePath+"\\Interaction_exc_DataManager0" + ".png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Can not Enter DataManager"
        shotpath = ImagePath+"\\Interaction_exc_DataManager" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)

def enterDataManager2():
    global SucTimes
    global FailTimes
    global ImagePath
    
    try:
        if Flag_NoTV:
            cdevice.touch(200,364,MonkeyDevice.DOWN_AND_UP)
        else:
            cdevice.touch(280,282,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        text_wind = wait_time(5)
        if common.isEnterApp(ceasy_device,id_name.DataManager2_ID):
            MonkeyRunner.sleep(1)
            #middle
            ceasy_device.touchtext(By.id('id/text_tab'),'APPS',MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            times = 0
            while ceasy_device.visible(By.id('id/ProgressBar')):
                MonkeyRunner.sleep(1)
                times = times + 1
                print 'progress ... ',times
            #right
            ceasy_device.touchtext(By.id('id/text_tab'),'MOBILE',MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            #left
            ceasy_device.touchtext(By.id('id/text_tab'),'BATTERY',MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter DataManager2"
            print '111111111111111111111111111111'
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter DataManager2"
            shotpath = ImagePath+"\\Fail_enter_DataManager2" + ".png"
            common.SaveFailImg(cdevice,shotpath) 
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Exception,Can not Enter DataManager2"
        shotpath = ImagePath+"\\Interaction_exc_DataManager2" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)

def enterAT_T(i=1):
    cdevice.touch(270,360,MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    if i==1:
        enterCodeScanner()
    elif i==2:
        enterDriveMode2()
    elif i==3:
        enterDigtallocker(0)
    elif i==4:
        enterTeleNav(0)
    if i>=1 and i<=3:
        i = i + 1
        enterAT_T(i)
    common.BackToIdle(cdevice)
#---------------------google set---------------------------
def enterChrome():
    global SucTimes
    global FailTimes
    global ImagePath
    
    try:
        cdevice.touch(40,200,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)
        text_wind = wait_time(5)
        #common.isEnterApp(ceasy_device,id_name.ChromeID)
        if str(text_wind).find(id_name.Package_Chrome_ID) > -1:
            MonkeyRunner.sleep(2)
            cdevice.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter Chrome"
            print '111111111111111111111111111111'
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter Chrome"
            shotpath = ImagePath+"\\Fail_enter_Chrome" + ".png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Exception,Can not Enter Chrome"
        shotpath = ImagePath+"\\Interaction_exc_Chrome" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)

def enterHangouts():
    global SucTimes
    global FailTimes
    global ImagePath
    
    try:
        cdevice.touch(40,200,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)
        text_wind = wait_time(5)
        #common.isEnterApp(ceasy_device,id_name.ChromeID)
        if str(text_wind).find(id_name.Package_Google_Talk_ID) > -1:
            MonkeyRunner.sleep(2)
            cdevice.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter Hangouts"
            print '111111111111111111111111111111'
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter Hangouts"
            shotpath = ImagePath+"\\Fail_enter_Hangouts" + ".png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Exception,Can not Enter Hangouts"
        shotpath = ImagePath+"\\Interaction_exc_Hangouts" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)
    
def enter_Google_Email():
    global SucTimes
    global FailTimes
    global ImagePath
    
    try:
        cdevice.touch(120,200,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)
        text_wind = wait_time(5)
        #common.isEnterApp(ceasy_device,id_name.Google_Gmail_ID)
        if str(text_wind).find(id_name.Package_Google_Gmail_ID) > -1:
            MonkeyRunner.sleep(2)
            cdevice.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter Google_Email"
            print '111111111111111111111111111111'
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter Google_Email"
            shotpath = ImagePath+"\\Fail_enter_Google_Email.png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Exception,Can not Enter Google_Email"
        shotpath = ImagePath+"\\Interaction_exc_Google_Email.png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)
    
def enter_Google_Plus():
    global SucTimes
    global FailTimes
    global ImagePath
    
    try:
        cdevice.touch(200,200,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)
        text_wind = wait_time(5)
        #common.isEnterApp(ceasy_device,id_name.Google_Plus_ID) or common.isEnterApp(ceasy_device,id_name.Google_Plus2_ID):
        if str(text_wind).find(id_name.Package_Plus_ID) > -1:
            MonkeyRunner.sleep(2)
            cdevice.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter Google_Plus"
            print '111111111111111111111111111111'
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter Google_Plus"
            shotpath = ImagePath + "\\Fail_enter_Google_Plus.png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Exception,Can not Enter Google_Plus"
        shotpath = ImagePath + "\\Interaction_exc_Google_Plus.png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)

def enter_Google_Map():
    global SucTimes
    global FailTimes
    global ImagePath
    
    try:
        cdevice.touch(280,200,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)
        text_wind = wait_time(5)
        #common.isEnterApp(ceasy_device,id_name.Google_Map_ID)
        if str(text_wind).find(id_name.Package_Google_Map_ID) > -1:
            MonkeyRunner.sleep(2)
            cdevice.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter Google_Map"
            print '111111111111111111111111111111'
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter Google_Map"
            shotpath = ImagePath+"\\Fail_enter_Google_Map.png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Exception,Can not Enter Google_Map"
        shotpath = ImagePath+"\\Interaction_exc_Google_Map.png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)
    
def enter_Google_Music():
    global SucTimes
    global FailTimes
    global ImagePath
    
    try:
        cdevice.touch(40,282,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)
        text_wind = wait_time(5)
        #common.isEnterApp(ceasy_device,id_name.Google_Music_ID)
        if str(text_wind).find(id_name.Package_Google_Music_ID) > -1:
            MonkeyRunner.sleep(2)
            cdevice.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter Google_Music"
            print '111111111111111111111111111111'
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter Google_Music"
            shotpath = ImagePath+"\\Fail_enter_Google_Music.png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Exception,Can not Enter Google_Music"
        shotpath = ImagePath+"\\Interaction_exc_Google_Music.png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)

def enter_Google_Movie():
    global SucTimes
    global FailTimes
    global ImagePath
    
    try:
        cdevice.touch(120,282,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)
        text_wind = wait_time(5)
        #common.isEnterApp(ceasy_device,id_name.Google_Movie_ID)
        if str(text_wind).find(id_name.Package_Google_Movie_ID) > -1:
            MonkeyRunner.sleep(2)
            cdevice.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter Google_Movie"
            print '111111111111111111111111111111'
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter Google_Movie"
            shotpath = ImagePath+"\\Fail_enter_Google_Movie.png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Exception,Can not Enter Google_Movie"
        shotpath = ImagePath+"\\Interaction_exc_Google_Movie.png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)

def enter_Google_PlayBooks():
    global SucTimes
    global FailTimes
    global ImagePath
    
    try:
        cdevice.touch(200,282,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)
        text_wind = wait_time(5)
        #common.isEnterApp(ceasy_device,id_name.Google_Play_Books_ID)
        if str(text_wind).find(id_name.Package_Google_Play_Books_ID) > -1:
            MonkeyRunner.sleep(2)
            cdevice.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter Google_PlatBooks"
            print '111111111111111111111111111111'
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter Google_PlatBooks"
            shotpath = ImagePath+"\\Fail_enter_Google_PlatBooks.png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Exception,Can not Enter Google_PlatBooks"
        shotpath = ImagePath+"\\Interaction_exc_Google_PlatBooks.png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)
    
def enter_Google_Play_Newsstand():
    global SucTimes
    global FailTimes
    global ImagePath
    
    try:
        cdevice.touch(280,282,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)
        text_wind = wait_time(5)
        #common.isEnterApp(ceasy_device,id_name.Google_Play_Newsstand_ID)
        if str(text_wind).find(id_name.Package_Google_Play_Newsstand_ID) > -1:
            MonkeyRunner.sleep(2)
            cdevice.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter Google_PlayNewsstand"
            print '111111111111111111111111111111'
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter Google_PlayNewsstand"
            shotpath = ImagePath+"\\Fail_enter_Google_PlayNewsstand.png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Exception,Can not Enter Google_PlayNewsstand"
        shotpath = ImagePath+"\\Interaction_exc_Google_PlayNewsstand.png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)
    
def enter_Google_Play_Games():
    global SucTimes
    global FailTimes
    global ImagePath
    
    try:
        cdevice.touch(40,364,MonkeyDevice.DOWN_AND_UP) 
        MonkeyRunner.sleep(2)
        text_wind = wait_time(5)
        #common.isEnterApp(ceasy_device,id_name.Google_Play_Games_ID) or common.isEnterApp(ceasy_device,id_name.Google_Play_Games_Sign_ID)
        if str(text_wind).find(id_name.Package_Google_Play_Games_ID) > -1 or str(text_wind).find(id_name.Package_Google_Play_Games_Sign_ID) > -1:
            MonkeyRunner.sleep(2)
            cdevice.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter Google_PlayGames"
            print '111111111111111111111111111111'
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter Google_PlayGames"
            shotpath = ImagePath+"\\Fail_enter_Google_PlayGames.png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Exception,Can not Enter Google_PlayGames"
        shotpath = ImagePath+"\\Interaction_exc_Google_PlayGames.png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)
    
def enter_Google_Play_Drive():
    global SucTimes
    global FailTimes
    global ImagePath
    
    try:
        cdevice.touch(120,364,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)
        text_wind = wait_time(5)
        #common.isEnterApp(ceasy_device,id_name.Google_Play_Drive_ID)
        if str(text_wind).find(id_name.Package_Google_Play_Drive_ID) > -1:
            MonkeyRunner.sleep(2)
            cdevice.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter Google_PlayDrive"
            print '111111111111111111111111111111'
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter Google_PlayDrive"
            shotpath = ImagePath+"\\Fail_enter_Google_PlayDrive.png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Exception,Can not Enter Google_PlayDrive"
        shotpath = ImagePath+"\\Interaction_exc_Google_PlayDrive.png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)
    
def enter_Google_Play_Youtube():
    global SucTimes
    global FailTimes
    global ImagePath
    
    try:
        cdevice.touch(200,364,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)
        text_wind = wait_time(5)
        #common.isEnterApp(ceasy_device,id_name.Google_Play_Youtube_ID)
        if str(text_wind).find(id_name.Package_Google_Play_Youtube_ID) > -1:
            MonkeyRunner.sleep(2)
            cdevice.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter Google_PlayYoutube"
            print '111111111111111111111111111111'
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter Google_PlayYoutube"
            shotpath = ImagePath+"\\Fail_enter_Google_PlayYoutube.png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Exception,Can not Enter Google_PlayYoutube"
        shotpath = ImagePath+"\\Interaction_exc_Google_PlayYoutube.png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)
    
def enter_Google_Photo():
    global SucTimes
    global FailTimes
    global ImagePath
    
    try:
        cdevice.touch(280,364,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)
        text_wind = wait_time(5)
        #common.isEnterApp(ceasy_device,id_name.Google_Photos_ID) or common.isEnterApp(ceasy_device,id_name.Google_Photos2_ID)
        if str(text_wind).find(id_name.Package_Google_Photos_ID) > -1:
            MonkeyRunner.sleep(2)
            cdevice.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter Google_Photos"
            print '111111111111111111111111111111'
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter Google_Photos"
            shotpath = ImagePath+"\\Fail_enter_Google_Photos.png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Exception,Can not Enter Google_Photos"
        shotpath = ImagePath+"\\Interaction_exc_Google_Photos.png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)
    
#-------------------------------------------------

def enterAT_T2(i=1):
    cdevice.touch(275,350,MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    if i==1:
        #print 'ok'
        enterTeleNav()
    elif i==2:
        #print 'ok'
        enterDigtallocker()
    elif i==3:
        #print 'ok'
        if Flag_NoTV:
            enterDataManager2()
        else:
            enterMobiTVPlayer()
    elif i==4:
        #print 'ok'
        if Flag_NoTV:
            enterDeviceHelp()
        else:
            enterDataManager2()
    if not Flag_NoTV:
        if i==5:
            enterDeviceHelp()
        maxn = 4
    else:
        maxn = 3
    if i>=1 and i<=maxn:
        i = i + 1
        enterAT_T2(i)
    common.BackToIdle(cdevice)

flag_work = True
def enter_Goole_set(i=1):
    global flag_work
    cdevice.touch(200,350,MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    if flag_work:
        print 'first space!!!'
        cdevice.drag((100,240),(300,240),0.5,10, MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    else:
        print 'second space!!!'
        cdevice.drag((300,240),(100,240),0.5,10, MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    if i==1:
        #print 'ok'
        enterChrome()
    elif i==2:
        #print 'ok'
        enter_Google_Email()
    elif i==3:
        #print 'ok'
        enter_Google_Plus()
    elif i==4:
        #print 'ok'
        enter_Google_Map()
    elif i==5:
        #print 'ok'
        enter_Google_Music()
    elif i==6:
        enter_Google_Movie()
    elif i==7:
        #print 'ok'
        enter_Google_PlayBooks()
    elif i==8:
        #print 'ok'
        enter_Google_Play_Newsstand()
    elif i==9:
        #print 'ok'
        enter_Google_Play_Games()
    elif i==10:
        #print 'ok'
        enter_Google_Play_Drive()
    elif i==11:
        #print 'ok'
        enter_Google_Play_Youtube()
    elif i==12:
        #print 'ok'
        enter_Google_Photo()
        flag_work = False
    elif i==13:
        enterHangouts()
    if i>=1 and i<=12:
        i = i + 1
        enter_Goole_set(i)
    common.BackToIdle(cdevice)
    
#--------------worksapce 3 ----------------#
def enterMobiTVPlayer():
    global SucTimes
    global FailTimes
    global ImagePath
    
    try:
        cdevice.touch(200,282,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(3)
        text_wind = wait_time(5)
        #common.isEnterApp(ceasy_device,id_name.MobiTVPlayer_ID)
        if str(text_wind).find(id_name.Package_MobiTVPlayer_ID) > -1:
            MonkeyRunner.sleep(1)

            cdevice.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter MobiTVPlayer"
            print '111111111111111111111111111111'
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter MobiTVPlayer"
            shotpath = ImagePath+"\\Fail_enter_MobiTVPlayer.png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        print "Exception,Can not Enter MobiTVPlayer"
        shotpath = ImagePath+"\\Interaction_exc_MobiTVPlayer.png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    finally:
        print 'finally go to here !!!!!!!!!!!!!!!!'
        #kill_service('com.mobitv.client.tv')
    common.BackToHome(cdevice)

def showArtisttabItem(text=None):
    cdevice.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    ceasy_device.touchtext(By.id('id/title'),text,MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    if text=='Sound effects':
        cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    
def enterMusic():
    global SucTimes   
    global FailTimes
    global ImagePath

    try:
        cdevice.touch(108,360,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
   
        if common.startapp(cdevice,ceasy_device,Music_ID):
            MonkeyRunner.sleep(1)

            #music menu
            ceasy_device.touch(By.id('id/artisttab'),MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            a = ['Party shuffle','Shuffle all','Sound effects']
            for loop2 in range(len(a)):
                showArtisttabItem(a[loop2])
            ceasy_device.touch(By.id('id/albumtab'),MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            for loop3 in range(len(a)):
                showArtisttabItem(a[loop3])
            ceasy_device.touch(By.id('id/songtab'),MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            b = ['Play all','Party shuffle','Shuffle all','Sound effects']
            for loop4 in range(len(b)):
                showArtisttabItem(b[loop4])
            ceasy_device.touch(By.id('id/playlisttab'),MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            c = ['Party shuffle','Sound effects']
            for loop5 in range(len(c)):
                showArtisttabItem(c[loop5])
            ceasy_device.touch(By.id('id/search_menu_nowplaying'),MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            for loop in range(3):
                cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
            #next
            cdevice.touch(280,356,MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            #play
            cdevice.touch(220,356,MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            
            SucTimes = SucTimes + 1
            print "Trace Success Enter Music"
        else:
            FailTimes = FailTimes + 1
            print "Can not Enter Music"
            shotpath = ImagePath+"\\Fail_enter_Music" + ".png"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        print "Exception,Can not Enter Music"
        FailTimes = FailTimes + 1
        shotpath = ImagePath+"\\Interaction_exc_Music" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)
    
def bottomMenu():
    enterDialtacts()
    enterEmail()
    enterLauncher2()
    enterBrowser()
    enterCamera()
    print 'test-------------'

def GoogleAndYellowPage():
    enterGoogleSearchBox()
    enterYellowpageSearch()
    enterYellowpageLocation()
    enterYellowpageOOBEIntro()
    enterYellowpageGasSRP()
    enterYellowpageRestaurantWizard()
    enterYellowpageBusinessSRP()
    enterYellowpageMyBookLanding()
    enterGoogleVoiceSearch()

def enterBar():
    cdevice.drag((200,9),(200,92),0.5,10, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    ceasy_device.touch(By.id('id/settings_button'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

def goLastIcon():
    #all icon
    #enterBar()
    List_Node = common.GetNode(cdevice,chierarchyviewer,'id/quick_settings_container')
    if List_Node is None:
        raise TypeError,"Get Node FAIL"
    num = List_Node.children.size()
    print 'num2 ' + str(num)
    for loop in range(2):
        statusBar_Node = chierarchyviewer.getAbsoluteCenterOfView(List_Node.children[num-4])
        cdevice.touch(statusBar_Node.x,statusBar_Node.y,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(5)
    #return the status before
    cdevice.drag((200,92),(200,300),0.5,10, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    
def dragPic(index=None):
    global SucTimes
    global FailTimes
    global ImagePath

    try:
        enterBar()
        #all icon
        List_Node = common.GetNode(cdevice,chierarchyviewer,'id/quick_settings_container')
        if List_Node is None:
            raise TypeError,"Get Node FAIL"
        num = List_Node.children.size()
        print 'num ' + str(num)
        num = num-4
        while index<num:
            print 'index = ' + str(index) 
            statusBar_Node = chierarchyviewer.getAbsoluteCenterOfView(List_Node.children[index])
            cdevice.touch(statusBar_Node.x,statusBar_Node.y,MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(5)

            if index==11 or index==7 or index==6 or index==5 or index==3 or index==1 or index==9:
                print '222222222222222222222 index ' + str(index)
                if index==9:
                   enterBar() 
                statusBar_Node = chierarchyviewer.getAbsoluteCenterOfView(List_Node.children[index])
                cdevice.touch(statusBar_Node.x,statusBar_Node.y,MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(5)
            
            if index==0 or index==9:
                enterBar()
            if index==2 or index==8:
                cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(2)
                enterBar()
            
            if index==11:
                cdevice.drag((200,300),(200,92),0.5,10, MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                goLastIcon()
            index = index + 1
            #hot spot
            if index==4 or index==10 :
                index = index+1
        
        SucTimes = SucTimes + 1
        print "Trace Success Enter Bar"
    except Exception,e:
        print "Can not Enter Bar"
        FailTimes = FailTimes + 1
        shotpath = ImagePath+"\\Interaction_exc_Bar" + ".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice) 

def runWorkSpaceOne():
    print 'test-------------1'
    enterMessage()
    enterGooglePlay()
    enter_Goole_set()
    enterAT_T2()
    
def runWorkSpaceTwo():
    print 'test-----------------2'
    enterPeople()
    enterGallery()
    enterDriveMode()
    enterReminder()
    bottomMenu()
    
def runWorkSpaceThree():
    print 'test------------3'
    #enterGoogleSearchBox(1)
    #for Version0
    '''
    GoogleAndYellowPage()
    enterCodeScanner()
    enterTeleNav()
    enterDigtallocker()
    enterMobiTVPlayer()
    enterMusic()
    '''
    bottomMenu()
    dragPic(0)
    #goLastIcon()
    
#modify end

#add by jianke 07/10/14
#add by jianke 04/23 002
point_arr = [[280,250],[40,340],[120,340],[200,340],[280,340]]
def SelectOneMenu(matrix_lst,loop,x,y):
    if False:
        child_matrix_Node = matrix_lst.children[loop].children[0]
        child_size = child_matrix_Node.children.size()
        print 'child_size ',child_size
        for loop_s in range(child_size):
            print 'loop_s bbbbbbb ',loop_s
            child_pos = chierarchyviewer.getAbsoluteCenterOfView(child_matrix_Node.children[loop_s])
            print 'child_pos ',child_pos
            if loop == 1:
                child_pos.x = child_pos.x - 480
            cdevice.touch(child_pos.x,child_pos.y,MonkeyDevice.DOWN_AND_UP)
            print 'child_pos --- ',child_pos
            MonkeyRunner.sleep(2)
            #test 04/23
            text_show = chierarchyviewer.getFocusedWindowName()
            for lp in range(3):
                cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                if False:
                    cdevice.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(1)
            if False: #for soul4
                cdevice.touch(420,590,MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(2)
            if True:
                cdevice.touch(280,250,MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(2)
    if True:
        child_matrix_Node = matrix_lst.children[loop]
        child_size = child_matrix_Node.children.size()
        print 'child_size ',child_size
        for loop_s in range(child_size):
            print 'loop_s bbbbbbb ',loop_s
            child_pos = chierarchyviewer.getAbsoluteCenterOfView(child_matrix_Node.children[loop_s])
            print 'child_pos ',child_pos
            if loop == 1:
                child_pos.x = child_pos.x - 480
            cdevice.touch(child_pos.x,child_pos.y,MonkeyDevice.DOWN_AND_UP)
            print 'child_pos --- ',child_pos
            MonkeyRunner.sleep(2)
            #test 04/23
            text_show = chierarchyviewer.getFocusedWindowName()
            print 'text_show ',text_show
            for lp in range(3):
                cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                if False:
                    cdevice.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(1)
            if False: #for soul4
                cdevice.touch(420,590,MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(2)
            if True:
                cdevice.touch(x,y,MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(2)

def enterGoogleService(x=point_arr[0][0],y=point_arr[0][1]):
    global SucTimes
    global FailTimes
    global ImagePath

    try:
        cdevice.touch(x,y,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)

        #test 05/14 002
        index = 0
        while False:
            index = index + 1
            get_wind = chierarchyviewer.getFocusedWindowName()
            print 'get_wind ',index , ' -> ',get_wind
        #end
            
        if common.isEnterApp(ceasy_device,id_name.Launcher2_ID):
            if False: #for soul4
                matrix_lst = common.GetNode(cdevice,chierarchyviewer,'id/screen_content')
                if matrix_lst is None:
                    raise TypeError,"Get Node FAIL"
                lst = matrix_lst.children.size()
                print 'matrix_lst ',lst
                for loop in range(lst):
                    SelectOneMenu(matrix_lst,loop)
                    if loop == 0:
                        cdevice.shell('input swipe 350 400 100 400')
                    if loop == 1:
                        cdevice.shell('input swipe 100 400 350 400')
            if True:
                matrix_lst = common.GetNode(cdevice,chierarchyviewer,'id/folder_content')
                if matrix_lst is None:
                    raise TypeError,"Get Node FAIL"
                c_list_size = matrix_lst.children.size()
                print 'c_list_size ',c_list_size
                for loop in range(c_list_size):
                    SelectOneMenu(matrix_lst,loop,x,y)
    
            MonkeyRunner.sleep(1)
            SucTimes = SucTimes + 1
            if x == point_arr[0][0] and y == point_arr[0][1]:
                print "Trace Success Enter GoogleService"
            elif x == point_arr[1][0] and y == point_arr[1][1]:
                print "Trace Success Enter Tools"
            elif x == point_arr[2][0] and y == point_arr[2][1]:
                print "Trace Success Enter Media" 
            elif x == point_arr[3][0] and y == point_arr[3][1]:
                print "Trace Success Enter Productivity" 
            elif x == point_arr[4][0] and y == point_arr[4][1]:
                print "Trace Success Enter Assistance"
            else:
                print "Trace wrong road"
        else:
            FailTimes = FailTimes + 1
            if x == point_arr[0][0] and y == point_arr[0][1]:
                print "Can not Enter GoogleService"
                shotpath = ImagePath+"\\Fail_enter_GoogleService" + ".png"
            elif x == point_arr[1][0] and y == point_arr[1][1]:
                print "Can not Enter Tools"
                shotpath = ImagePath+"\\Fail_enter_Tools" + ".png"
            elif x == point_arr[2][0] and y == point_arr[2][1]:
                print "Can not Enter Media"
                shotpath = ImagePath+"\\Fail_enter_Media" + ".png"
            elif x == point_arr[3][0] and y == point_arr[3][1]:
                print "Can not Enter Productivity"
                shotpath = ImagePath+"\\Fail_enter_Productivity" + ".png"
            elif x == point_arr[4][0] and y == point_arr[4][1]:
                print "Can not Enter Assistance"
                shotpath = ImagePath+"\\Fail_enter_Assistance" + ".png"
            else:
                print "Fail trace wrong road"
            common.SaveFailImg(cdevice,shotpath)
    except Exception,e:
        FailTimes = FailTimes + 1
        if x == point_arr[0][0] and y == point_arr[0][1]:
            print "Exception,Can not Enter GoogleService"
            shotpath = ImagePath+"\\Interaction_exc_GoogleService" + ".png"
        elif x == point_arr[1][0] and y == point_arr[1][1]:
            print "Exception,Can not Enter Tools"
            shotpath = ImagePath+"\\Interaction_exc_Tools" + ".png"
        elif x == point_arr[2][0] and y == point_arr[2][1]:
            print "Exception,Can not Enter Media"
            shotpath = ImagePath+"\\Interaction_exc_Media" + ".png"
        elif x == point_arr[3][0] and y == point_arr[3][1]:
            print "Exception,Can not Enter Productivity"
            shotpath = ImagePath+"\\Interaction_exc_Productivity" + ".png"
        elif x == point_arr[4][0] and y == point_arr[4][1]:
            print "Exception,Can not Enter Assistance"
            shotpath = ImagePath+"\\Interaction_exc_Assistance" + ".png"
        else:
            print "Exception trace wrong road"
        common.SaveFailImg(cdevice,shotpath)
        print 'interaction Exception Error: ',e
        traceback.print_exc()
    common.BackToIdle(cdevice)
#end
#workspace -> hotseat

def GetWorkSpace():
    workspace_node = common.GetNode(cdevice,chierarchyviewer,'id/workspace')
    if workspace_node is None:
        raise TypeError,"Get Node FAIL"
    wsize = workspace_node.children.size()
    print 'workspace_node size ',wsize
    return workspace_node,wsize
    
    
def FirstWorkSpace():
    width_w = int(str(width))
    width_w = width_w/4
    height_w = int(str(height))
    height_w = height_w/2
    width_w = int(width_w)
    print 'width_w 2222 ',width_w
    height_w = int(height_w)
    print 'height_w 2222 ',height_w
    parent_node,amount = GetWorkSpace()
    cell2_node = common.GetNode(cdevice,chierarchyviewer,'id/cell2',parent_node)
    if cell2_node is None:
        raise TypeError,"Get Node FAIL"
    list_cell2_node = cell2_node.children[0]
    number = list_cell2_node.children.size()
    print 'number 07/10 ',number
    for index in range(number):
        print 'go to here ============================ ',list_cell2_node.children[index].name
        if list_cell2_node.children[index].name.find('BubbleTextView') > -1 or list_cell2_node.children[index].name.find('FolderIcon') > -1:
            cell_pos = chierarchyviewer.getAbsoluteCenterOfView(list_cell2_node.children[index])
            print 'cell_pos ============== ',cell_pos
            cdevice.touch(cell_pos.x,cell_pos.y,MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            wind_id = chierarchyviewer.getFocusedWindowName()
            print 'current wind_id ',wind_id
            
            while wind_id == None:
                MonkeyRunner.sleep(1)
                wind_id = chierarchyviewer.getFocusedWindowName()
                print 'current wind_id2 ------> ',wind_id
            if list_cell2_node.children[index].name.find('FolderIcon') > -1: #jrdFolder id/drag_layer
                print 'array app ...'
                #jianke 07/10
                lst_node = common.GetNode(cdevice,chierarchyviewer,'id/drag_layer')
                if lst_node is None:
                    raise TypeError,"Get Node FAIL"
                lst_node_size = lst_node.children.size()
                print 'lst_node size ',lst_node_size
                for index in range(lst_node_size):
                    print 'lst_node.children[index].name ====== ',lst_node.children[index].name
                    if lst_node.children[index].name.find('JrdFolder') > -1: #id/folder_name
                        correct_node = lst_node.children[index]
                        print 'correct_node ',correct_node.children.size()
                        arr_content_node = common.GetNode(cdevice,chierarchyviewer,'id/screen_content',correct_node)
                        if arr_content_node is None:
                            raise TypeError,"Get Node FAIL"
                        #For test 07/10
                        MonkeyRunner.sleep(3)
                        #end
                        arr_content_node_size = arr_content_node.children.size()
                        print 'arr_content_node_size ',arr_content_node_size  #2
                        for arr_c in range(arr_content_node_size):
                            if arr_c == 1:
                                cdevice.shell('input swipe ' + str(width_w*3) + ' ' + str(height_w) + ' ' + str(width_w) + ' ' + str(height_w))
                            exact_node = arr_content_node.children[arr_c].children[0]
                            arr_size = exact_node.children.size()
                            print 'exact_node ======= ',arr_size
                            for loop_c in range(arr_size):
                                print 'go everywhere!!!'
                                #jianke 07/10
                                node_child_get = exact_node.children[loop_c]
                                #touch items
                                node_child_get_point =  chierarchyviewer.getAbsoluteCenterOfView(node_child_get)
                                print 'node_child_get_point 8888888 ',node_child_get_point
                                if node_child_get_point.x > width_w*4:
                                    node_child_get_point.x = node_child_get_point.x - width_w*4
                                print 'node_child_get_point 9999999 ',node_child_get_point
                                cdevice.touch(node_child_get_point.x,node_child_get_point.y,MonkeyDevice.DOWN_AND_UP)
                                MonkeyRunner.sleep(1)
                                #get wind_id
                                child_wind_id = chierarchyviewer.getFocusedWindowName()
                                print 'current child_wind_id ----> ',(loop_c + 1),' ----> ',child_wind_id
                                while child_wind_id == None:
                                    MonkeyRunner.sleep(1)
                                    child_wind_id = chierarchyviewer.getFocusedWindowName()
                                    print 'current child_wind_id2 ',(loop_c + 1),' ----> ',child_wind_id
                                if child_wind_id == id_name.ChromeID:
                                    print 'go into chrome'
                                    cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                                    MonkeyRunner.sleep(0.5)
                                    cdevice.touch(cell_pos.x,cell_pos.y,MonkeyDevice.DOWN_AND_UP)
                                    MonkeyRunner.sleep(1)
                                elif child_wind_id == id_name.Google_Gmail_ID:
                                    print 'go into Gmail'
                                    cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                                    MonkeyRunner.sleep(0.5)
                                    cdevice.touch(cell_pos.x,cell_pos.y,MonkeyDevice.DOWN_AND_UP)
                                    MonkeyRunner.sleep(1)
                                else:
                                    print 'go into else'
                                    cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                                    MonkeyRunner.sleep(0.5)
                                    while chierarchyviewer.getFocusedWindowName() !=  id_name.Launcher2_ID:
                                        cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                                        MonkeyRunner.sleep(0.5)
                            #add by jianke 07/10
                            if arr_c == 1:
                                cdevice.shell('input swipe ' + str(width_w) + ' ' + str(height_w) + ' ' + str(width_w*3) + ' ' + str(height_w))
                            #end
                           
            if wind_id == id_name.Message_ID:
                print 'enter Message!!!'
                cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(0.5)
            elif wind_id == id_name.GSTORE_ID:
                print 'enter Play Store!!!'
                cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(0.5)
                while chierarchyviewer.getFocusedWindowName() !=  id_name.Launcher2_ID:
                    cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(0.5)


#add by jianke 07/30
def wait_time(t):
    text_wind = chierarchyviewer.getFocusedWindowName()
    print 'text_wind ',text_wind
    Sleep_times = 0
    while text_wind == None or str(text_wind).find('com.android.launcher') > -1:
        MonkeyRunner.sleep(2)
        Sleep_times = Sleep_times + 1
        print 'Sleep time ',Sleep_times*2
        if Sleep_times > t:
            break
        text_wind = chierarchyviewer.getFocusedWindowName()
        print 'text_wind ' + str(Sleep_times) + ' -> ' + str(text_wind)
    return text_wind

def kill_service(serv):
    obj = cdevice.shell('ps | grep ' + serv)
    print 'obj ' + str(obj)
    strb = func(obj)
    print 'strb ' + str(strb)
    obj = cdevice.shell('kill ' + strb)
    print 'obj1 ' + str(obj) 
    obj = cdevice.shell('ps | grep ' + serv)
    print 'obj2 ' + str(obj)
#end
#end
    
def main():
    global ImagePath
    global flag
    global SucTimes
    global FailTimes

    time_Start = common.timeCalc()
    print 'Start Menu Navigation Test'
    common.ShowDeviceMemoryInfo(cdevice)
    common.BackToHome(cdevice)
    
    # Create Folders To Save Imgs Of Result
    ImagePath = common.CreateFolder('5.1.9')
    #the first workspace
    runWorkSpaceOne()
    SwithWorkSpace(1,2)
    
    flag = flag + 1
    #the second workspace
    runWorkSpaceTwo()
    
    flag = flag + 1
    #SwithWorkSpace(2,3)
    #the third workspace
    #runWorkSpaceThree()
    
    common.BackToHome(cdevice)
    #modify end
    print "Finished Menu_Navigation Test"
    common.ShowDeviceMemoryInfo(cdevice)

    #for test,
    if (SucTimes + FailTimes) == 0:
        SucTimes = 1
    
    print 'Success Times:',SucTimes
    print 'Trace Total Times ' + str(SucTimes + FailTimes)
    
    Rate = SucTimes/(SucTimes + FailTimes)*100
    if Rate < 99:
        print 'Result Fail Success Rate Is ' + str(Rate) + '%'
    else:
        print 'Result Pass Success Rate Is ' + str(Rate) + '%'
    timeEnd = common.timeCalc()
    totalTime = timeEnd - time_Start
    print '5.1.09_Menu_Navigation time = ' + str(totalTime) + 'mins'
    
if __name__ == "__main__":
    main()
#  Scrpit End







