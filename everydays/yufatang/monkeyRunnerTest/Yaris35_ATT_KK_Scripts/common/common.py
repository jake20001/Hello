#coding=UTF-8
from __future__ import division
import os
import sys
import string
import re
import ConfigParser
from datetime import *
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from com.android.monkeyrunner import MonkeyImage
from com.android.monkeyrunner.easy import EasyMonkeyDevice
from com.android.monkeyrunner.easy import By
from com.android.chimpchat.hierarchyviewer import HierarchyViewer
#from com.android.hierarchyviewerlib.models import ViewNode
#from com.android.hierarchyviewerlib.device import ViewNode
from  xml.dom import minidom

#add by jianke 0222
scriptpathr=sys.path[0][sys.path[0].find(':')+1:]+"\\..\\common"
sys.path.append(scriptpathr)
import common
config = ConfigParser.ConfigParser()
config.read(scriptpathr + "\\config.ini")
testpath = config.get("TestPath", "path")
project_name = config.get("Project", "project_name")
print 'project_name ',project_name
config_pixel = ConfigParser.ConfigParser()
if project_name == 'yaris35_ATT':
    config_pixel.read(scriptpathr + "\\yaris35_att.ini")
    import yaris35_att_id
    id_name = yaris35_att_id
else:
    print 'other project may add'
width = config_pixel.get("Pixel", "width")
height = config_pixel.get("Pixel", "height")
width = width.strip()
height = height.strip()
print 'width ',width
print 'height ',height
#end

xmldoc = minidom.parse(testpath + "\\TAT\\Configs\\MainConfig.xml")
for i in xmldoc.childNodes[0].getElementsByTagName("M-Device"):
    Client=i.childNodes[0].toxml()
print 'Client ' + str(Client)
for i in xmldoc.childNodes[0].getElementsByTagName("S-Device"):
    Server=i.childNodes[0].toxml()

def ConnectClientDevice():
    device=MonkeyRunner.waitForConnection(5,Client)    
    hierarchyviewer=device.getHierarchyViewer()    
    easy_device=EasyMonkeyDevice(device)    
    return device,hierarchyviewer,easy_device

def ConnectServerDevice():
    device=MonkeyRunner.waitForConnection(5,Server)
    hierarchyviewer=device.getHierarchyViewer()
    easy_device=EasyMonkeyDevice(device)
    return device,hierarchyviewer,easy_device

# The Image Need To Be Compared
# The Image Saved In Local
# Rect A Tuple (X, Y, W, H) Specifying The Selection
def CompareImage(newimg = None,expectPath = None,rect = None):
    if newimg == None or expectPath == None:
        return False
    expectImage = MonkeyRunner.loadImageFromFile(expectPath)
    if rect is None:
        if newimg.sameAs(expectImage,0.9):
            return True
    else:
        subexpectimg = expectImage.getSubImage(rect)
        if newimg.sameAs(subexpectimg,0.990):
            return True
    return False

def CreateFolder(module):
    scriptpath = sys.path[0][sys.path[0].find(':')+1:]
    print scriptpath
    resultfolderpath = scriptpath + '\\..\\results\\'
    print resultfolderpath
    modulefoldertpath = resultfolderpath + module + '\\'
    saveimagepath = modulefoldertpath + datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    if not os.path.exists(resultfolderpath):
        print '---------------------------------'
        print resultfolderpath
        os.mkdir(resultfolderpath)
    if not os.path.exists(modulefoldertpath):
        os.mkdir(modulefoldertpath)
    if not os.path.exists(saveimagepath):
        os.mkdir(saveimagepath)
    print 'Create Folder'
    return saveimagepath

def BatteryFull(easy_device):
    if easy_device.visible(By.id("id/button3")):
        easy_device.touch(By.id("id/button3"),MonkeyDevice.DOWN_AND_UP)
        print "Clean up battery full popup"
        MonkeyRunner.sleep(1)

def ShowDeviceMemoryInfo(device):
    print device
    if device is not None:
        meminfo = device.shell("cat /proc/meminfo")
        print "Print Memory Infomation "
        print meminfo.encode("utf-8")
    else:
        print "Device is not connected"

def SaveFailImg(device,savepath):
    try:
        newimg = device.takeSnapshot()
        #jianke test 07/19
        #print 'newimg 8989898989 ',newimg
        #print 'get savepath ',savepath
        #end
        if newimg is None:
            print "Image is none."
            return False
        #add by jianke for TimeOutException
        try:
            newimg.writeToFile(savepath, 'png')
            print '@#$Fail$#@ '+ savepath
        except:
            print 'TimeOutException'
            return False
        return True
    except Exception,e:
        print 'Save image Exception',e



def CheckWinID(easy_device,win_id):
    for looptime in range(len(win_id)):
        if win_id[looptime] == easy_device.getFocusedWindowId():
            return True
    return False
    
def isEnterApp(easy_device,win_id):
    if type(win_id) is str:
        win_id = (win_id,)
    counter = 0
    while not CheckWinID(easy_device,win_id):
        MonkeyRunner.sleep(1)
        counter += 1
        if (counter) > 5:
            cwinID = easy_device.getFocusedWindowId()
            if cwinID is not None:
                print "Current Win ID is",cwinID.encode("utf-8")
            return False
    MonkeyRunner.sleep(1)
    return True
    
# Enter App
def startapp(device,easy_device,app_id,*win_id):
    if len(win_id) == 0:
        win_id = (app_id,)
    device.startActivity(component=app_id)
    if isEnterApp(easy_device,win_id):
        print "Enter APP",app_id
        return True
    print "Start Activity Fail"
    BackToHome(device)
    return False


# Back To Idle For One Device
def BackToHome(device):
    if device is not None: 
        for backtimes in range(3):
            device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(0.2)
        device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)
        
def BackToIdle(device):
    if device is not None: 
        for backtimes in range(5):
            device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(0.2)

#add 07/28
def BackToIdleAgain(device):
    if device is not None: 
        for backtimes in range(5):
            device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(0.5)
#end

def getDataServiceState(device):
    data = device.shell("dumpsys telephony.registry")

    if not data:
        return None    
    index = data.find("mServiceState")

    if index < 0:           
        return None
    index2 = data.find("\n", index)

    assert index2 > 0        
    data = data[index:index2-1].lower()

    if data.find("edge") > 0 or data.find ("gprs") > 0 or data.find("1xrtt") > 0:
        return "2G"
    elif data.find("evdo") > 0 or data.find("hsupa") > 0 or data.find("hsdpa") > 0 or data.find("hspa") > 0:
        return "3G"
    elif data.find("lte") > 0:
        return "LTE"            
    else:      
        return "UNKNOWN"


def getDataConnectedStatus(device):
    status = device.shell("netcfg")
    m = re.search(r'rmnet0:\sip\s(?P<g1>.*)\smask.*\[up', status)
    if not m:
        return False
    return True

def SwitchNetwork(device,easy_device,hierarchyviewer,type = None):
    #add by jianke 07/08
    width_w = int(str(width))
    width_w = width_w/2
    height_w = int(str(height))
    height_w = height_w/4
    width_w = int(width_w)
    print 'width_w 2222 ',width_w
    height_w = int(height_w)
    print 'height_w 2222 ',height_w
    if project_name == 'yaris35_ATT':
        wind_ID = "com.mediatek.engineermode/com.mediatek.engineermode.EngineerMode" 
        if not startapp(device,easy_device,wind_ID):
            return False
        #add by jianke 04/23
        Flag_search = True
        refresh_times = 0
        while Flag_search:
            page_node = GetNode(device,hierarchyviewer,'id/viewpager')
            if page_node is None:
                raise TypeError,"Get Node FAIL"
            list_node = GetNode(device,hierarchyviewer,'id/list',page_node.children[1])
            if list_node is None:
                raise TypeError,"Get Node FAIL"
            #add by jianke 06/23/14
            number = list_node.children.size()
            print 'number ',number
            for lp in range(number):
                node_title = GetNode(device,hierarchyviewer,'id/title',list_node.children[lp].children[1])
                if node_title is None:
                    raise TypeError,"Get Node FAIL"
                node_title_text = hierarchyviewer.getText(node_title)
                print 'node_title_text ',node_title_text
                if str(node_title_text).find('RAT Mode') > -1:
                    Node_touch = hierarchyviewer.getAbsoluteCenterOfView(list_node.children[lp])
                    print 'Node_touch point ',Node_touch
                    MonkeyRunner.sleep(1)
                    device.touch(Node_touch.x,Node_touch.y,MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(1)
                    Flag_search = False
                    break
            #add by jianke 07/26
            refresh_times = refresh_times + 1
            if refresh_times > 4:
                print 'search no word!!!!!touch it!!!',refresh_times
                Node_touch = [160,288]
                MonkeyRunner.sleep(1)
                device.touch(Node_touch[0],Node_touch[1],MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                Flag_search = False
            #end
            device.drag((width_w,height_w*3),(width_w,height_w),0.5,10)
            MonkeyRunner.sleep(0.5)
        #end
        if hierarchyviewer.getFocusedWindowName() == "com.mediatek.engineermode/com.mediatek.engineermode.ratmode.SimSelect":
            easy_device.touchtext(By.id("id/text1"),'SIM1',MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
        #end
        if type != '2G' and type != '3G' and type != 'LTE' and type != 'All':
            return False
        if type == '2G':
            text_type = 'GSM only'
        if type == '3G':
            text_type = 'WCDMA only'
        if type == 'LTE':
            text_type = 'LTE only'
        if type == 'All':
            text_type = 'LTE/GSM/WCDMA'
        netmode_node = hierarchyviewer.findViewById('id/text1')
        if netmode_node is None:
            return False
        netmode_text = hierarchyviewer.getText(netmode_node)
        print 'netmode_text ' + str(netmode_text)
        if netmode_text.find(text_type) < 0:
            netmodepos2 = hierarchyviewer.getAbsoluteCenterOfView(netmode_node)
            MonkeyRunner.sleep(1)
            device.touch(netmodepos2.x,netmodepos2.y,MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            #add by jianke 0303
            touchTimes = 0
            while hierarchyviewer.getFocusedWindowName()=="com.mediatek.engineermode/com.mediatek.engineermode.ratmode.RadioInfo":
                print 'no touch, come here'
                device.touch(netmodepos2.x,netmodepos2.y,MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                touchTimes = touchTimes + 1
                if touchTimes>2:
                    return False
            #end
            #add by jianke 07/27
            show_times = 0
            while True:
                if hierarchyviewer.getFocusedWindowName().find('PopupWindow') > -1:
                    easy_device.touchtext(By.id("id/text1"),text_type,MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(1)
                    print 'get !!!!!!!!!!!!!!!!!'
                    break
                else:
                    MonkeyRunner.sleep(1)
                    show_times = show_times + 1
                    if show_times > 2:
                        print 'show PopupWindow',show_times
                        break
            #end
            print 'sleep 6s'
            MonkeyRunner.sleep(4)   #30              
            observedMode = getDataServiceState(device)
            MonkeyRunner.sleep(5)
        print type,"now."
        #jianke 03/19
        BackToIdle(device)
        #add by jianke 07/28
        if hierarchyviewer.getFocusedWindowName() != 'com.android.launcher/com.android.launcher2.Launcher':
	    print 'get no command!!!'
            BackToIdleAgain(device)
        #end
    return True


def SwitchNetwork_old(device,easy_device,hierarchyviewer,type = None):
    if not startapp(device,easy_device,"com.android.settings/com.android.settings.RadioInfo"):
        return False
    if type != '2G' and type != '3G' and type != 'LTE' and type != 'All':
        return False
    if type == '2G':
        text_type = 'GSM only'
    if type == '3G':
        text_type = 'WCDMA only'
    if type == 'LTE':
        text_type = 'LTE only'
    if type == 'All':
        text_type = 'LTE/GSM/WCDMA'
    netmode_node = hierarchyviewer.findViewById('id/text1')
    if netmode_node is None:
        return False
    netmodepos = hierarchyviewer.getAbsoluteCenterOfView(netmode_node)
    print netmodepos.y  #713
    if netmodepos.y < 0:
        print("Exist Input Method ")
        device.press("KEYCODE_BACK",MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    device.drag((150,400),(150,150),1,10)
    MonkeyRunner.sleep(1)
    device.drag((150,400),(150,200),1,10)
    MonkeyRunner.sleep(1)
    netmode_node = hierarchyviewer.findViewById('id/text1')
    if netmode_node is None:
        return False
    netmodepos2 = hierarchyviewer.getAbsoluteCenterOfView(netmode_node)
    print netmodepos2
    #add by jianke 0131
    while netmodepos2.y>480:
        device.drag((150,400),(150,300),0.5,10)
        MonkeyRunner.sleep(1)
        netmode_node = hierarchyviewer.findViewById('id/text1')
        if netmode_node is None:
            return False
        netmodepos2 = hierarchyviewer.getAbsoluteCenterOfView(netmode_node)
        print netmodepos2
    #end
    netmode_text = hierarchyviewer.getText(netmode_node)
    print 'netmode_text ' + str(netmode_text)
    if netmode_text.find(text_type) < 0:
        MonkeyRunner.sleep(3)
        device.touch(netmodepos2.x,netmodepos2.y,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(3)
        #add by jianke 0303
        touchTimes = 0
        while hierarchyviewer.getFocusedWindowName()=="com.android.settings/com.android.settings.RadioInfo":
            print 'no touch, come here'
            device.touch(netmodepos2.x,netmodepos2.y,MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(3)
            touchTimes = touchTimes + 1
            if touchTimes>2:
                return False
        #end
        if text_type == 'WCDMA only' or text_type == 'GSM only':
            #add by jianke 1210
            if netmodepos2.y>=240:
                device.drag((netmodepos2.x,netmodepos2.y-200),(netmodepos2.x,netmodepos2.y-50),0.1,10) 
            elif netmodepos2.y<240:
                device.drag((netmodepos2.x,netmodepos2.y+50),(netmodepos2.x,netmodepos2.y+190),0.1,10)
            MonkeyRunner.sleep(3)
        else:
            device.drag((150,420),(150,100),0.1,10)
            MonkeyRunner.sleep(3)
        easy_device.touchtext(By.id("id/text1"),text_type,MonkeyDevice.DOWN_AND_UP)
        print 'sleep 3s'
        MonkeyRunner.sleep(3)   #30              
        observedMode = getDataServiceState(device)
        MonkeyRunner.sleep(5)
    #add by jianke 1206
    device.drag((150,150),(150,400),0.1,10)
    MonkeyRunner.sleep(1)
    device.drag((150,100),(150,400),0.1,10)
    MonkeyRunner.sleep(1)
    print type,"now."
    BackToIdle(device)
    return True

def GetNode(device,hierarchyviewer,strID,root_node = None):
    tempnode = None
    Maxtime = 0
    while tempnode is None:
        Maxtime = Maxtime + 1
        if Maxtime == 4:
            RestartViewserver(device)
        if Maxtime > 5:
            return None
        if root_node is None:
            tempnode = hierarchyviewer.findViewById(strID)
            print 'strID = ',strID
            print 'tempnode = ',tempnode
        else:
            tempnode = hierarchyviewer.findViewById(strID,root_node)
            print 'strID = ',strID
            print 'tempnode = ',tempnode
    return tempnode
    

def RestartViewserver(device):
    print("Debug Restart View server")
    device.shell("service call window 2")
    MonkeyRunner.sleep(2.5)
    result = device.shell("service call window 3")
    if result.find("00000000 00000000") > -1:
        device.shell("service call window 1 i32 4939")
        MonkeyRunner.sleep(2.5)
        result = device.shell("service call window 3")
        if result.find("00000000 00000001") > -1:
            return True
        else:
            print("Start Viewserver fail.")
            return False
    else:
        print("Exit Viewserver fail.")
        return False

#add by jianke 03/27

def GetNode_new(device,hierarchyviewer,strID,root_node = None):
    tempnode = None
    Maxtime = 0
    print 'go tooooooooooooooooo'
    while tempnode is None:
        Maxtime = Maxtime + 1
        if Maxtime > 5:
            return None
        if root_node is None:
            tempnode = hierarchyviewer.findViewById(strID)
            print 'strID = ',strID
            print 'tempnode = ',tempnode
        else:
            tempnode = hierarchyviewer.findViewById(strID,root_node)
            print 'strID = ',strID
            print 'tempnode = ',tempnode
    return tempnode

#Fuction : calculate time
#Return : current time
#
def timeCalc():
    times =datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    hourstart=int(datetime.now().strftime('%H'))
    minutestart=int(datetime.now().strftime('%M'))
    secondstart=int(datetime.now().strftime('%S'))
    crrenttime=hourstart*60+minutestart+secondstart/60
    return crrenttime

#Funtion : get the window_id and get the key_id with juding the key string
#parameters:
# wind_Id : windows id
# key_id : for example 'id/action_bar_title'
# key_word : for example 'General settings'
# delay_time : for example 1
# del_times : for exmaple 3
#Return :Whether enter the correct screen
#
def GetWind_Keyword(hierarchyviewer,easy_device,device,wind_Id,key_id,key_word,delay_time,del_times):
    wind_times = 0
    wind_Flag = True
    txt_wind_get = hierarchyviewer.getFocusedWindowName()
    while wind_Id != txt_wind_get:
        #add by jianke 04/01 002
        BatteryFull(easy_device)
        #end
        MonkeyRunner.sleep(delay_time)
        txt_wind_get = hierarchyviewer.getFocusedWindowName()
        wind_times = wind_times + 1
        print 'wind_times ',wind_times
        if wind_times > del_times:
            wind_Flag = False
            return wind_Flag
    if wind_Id == txt_wind_get:
        #add by jianke 04/13
        key_node = GetNode(device,hierarchyviewer,key_id)
        if key_node is None:
            raise TypeError,"Get Node FAIL"
        #end
        if easy_device.getText(By.id(key_id)).find(key_word) > -1:
            wind_Flag = True
        else:
            wind_Flag = False
        return wind_Flag
    return wind_Flag

#Funtion : get the window_id with juding the key_id
#parameters:
# wind_Id : windows id
# key_id : for example 'id/menu_add_group'
# delay_time : for example 1
# del_times : for exmaple 3
# delay_id_time : for example 0.5
# del_id_times : for exmaple 3
#Return :Whether enter the correct screen
#
def GetWind_Id(hierarchyviewer,easy_device,wind_Id,key_id,delay_time,del_times,delay_id_time,del_id_times):
    wind_times = 0
    wind_id_times = 0
    wind_Flag = True
    txt_wind_get = hierarchyviewer.getFocusedWindowName()
    while wind_Id != txt_wind_get:
        #add by jianke 04/01 001
        BatteryFull(easy_device)
        #end
        MonkeyRunner.sleep(delay_time)
        txt_wind_get = hierarchyviewer.getFocusedWindowName()
        wind_times = wind_times + 1
        print 'wind_times ',wind_times
        if wind_times > del_times:
            wind_Flag = False
            return wind_Flag
    if wind_Flag:
        while not easy_device.visible(By.id(key_id)):
            MonkeyRunner.sleep(delay_id_time)
            wind_id_times = wind_id_times + 1
            print 'wind_id_times ',wind_id_times
            if wind_id_times > del_id_times:
                wind_Flag = False
                return wind_Flag
    return wind_Flag


#Funtion : get the window_pop with juding the key_str
#parameters:
# key_pop_str : pop key string for example 'PopupWindow'
# key_id : for example 'id/top_button_date'
# delay_time : for example 1
# del_times : for exmaple 3
# bool_Flag : True for 'KEYCODE_MENU' and False for others as 'id/top_button_date'
#Return :Whether enter the correct screen
#
def GetWind_Pop_KeyWord(hierarchyviewer,device,easy_device,key_pop_str,key_id,delay_time,del_times,bool_Flag):
    wind_pop_Flag = True
    wind_pop_times = 0
    txt_wind_get = hierarchyviewer.getFocusedWindowName()
    while str(txt_wind_get).find(key_pop_str) == -1:
        #add by jianke 04/01 003
        BatteryFull(easy_device)
        #end
        if bool_Flag:
            device.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
        else:
            easy_device.touch(By.id(key_id),MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(delay_time)
        txt_wind_get = hierarchyviewer.getFocusedWindowName()
        wind_pop_times = wind_pop_times + 1
        print 'wind_pop_times ',wind_pop_times
        if wind_pop_times > del_times:
            wind_pop_Flag = False
            return wind_pop_Flag
    return wind_pop_Flag

#Funtion : get the key_list with juding the key_txt
#parameters:
# key_lst_id : key id for example 'id/list'
# key_txt_found : text which is wanted to find
#Return :Whether found the key text
#
def GetWind_KeyList(hierarchyviewer,device,key_lst_id,key_txt_found):
    Key_txt_Key = False
    lst_node = GetNode(device,hierarchyviewer,key_lst_id)
    if lst_node is None:
        raise TypeError,"Get Node FAIL"
    num_lst = lst_node.children.size()
    print 'num_lst ',num_lst
    for index in range(num_lst):
        text_child = hierarchyviewer.getText(lst_node.children[index])
        if str(text_child).find(key_txt_found) > -1:
            Key_txt_Key = True
            return Key_txt_Key
    return Key_txt_Key

#Funtion : get the keyBorad with juding the keyBoard height
#parameters:
# key_id : key id for example 'id/content'
# key_height : key height for 480x800 is 
#Return : void
#
def Get_keyBoard_wind(device,hierarchyviewer,key_id,key_height):
    Flag_keyBoard = True
    while Flag_keyBoard:
        print 'go to keyBoard2'
        lay_node = GetNode(device,hierarchyviewer,key_id)
        if lay_node is None:
            raise TypeError,"Get Node FAIL"
        lay_height = lay_node.height
        print 'lay_height2 ',lay_height
        if lay_height < 10 or lay_height > key_height:
            MonkeyRunner.sleep(1)
            continue
        else:
            break

#Funtion : get the keyType with juding the keyBoard_self
#parameters:
# key_id : key id for example 'id/button1'
# delay_times : delay time for example 2
#Return : whether get the visible id
#
def Get_keyType(easy_device,hierarchyviewer,key_id,delay_times):
    Flag_keyType = True
    wait_times = 0
    while not easy_device.visible(By.id(key_id)):
        #add by jianke 04/01 004
        BatteryFull(easy_device)
        #end
        MonkeyRunner.sleep(1)
        wait_times = wait_times + 1
        print 'Get_keyType ',wait_times
        if wait_times > delay_times:
            Flag_keyType = False
            return Flag_keyType
    return Flag_keyType

#Funtion : get the browser unusual pop
#parameters:
# key_id :  key id for example 'id/button1'
# key_str1 : key str for example 'No'
# key_str2 : key str for example 'OK'
#Return : void
#
def GetWind_Unusual_Pop(hierarchyviewer,device,easy_device,key_id,key_str1,key_str2):
    sa = [key_str1,key_str2]
    print 'sa ',sa
    if easy_device.visible(By.id(key_id)):
        easy_device.touch(By.id(key_id),MonkeyDevice.DOWN_AND_UP)                                           
        MonkeyRunner.sleep(0.5)
        '''
        for loop in range(len(sa)):
            key_node = GetNode(device,hierarchyviewer,key_id)
            if key_node is None:
                raise TypeError,"Get Node FAIL"
            print 'button1 .............'
            if easy_device.getText(By.id(key_id)).find(sa[loop]) > -1:
                print sa[loop],'............'
                easy_device.touchtext(By.id(key_id),sa[loop],MonkeyDevice.DOWN_AND_UP)                                           
                MonkeyRunner.sleep(0.5)
        '''
#end
