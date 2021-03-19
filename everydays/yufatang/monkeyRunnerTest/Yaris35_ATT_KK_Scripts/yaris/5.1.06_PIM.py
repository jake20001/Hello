#coding=UTF-8
#*****************************************************************************
# Title:        5.1.06_PIM
# Precondition: 
# Description:  Used for Yaris-3.5-att
# Platform:     4.2.2
# version:      SWC1P
# Resolution:   480x800
# modify : change stemp time for drag from 0.5 to 0.2
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
strname = 'AutoTest'
numseed = "0123456789"
if testtype == "mini":
    Add_Calendar = 5 #5
    Del_Calendar = 5 #5
else:
    Add_Calendar = 5 #5
    Del_Calendar = 5 #5
    
Add_Alarm = 1
Del_Alarm = 1

'''
#add by jianke
Add_ToDo = 1
Del_ToDo = 1
#add end
'''

TestTimes = Add_Calendar + Del_Calendar + Add_Alarm + Del_Alarm  #+ Add_ToDo + Del_ToDo
print 'Trace Total Times ' + str(TestTimes)
SucTimes = 0

def EnterCalendar():
    print "Enter Calendar"
    if common.isEnterApp(ceasy_device,id_name.Calendar_ID) or common.startapp(cdevice,ceasy_device,id_name.Calendar_ID):
        return True
    return False

#add by jianke
def EnterTodo():
    print "Enter Todo"
    if common.isEnterApp(ceasy_device,id_name.ToDo_ID) or common.startapp(cdevice,ceasy_device,id_name.ToDo_ID):
        return True
    return False
#end

def BackToCalendar():
    for i in range(5):
        if common.isEnterApp(ceasy_device,id_name.Calendar_ID):
            return True
        cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    return False

def SwitchView_old(strsort):
    if not ceasy_device.visible(By.id('id/agenda_events_list')):
        maxtime = 0
        while not ceasy_device.visible(By.id('id/button_view')):
            maxtime = maxtime + 1
            ceasy_device.touch(By.id('id/top_button_date'),MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            if maxtime > 3:
                break
        if maxtime > 3:
            print "Cannot Switch To Enter Agenda View"
            shotpath = ImagePath + "\\Fail_Switch_View" + ".png"
            common.SaveFailImg(cdevice,shotpath)
            return False
        ceasy_device.touchtext(By.id('id/button_view'),strsort,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    print "Enter Agenda View Now1"
    return True

#add by jianke 06/24/14
def SwitchView(strsort=None):
    if common.GetWind_Id(chierarchyviewer,ceasy_device,id_name.Calendar_ID,'id/top_button_date',1,3,1,3):
        try:
            top_button_date_node = common.GetNode(cdevice,chierarchyviewer,'id/top_button_date')
            if top_button_date_node is None:
                raise TypeError,"Get Node FAIL"
            agenda_buttom_bar_point = chierarchyviewer.getAbsoluteCenterOfView(top_button_date_node)
            cdevice.touch(agenda_buttom_bar_point.x,agenda_buttom_bar_point.y, MonkeyDevice.DOWN_AND_UP)  
            MonkeyRunner.sleep(1)
            #add by jianke 07/09
            if chierarchyviewer.getFocusedWindowName().find('PopupWindow') > -1:
                ceasy_device.touchtext(By.id('id/button_view'),strsort,MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
            #end
        except:
            print "Cannot Switch To Enter Agenda View"
            shotpath = ImagePath + "\\Fail_Switch_View" + ".png"
            common.SaveFailImg(cdevice,shotpath)
            return False
    print "Enter Agenda View Now"
    return True
#end

def SelectMenuItem(stritem=None):
    #add by jianke 07/09
    if stritem == None and project_name == 'yaris35_ATT': 
        action_bar = common.GetNode(cdevice,chierarchyviewer,'id/action_create_event')
        if action_bar is None:
            raise TypeError,"Get Node FAIL"
        #add by jianke 05/13
        action_bar_point = chierarchyviewer.getAbsoluteCenterOfView(action_bar)
        cdevice.touch(action_bar_point.x,action_bar_point.y, MonkeyDevice.DOWN_AND_UP)  
        MonkeyRunner.sleep(1)
    else:
        print 'other projects come here!!!'
        action_bar = common.GetNode(cdevice,chierarchyviewer,'id/action_bar')
        if action_bar is None:
            raise TypeError,"Get Node FAIL"
        cdevice.press('KEYCODE_MENU',MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        ceasy_device.touchtext(By.id('id/title'),stritem,MonkeyDevice.DOWN_AND_UP)    
        MonkeyRunner.sleep(1)
    
def TypeEventName():
    #add by jianke 04/06
    common.Get_keyBoard_wind(cdevice,chierarchyviewer,'id/content',int(height))
    #end
    print 'Type Name'
    sa = []
    for i in range(5):
        sa.append(random.choice(numseed))
    stamp = ''.join(sa)
    strname = 'AutoTest_'+stamp
    MonkeyRunner.sleep(1)
    ceasy_device.type(By.id('id/title'),strname)
    MonkeyRunner.sleep(3)
    return strname

def ChangeDay_old(seed):
    seed = 0
    print seed
    print 'Change Day'
    ceasy_device.touch(By.id('id/start_date'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    day = str(seed + 1)
    ceasy_device.touch(By.id("id/day"),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    for loop in range(2):
        cdevice.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(0.5)
    cdevice.type(day)
    MonkeyRunner.sleep(1)
    cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    #add by jianke 04/04
    if common.Get_keyType(ceasy_device,chierarchyviewer,'id/button1',2):
        ceasy_device.touch(By.id('id/button1'),MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    #end
    ceasy_device.touch(By.id('id/start_time'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    ceasy_device.touch(By.id("id/numberpicker_input"),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    for loop in range(2):
        cdevice.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(0.5)
    cdevice.type('1')
    MonkeyRunner.sleep(1)
    cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    #add by jianke 03/29 002
    Flag_keyType = common.Get_keyType(ceasy_device,chierarchyviewer,'id/button1',2)
    if Flag_keyType:
        print 'go tooooooooooooooooooooo'
    #end
        ceasy_device.touch(By.id('id/button1'),MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)

#add by jianke 08/13
def ChangeDay(loop):
    if ceasy_device.visible(By.id('id/start_date')):
        ceasy_device.touch(By.id('id/start_date'),MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        if common.GetWind_Id(chierarchyviewer,ceasy_device,id_name.Calendar_EditEvent_ID,'id/animator',1,2,1,3):
            animator_node = common.GetNode(cdevice,chierarchyviewer,'id/animator')
            if animator_node is None:
                raise TypeError,"Get Node FAIL"
            animator_node_pos =  chierarchyviewer.getAbsolutePositionOfView(animator_node)
            #rect = (animator_node_pos.x,animator_node_pos.y,animator_node.width,animator_node.height)
            x_begin = animator_node_pos.x + animator_node.width*(loop+2)/7
            y_begin = animator_node_pos.y + animator_node.height*6/8
            print 'x_begin ',x_begin
            print 'y_begin ',y_begin
            x_begin = int(x_begin)
            y_begin = int(y_begin)
            if x_begin < (animator_node_pos.x + animator_node.width):
                cdevice.touch(x_begin,y_begin, MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                ceasy_device.touch(By.id('id/done'),MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)

#add by jianke 03/17
def isAdded(strname):
    print 'strname -> ',strname
    #add by jianke 07/09
    print 'width --> ',(int(str(width)))
    width_w = int(str(width))
    width_w = width_w/2
    print 'width_w ',width_w
    width_w = int(width_w)
    print 'width_w 2222 ',width_w
    height_w = int(str(height))
    height_w = height_w/4
    print 'height_w ',height_w
    height_w = int(height_w)
    print 'height_w 2222 ',height_w
    maxtime = 0
    while True:
        maxtime = maxtime + 1
        lst = common.GetNode(cdevice,chierarchyviewer,'id/agenda_events_list')
        if lst is None:
            raise TypeError,"Get Node FAIL"
        num = lst.children.size()
        print 'num -> ',num
        for index in range(num):
            chNode = lst.children[index]
            print 'chNode -> ',chNode.id
            if str(chNode.id).find('id/content') > -1:
                nodec = chierarchyviewer.findViewById('id/content',chNode)
                nodecc = chierarchyviewer.findViewById('id/agenda_item_text_container',nodec)
                name_get = chierarchyviewer.getText(nodecc.children[0])
                print 'name_get -> ',name_get
                if name_get == strname:                
                    return True
        #add by jianke 04/05 for some person don not pre congfig with document.
        if maxtime < 3:
            print 'maxtime ',maxtime
            cdevice.drag((width_w,height_w*2),(width_w,height_w),0.5,10)
            MonkeyRunner.sleep(1)
        if maxtime >= 3 and maxtime <= 5:
            print 'maxtime2 ',maxtime
            cdevice.drag((width_w,height_w),(width_w,height_w*2),0.5,10)
            MonkeyRunner.sleep(1)
        if maxtime > 5:
            break
        #end
    return False
#end

#add by jianke
def isAddedTodo(strname):
    maxtime = 0
    while True:
        maxtime = maxtime + 1
        list = common.GetNode(cdevice,chierarchyviewer,'id/list_todos')
        if list is None:
            raise TypeError,"Get Node FAIL"
        for index in range(list.children.size()):
            name_node = chierarchyviewer.findViewByIdText('id/item_text',strname)
            if name_node != None:
                #open todo
                point = chierarchyviewer.getAbsoluteCenterOfView(name_node)
                cdevice.touch(point.x,point.y, MonkeyDevice.DOWN_AND_UP)
                return True
        cdevice.drag((150,150),(150,300),0.2,10)
        MonkeyRunner.sleep(1)
        if maxtime > 3:
            break
    return False
#end

def AddCalendar(times):
    global SucTimes
    
    if EnterCalendar():
        #add by jianke 08/01
        if not ceasy_device.visible(By.id('id/agenda_sticky_header_list')):
            print 'change to agenda in AddCalendar!!'
            SwitchView("Agenda")
        #end
        for loop in range (times):
            try:
                SelectMenuItem()   
                event_name = TypeEventName()
                # Change Day 08/13
                cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                ChangeDay(loop)
                # Save Calendar
                #add by jianke 07/09
                if common.GetWind_Id(chierarchyviewer,ceasy_device,id_name.Calendar_EditEvent_ID,'id/action_done',1,3,1,3):
                    ceasy_device.touch(By.id('id/action_done'),MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(1)
                print 'Save The Calendar'
                # Check Add
                if isAdded(event_name):
                    SucTimes = SucTimes + 1
                    print "Trace Success Loop " + str(loop+1)
                else:
                    shotpath = ImagePath + "\\Fail_AddCalendar_" + str(loop+1) + ".png"
                    common.SaveFailImg(cdevice,shotpath)
                MonkeyRunner.sleep(1)
            except Exception,e:
                shotpath = ImagePath + "\\AddCalendar_exc" + str(loop+1) + ".png"
                common.SaveFailImg(cdevice,shotpath)
                print 'AddCalendar Exception Error: ',e
                traceback.print_exc()
                BackToCalendar()
    print 'Add Calendar Test complete'

#add by jianke
def AddToDo(times):
    global SucTimes
    if EnterTodo():
        for loop in range (times):
            try:
                ceasy_device.touch(By.id('id/footer_info'),MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                ceasy_device.type(By.id('id/title'),strname)
                MonkeyRunner.sleep(1)
                # add Details
                ceasy_device.touch(By.id('id/details'),MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                ceasy_device.type(By.id('id/details'),strname)
                MonkeyRunner.sleep(1)
                # done
                ceasy_device.touch(By.id('id/btn_done'),MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                print 'Save The Todo'
                # Back To idle to check the exist todo
                common.BackToHome(cdevice)
                # Check Add
                EnterTodo()
                if not isAddedTodo(strname):
                    shotpath = ImagePath+"\\Fail_AddCalendar_"+str(loop+1)+".png"
                    common.SaveFailImg(cdevice,shotpath)
                else:
                    SucTimes = SucTimes + 1
                    print "Trace Success Loop "+ str(loop+1)
                MonkeyRunner.sleep(1)
            except Exception,e:
                shotpath = ImagePath+"\\Todo_exc"+str(loop+1)+".png"
                common.SaveFailImg(cdevice,shotpath)
                print 'AddTodo Exception Error: ',e
                traceback.print_exc()
                common.BackToHome(cdevice)
    print 'Add Todo Test complete'
#end
    
#--------------------------------------------------------
def EnterAlarm():
    print "Launch Alarm And Wait"
    # Launch Alarm And Wait
    if common.isEnterApp(ceasy_device,id_name.Alarm_ID) or common.startapp(cdevice,ceasy_device,id_name.Alarm_ID):
        ceasy_device.touchtext(By.id('id/tab_label'),'Alarm',MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        return True
    return False

def BackToAlarm():
    for i in range(5):
        if common.startapp(cdevice,ceasy_device,id_name.Alarm_ID):
            return True
        cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    return False

def GetAlarmNumber():
    list_node = common.GetNode(cdevice,chierarchyviewer,'id/alarms_list')
    if list_node is None:
        raise TypeError,"Get Node FAIL"
    print list_node.children.size()
    return list_node.children.size()

#add by jianke 0315
def GetListNumber(idnumber):
    list_node = common.GetNode(cdevice,chierarchyviewer,idnumber)
    if list_node is None:
        raise TypeError,"Get Node FAIL"
    print list_node.children.size()
    return list_node.children.size()

#end

def AddAlarmWithoutChange():
    # Add Alarm
    ceasy_device.touch(By.id('id/menu_item_add_alarm'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    # Type Alarm Time 1:00
    # Input 1
    list_node_1 = common.GetNode(cdevice,chierarchyviewer,'id/first')
    if list_node_1 is None:
            raise TypeError,"Get Node FAIL"
    point = chierarchyviewer.getAbsoluteCenterOfView(list_node_1.children[0])
    cdevice.touch(point.x,point.y, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    # Input :00
    list_node_2 = common.GetNode(cdevice,chierarchyviewer,'id/fourth')
    if list_node_2 is None:
            raise TypeError,"Get Node FAIL"
    point = chierarchyviewer.getAbsoluteCenterOfView(list_node_2.children[0])
    cdevice.touch(point.x,point.y, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    # Save Alarm
    ceasy_device.touch(By.id('id/set_button'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    print "Add An Alarm"

#add by jianke
def AddAlarmWithoutChange2():
    # Add Alarm
    ceasy_device.touch(By.id('id/add_alarm'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    # Type Alarm Time 1:00
    # Input 1
    list_node_1 = common.GetNode(cdevice,chierarchyviewer,'id/timerpicker_hour')
    if list_node_1 is None:
            raise TypeError,"Get Node FAIL"
    point = chierarchyviewer.getAbsoluteCenterOfView(list_node_1)
    #cdevice.touch(point.x,point.y, MonkeyDevice.DOWN_AND_UP)
    cdevice.drag((point.x,point.y),(point.x,point.y+150),0.2,10,MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    # Input :00
    list_node_2 = common.GetNode(cdevice,chierarchyviewer,'id/timerpicker_minute')
    if list_node_2 is None:
            raise TypeError,"Get Node FAIL"
    point = chierarchyviewer.getAbsoluteCenterOfView(list_node_2)
    #cdevice.touch(point.x,point.y, MonkeyDevice.DOWN_AND_UP)
    cdevice.drag((point.x,point.y),(point.x,point.y+150),0.2,10,MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    # Save Alarm
    ceasy_device.touch(By.id('id/alarm_save'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    print "Add An Alarm"
#end

def DeactivateAlarm():
    alarm_num = GetListNumber('id/alarms_list') - 1
    print alarm_num
    for index in range(alarm_num):
        list_node = common.GetNode(cdevice,chierarchyviewer,'id/alarms_list')
        if list_node is None:
            raise TypeError,"Get Node FAIL"
        alarm_node = list_node.children[index]
        slipbtn_node = common.GetNode(cdevice,chierarchyviewer,'id/onoff',alarm_node)
        if slipbtn_node is None:
            raise TypeError,"Get Node FAIL"
        if slipbtn_node.namedProperties.get("isChecked").value == "false":
            slipbtn_pos = chierarchyviewer.getAbsoluteCenterOfView(slipbtn_node)
            cdevice.touch(slipbtn_pos.x,slipbtn_pos.y,MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            
#add by jianke
def DeactivateAlarm2():
    alarm_num = GetListNumber('id/alarms_list') - 1
    print alarm_num
    for index in range(alarm_num):
        list_node = common.GetNode(cdevice,chierarchyviewer,'id/alarms_list')
        if list_node is None:
            raise TypeError,"Get Node FAIL"
        alarm_node = list_node.children[index]
        slipbtn_node = common.GetNode(cdevice,chierarchyviewer,'id/slipbtn',alarm_node)
        if slipbtn_node is None:
            raise TypeError,"Get Node FAIL"
        if slipbtn_node.namedProperties.get("isChecked").value == "false":
            slipbtn_pos = chierarchyviewer.getAbsoluteCenterOfView(slipbtn_node)
            cdevice.touch(slipbtn_pos.x,slipbtn_pos.y,MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
#end
            
def AddAlarm(times):
    global SucTimes
    
    if EnterAlarm():
        for loop in range (times):
            try:
                Preconfigenumber = GetListNumber('id/alarms_list')
                print 'Preconfigenumber',Preconfigenumber
                # Only leave less than two alarm
                while Preconfigenumber > 2:
                    Preconfigenumber = GetListNumber('id/alarms_list')
                    Preconfigenumber = Preconfigenumber - 1 
                    LTOneAlarm(0)
                    DelOneAlarm()                   
                    MonkeyRunner.sleep(1)
                    if Preconfigenumber <= 2:
                        break                
                Beforenumber = GetListNumber('id/alarms_list')
                AddAlarmWithoutChange()
                DeactivateAlarm()
                # Check Add
                Afternumber = GetListNumber('id/alarms_list')
                print 'Beforenumber',Beforenumber
                print 'Afternumber',Afternumber
                if Afternumber <= Beforenumber:
                    shotpath = ImagePath+"\\Fail_AddAlarm_"+str(loop+1)+".png"
                    common.SaveFailImg(cdevice,shotpath)
                else:
                    SucTimes = SucTimes + 1
                    print "Trace Success Loop "+ str(loop+1)
            except Exception,e:
                shotpath = ImagePath+"\\DelAlarm_exc"+str(loop+1)+".png"
                common.SaveFailImg(cdevice,shotpath)
                print 'DelAlarm Exception Error: ',e
                traceback.print_exc()
                BackToAlarm()
    print 'Add Alarm Test complete'

#add by jianke
def AddAlarm2(times,idnumber):
    global SucTimes
    
    if EnterAlarm():
        for loop in range(times):
            try:
                Preconfigenumber = GetListNumber(idnumber)
                print 'Preconfigenumber',Preconfigenumber
                # Only leave less than two alarm
                while Preconfigenumber > 2:
                    Preconfigenumber = GetListNumber(idnumber)
                    Preconfigenumber = Preconfigenumber - 1 
                    LTOneAlarm(0)
                    DelOneAlarm2()                   
                    MonkeyRunner.sleep(1)
                    if Preconfigenumber <= 2:
                        break                
                Beforenumber = GetListNumber(idnumber)
                AddAlarmWithoutChange2()
                DeactivateAlarm2()
                # Check Add
                Afternumber = GetListNumber(idnumber)
                print 'Beforenumber',Beforenumber
                print 'Afternumber',Afternumber
                if Afternumber <= Beforenumber:
                    shotpath = ImagePath + "\\Fail_AddAlarm_" + str(loop+1) + ".png"
                    common.SaveFailImg(cdevice,shotpath)
                else:
                    SucTimes = SucTimes + 1
                    print "Trace Success Loop " + str(loop+1)
            except Exception,e:
                shotpath = ImagePath + "\\DelAlarm_exc" + str(loop+1) + ".png"
                common.SaveFailImg(cdevice,shotpath)
                print 'DelAlarm Exception Error: ',e
                traceback.print_exc()
                BackToAlarm()
    print 'Add Alarm Test complete'
#end
#---------------------------------------------------------------

def SelectOneCalendar(index):
    # Select A Calendar
    print "Select A Calendar"
    #add by jianke 07/09
    print 'width --> ',(int(str(width)))
    width_w = int(str(width))
    width_w = width_w/2
    print 'width_w ',width_w
    width_w = int(width_w)
    print 'width_w 2222 ',width_w
    height_w = int(str(height))
    height_w = height_w/4
    print 'height_w ',height_w
    height_w = int(height_w)
    print 'height_w 2222 ',height_w
    if common.GetWind_Id(chierarchyviewer,ceasy_device,id_name.Calendar_ID,'id/agenda_events_list',1,2,1,2):
        if project_name == 'yaris35_ATT':
            for i in range(3):
                cdevice.drag((width_w,height_w),(width_w,height_w*2),0.5,10)
                MonkeyRunner.sleep(0.5)
        MonkeyRunner.sleep(2)
        list = common.GetNode(cdevice,chierarchyviewer,'id/agenda_events_list')
        if list is None:
            raise TypeError,"Get Node FAIL"
        first_Event =  chierarchyviewer.getAbsoluteCenterOfView(list.children[index+2])
        cdevice.touch(first_Event.x,first_Event.y,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)
    else:
        print "it does not get list"
    
def GetCalendarName():
    if common.GetWind_Id(chierarchyviewer,ceasy_device,id_name.Calendar_EventInfo_ID,'id/title',1,2,1,2):
        name_node = common.GetNode(cdevice,chierarchyviewer,'id/title')
        print '------------',name_node
        if name_node is None:
            raise TypeError,"Get Node FAIL"
        text = chierarchyviewer.getText(name_node)
    else:
        text = None
    return text

def DelOneCalendar():
    # Delete The Calendar
    #add by jianke 2014/04/01 001
    if common.GetWind_Id(chierarchyviewer,ceasy_device,id_name.Calendar_EventInfo_ID,'id/info_action_delete',1,2,1,2):
        ceasy_device.touch(By.id('id/info_action_delete'),MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        # Confirm Delete
        ceasy_device.touch(By.id('id/button1'),MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    else:
        print "Delete The Calendar failed"
    print "Delete The Calendar"
    
def DelCalendar(times):
    global SucTimes
    
    if EnterCalendar():
        #add by jianke 08/01
        if not ceasy_device.visible(By.id('id/agenda_sticky_header_list')):
            print 'change to agenda in DelCalendar!!'
            SwitchView("Agenda")
        #end
        for loop in range (times):
            try:
                print loop,'------'
                SelectOneCalendar(0)
                event_name = GetCalendarName()
                MonkeyRunner.sleep(1)
                DelOneCalendar()
                if isAdded(event_name):
                    shotpath = ImagePath + "\\Fail_DelCalendar_" + str(loop+1) + ".png"
                    common.SaveFailImg(cdevice,shotpath)
                else:
                    SucTimes = SucTimes + 1
                    print "Trace Success Loop " + str(loop+1)
                BackToCalendar()
            except Exception,e:
                shotpath = ImagePath + "\\DelCalendar_exc" + str(loop+1) + ".png"
                common.SaveFailImg(cdevice,shotpath)
                print 'DelCalendar Exception Error: ',e
                traceback.print_exc()
                BackToCalendar()
    print 'Del Calendar Test complete'

#------------------------------------------------------------------
    
def SelectOneAlarm(index):
    print "Select an Alarm"
    # Select an Alarm
    list = common.GetNode(cdevice,chierarchyviewer,'id/alarms_list')
    if list is None:
        raise TypeError,"Get Node FAIL"
    fir_Alarm = chierarchyviewer.getAbsoluteCenterOfView(list.children[index])
    cdevice.touch(fir_Alarm.x,fir_Alarm.y,MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

def LTOneAlarm(index):
    print "Select an Alarm"
    # Long touch an Alarm
    list = common.GetNode(cdevice,chierarchyviewer,'id/alarms_list')
    if list is None:
        raise TypeError,"Get Node FAIL"
    fir_Alarm = chierarchyviewer.getAbsoluteCenterOfView(list.children[index])
    cdevice.touch(fir_Alarm.x,fir_Alarm.y,MonkeyDevice.DOWN)
    MonkeyRunner.sleep(2)
    cdevice.touch(fir_Alarm.x,fir_Alarm.y,MonkeyDevice.UP)

def DelOneAlarm():
    ceasy_device.touch(By.id('id/menu_item_delete_alarm'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    ceasy_device.touch(By.id('id/button1'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    print "Delete The Alarm"
    
#add by jianke
def DelOneAlarm2():
    ceasy_device.touchtext(By.id('id/title'),'Delete alarm',MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    ceasy_device.touch(By.id('id/button1'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    print "Delete The Alarm"

def DelAlarm2(times,idnumber):
    global SucTimes
    
    if EnterAlarm():
        for loop in range (times):
            try:
                Beforenumber = GetListNumber(idnumber)
                print 'Before numeber:',Beforenumber
                LTOneAlarm(0)
                DelOneAlarm2()
                Afternumber = GetListNumber(idnumber)
                print 'After numeber:',Beforenumber
                if Beforenumber <= Afternumber:
                    shotpath = ImagePath + "\\Fail_DelAlarm_" + str(loop+1) + ".png"
                    common.SaveFailImg(cdevice,shotpath)
                else:
                    SucTimes = SucTimes + 1
                    print "Trace Success Loop " + str(loop+1)
                MonkeyRunner.sleep(1)
            except Exception,e:
                shotpath = ImagePath + "\\DelAlarm_exc" + str(loop+1) + ".png"
                common.SaveFailImg(cdevice,shotpath)
                print 'DelAlarm Exception Error: ',e
                traceback.print_exc()
                BackToAlarm()
    print 'Delete Alarm Test complete'
#end
    
def DelAlarm(times):
    global SucTimes
    if EnterAlarm():
        for loop in range (times):
            try:
                Beforenumber = GetListNumber('id/alarms_list')
                print 'Before numeber:',Beforenumber
                LTOneAlarm(0)
                DelOneAlarm()
                Afternumber = GetListNumber('id/alarms_list')
                print 'After numeber:',Beforenumber
                if Beforenumber <= Afternumber:
                    shotpath = ImagePath+"\\Fail_DelAlarm_"+str(loop+1)+".png"
                    common.SaveFailImg(cdevice,shotpath)
                else:
                    SucTimes = SucTimes + 1
                    print "Trace Success Loop "+ str(loop+1)
                MonkeyRunner.sleep(1)
            except Exception,e:
                shotpath = ImagePath+"\\DelAlarm_exc"+str(loop+1)+".png"
                common.SaveFailImg(cdevice,shotpath)
                print 'DelAlarm Exception Error: ',e
                traceback.print_exc()
                BackToAlarm()
    print 'Delete Alarm Test complete'

#add by jianke
def DelOneToDo(Del_ToDo):
    global SucTimes
    try:
        ceasy_device.touch(By.id('id/btn_delete'),MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        ceasy_device.touch(By.id('id/button1'),MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        SucTimes = SucTimes + 1
        print "Trace Success Loop "
    except Exception,e:
        shotpath = ImagePath+"\\DelTodo_exc"+".png"
        common.SaveFailImg(cdevice,shotpath)
        print 'DelAlarm Exception Error: ',e
        traceback.print_exc()
    print "Delete The Todo"
#end
    
def main():
    global ImagePath

    time_Start = common.timeCalc()
    print 'Start PIM Test'
    # Create Folders To Save Imgs Of Result
    ImagePath = common.CreateFolder('5.1.6')
    common.ShowDeviceMemoryInfo(cdevice)
    common.BackToHome(cdevice)
    
    print 'Add five Calendars ' + str(Add_Calendar) + ' Times'
    #------1-----------------
    AddCalendar(Add_Calendar)
   
    print 'Del five Calendars ' + str(Del_Calendar) + ' Times'
    #------2-----------------
    DelCalendar(Del_Calendar)
    
    print 'Add an Alarm ' + str(Add_Alarm) + ' Times'
    #------3------------------
    alarm2_id = 'id/alarms_list'
    AddAlarm2(Add_Alarm,alarm2_id)
 
    print 'Del an Alarm ' + str(Del_Alarm) + ' Times'
    #------4-----------------
    DelAlarm2(Del_Alarm,alarm2_id)
    
    '''
    #add by jianke
    #---------5--------------- 
    print 'Add an Task'  
    AddToDo(Add_ToDo)
    #--------6----------------
    print 'Del an Task '
    DelOneToDo(Del_ToDo)
    #end
    '''
    
    # Return to idle
    common.BackToHome(cdevice)
    common.ShowDeviceMemoryInfo(cdevice)
    
    print 'PIM Mission Complete'
    print "Success Times: ",SucTimes
    Rate = SucTimes/TestTimes*100
    if Rate < 99:
        print 'Result Fail Success Rate Is ' + str(Rate) + '%'
    else:
        print 'Result Pass Success Rate Is ' + str(Rate) + '%'
    timeEnd = common.timeCalc()
    totalTime = timeEnd - time_Start
    print '5.1.06_PIM time = ' + str(totalTime) + 'mins'
    
# Script End
if __name__ == "__main__":
    main()
#  Scrpit End
