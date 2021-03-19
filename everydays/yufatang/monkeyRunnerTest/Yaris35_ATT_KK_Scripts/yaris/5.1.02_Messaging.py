#coding=UTF-8
#-------------------------------------------------------------------------------
#Title:                 5.1.02_Messaging
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
scriptpath = sys.path[0][sys.path[0].find(':')+1:] + "\\..\\common"
sys.path.append(scriptpath)
import common
from common import ConnectClientDevice
from common import ConnectServerDevice

cdevice,chierarchyviewer,ceasy_device=ConnectClientDevice()
sdevice,shierarchyviewer,seasy_device=ConnectServerDevice()

# Change Depend On Real Condition
config = ConfigParser.ConfigParser()
config.read(scriptpath+"\\config.ini")
SEND_TO_NUMBER = config.get("Message","MSG_RECEIVER")
print 'SEND_TO_NUMBER ='+SEND_TO_NUMBER 
print type(SEND_TO_NUMBER)
RECEIVERLIST = SEND_TO_NUMBER.split(",")
print 'RECEIVERLIST = '+str(RECEIVERLIST)
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
print 'width ',width
print 'height ',height
#end

#add by jianke 14/06/10 for test
Flag_mini = True

if supportedNetworkType == "2G3GLTE":
   if testtype == "mini": 
        SMS2G = 2
        SMS3G = 0
        SMSLTE = 0
        Auiod2G = 2
        Auiod3G = 0
        AuiodLTE = 0
        Video2G = 2
        Video3G = 0
        VideoLTE = 0
        Pic2G = 2
        Pic3G = 0
        PicLTE = 0
        OpenTimes = 2
   else:
        SMS2G = 5
        SMS3G = 20
        SMSLTE = 25
        Auiod2G = 5
        Auiod3G = 20
        AuiodLTE = 25
        Video2G = 5
        Video3G = 20
        VideoLTE = 25
        Pic2G = 5
        Pic3G = 20
        PicLTE = 25
        OpenTimes = 50
   TestTimes = SMS2G+SMS3G+SMSLTE+Auiod2G+Auiod3G+AuiodLTE+Video2G+Video3G+VideoLTE+Pic2G+Pic3G+PicLTE+OpenTimes*4
if supportedNetworkType == "2G3G":
   if testtype == "mini":
      if Flag_mini:
         SMS2G = 0 #10
         SMS3G = 1 #40
         Auiod2G = 0 #10
         Auiod3G = 1 #40
         Video2G = 0 #10
         Video3G = 1 #40
         Pic2G = 0 #10
         Pic3G = 1 #40
         OpenTimes = 1 #50
      else:
         SMS2G = 5 #10
         SMS3G = 0 #40
         Auiod2G = 5 #10
         Auiod3G = 0 #40
         Video2G = 5 #10
         Video3G = 0 #40
         Pic2G = 5 #10
         Pic3G = 0 #40
         OpenTimes = 10 #50
   else:
      SMS2G = 0 #10
      SMS3G = 50 #40
      Auiod2G = 0 #10
      Auiod3G = 50 #40
      Video2G = 0 #10
      Video3G = 50 #40
      Pic2G = 0 #10
      Pic3G = 50 #40
      OpenTimes = 50 #50
   TestTimes = SMS2G+SMS3G+Auiod2G+Auiod3G+Video2G+Video3G+Pic2G+Pic3G+OpenTimes*4
   
print 'Trace Total Times ' + str(TestTimes)
SucTimes = 0
MsgOrder = {'Audio':0,'Video':1,'Photo':2,'Text':3}

ImagePath = common.CreateFolder('5.1.2')
#add by jianke 1230
scriptpath2 = sys.path[0][sys.path[0].find(':')+1:] + "\\sentSuccessState.png"
scriptpath3 = sys.path[0][sys.path[0].find(':')+1:] + "\\sentFailState.png"
#end

def EnterMSG(device = cdevice,easy_device = ceasy_device):
    print "Launch Message And Wait"
    common.BackToHome(device)
    if common.isEnterApp(easy_device,id_name.MSG_APPID) or common.startapp(device,easy_device,id_name.MSG_APPID):
        return True
    return False

def SelectMsg(device = cdevice,hierarchyviewer = chierarchyviewer,\
              index = None,offset = None,strtype = None, listnode = None):
    print "Select the Msg",str(strtype)
    #add by jianke 04/01 001
    if common.GetWind_Id(chierarchyviewer,ceasy_device,id_name.MSG_APPID,'id/list',1,2,1,2):
       if listnode is None:
           listnode = common.GetNode(device,hierarchyviewer,'id/list')
       if listnode is None:
           raise TypeError,"Get Node FAIL"
       #add by jianke 04/21
       number = listnode.children.size()
       print 'lst number = ',number
       listTimes = 0
       while number == 0:
          MonkeyRunner.sleep(2)
          listnode = common.GetNode(device,hierarchyviewer,'id/list')
          if listnode is None:
             raise TypeError,"Get Node FAIL"
          number = listnode.children.size()
          listTimes = listTimes + 1
          if listTimes > 2:
             break
       #end
       if offset != None:
           addition = number - offset
           index = MsgOrder[strtype] + addition
       print "Debug Msg index is",index
       msg_pos = hierarchyviewer.getAbsoluteCenterOfView(listnode.children[index])
       #add by jianke 03/20
       print "Debug Touch x=",msg_pos.x,"y=",msg_pos.y
       #end
       totimes = 0
       textt = hierarchyviewer.getFocusedWindowName()
       while textt != id_name.MSG_ComMsgID: #07/08
          device.touch(msg_pos.x,msg_pos.y,MonkeyDevice.DOWN_AND_UP)
          MonkeyRunner.sleep(2)
          textt = hierarchyviewer.getFocusedWindowName()
          totimes = totimes + 1
          if totimes > 2:
             print "Cannot Enter Msg",str(strtype)
             return False
       return True
    #end

def Selcet_Msg_Opt(str_option,device=cdevice,easy_device=ceasy_device,hierarchyviewer=chierarchyviewer):
    print "Trace",str_option
    history_node = common.GetNode(device,hierarchyviewer,'id/history')
    if history_node is None:
        raise TypeError,"Get Node FAIL"
    number = history_node.children.size()
    print 'history_node.children = ' + str(number)
    #add by jianke 03/19
    selectTimes = 0
    while number == 0:
       MonkeyRunner.sleep(2)
       history_node = common.GetNode(device,hierarchyviewer,'id/history')
       if history_node is None:
           raise TypeError,"Get Node FAIL"
       number = history_node.children.size()
       selectTimes = selectTimes + 1
       if selectTimes > 2:
          break
    #end
    Msg_node = history_node.children[number - 1]
    text_node = hierarchyviewer.findViewById("id/text_view",Msg_node)
    text_pos =  hierarchyviewer.getAbsoluteCenterOfView(text_node)
    print 'text_pos = ' + str(text_pos)
    #add by jianke 04/22 
    wind_Id = id_name.MSG_ComMsgID
    if common.GetWind_Id(chierarchyviewer,ceasy_device,wind_Id,'id/changed_linear_layout',1,3,1,3):
       MonkeyRunner.sleep(1)
       device.touch(text_pos.x,text_pos.y,MonkeyDevice.DOWN)
       MonkeyRunner.sleep(2)
       device.touch(text_pos.x,text_pos.y,MonkeyDevice.UP)
    #end
    #jianke 20140105
    MonkeyRunner.sleep(2)
    #add by jianke 03/20
    easy_device.touchtext(By.id("id/title"), str_option, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    textForward = id_name.MSG_FrdMsgID  #07/08
    time_fd = 0
    text_fd = hierarchyviewer.getFocusedWindowName()
    while text_fd != textForward:
       print 'Be sure enter forward'
       MonkeyRunner.sleep(2)
       text_fd = hierarchyviewer.getFocusedWindowName()
       time_fd = time_fd + 1
       if time_fd > 2:
          break
    #end

def InputOneRecipient(strnumber):
    print "Input Number"
    ceasy_device.type(By.id('id/recipients_editor'),strnumber)
    MonkeyRunner.sleep(2)
    cdevice.press('KEYCODE_BACK',MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

def Send_Msg():
    max_time = 0
    #0105 jianke
    ceasy_device.touch(By.id('id/button_with_counter'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(3)
    #delete by jianke 20140105
    '''
    while ceasy_device.visible(By.id('id/button_with_counter')):
        max_time = max_time + 1
        if max_time > 3:
            return False
        #ceasy_device.touch(By.id('id/button_with_counter'),MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(5)
    return True
   '''
    
def Confirm_Warning():
    if chierarchyviewer.getFocusedWindowName() != id_name.MSG_ComMsgID:
        cdevice.press('KEYCODE_DPAD_RIGHT',MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(0.5)
        cdevice.press('KEYCODE_DPAD_RIGHT',MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(0.5)
        cdevice.press('KEYCODE_DPAD_CENTER',MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)

def isSent(MsgType,loop):
    MaxTime = 0
    
    for time in range(120):
       try:
          sent_node = common.GetNode(cdevice,chierarchyviewer,'id/delivered_indicator')
          #begin add by jianke 20140130
          if sent_node is None:
             print "sent_node is none."
             sent_node_new_img = cdevice.takeSnapshot()
             shotpath = ImagePath + "\\IsSent_exc_sent_node_new_img_" + MsgType + '_' + NetWork_type + '_' + str(loop+1) + ".png"
             common.SaveFailImg(cdevice,shotpath)
             return False
          #end
          view_pos =  chierarchyviewer.getAbsolutePositionOfView(sent_node)
          rect = (view_pos.x,view_pos.y,sent_node.width,sent_node.height)
          
          new_img = cdevice.takeSnapshot()
          #begin add by jianke 20140130
          if new_img is None:
             print "Image is none."
             return False
          #end
          #try RasterFormatException jianke 0131
          try:
             sub_new_img = new_img.getSubImage(rect)
             #test to catch 07/27
             #savepath = ImagePath + "\\test_img_loop " + str(loop) + '_' + str(time) + ".png"
             #sub_new_img.writeToFile(savepath, 'png')
             #end
          except:
             print "RasterFormatException."
             return False
          #add by jianke 07/30 
          Falg_Fail = common.CompareImage(sub_new_img,scriptpath3)
          if Falg_Fail:
              print 'the network so bad!!!'
              return False
          #end
          Flag = common.CompareImage(sub_new_img,scriptpath2)
          if Flag:
             return True
          if not Flag:
             MonkeyRunner.sleep(5)
             print "Message still in sending, past " + str(MaxTime+1) + " by 5s"
             MaxTime = MaxTime + 1
          if MaxTime == 60:
             print "5 min pass Sending message time out"
             return False
       except Exception,e:
          shotpath = ImagePath + "\\IsSent_exc_" + MsgType + '_' + NetWork_type + '_' + str(loop+1) + ".png"
          common.SaveFailImg(cdevice,shotpath)
          print "IsSent Exception Error:",e
          traceback.print_exc()
         
def isSent_old(MsgType,loop):
    MaxTime = 0

    while getStatus().find("Send") > -1:
       print '344444444444444 - > ' + str(MaxTime+1)
       MaxTime = MaxTime + 1
       print "waiting for send message :",MaxTime
       MonkeyRunner.sleep(10)
       '''
       #add by jianke 0105  --002
       sent_node = common.GetNode(cdevice,chierarchyviewer,'id/delivered_indicator')
       view_pos =  chierarchyviewer.getAbsolutePositionOfView(sent_node)
       rect = (view_pos.x,view_pos.y,sent_node.width,sent_node.height)
       new_img = cdevice.takeSnapshot()
       sub_new_img = new_img.getSubImage(rect)
       #add by jianke for detail debug 0106  {'Audio':0,'Video':1,'Photo':2,'Text':3}
       debugimagepath = ImagePath + "\\" + MsgType
       debugimagepathTime = debugimagepath + "\\" + str(loop)
       if not os.path.exists(debugimagepath):
          os.mkdir(debugimagepath)
       if not os.path.exists(debugimagepathTime):
          os.mkdir(debugimagepathTime)
       scriptpath3 = debugimagepathTime+"\\isSent_"+MsgType+"_"+NetWork_type+'_'+str(MaxTime)+".png"
       print 'send status ' + str(scriptpath3)
       try:
          sub_new_img.writeToFile(scriptpath3, 'png')
       except Exception,e:
          print e
       if common.CompareImage(sub_new_img,scriptpath2):  #scriptpath2
          return False
       #end
       '''
       if MaxTime > 60: #30:
          return False
    #add by jianke 1230
    if getStatus().find("Unkown") > -1:
       return False
    #end
    return True

def getStatus():
    history_node = common.GetNode(cdevice,chierarchyviewer,'id/history')
    if history_node is None:
        raise TypeError,"Get Node FAIL"
    history_number = history_node.children.size()
    print 'history_number ' + str(history_number)
    if history_number != 0:
        order = history_number - 1
        date_node = common.GetNode(cdevice,chierarchyviewer,'id/date_view',history_node.children[order])
        if date_node is None:
            raise TypeError,"Get Node FAIL"
        #add by jianke 0105  ---001
        try:
           strdate = chierarchyviewer.getText(date_node)
           #print str(strdate).encode('utf-8')
        except:
           print '656565656565656565656'
           #traceback.print_exc()
           strdate = "Unkown"
        #end
    else:
        strdate = "Unkown"
    return strdate


def DeleteMsg(hierarchyviewer = chierarchyviewer,device = cdevice,\
              easy_device = ceasy_device):
    print device
    print "Select Delete thread"
    #modify by jianke 1220 Delete -> Delete message
    Selcet_Msg_Opt("Delete message",device,easy_device,hierarchyviewer)
    easy_device.touchtext(By.id('id/button1'),'Delete', MonkeyDevice.DOWN_AND_UP)
    #jianke add 0106 need time
    MonkeyRunner.sleep(1)
    #end
    if common.isEnterApp(easy_device,MSG_APPID):
        print "Del Msg Successfully"
        return True
    Maxtime = 0                
    while not common.isEnterApp(easy_device,MSG_APPID):
        print '0106----- DeleteMsg ------------- ' + str(Maxtime)
        device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        Maxtime = Maxtime + 1
        if (Maxtime > 5):
            break
    return False

def GetMsgNumber():
    list_node = common.GetNode(cdevice,chierarchyviewer,'id/list')
    if list_node is None:
        raise TypeError,"Get Node FAIL"
    numMSG = list_node.children.size()
    print "number of msg is GetMsgNumber ",numMSG
    return numMSG

def BackToMSG(device = cdevice,easy_device = ceasy_device):
    for loop_time in range(5):
        if common.isEnterApp(easy_device,id_name.MSG_APPID):
           return True
        device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        if easy_device.visible(By.id('id/button1')):
            easy_device.touch(By.id('id/button1'),MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(2)
    return False

def MakeSureNumOfMsgList(hierarchyviewer = chierarchyviewer,device = cdevice,\
              easy_device = ceasy_device):
    print 'Make Sure Num Of Message List is 4 or sdevice is 0'
    list_node = common.GetNode(device,hierarchyviewer,'id/list')
    if list_node is None:
       raise TypeError,"Get Node FAIL"
    numMSG = list_node.children.size()
    print 'numMSG 0131 -> ' + str(numMSG)
    if device == cdevice:
        msg_num = 4
    else:
        msg_num = 0
    while numMSG > msg_num:
       msg_pos = hierarchyviewer.getAbsoluteCenterOfView(list_node.children[0])
       device.touch(msg_pos.x,msg_pos.y,MonkeyDevice.DOWN)
       MonkeyRunner.sleep(2)
       device.touch(msg_pos.x,msg_pos.y,MonkeyDevice.UP)
       MonkeyRunner.sleep(1)
       #add by jianke 04/11 001
       print 'go to here to delete'
       if True: #common.GetWind_Keyword(chierarchyviewer,ceasy_device,cdevice,MSG_APPID,'id/selection_menu','selected',1,3):
          MonkeyRunner.sleep(1)
          easy_device.touch(By.id('id/delete'),MonkeyDevice.DOWN_AND_UP)
          MonkeyRunner.sleep(1)
       #end
       #add by jianke 04/04 001
       if common.Get_keyType(easy_device,hierarchyviewer,'id/parentPanel',10):
          MonkeyRunner.sleep(1)
          print 'delete ok'
          easy_device.touchtext(By.id('id/button1'),'Delete', MonkeyDevice.DOWN_AND_UP)
          if device == cdevice:
              MonkeyRunner.sleep(2)
          else:
              MonkeyRunner.sleep(6)
       else:
          for loop in range(2):
             print 'back ok'
             device.press('KEYCODE_BACK',MonkeyDevice.DOWN_AND_UP)
             MonkeyRunner.sleep(1)
       #add by jianke 04/17 001
       if common.GetWind_Id(hierarchyviewer,easy_device,id_name.MSG_APPID,'id/content',1,10,1,5):
          MonkeyRunner.sleep(1)
       #end
          list_node = common.GetNode(device,hierarchyviewer,'id/list')
          if list_node is None:
             raise TypeError,"Get Node FAIL"
          numMSG = list_node.children.size()
          print 'numMSG 0417 -> ',numMSG
       #end
    MonkeyRunner.sleep(2)

def ForwardMsg(MsgType,LoopTime):
   global SucTimes
   
   for loop in range(LoopTime):
      try:
         #jianke 0206
         EnterMSG()
         MakeSureNumOfMsgList()
         SelectMsg(strtype = MsgType,offset = 4)
         MonkeyRunner.sleep(0.5)
         Selcet_Msg_Opt("Forward")
         Receiver = random.choice(RECEIVERLIST)
         print "Receiver: ",Receiver
         Receiver = Receiver.strip()
         print "Receiver: ",Receiver
         #add by jianke 07/22
         common.Get_keyBoard_wind(cdevice,chierarchyviewer,'id/content',210)
         InputOneRecipient(Receiver)
         #end
         Send_Msg()
         #Confirm_Warning()
         #MonkeyRunner.sleep(1)
         #Back To List
         #cdevice.press('KEYCODE_BACK',MonkeyDevice.DOWN_AND_UP)
         #MonkeyRunner.sleep(3)
         #Verified Sent Successfully
         print "Choose the send message"
         list_node = common.GetNode(cdevice,chierarchyviewer,'id/list')
         if list_node is None:
            raise TypeError,"Get Node FAIL"
         SelectMsg(index = 0,listnode = list_node)
         MonkeyRunner.sleep(2)
         if not isSent(MsgType,loop):
            print "Sending Msg More Than 5 Mins or sending failed"
            shotpath = ImagePath + "\\Fail_Send_" + MsgType + "_" + NetWork_type + '_' + str(loop+1) + ".png"
            common.SaveFailImg(cdevice,shotpath)
            Sendflag = False
         else:
            print "Sent Message Successfully"
            SucTimes = SucTimes + 1
            print "Trace Success Loop "+ str(loop+1)
            Sendflag = True
         #-------delete-----
         MonkeyRunner.sleep(1)
         cdevice.press('KEYCODE_BACK',MonkeyDevice.DOWN_AND_UP)
         MonkeyRunner.sleep(2)               
         #MakeSureNumOfMsgList()
      except Exception,e:
         shotpath = ImagePath + "\\ForwardMsg_exc_" + MsgType + "_" + NetWork_type + '_' + str(loop+1) + ".png"
         common.SaveFailImg(cdevice,shotpath)
         print "ForwardMsg Exception Error:",e
         traceback.print_exc()
         BackToMSG() 
   
def ForwardMsg_old(MsgType, LoopTime):
    global SucTimes
    
    for loop in range(LoopTime):
       if EnterMSG():
            try:
                MakeSureNumOfMsgList()
                if not SelectMsg(strtype = MsgType,offset = 4):
                    continue
                Selcet_Msg_Opt("Forward")
                Receiver = random.choice(RECEIVERLIST)
                print '~~~~~~~~~~~'
                print Receiver
                Receiver = Receiver.strip()
                print Receiver
                InputOneRecipient(Receiver)
                Send_Msg()
                Confirm_Warning()
                # Back To List
                MonkeyRunner.sleep(0.5)
                cdevice.press('KEYCODE_BACK',MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(3)
                # Verified Sent Successfully
                list_node = common.GetNode(cdevice,chierarchyviewer,'id/list')
                if list_node is None:
                    raise TypeError,"Get Node FAIL"
                numMSG = list_node.children.size()
                print 'debug-----------------------'
                print "number of msg is",numMSG
                if numMSG > 4:
                    if not SelectMsg(index = 0,listnode = list_node):
                        print '111111111111111111111111111111111111'
                        continue
                    if not isSent(MsgType,loop): #modify by jianke for detail debug 0106
                        print "Sending Msg More Than 5 Mins or sending failed"
                        shotpath = ImagePath+"\\Fail_Send_"+MsgType+"_"+\
                                   NetWork_type+'_'+str(loop+1)+".png"
                        common.SaveFailImg(cdevice,shotpath)
                        
                        Sendflag = False
                    else:
                        print "Sent Message Successfully"
                        Sendflag = True
                    #-------delete-----
                    Delflag = DeleteMsg()
                    if not Delflag:
                        print "Delete MSG Failed"
                        shotpath = ImagePath+"\\Fail_Del_"+MsgType+"_"+\
                                   NetWork_type+'_'+str(loop+1)+".png"
                        common.SaveFailImg(cdevice,shotpath)
                    if Sendflag and Delflag:
                        SucTimes = SucTimes + 1
                        print "Trace Success Loop "+ str(loop+1)
                else:
                    print "Send SMS Failed"
                    shotpath = ImagePath+"\\Fail_Send_"+MsgType+"_"+\
                               NetWork_type+'_'+str(loop+1)+".png"
                    common.SaveFailImg(cdevice,shotpath)
                print "Delete the extra SMS"
                for loop_i in range(5):
                    if GetMsgNumber() <= 4:
                        break
                    #jianke 0106
                    print 'extra msg is ' + str(loop_i+1)
                    SelectMsg(index = 0,listnode = list_node)    
                    DeleteMsg()
            except Exception,e:
                shotpath = ImagePath+"\\ForwardMsg_exc_"+MsgType+"_"+\
                                   NetWork_type+'_'+str(loop+1)+".png"
                common.SaveFailImg(cdevice,shotpath)
                print "ForwardMsg Exception Error:",e
                traceback.print_exc()
                #BackToMSG()
                
    print 'Send Msg Test complete'
    MonkeyRunner.sleep(1) 

def OpenMessage(MsgType = None, LoopTime = None):
    global SucTimes
    
    for loop in range(LoopTime):
       if EnterMSG():
            try:
                SelectMsg(strtype = MsgType,offset = 4)
                if ceasy_device.visible(By.id('id/history')):
                    SucTimes = SucTimes + 1
                    print "Trace Success Loop " + str(loop+1)
                else:
                    shotpath = ImagePath + "\\Fail_Open_" + MsgType + '_' + NetWork_type + '_' + str(loop+1) + ".png"
                    common.SaveFailImg(cdevice,shotpath)
                cdevice.press('KEYCODE_BACK',MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(2)
            except Exception,e:
                shotpath = ImagePath + "\\OpenMessage_exc_" + str(loop+1) + ".png"
                common.SaveFailImg(cdevice,shotpath)
                print "OpenMessage Exception Error:",e
                traceback.print_exc()
                BackToMSG()
    print 'Open ' + MsgType + ' Test complete'

def DeleteSdeviceMSG(hierarchyviewer = chierarchyviewer,device = cdevice,easy_device = ceasy_device):
    if EnterMSG(device,easy_device):
        MakeSureNumOfMsgList(hierarchyviewer,device,easy_device)
        
def main():
    global NetWork_type

    time_Start = common.timeCalc()
    
    print 'Start Messaging Test'
    common.ShowDeviceMemoryInfo(cdevice)
    common.BackToHome(cdevice)
    common.BackToHome(sdevice)
    
    #-------------1--------------------
    if True:
       NetWork_type = '3G'
       print 'Make ' + NetWork_type + ' Send SMS ' + str(SMS3G) + ' Times'
       ForwardMsg('Text',SMS3G)    
       #add by jinke 08/13
       DeleteSdeviceMSG(shierarchyviewer,sdevice,seasy_device)
       #end
    #---------------2-------------------
    if True:
       NetWork_type = '3G'
       print 'Make ' + NetWork_type + ' Send audioMMS ' + str(Auiod3G) + ' Times'
       ForwardMsg('Audio', Auiod3G)
       #add by jinke 08/13
       DeleteSdeviceMSG(shierarchyviewer,sdevice,seasy_device)
       #end
    
    #---------------------3------------------
    if True:
       NetWork_type = '3G'
       print 'Make ' + NetWork_type + ' Send videoMMS ' + str(Video3G) + ' Times'
       ForwardMsg('Video', Video3G)
       #add by jinke 08/13
       DeleteSdeviceMSG(shierarchyviewer,sdevice,seasy_device)
       #end
    #------------------4-------------------
    if True:
       NetWork_type = '3G'
       print 'Make ' + NetWork_type + ' Send picMMS ' + str(Pic3G) + ' Times'
       ForwardMsg('Photo', Pic3G)
       #add by jinke 08/13
       DeleteSdeviceMSG(shierarchyviewer,sdevice,seasy_device)
       #end
       
    #------------5------------
    print 'Make ' + NetWork_type + ' Open AudioMMS ' + str(OpenTimes) + ' Times'
    OpenMessage('Audio', OpenTimes)
    print 'Make ' + NetWork_type + ' Open VideoMMS ' + str(OpenTimes) + ' Times'
    OpenMessage('Video', OpenTimes)
    print 'Make ' + NetWork_type + ' Open PicMMS ' + str(OpenTimes) + ' Times'
    OpenMessage('Photo', OpenTimes)
    print 'Make ' + NetWork_type + ' Open SMS ' + str(OpenTimes) + ' Times'
    OpenMessage('Text', OpenTimes)
    
    common.BackToHome(cdevice)
    common.BackToHome(sdevice)
    print "Finished Messaging Test"

    print "Success Times:", SucTimes
    Rate = SucTimes/TestTimes*100
    if Rate < 95:
        print 'Result Fail Success Rate Is ' + str(Rate) + '%'
    else:
        print 'Result Pass Success Rate Is ' + str(Rate) + '%'
    timeEnd = common.timeCalc()
    totalTime = timeEnd-time_Start
    print '5.1.02_Messaging time = ' + str(totalTime) + 'mins'
    
if __name__ == "__main__":
    main()
# Scrpit End







