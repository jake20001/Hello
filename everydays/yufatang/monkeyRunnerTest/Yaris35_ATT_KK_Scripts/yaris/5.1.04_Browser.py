#coding=UTF-8
#-------------------------------------------------------------------------------
#Title:                 5.1.04_Browser
#Precondition:          1.Two devices connected
#                       2.Sim Card Exist
#Description:           Used for Yaris_3.5_ATT
#Platform:              4.2.2
#Resolution:            320x480
#Version:               C68
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
        ATTPage2G = 2
        ATTPage3G = 2
        ATTPageLTE = 2
        Navigate2G = 2
        Navigate3G = 2
        NavigateLTE = 2
        TopSites2G = 2
        TopSites3G = 2
        TopSitesLTE = 2
   else:
        ATTPage2G = 5
        ATTPage3G = 20
        ATTPageLTE = 25
        Navigate2G = 5
        Navigate3G = 20
        NavigateLTE = 25
        TopSites2G = 1
        TopSites3G = 4
        TopSitesLTE = 5
   TestTimes = ATTPage2G+ATTPage3G+ATTPageLTE+Navigate2G+Navigate3G+NavigateLTE+TopSites2G+TopSites3G+TopSitesLTE
if supportedNetworkType == "2G3G":
   if testtype == "mini":
      if Flag_mini:
         ATTPage2G = 1 #10
         ATTPage3G = 1 #40
         Navigate2G = 1 #10
         Navigate3G = 1 #40
         TopSites2G = 1 #2
         TopSites3G = 1 #8
      else:
         ATTPage2G = 1 #10
         ATTPage3G = 4 #40
         Navigate2G = 1 #10
         Navigate3G = 4 #40
         TopSites2G = 1 #2
         TopSites3G = 4 #8
   else:
      ATTPage2G = 0 #10
      ATTPage3G = 50 #40
      Navigate2G = 0 #10
      Navigate3G = 50 #40
      TopSites2G = 0 #2
      TopSites3G = 10 #8
   TestTimes = ATTPage2G + ATTPage3G + Navigate2G + Navigate3G + (TopSites2G + TopSites3G)*5

MaxTime = 100
print 'Trace Total Times ' + str(TestTimes)
SucTimes = 0

# Create Folders To Save Imgs Of Result
ImagePath = common.CreateFolder('5.1.4')

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

#add by jianke 07/30
def getRightView():
    action_bar_container_node = common.GetNode(cdevice,chierarchyviewer,'id/action_bar_container')
    if action_bar_container_node is None:
        raise TypeError,"Get Node FAIL"
    action_bar_container_node_num = action_bar_container_node.children.size()
    print 'action_bar_container_node ',action_bar_container_node_num
    for index in range(action_bar_container_node_num):
        if action_bar_container_node.children[index].name == 'ScrollingTabContainerView':
            bookmark_node = action_bar_container_node.children[index].children[0].children[0]
            bookmark_node_pos = chierarchyviewer.getAbsoluteCenterOfView(bookmark_node)
            cdevice.touch(bookmark_node_pos.x,bookmark_node_pos.y,MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(2)
            break
    #drag
    cdevice.drag((160,240),(160,400),0.5,10, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    grid_node = common.GetNode(cdevice,chierarchyviewer,'id/grid')
    if grid_node is None:
        raise TypeError,"Get Node FAIL"
    grid_size = grid_node.children.size()
    print 'grid_node ',grid_size
    if grid_size == 2 or grid_size == 5:
        print 'open the first view!!'
        bookmark_node2_pos = chierarchyviewer.getAbsoluteCenterOfView(grid_node.children[0])
        cdevice.touch(bookmark_node2_pos.x,bookmark_node2_pos.y,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    else:
        print 'it is ok view !!'
    MonkeyRunner.sleep(1)
#end

def EnterBrowser():
    global NetWork_type
    
    common.BackToHome(cdevice)
    print "Lauch Browser And Wait"
    '''
    obj = cdevice.shell('ps | grep com.android.browser')
    #print 'obj ' + str(obj)
    strb = func(obj)
    #print 'strb ' + str(strb)
    obj = cdevice.shell('kill ' + strb)
    #print 'obj1 ' + str(obj) 
    obj = cdevice.shell('ps | grep com.android.browser')
    #print 'obj2 ' + str(obj)
    '''
    if common.isEnterApp(ceasy_device,id_name.BROWSER_APPID) or common.startapp(cdevice,ceasy_device,id_name.BROWSER_APPID):
       try:
          common.GetWind_Unusual_Pop(chierarchyviewer,cdevice,ceasy_device,'id/button1','No','OK')
          times = 0
          txt_get = chierarchyviewer.getFocusedWindowName()
          print 'txt_get 111111 ',txt_get
          while txt_get != id_name.BROWSER_APPID:
             MonkeyRunner.sleep(2)
             txt_get = chierarchyviewer.getFocusedWindowName()
             print 'txt_get 22222 ',txt_get
             times = times + 1
             print 'times --- ',times 
             if times > 3:
                return False
          return True
       except Exception,e:
         shotpath = ImagePath + "\\Enter_Browser_exc_" + NetWork_type + ".png"
         common.SaveFailImg(cdevice,shotpath)
         print "Enter Browser Exception Error:",e
         traceback.print_exc()
         return False
       #end
                            
def SelectMenuItem(strtitle):
    print 'Refresh Page'
    common.GetWind_Unusual_Pop(chierarchyviewer,cdevice,ceasy_device,'id/button1','No','OK')
    cdevice.press('KEYCODE_MENU',MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    common.GetWind_Unusual_Pop(chierarchyviewer,cdevice,ceasy_device,'id/button1','No','OK')
    text = chierarchyviewer.getFocusedWindowName()
    print 'text ',text
    br_times = 0
    #07/09
    while text != id_name.BROWSER_DLG_APPID:
        br_times = br_times + 1
        cdevice.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)
        text = chierarchyviewer.getFocusedWindowName()
        print 'text22 ',text
        common.GetWind_Unusual_Pop(chierarchyviewer,cdevice,ceasy_device,'id/button1','No','OK')
        if br_times > 2:
            return False
    common.GetWind_Unusual_Pop(chierarchyviewer,cdevice,ceasy_device,'id/button1','No','OK')
    cdevice.drag((174,381),(164,92),0.5,10, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    common.GetWind_Unusual_Pop(chierarchyviewer,cdevice,ceasy_device,'id/button1','No','OK')
    ceasy_device.touchtext(By.id("id/title"),strtitle,MonkeyDevice.DOWN_AND_UP)                                           
    MonkeyRunner.sleep(3)
    print "Enter",strtitle
    return True

# index: 1 is www.yahoo.com
#        2 is www.att.com
#        3 is www.facebook.com
#        4 is www.youtube.com
#        5 is www.nytimescom

def SelectOneBookmark(index):
    line = int((index)/3) + 1
    number = (index) % 3
    list = common.GetNode(cdevice,chierarchyviewer,'id/grid')
    if list is None:
        raise TypeError,"Get Node FAIL"
    bookmark_pos = chierarchyviewer.getAbsoluteCenterOfView(list.children[line].children[number])
    cdevice.touch(bookmark_pos.x,bookmark_pos.y,MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    print "Open Bookmark",index


def IsMainCotent():
    maxtimes = 0
    while not ceasy_device.visible(By.id('id/main_content')):
        maxtimes = maxtimes + 1
        cdevice.press('KEYCODE_BACK',MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        if maxtimes > 3:
            return False
    return True


def ClearCache(loop):
    global NetWork_type
    if IsMainCotent():
        SelectMenuItem("Settings")
        # Enter Pravacy&Scurity
        print 'Privacy & Security'
        common.GetWind_Unusual_Pop(chierarchyviewer,cdevice,ceasy_device,'id/button1','No','OK')
        ceasy_device.touchtext(By.id("id/title"),"Privacy & security",MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)
        ceasy_device.touchtext(By.id("id/title"),"Clear cache",MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        if ceasy_device.visible(By.id('id/alertTitle')):
            print 'ClearCache: Clear Cache'
            ceasy_device.touch(By.id("id/button1"),MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(2)
            cdevice.press('KEYCODE_BACK',MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            cdevice.press('KEYCODE_BACK',MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            return True
    shotpath = (ImagePath+"\\Fail_ClearCache_"+NetWork_type+'_'+str(loop+1)+".png")
    common.SaveFailImg(cdevice,shotpath)
    print 'ClearCache: Clear Cache Failed'
    return False

#----------------------------------------------------------------------------
# Open AT&T Home Page
def VisitATT(times,NetWork_type):
   global SucTimes
    
   for loop in range (times):
      if EnterBrowser():
         try:
            result = True
            SelectMenuItem("Bookmarks/History")
            #add by jianke 07/30
            getRightView()
            #end
            #add by jianke 07/14
            enterbrowser_times = 0
            while id_name.BComboView_APPID == chierarchyviewer.getFocusedWindowName():
                SelectOneBookmark(1)
                enterbrowser_times = enterbrowser_times + 1
                print 'enterbrowser_times ',enterbrowser_times
                if enterbrowser_times > 3:
                    break
            #end
            if id_name.BROWSER_APPID != chierarchyviewer.getFocusedWindowName():
               shotpath = ImagePath + "\\Fail_OpenATT_" + str(loop+1) + "_" + NetWork_type + ".png"
               common.SaveFailImg(cdevice,shotpath)
               continue
            progress_times = 0
            while not ceasy_device.visible(By.id('id/progress')):
               MonkeyRunner.sleep(1)
               progress_times = progress_times + 1
               if progress_times > 2:
                  break
            #end
            Maxtime = 0
            Progress_Flag = True
            while ceasy_device.visible(By.id('id/progress')):
               Progress_Flag = False
               MonkeyRunner.sleep(2)
               Maxtime = Maxtime + 1
               print 'Maxtime ',Maxtime*2
               if (Maxtime > MaxTime) or (ceasy_device.visible(By.id('id/alertTitle'))):
                  break        
            if ceasy_device.visible(By.id('id/alertTitle')):
               if ceasy_device.getText(By.id('id/alertTitle')).find("Problem") > -1:
                  shotpath = ImagePath + "\\Fail_OpenATT_alert" + str(loop+1) + "_" + NetWork_type + ".png"
                  common.SaveFailImg(cdevice,shotpath)
                  result = False
                  ceasy_device.touch(By.id('id/button1'),MonkeyDevice.DOWN_AND_UP)
                  MonkeyRunner.sleep(2)   
            elif Maxtime > MaxTime :
               shotpath = ImagePath + "\\Fail_OpenATT_outoftime" + str(loop+1) + "_" + NetWork_type + ".png"
               common.SaveFailImg(cdevice,shotpath)
               result = False
               MonkeyRunner.sleep(2)
                    
            tempresult = ClearCache(loop)
            if result:
               result = tempresult
            tempresult = SelectMenuItem("Close") 
            #add by jianke 08/03
            delay_times = 0
            while not ceasy_device.visible(By.id('id/parentPanel')):
                MonkeyRunner.sleep(1)
                delay_times = delay_times + 1
                if delay_times > 2:
                    break
            else:
                ceasy_device.touchtext(By.id('id/text1'),'Quit',MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(0.5)
            if result:
               result = tempresult
            if result == True :
               SucTimes = SucTimes + 1
               print "Trace Success Loop " + str(loop+1)
            if Progress_Flag:
               if not ceasy_device.visible(By.id('id/progress')):
                  print 'not progress ... '
                  shotpath = ImagePath + "\\VisitATT_not_progress_" + str(loop+1) + "_" + NetWork_type + ".png"
                  common.SaveFailImg(cdevice,shotpath)
            #end
         except Exception,e:
            shotpath = ImagePath + "\\VisitATT_exc_" + str(loop+1) + "_" + NetWork_type + ".png"
            common.SaveFailImg(cdevice,shotpath)
            print "VisitATT Exception Error:",e
            traceback.print_exc()
      else:
         shotpath = ImagePath + "\\Not_Enter_VisitATT_" + str(loop+1) + "_" + NetWork_type + ".png"
         common.SaveFailImg(cdevice,shotpath)
            
#------------------------------------------------------------------------------
def Navigation(times,NetWork_type):
   global SucTimes
                            
   for loop in range(times):
      if EnterBrowser():
         try:
            SelectMenuItem("Bookmarks/History")
            #add by jianke 07/30
            getRightView()
            #end
            SelectOneBookmark(0)
            Maxtime = 0
            while ceasy_device.visible(By.id('id/progress')):
               MonkeyRunner.sleep(2)
               Maxtime = Maxtime + 1
               print 'Maxtime ',Maxtime*2
               if (Maxtime > MaxTime) or (ceasy_device.visible(By.id('id/alertTitle'))):
                  break
               if common.Get_keyType(ceasy_device,chierarchyviewer,'id/dont_share_button',1):
                  print 'dont_share_button ',Maxtime
                  ceasy_device.touchtext(By.id('id/dont_share_button'),'Decline',MonkeyDevice.DOWN_AND_UP)
                  MonkeyRunner.sleep(1)
               if common.Get_keyType(ceasy_device,chierarchyviewer,'id/buttonPanel',1):
                  print 'buttonPanel ',Maxtime
                  ceasy_device.touchtext(By.id('id/button1'),'OK',MonkeyDevice.DOWN_AND_UP)
                  MonkeyRunner.sleep(1)
            if ceasy_device.visible(By.id('id/alertTitle')):
               if ceasy_device.getText(By.id('id/alertTitle')).find("Problem") > -1:
                  shotpath = ImagePath + "\\Fail_Navigation_alert" + str(loop+1) + "_" + NetWork_type + ".png"
                  common.SaveFailImg(cdevice,shotpath)
               ceasy_device.touch(By.id('id/button1'),MonkeyDevice.DOWN_AND_UP)
               MonkeyRunner.sleep(2)   
            elif Maxtime > MaxTime:
               shotpath = ImagePath + "\\Fail_Navigation_outoftime" + str(loop+1) + "_" + NetWork_type + ".png"
               common.SaveFailImg(cdevice,shotpath)
               MonkeyRunner.sleep(2)
            cdevice.shell("input tap 160 170")
            MonkeyRunner.sleep(1)
            if ceasy_device.visible(By.id('id/url')):
               url_node = common.GetNode(cdevice,chierarchyviewer,'id/url')
               if url_node is None:
                  raise TypeError,"Get Node FAIL"
               if ceasy_device.getText(By.id('id/url')).find("shopmobile") == -1:
                  Maxtime = 0
                  while ceasy_device.visible(By.id('id/progress')):
                     MonkeyRunner.sleep(2)
                     Maxtime = Maxtime + 1
                     print 'Maxtime ',Maxtime*2
                     if (Maxtime > MaxTime) or (ceasy_device.visible(By.id('id/alertTitle'))):
                        break
               if ceasy_device.visible(By.id('id/alertTitle')):
                  ceasy_device.touch(By.id('id/button1'),MonkeyDevice.DOWN_AND_UP)
                  MonkeyRunner.sleep(2)
               elif Maxtime <= MaxTime:
                  SucTimes = SucTimes + 1
                  print "Navigation Page Succeessfully"
                  print "Trace Success Loop "+ str(loop+1)
               else:
                  shotpath = ImagePath + "\\Fail_Navigation_" + str(loop+1) + "_" + NetWork_type + ".png"
                  common.SaveFailImg(cdevice,shotpath)
            else:
               SucTimes = SucTimes + 1
               print "Navigation Page Succeessfully"
               print "Trace Success Loop " + str(loop+1)
               cdevice.press('KEYCODE_BACK',MonkeyDevice.DOWN_AND_UP)
               MonkeyRunner.sleep(1)
            ClearCache(loop)
            SelectMenuItem("Close")
            ceasy_device.touchtext(By.id('id/text1'),'Quit',MonkeyDevice.DOWN_AND_UP)
         except Exception,e:
            shotpath = ImagePath + "\\Navigation_exc_" + str(loop+1) + "_" + NetWork_type + ".png"
            common.SaveFailImg(cdevice,shotpath)
            print "Navigation Exception Error:",e
            traceback.print_exc()
            print 'exception ........... '
            common.GetWind_Unusual_Pop(chierarchyviewer,cdevice,ceasy_device,'id/button1','No','OK')
            #EnterBrowser()
      else:
         shotpath = ImagePath + "\\Not_Enter_Navigation_" + str(loop+1) + "_" + NetWork_type + ".png"
         common.SaveFailImg(cdevice,shotpath)
        
#------------------------------------------------------------------------    
def Topweb(times,NetWork_type):
    global SucTimes
    
    for loop in range(times):
        if EnterBrowser():
            try:
                for index in range(5):
                    result = True
                    SelectMenuItem("Bookmarks/History")
                    #add by jianke 07/30
                    getRightView()
                    #end
                    SelectOneBookmark(index)
                    winid = chierarchyviewer.getFocusedWindowName()
                    #jianke 07/09
                    if winid != id_name.BROWSER_APPID:
                        shotpath = ImagePath + "\\Fail_TopWeb_" + str(loop+1) + "_" + str(index) + '_' + NetWork_type + ".png"
                        common.SaveFailImg(cdevice,shotpath)
                        break
                    Maxtime = 0
                    while ceasy_device.visible(By.id('id/progress')):
                        MonkeyRunner.sleep(2)
                        Maxtime = Maxtime + 1
                        print 'Maxtime ',Maxtime*2
                        if (Maxtime > MaxTime) or (ceasy_device.visible(By.id('id/alertTitle'))):
                            break      
                    if ceasy_device.visible(By.id('id/alertTitle')):
                        if ceasy_device.getText(By.id('id/alertTitle')).find("Problem") > -1:
                            shotpath = ImagePath + "\\Fail_TopWeb_alert" + str(loop+1) + "_" + str(index) + '_' + NetWork_type + ".png"
                            common.SaveFailImg(cdevice,shotpath)
                            result = False
                        ceasy_device.touch(By.id('id/button1'),MonkeyDevice.DOWN_AND_UP)
                        MonkeyRunner.sleep(2)   
                    elif Maxtime > MaxTime :
                        shotpath = ImagePath + "\\Fail_TopWeb_outoftime" + str(loop+1) + "_" + str(index) + '_' + NetWork_type + ".png"
                        common.SaveFailImg(cdevice,shotpath)
                        result = False
                        MonkeyRunner.sleep(2)
                    if result:
                       SucTimes = SucTimes + 1
                       print "Trace Success Loop " + str(loop+1) + '_' + str(index) 
                ClearCache(loop)
                SelectMenuItem("Close")
                ceasy_device.touchtext(By.id('id/text1'),'Quit',MonkeyDevice.DOWN_AND_UP)
            except Exception,e:
                shotpath = ImagePath + "\\Topweb_exc_" + str(loop+1) + "_" + NetWork_type + ".png"
                common.SaveFailImg(cdevice,shotpath)
                print "Topweb Exception Error:",e
                traceback.print_exc()
                EnterBrowser()
        else:
           shotpath = ImagePath + "\\Not_Enter_Topweb_" + str(loop+1) + "_" + NetWork_type + ".png"
           common.SaveFailImg(cdevice,shotpath)
         
def main():
    global NetWork_type

    time_Start = common.timeCalc()
    
    print 'Start Browser Test'
    common.ShowDeviceMemoryInfo(cdevice)
    common.BackToHome(cdevice)

    if True:
       NetWork_type = '3G'
       print 'Use ' + NetWork_type + ' Visit ATT ' + str(ATTPage3G) + ' Times'
       VisitATT(ATTPage3G,NetWork_type)

    if True:
       NetWork_type = '3G'
       print 'Use ' + NetWork_type + ' Navigation ' + str(Navigate3G) + ' Times'
       Navigation(Navigate3G,NetWork_type)

    if True:
       NetWork_type = '3G'
       print 'Use ' + NetWork_type + ' Top Web ' + str(TopSites3G) + ' Times'
       Topweb(TopSites3G,NetWork_type)
           
    common.BackToHome(cdevice)    
    
    print "Finished Browser Test"
    common.ShowDeviceMemoryInfo(cdevice)
    print "Success Times: ",SucTimes
    Rate = SucTimes/TestTimes*100
    if Rate < 95:
        print 'Result Fail Success Rate Is ' + str(Rate) + '%'
    else:
        print 'Result Pass Success Rate Is ' + str(Rate) + '%'
    timeEnd = common.timeCalc()
    totalTime = timeEnd-time_Start
    print '5.1.04_Browser time = ' + str(totalTime) + 'mins'
   
if __name__ == "__main__":
    main()
# Scrpit End
