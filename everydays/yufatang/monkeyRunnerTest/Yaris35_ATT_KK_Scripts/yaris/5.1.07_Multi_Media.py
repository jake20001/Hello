#coding=UTF-8
#*****************************************************************************
# Title:        5.1.07_Multi_Media
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

if testtype == "mini":
    VIDEOTIMES = 1
    PHOTOTIMES = 2 #20
    AUDIOTIMES = 1
    STREAMTIMES = 2 #10
    OPENCLOSETIMES = 2  #20
    MUSICPLAYTIMES = 5 #50
    EXITPLAYTIMES = 1
else:
    VIDEOTIMES = 1
    PHOTOTIMES = 20 #20
    AUDIOTIMES = 1
    STREAMTIMES = 10 #10
    OPENCLOSETIMES = 20  #20
    MUSICPLAYTIMES = 50 #50
    EXITPLAYTIMES = 1
SucTimes = 0
TestTimes = VIDEOTIMES*3 + AUDIOTIMES*3 + PHOTOTIMES*3 + STREAMTIMES + OPENCLOSETIMES + MUSICPLAYTIMES + EXITPLAYTIMES
print 'Trace Total Times ' + str(TestTimes)




sdcard = "/storage/sdcard1/DCIM/Camera/"
sdcardRecord = "/storage/sdcard1/Recording/"

def GetFileNumber(DevicePath,format):
    content = cdevice.shell("ls " + DevicePath)
    num = content.count(format)
    print format,"file num is",num
    return num


def EnterCamera():
    #add by jianke 03/20
    if common.isEnterApp(ceasy_device,id_name.Video_Camera_ID) or common.startapp(cdevice,ceasy_device,id_name.Video_Camera_ID):
        text_cm = chierarchyviewer.getFocusedWindowName()
        cmtimes = 0
        cmtimes_2 = 0
        while True:
            if text_cm == id_name.Video_Camera_ID:
                print 'start activity and be ready to record'
                return True
            else:
                MonkeyRunner.sleep(2)
                text_cm = chierarchyviewer.getFocusedWindowName()
                cmtimes = cmtimes + 1
                print 'cmtimes ',cmtimes
                if cmtimes > 2:
                    return False
    #end
    '''
    if not common.isEnterApp(ceasy_device,(camera_app_id,video_app_id)):
        print "Enter Camera And Wait"
        # Launch Camera And Wait
        return common.startapp(cdevice,ceasy_device,camera_app_id)
    else:
        print "It's already in the app."
        return True
    '''
    
def SwitchDV():
    ceasy_device.touch(By.id('id/switch_controlpanel_layout'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    
def Recordvideo(times):
    global SucTimes

    for loop in range(times):
        if EnterCamera():
            try:
                #jianke 1220
                oldCountVideo3gp = GetFileNumber(sdcard,".3gp")
                oldCountVideoMp4 = GetFileNumber(sdcard,".mp4")
                oldCountVideojpg = GetFileNumber(sdcard,".jpg")
                # Take video
                
                #add by jianke 05/13
                timeStable = 0
                while not ceasy_device.visible(By.id('id/shutter_button_video')):
                    print 'stable status'
                    MonkeyRunner.sleep(1)
                    timeStable = timeStable + 1
                    print 'timeStable ',timeStable
                    if timeStable > 5:
                        break
                    sleep_switcher = 0
                    while not ceasy_device.visible(By.id('id/mode_switcher')):
                        MonkeyRunner.sleep(1)
                        sleep_switcher = sleep_switcher + 1
                        print 'sleep_switcher ',sleep_switcher
                        if sleep_switcher > 10:
                            break
                    switcher_node = common.GetNode(cdevice,chierarchyviewer,'id/mode_switcher')
                    if switcher_node is None:
                        raise TypeError,"Get Node FAIL"
                    switcher_node_pos = chierarchyviewer.getAbsoluteCenterOfView(switcher_node)
                    cdevice.touch(switcher_node_pos.x,switcher_node_pos.y,MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(1)
                #end
                while not ceasy_device.visible(By.id('id/shutter_button_video')):
                    MonkeyRunner.sleep(1)
                else:
                    ceasy_device.touch(By.id('id/shutter_button_video'),MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(3)
                # judge whether start recording
                if not ceasy_device.visible(By.id('id/recording_time')):
                    shotpath = ImagePath + "\\Fail_Record_video.png"
                    common.SaveFailImg(cdevice,shotpath)
                    return False
                else:
                    MonkeyRunner.sleep(5) #29
                    # Stop
                    ceasy_device.touch(By.id('id/shutter_button_video'),MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(3)
                    # judge whether stop recording
                    if ceasy_device.visible(By.id('id/recording_time')):
                        shotpath = ImagePath + "\\Fail_Stop_Record_video.png"
                        common.SaveFailImg(cdevice,shotpath)
                        return False
                    else:
                        #jianke 1220
                        #modify by gqding for C1N SD card input
                        nowCountVideo3gp = GetFileNumber(sdcard,".3gp")
                        nowCountVideoMp4 = GetFileNumber(sdcard,".mp4")
                        nowCountVideojpg = GetFileNumber(sdcard,".jpg")
                        MonkeyRunner.sleep(0.5)
                        if (nowCountVideo3gp + nowCountVideoMp4 + nowCountVideojpg) == (oldCountVideo3gp + oldCountVideoMp4 + oldCountVideojpg + 1):
                            SucTimes = SucTimes + 1
                            print "Trace Success Recording video"
                            print 'Record video Test complete'
                            return True
                        else:
                            print 'Calc number is wrong!'
                            return False
            except Exception,e:
                shotpath = ImagePath + "\\Recordvideo_exc.png"
                common.SaveFailImg(cdevice,shotpath)
                print 'Recordvideo Exception Error: ',e
                traceback.print_exc()
                return False
        else:
            shotpath = ImagePath + "\\Fail_enter_video_" + str(loop+1) + ".png"
            common.SaveFailImg(cdevice,shotpath)
            return False
    

#Play Back video
def EnterPreview(id_ID=None):
    # Launch Enter Gallery To Preview
    print "Enter Gallery To Preview"
    #add by jianke 07/09
    width_w = int(str(width))
    width_w = width_w/2
    height_w = int(str(height))
    height_w = height_w/2
    width_w = int(width_w)
    print 'width_w 2222 ',width_w
    height_w = int(height_w)
    print 'height_w 2222 ',height_w
    if id_ID == None:
        cdevice.shell("input swipe " + str(width_w+120) + ' ' + str(height_w) + ' ' + str(width_w-120) + ' ' + str(height_w))
    else:
        ceasy_device.touch(By.id(id_ID),MonkeyDevice.DOWN_AND_UP)
    #end
    MonkeyRunner.sleep(1)


def PlayBackvideo():
    global SucTimes
    if EnterCamera():
        try:
            EnterPreview()
            # Play video
            ceasy_device.touch(By.id('id/gl_root_view'),MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(3)
            text = 'com.android.gallery3d/com.android.gallery3d.app.MovieActivity'
            if text == chierarchyviewer.getFocusedWindowName():
                SucTimes = SucTimes + 1
                print "Trace Success Start Playing video..."
                MonkeyRunner.sleep(32)
                cdevice.press('KEYCODE_BACK',MonkeyDevice.DOWN_AND_UP)
            else:
                shotpath = ImagePath+"\\Fail_Start_Play_video.png"
                common.SaveFailImg(cdevice,shotpath)
        except Exception,e:
            shotpath = ImagePath+"\\PlayBackvideo_exc.png"
            common.SaveFailImg(cdevice,shotpath)
            print 'PlayBackvideo Exception Error: ',e
            traceback.print_exc()
    # Return to idle
    print 'Play Back video Test complete'

#add by jianke
def PlayBackvideo2(times):
    global SucTimes

    for loop in range(times):
        if EnterCamera():
            try:
                EnterPreview('id/thumbnail')
                # Play video
                MonkeyRunner.sleep(2)
                ceasy_device.touch(By.id('id/focus_indicator'),MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(2)
                if ceasy_device.visible(By.id('id/text1')):
                    ceasy_device.touchtext(By.id('id/text1'),'Video player', MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(1)
                    if id_name.Gallery3d_Movie_ID != chierarchyviewer.getFocusedWindowName():
                        ceasy_device.touch(By.id('id/button_once'),MonkeyDevice.DOWN_AND_UP)
                        MonkeyRunner.sleep(2)
                #jianke 07/09
                if id_name.Gallery3d_Movie_ID == chierarchyviewer.getFocusedWindowName():
                    SucTimes = SucTimes + 1
                    print "Trace Success Start Playing video..."
                    times = 0
                    while not ceasy_device.visible(By.id('id/focus_indicator')):
                        times = times + 1
                        print 'times ' + str(times*5)
                        MonkeyRunner.sleep(5)
                        if id_name.Gallery3d_Movie_ID != chierarchyviewer.getFocusedWindowName():
                            break
                    print "End Playing video..."
                else:
                    shotpath = ImagePath + "\\Fail_Start_Play_video.png"
                    common.SaveFailImg(cdevice,shotpath)
            except Exception,e:
                shotpath = ImagePath + "\\PlayBackvideo_exc.png"
                common.SaveFailImg(cdevice,shotpath)
                print 'PlayBackvideo Exception Error: ',e
                traceback.print_exc()
        else:
            shotpath = ImagePath + "\\Fail_enter_video_" + str(loop + 1) + ".png"
            common.SaveFailImg(cdevice,shotpath)
    # Return to idle
    print 'Play Back video Test complete'
#end

def SelectMenuItem(stritem=None):
    MonkeyRunner.sleep(1)
    width_w = int(str(width))
    width_w = width_w/2
    height_w = int(str(height))
    height_w = height_w/2
    width_w = int(width_w)-60
    print 'width_w 2222 ',width_w
    height_w = int(height_w)-60
    print 'height_w 2222 ',height_w
    cdevice.shell("input tap " + str(width_w) + ' ' + str(height_w))
    MonkeyRunner.sleep(0.5)
    #add by jianke 2014/02/12 id/action_delete
    maxTime = 0
    while not ceasy_device.visible(By.id('id/action_delete')):
        cdevice.shell("input tap " + str(width_w) + ' ' + str(height_w))
        MonkeyRunner.sleep(0.5)
        maxTime = maxTime + 1
        if maxTime > 2:
            return False
    #add by jianke 14/06/06
    if stritem == None:
        print 'enter to delete video ... 07/09'
        ceasy_device.touch(By.id('id/action_delete'), MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    #end
    else:
        print 'enter to delete video ... 888888888888888888'
        ceasy_device.touchtext(By.id("id/title"),stritem, MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
    #For test
    submenu_node2 = common.GetNode(cdevice,chierarchyviewer,'id/buttonPanel')
    print submenu_node2
    #end
    return True


def Delvideo(times):
    global SucTimes

    for loop in range(times):
        if EnterCamera():
            try:
                oldCountVideo3gp = GetFileNumber(sdcard,".3gp")
                oldCountVideoMp4 = GetFileNumber(sdcard,".mp4")
                oldCountVideojpg = GetFileNumber(sdcard,".jpg")
                #EnterPreview()
                # delete
                SelectMenuItem()
                # confirm delete
                ceasy_device.touch(By.id('id/button1'), MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(5)
                # judge delete success
                nowCountVideo3gp = GetFileNumber(sdcard,".3gp")
                nowCountVideoMp4 = GetFileNumber(sdcard,".mp4")
                nowCountVideojpg = GetFileNumber(sdcard,".jpg")
                if (nowCountVideo3gp + nowCountVideoMp4 +nowCountVideojpg) == (oldCountVideo3gp + oldCountVideoMp4 + oldCountVideojpg - 1):
                    SucTimes = SucTimes + 1
                    print "Trace Success Delete video"
                else:
                    shotpath = ImagePath + "\\Fail_Delete_video.png"
                    common.SaveFailImg(cdevice,shotpath)
            except Exception,e:
                shotpath = ImagePath + "\\Delvideo_exc.png"
                common.SaveFailImg(cdevice,shotpath)
                print 'Delvideo Exception Error: ',e
                traceback.print_exc()
            #add by jianke 14/06/09
            if True:
                cdevice.press('KEYCODE_BACK',MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
            #end
        else:
            shotpath = ImagePath + "\\enter_Video_fail_" + str(loop + 1) + ".png"
            common.SaveFailImg(cdevice,shotpath)
    print 'Delete video Test complete'
    # Return to idle
    # common.BackToHome(cdevice)
    

#-------------------------------------------------------------
def TakePhoto(times):
    global SucTimes
    global pic_num
    
    pic_num = 0
    for loop in range(times):
        if EnterCamera():
            try:	
                oldPhotoNumberjpg = GetFileNumber(sdcard,".jpg")
                oldPhotoNumber3pg = GetFileNumber(sdcard,".3gp")
                oldPhotoNumbermp4 = GetFileNumber(sdcard,".mp4")
                #shutter_button_photo
                #add by jianke 05/13
                if not ceasy_device.visible(By.id('id/shutter_button_photo')):
                    switcher_node = common.GetNode(cdevice,chierarchyviewer,'id/mode_switcher')
                    if switcher_node is None:
                        raise TypeError,"Get Node FAIL"
                    switcher_node_pos = chierarchyviewer.getAbsoluteCenterOfView(switcher_node)
                    cdevice.touch(switcher_node_pos.x,switcher_node_pos.y,MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(1)
                ceasy_device.touch(By.id('id/shutter_button_photo'),MonkeyDevice.DOWN_AND_UP) 
                MonkeyRunner.sleep(5)
                # judge delete success
                newPhotoNumberjpg = GetFileNumber(sdcard,".jpg")
                newPhotoNumber3gp = GetFileNumber(sdcard,".3gp")
                newPhotoNumbermp4 = GetFileNumber(sdcard,".mp4")
                if (newPhotoNumberjpg + newPhotoNumber3gp + newPhotoNumbermp4) == (oldPhotoNumberjpg + oldPhotoNumber3pg + oldPhotoNumbermp4 + 1):
                    print "Trace Success Loop " + str(loop+1)
                    SucTimes = SucTimes + 1
                    pic_num = pic_num + 1
                else:
                    print 'Take photo Failed'
                    shotpath = ImagePath + "\\Fail_Take_Photo" + str(loop+1) + ".png"
                    common.SaveFailImg(cdevice,shotpath)
                MonkeyRunner.sleep(2)
            except Exception,e:
                shotpath = ImagePath + "\\TakePhoto_exc" + str(loop+1) + ".png"
                common.SaveFailImg(cdevice,shotpath)
                print 'TakePhoto Exception Error: ',e
                traceback.print_exc()
                EnterCamera()
        else:
            shotpath = ImagePath + "\\Fail_entre_Camera_" + str(loop+1) + ".png"
            common.SaveFailImg(cdevice,shotpath)
    print 'Take Photo Test complete'
    return pic_num

#Open Photo
def OpenPhoto(times):
    global SucTimes
    
    for loop in range(times):
        if EnterCamera():
            try:
                EnterPreview()
                if not ceasy_device.visible(By.id('id/shutter_button_photo')):
                    print "Trace Success Loop " + str(loop+1)
                    SucTimes = SucTimes + 1
                else:
                    shotpath = ImagePath + "\\Fail_Open_photo" + str(loop+1) + ".png"
                    common.SaveFailImg(cdevice,shotpath)
            except Exception,e:
                shotpath = ImagePath + "\\OpenPhoto_exc" + str(loop+1) + ".png"
                common.SaveFailImg(cdevice,shotpath)
                print 'OpenPhoto Exception Error: ',e
                traceback.print_exc()
        else:
            shotpath = ImagePath + "\\Fail_entre_Camera_" + str(loop+1) + ".png"
            common.SaveFailImg(cdevice,shotpath)
    print 'Open Photo Test complete'

#Delete photo
def DelPhoto(times):
    global SucTimes
    
    for loop in range(times):
        if EnterCamera():
            EnterPreview()
            try:
                oldPhotoNumberjpg = GetFileNumber(sdcard,".jpg")
                oldPhotoNumber3gp = GetFileNumber(sdcard,".3gp")
                oldPhotoNumbermp4 = GetFileNumber(sdcard,".mp4")
                # delete
                SelectMenuItem()
                # confirm delete
                ceasy_device.touch(By.id('id/button1'), MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                # judge delete success
                nowPhotoNumberjpg = GetFileNumber(sdcard,".jpg")
                nowPhotoNumber3gp = GetFileNumber(sdcard,".3gp")
                nowPhotoNumbermp4 = GetFileNumber(sdcard,".mp4")
                if (nowPhotoNumberjpg + nowPhotoNumber3gp + nowPhotoNumbermp4) == (oldPhotoNumberjpg + oldPhotoNumber3gp + oldPhotoNumbermp4 - 1):
                    print "Delete picture"
                    SucTimes = SucTimes + 1
                    print "Trace Success Loop " + str(loop+1)
                else:
                    shotpath = ImagePath + "\\Fail_Delete_Pic" + str(loop+1) + ".png"
                    common.SaveFailImg(cdevice,shotpath)
            except Exception,e:
                shotpath = ImagePath + "\\DelPhoto_exc" + str(loop+1) + ".png"
                common.SaveFailImg(cdevice,shotpath)
                print 'DelPhoto Exception Error: ',e
                traceback.print_exc()
        else:
            shotpath = ImagePath + "\\Fail_enter_Camera_" + str(loop+1) + ".png"
            common.SaveFailImg(cdevice,shotpath)
    #common.BackToHome(cdevice)
    print 'Delete Photo Test complete'


#----------------------------------------------------------------
def RecordAudio(times):
    global SucTimes

    for loop in range(times):
        if EnterRecorder():
            currentnumber_3gpp = GetFileNumber(sdcardRecord,".3gpp")
            currentnumber_amr = GetFileNumber(sdcardRecord,".amr")
            currentnumber_m4a = GetFileNumber(sdcardRecord,".m4a")
            try:
                # Recording
                #add by jianke 04/04 001
                if common.GetWind_Id(chierarchyviewer,ceasy_device,id_name.Srecorder_App_ID,'id/recordButton',1,3,1,6):
                    MonkeyRunner.sleep(1)
                    print '99999999999999999 recordButton'
                    ceasy_device.touch(By.id('id/recordButton'),MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(3) 
                #end
                if not ceasy_device.visible(By.id('id/stateMessage2')):
                    shotpath = ImagePath + "\\Fail_Start_Record_Audio.png"
                    common.SaveFailImg(cdevice,shotpath)
                    return False
                else:
                    MonkeyRunner.sleep(5)
                    # Stop
                    ceasy_device.touch(By.id('id/stopButton'),MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(1)
                    #judge stopped
                    #add by jianke 07/09
                    stop_times = 0
                    while not ceasy_device.visible(By.id('id/acceptButton')):
                        MonkeyRunner.sleep(1)
                        stop_times = stop_times + 1
                        print 'stop delay ',stop_times
                    if True:
                        # Save
                        ceasy_device.touch(By.id('id/acceptButton'),MonkeyDevice.DOWN_AND_UP)
                        MonkeyRunner.sleep(1)
                        save_times = 0
                        while not ceasy_device.visible(By.id('id/fileListButton')):
                            MonkeyRunner.sleep(1)
                            save_times = save_times + 1
                            print 'save time ',save_times
                        # judge Saved
                        nowcurrentnumber_3gpp = GetFileNumber(sdcardRecord,".3gpp")
                        nowcurrentnumber_amr = GetFileNumber(sdcardRecord,".amr")
                        nowcurrentnumber_m4a = GetFileNumber(sdcardRecord,".m4a")
                        if (nowcurrentnumber_amr + nowcurrentnumber_3gpp + nowcurrentnumber_m4a) == (currentnumber_3gpp + currentnumber_amr + currentnumber_m4a + 1):
                            SucTimes = SucTimes + 1
                            print "Trace Success Record Audio"
                            print 'Record Audio Test complete'
                            return True
                        else:
                            shotpath = ImagePath + "\\Fail_Save_Record_Audio.png"
                            common.SaveFailImg(cdevice,shotpath)
                            return False
                    else:
                        shotpath = ImagePath + "\\Fail_Stop_Record_Audio.png"
                        common.SaveFailImg(cdevice,shotpath)
                        return False
            except Exception,e:
                shotpath = ImagePath + "\\RecordAudio_exc.png"
                common.SaveFailImg(cdevice,shotpath)
                print 'RecordAudio Exception Error: ',e
                traceback.print_exc()
                return False
        else:
            shotpath = ImagePath + "\\Fail_enter_Record_Audio.png"
            common.SaveFailImg(cdevice,shotpath)
            return False
    #common.BackToHome(cdevice)
    

def EnterRecorder():
    if not common.isEnterApp(ceasy_device,id_name.Srecorder_App_ID):
        print "Enter Sound Recorder"
        # Launch Sound Recorder And Wait
        return common.startapp(cdevice,ceasy_device,id_name.Srecorder_App_ID)
    else:
        print "It's already in the app."
        return True
    
#add by jianke 06/25
def EnterRecorderList():
    if not common.isEnterApp(ceasy_device,id_name.Srecorder_List_ID):
        print "Enter Sound RecorderList"
        # Launch Sound Recorder And Wait
        return common.startapp(cdevice,ceasy_device,id_name.Srecorder_List_ID)
    else:
        print "It's already in the app."
        return True
#end

#Play Back Audio
def EnterAudioList():
    print "Enter Audio List"
    ceasy_device.touch(By.id('id/fileListButton'),MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)

def SelectAudio(index,tType = None):
    list = common.GetNode(cdevice,chierarchyviewer,'id/recording_file_list_view')
    if list is None:
        raise TypeError,"Get Node FAIL"
    first_pos =  chierarchyviewer.getAbsoluteCenterOfView(list.children[index])
    if tType == "Long":
        cdevice.touch(first_pos.x,first_pos.y,MonkeyDevice.DOWN)
        MonkeyRunner.sleep(2)
        cdevice.touch(first_pos.x,first_pos.y,MonkeyDevice.UP)
    else:
        cdevice.touch(first_pos.x,first_pos.y,MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

def getCurrentTime():
    current_time = common.GetNode(cdevice,chierarchyviewer,'id/timerView')
    if current_time is None:
        raise TypeError,"Get Node FAIL"
    current_time_txt = chierarchyviewer.getText(current_time)
    print 'current_time_txt ',current_time_txt
    return current_time_txt
    
def PlayBackAudio(times):
    global SucTimes

    for loop in range(times):
        if EnterRecorderList():
            try:
                EnterAudioList()
                # Play Back The Audio
                SelectAudio(0)
                # judge start Playing  currentTime  totalTime  jianke 07/09
                paly_time = 0
                while True:
                    time1 = getCurrentTime()
                    MonkeyRunner.sleep(1)
                    paly_time = paly_time + 1
                    print 'paly_time ',paly_time
                    time2 = getCurrentTime()
                    if time2 == time1:
                        break
                if ceasy_device.visible(By.id('id/playButton')):
                    SucTimes = SucTimes + 1
                    print "Trace Success PlayBack Audio"
                else:
                    shotpath = ImagePath + "\\Fail_Start_Play_Audio.png"
                    common.SaveFailImg(cdevice,shotpath)
                '''
                current_time = common.GetNode(cdevice,chierarchyviewer,'id/currentTime')
                if current_time is None:
                    raise TypeError,"Get Node FAIL"
                current_time_txt = chierarchyviewer.getText(current_time)
                print 'current_time_txt ',current_time_txt
                total_time = common.GetNode(cdevice,chierarchyviewer,'id/totalTime')
                if total_time is None:
                    raise TypeError,"Get Node FAIL"
                total_time_txt = chierarchyviewer.getText(total_time)
                print 'total_time_txt ',total_time_txt
                audio_times = 0
                while current_time_txt != total_time_txt:
                    print "Trace Success Playing Audio..."
                    MonkeyRunner.sleep(2)
                    audio_times = audio_times + 1
                    print 'audio_times ',audio_times*2
                    current_time = common.GetNode(cdevice,chierarchyviewer,'id/currentTime')
                    if current_time is None:
                        raise TypeError,"Get Node FAIL"
                    current_time_txt = chierarchyviewer.getText(current_time)
                    print 'current_time_txt ',current_time_txt
                    if current_time_txt == total_time_txt:
                        SucTimes = SucTimes + 1
                        break
                '''
            except Exception,e:
                shotpath = ImagePath + "\\PlayBackAudio_exc.png"
                common.SaveFailImg(cdevice,shotpath)
                print 'PlayBackAudio Exception Error: ',e
                traceback.print_exc()
        else:
            shotpath = ImagePath + "\\Fail_enter_Play_Audio.png"
            common.SaveFailImg(cdevice,shotpath)
    # Return to idle
    #common.BackToHome(cdevice)
    print 'Play Back Audio Test complete'

#Delete Audio
def DelAudio(times):
    global SucTimes

    for loop in range(times):
        if EnterRecorderList():
            try:
                currentnumber_3gpp = GetFileNumber(sdcardRecord,".3gpp")
                currentnumber_amr = GetFileNumber(sdcardRecord,".amr")
                currentnumber_m4a = GetFileNumber(sdcardRecord,".m4a")
                EnterAudioList()
                # Delete The First Audio
                print "Delete Audio"
                SelectAudio(0,"Long")
                '''
                #add by jianke 06/25
                cdevice.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                ceasy_device.touchtext(By.id('id/title'),'Delete', MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                if common.GetWind_Id(chierarchyviewer,ceasy_device,id_name.Srecorder_List_ID,'id/recording_file_list_view',1,2,1,3):
                    file_list_Node = common.GetNode(cdevice,chierarchyviewer,'id/recording_file_list_view')
                    if file_list_Node is None:
                        raise TypeError,"Get Node FAIL"
                    file_list_num = file_list_Node.children.size()
                    print 'file_list_num ',file_list_num
                    file_list_One_Node = file_list_Node.children[0]
                    file_list_One_Node_Pos =  chierarchyviewer.getAbsoluteCenterOfView(file_list_One_Node)
                    print 'file_list_One_Node_Pos ',file_list_One_Node_Pos
                    cdevice.touch(file_list_One_Node_Pos.x,file_list_One_Node_Pos.y,MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(1)
                    #Delete
                #end
                '''
                ceasy_device.touch(By.id('id/deleteButton'),MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                # Confirm delete
                ceasy_device.touch(By.id('id/button1'),MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(1)
                nowcurrentnumber_3gpp = GetFileNumber(sdcardRecord,".3gpp")
                nowcurrentnumber_amr = GetFileNumber(sdcardRecord,".amr")
                nowcurrentnumber_m4a = GetFileNumber(sdcardRecord,".m4a")
                if (nowcurrentnumber_3gpp + nowcurrentnumber_amr + nowcurrentnumber_m4a) == (currentnumber_3gpp + currentnumber_amr + currentnumber_m4a - 1):
                    SucTimes = SucTimes + 1
                    print "Trace Success Delete Audio"
                else:
                    shotpath = ImagePath + "\\Fail_Delete_Audio.png"
                    common.SaveFailImg(cdevice,shotpath)
                #add by jianke 07/22
                cdevice.press('KEYCODE_BACK',MonkeyDevice.DOWN_AND_UP)
                MonkeyRunner.sleep(0.5)
                #end
            except Exception,e:
                shotpath = ImagePath + "\\DelAudio_exc.png"
                common.SaveFailImg(cdevice,shotpath)
                print 'DelAudio Exception Error: ',e
                traceback.print_exc()
        else:
            shotpath = ImagePath + "\\Fail_enter_Audio_del.png"
            common.SaveFailImg(cdevice,shotpath)
    #common.BackToHome(cdevice)
    print 'Delete Audio Test complete'

#--------------------------------------------------------
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

def EnterBrowser():
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
    return common.isEnterApp(ceasy_device,id_name.Browser_App_ID) or common.startapp(cdevice,ceasy_device,id_name.Browser_App_ID)

def TypeURL(straddress):
    width_w = int(str(width))
    width_w = width_w/2
    height_w = int(str(height))
    height_w = height_w/2
    width_w = int(width_w)
    height_w = int(height_w)
    urlNode = common.GetNode(cdevice,chierarchyviewer,'id/url')
    if urlNode is None:
        raise TypeError,"Get Node FAIL"
    urlPos =  chierarchyviewer.getAbsoluteCenterOfView(urlNode)
    if urlPos.y == 0:
        cdevice.drag((width_w,height_w),(width_w,height_w*2),0.2,10)
        MonkeyRunner.sleep(0.5)
    ceasy_device.type(By.id('id/url'),straddress)
    MonkeyRunner.sleep(3)
    cdevice.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(5)

#add by jianke
def TypeURL2(straddress):
    Maxtime = 0
    urlNode = common.GetNode(cdevice,chierarchyviewer,'id/url')
    if urlNode is None:
        raise TypeError,"Get Node FAIL"
    urlPos =  chierarchyviewer.getAbsoluteCenterOfView(urlNode)
    if urlPos.y == 0:
        cdevice.drag((150,150),(150,300),0.2,10)
        MonkeyRunner.sleep(0.5)
    ceasy_device.type(By.id('id/url'),straddress)
    MonkeyRunner.sleep(3)
    cdevice.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    #add by jianke 14/06/10
    if ceasy_device.visible(By.id('id/text1')):
    #end
        print 'enter choose Video player'
        ceasy_device.touchtext(By.id("id/text1"),'Video player', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        '''
        ceasy_device.touch(By.id('id/button_once'),MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(5)
        '''
    #add by jianke 05/13 id/movie_view_root
    while isLoading():
        MonkeyRunner.sleep(5)
        Maxtime = Maxtime + 1
        print 'Maxtime ',Maxtime*5
        if Maxtime > 5:
            break
    #end
#end
    
def isLoading():
    vRootNode = common.GetNode(cdevice,chierarchyviewer,"id/movie_view_root")
    if vRootNode is None:
        raise TypeError,"Get Node FAIL"   
    loadingNode = vRootNode.children[5].children[2].children[0]
    #For test 14/06/06
    loadingNode_name = loadingNode.name
    print 'loadingNode_name ',loadingNode_name
    #end
    if chierarchyviewer.visible(loadingNode):
        return True
    return False

def Streaming(times):
    global SucTimes
    
    MAXTime = 10
    for loop in range(times):
        if EnterBrowser():
            MonkeyRunner.sleep(2)
            # drag status bar 07/09
            width_w = int(str(width))
            width_w = width_w/2
            height_w = int(str(height))
            height_w = height_w/2
            width_w = int(width_w)
            height_w = int(height_w)
            cdevice.drag((width_w,height_w),(width_w,height_w*2),0.2,10)
            MonkeyRunner.sleep(0.5)
            try:
                TypeURL(id_name.STREAMADDRESS)
                MonkeyRunner.sleep(2)
                #add by jianke 07/22
                progress_times = 0
                while ceasy_device.visible(By.id('id/progress')):
                    MonkeyRunner.sleep(2)
                    progress_times = progress_times + 1
                    print 'progress_times ',progress_times*2
                    if progress_times > 10:
                        break
                #end
                maxtime = 0
                if ceasy_device.visible(By.id('id/alertTitle')):
                    if ceasy_device.getText(By.id('id/alertTitle')).find("Complete") > -1:
                        #jianke 1220
                        ceasy_device.touchtext(By.id("id/text1"), "Video player", MonkeyDevice.DOWN_AND_UP)
                        MonkeyRunner.sleep(1)
                        print "after sleep 1 second"
                        #ceasy_device.touch(By.id('id/button2'),MonkeyDevice.DOWN_AND_UP)
                        ceasy_device.touch(By.id('id/button_once'),MonkeyDevice.DOWN_AND_UP) 
                MonkeyRunner.sleep(3)
                print "before drug"
                cdevice.drag((width_w,height_w),(width_w,height_w*2),0.2,10)
                MonkeyRunner.sleep(2)
                cdevice.shell("input tap " + str(width_w) + ' ' + str(height_w))    
                data = cdevice.shell("dumpsys media.player")
                #add by jianke 07/22
                audio_data = cdevice.shell("dumpsys media.audio_flinger")
                router_data = cdevice.shell("dumpsys media_router")
                print 'data ' + str(data)
                print 'audio_data ' + str(audio_data)
                print 'router_data ' + str(router_data)
                #end
                if not data:
                    return None
                if not audio_data:
                    return None
                if not router_data:
                    return None
                while not(data.find("videoDimensions") > -1 and (data.find("active(1)") > -1 or data.find('AwesomePlayer') > -1)):
                    print "The streaming is loading... ",maxtime
                    #add by jianke 03/30 001 
                    if not (data.find("msec per frame") > -1 and data.find("Track 2") > -1):
                        print 'gotooooooooooooooo'
                        cdevice.shell("input tap " + str(width_w) + ' ' + str(height_w))
                    #end
                    #add by jianke 07/22 
                    if audio_data.find('Normal frame count') > -1:
                        print 'get the audio ... '
                        break
                    if router_data.find('mRunning=true') > -1:
                        print 'get the router data ... '
                        break
                    #end
                    maxtime = maxtime + 1
                    if maxtime > MAXTime:
                        break
                    MonkeyRunner.sleep(2)
                    data = cdevice.shell("dumpsys media.player")
                    print 'data2 ' + str(data)
                    #add by jianke 07/22
                    audio_data = cdevice.shell("dumpsys media.audio_flinger")
                    print 'audio_data2 ' + str(audio_data)
                    router_data = cdevice.shell("dumpsys media_router")
                    print 'router_data2 ' + str(router_data)
                    #end
                    
                if maxtime > MAXTime:
                    shotpath = ImagePath + "\\Fail_PalyStreaming_" + str(loop+1) + ".png"
                    common.SaveFailImg(cdevice,shotpath)
                else:
                    SucTimes = SucTimes + 1
                    print "Trace Success Loop " + str(loop+1)
                    MonkeyRunner.sleep(10)
                    cdevice.press('KEYCODE_BACK',MonkeyDevice.DOWN_AND_UP)
                    MonkeyRunner.sleep(0.5)
            except Exception,e:
                shotpath = ImagePath + "\\Streaming_exc" + str(loop+1) + ".png"
                common.SaveFailImg(cdevice,shotpath)
                print 'Streaming Exception Error: ',e
                traceback.print_exc()
        # Return to idle
        common.BackToHome(cdevice)
    print 'Trace Streaming Test complete'

#-------------------------------------------------------------
def EnterMusic():
    # Launch Music Player And Wait
    print "Enter music and wait"
    #add by jianke 07/10
    if project_name == 'yaris35_ATT': 
        return common.isEnterApp(ceasy_device,id_name.Music_App_ID) or common.startapp(cdevice,ceasy_device,id_name.Music_App_ID)
    else:
        print 'other project come here!!'
        return common.isEnterApp(ceasy_device,id_name.Music_New_ID) or common.startapp(cdevice,ceasy_device,id_name.Music_New_ID)


def ExitMusic():
    cdevice.press('KEYCODE_HOME',MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    
def OpenClosePlayer(times):
    global SucTimes

    for loop in range(times):
        try:
            # start Musicplayer
            if not EnterMusic():
                print 'Stat music player Failed'
                shotpath = ImagePath + "\\Fail_Open_Close_Player_" + str(loop+1) + ".png"
                common.SaveFailImg(cdevice,shotpath)
                continue
            else:
                MonkeyRunner.sleep(3)
                ExitMusic()
                text = chierarchyviewer.getFocusedWindowName()
                if text != id_name.Launcher_Andr_ID:
                    print 'Open and Close music player Failed'
                    shotpath = ImagePath + "\\Fail_Open_Close_Player_" + str(loop+1) + ".png"
                    common.SaveFailImg(cdevice,shotpath)
                else:
                    SucTimes = SucTimes + 1
                    print "Trace Success Loop " + str(loop + 1)
        except Exception,e:
            shotpath = ImagePath + "\\OpenClosePlayer_exc_" + str(loop+1) + ".png"
            common.SaveFailImg(cdevice,shotpath)
            print 'OpenClosePlayer Exception Error: ',e
            traceback.print_exc()

#Play Music
def SelectOneMusic(index,flag=None):
    #add by jianke 0204
    width_w = int(str(width))
    width_w = width_w/2
    height_w = int(str(height))
    height_w = height_w/2
    width_w = int(width_w)
    height_w = int(height_w)
    cdevice.drag((width_w,height_w),(width_w,height_w*2),0.2,10)
    MonkeyRunner.sleep(1)
    if flag == 'OLD':
        view_page = common.GetNode(cdevice,chierarchyviewer,'id/viewpage')
        if view_page is None:
            raise TypeError,"Get Node FAIL"
        content_node = common.GetNode(cdevice,chierarchyviewer,'id/content',view_page.children[0].children[0])
        if content_node is None:
            raise TypeError,"Get Node FAIL"
        main_music_list = common.GetNode(cdevice,chierarchyviewer,'id/mainLayout',content_node)
        if main_music_list is None:
            raise TypeError,"Get Node FAIL"
    else:
        print 'enter new feature ... '
        main_music_list = common.GetNode(cdevice,chierarchyviewer,'id/mainLayout')
        if main_music_list is None:
            raise TypeError,"Get Node FAIL"
    # select one music
    music_list = common.GetNode(cdevice,chierarchyviewer,'id/list',main_music_list.children[0])
    if music_list is None:
        raise TypeError,"Get Node FAIL"
    MonkeyRunner.sleep(1)
    print "select music ",index
    music_pos =  chierarchyviewer.getAbsoluteCenterOfView(music_list.children[index])
    print "press ",music_pos
    #add by jianke 0214 begin  because of four page
    x_pos = music_pos.x
    while x_pos<0:
        x_pos = x_pos + width_w*2
    #add by jianke 0214 end
    cdevice.touch(x_pos,music_pos.y, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    
				
def PlayMusic(times):
    global SucTimes
    
    width_w = int(str(width))
    width_w = width_w/2
    height_w = int(str(height))
    height_w = height_w/2
    width_w = int(width_w)
    height_w = int(height_w)
    
    if EnterMusic():
        #add by jianke 07/10
        if project_name == 'yaris35_ATT':
            print "Change To Song Tab"
            ceasy_device.touch(By.id('id/songtab'), MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(3)
            #for up to down paly 07/10
            cdevice.drag((width_w,height_w),(width_w,height_w*2),0.2,10)
            MonkeyRunner.sleep(0.5)
            for loop in range(times):
                try:
                    index = loop % 5
                    print '-----------',index             
                    SelectOneMusic(index)
                    MonkeyRunner.sleep(2)
                    #jianke 07/10
                    if id_name.MediaPlay_ID != chierarchyviewer.getFocusedWindowName():
                        print 'Open music file Failed'
                        shotpath = ImagePath + "\\Fail_Play_Music_" + str(loop+1) + ".png"
                        common.SaveFailImg(cdevice,shotpath)
                    else:
                        MonkeyRunner.sleep(8)
                        SucTimes = SucTimes + 1
                        print "Trace Success Loop " + str(loop + 1)
                        ceasy_device.touch(By.id('id/pause'),MonkeyDevice.DOWN_AND_UP)
                        MonkeyRunner.sleep(1)
                        cdevice.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
                        MonkeyRunner.sleep(2)
                except Exception,e:
                    shotpath = ImagePath + "\\PlayMusic_exc_" + str(loop+1) + ".png"
                    common.SaveFailImg(cdevice,shotpath)
                    print 'PlayMusic Exception Error: ',e
                    traceback.print_exc()
        else:
            print 'other project come here!!!'
            print "Choose first array All"
            #add by jianke 06/25 001 id/library_music
            library_music_node = common.GetNode(cdevice,chierarchyviewer,'id/library_music')
            if library_music_node is None:
                raise TypeError,"Get Node FAIL"
            print 'library_music_node size ',library_music_node.children.size()
            library_music_One_node = library_music_node.children[0]
            library_music_One_node_pos = chierarchyviewer.getAbsoluteCenterOfView(library_music_One_node)
            cdevice.touch(library_music_One_node_pos.x,library_music_One_node_pos.y,MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            enter_times = 0
            while not chierarchyviewer.getFocusedWindowName() == id_name.Music_Track_ID:
                MonkeyRunner.sleep(1)
                enter_times = enter_times + 1
                print 'enter_times ',enter_times
                if enter_times > 3:
                    break
            #end
            for loop in range(times):
                try:
                    index = loop % 5
                    print '-----------',index             
                    SelectOneMusic(index)
                    MonkeyRunner.sleep(2)
                    #add by jianke 06/25
                    if WhetherPlay():
                        MonkeyRunner.sleep(8)
                        SucTimes = SucTimes + 1
                        print "Trace Success Loop " + str(loop + 1)
                        ceasy_device.touch(By.id('id/play_icon'),MonkeyDevice.DOWN_AND_UP)
                        MonkeyRunner.sleep(1)
                    else:
                        print 'Open music file Failed'
                        shotpath = ImagePath + "\\Fail_Play_Music_" + str(loop+1) + ".png"
                        common.SaveFailImg(cdevice,shotpath)
                    #end      
                except Exception,e:
                    shotpath = ImagePath + "\\PlayMusic_exc_" + str(loop+1) + ".png"
                    common.SaveFailImg(cdevice,shotpath)
                    print 'PlayMusic Exception Error: ',e
                    traceback.print_exc()

#add by jianke 06/25
def WhetherPlay():
    play_icon_node = common.GetNode(cdevice,chierarchyviewer,'id/play_icon')
    if play_icon_node is None:
        print "play_icon_node is none."
        play_icon_node_img = cdevice.takeSnapshot()
        shotpath = ImagePath + "\\play_icon_node_img.png"
        common.SaveFailImg(cdevice,shotpath)
        return False
    play_icon_node_pos = chierarchyviewer.getAbsolutePositionOfView(play_icon_node)
    rect = (play_icon_node_pos.x,play_icon_node_pos.y,play_icon_node.width,play_icon_node.height)
    new_all_img = cdevice.takeSnapshot()
    if new_all_img is None:
        print "Image is none."
        return False
    #try RasterFormatException
    try:
        sub_new_img = new_all_img.getSubImage(rect)
        #test to catch 06/25
        #savepath = ImagePath + "\\play_icon_node_test_img.png"
        #sub_new_img.writeToFile(savepath, 'png')
        #end
    except:
        print "RasterFormatException."
        return False
    if common.CompareImage(sub_new_img,scriptpath2):
        return True
    else:
        return False
#end
                
#Close Musicplayer
def CloseMusicPlayer(times):
    global SucTimes

    for loop in range(times):
        try:
            ExitMusic()
            text = chierarchyviewer.getFocusedWindowName()
            #jianke 07/09
            if text != id_name.Launcher_Andr_ID:
                print 'Close music player Failed'
                shotpath = ImagePath + "\\Fail_Close_Play_Music.png"
                common.SaveFailImg(cdevice,shotpath)
            else:
                SucTimes = SucTimes + 1
                print "Trace Success Close Music Player"
        except Exception,e:
            shotpath = ImagePath + "\\CloseMusicPlayer_exc.png"
            common.SaveFailImg(cdevice,shotpath)
            print 'CloseMusicPlayer Exception Error: ',e
            traceback.print_exc()

#add by jianke 03/10
def showFiles(path,name):
    content = cdevice.shell("ls " + path)
    num = content.count(name)
    print name,"num is",num
    return num

def rmFloder(path,name):
    numa = showFiles(path,name)
    depath = path + name
    if numa>0:
        for i in range(numa+1):
            cdevice.shell("rm -rf " + depath)
    numb = showFiles(path,name)
    if numb == 0:
        print 'rm',name,'File'
    else:
        print 'failed delete',name
#end

def main():
    global ImagePath

    time_Start = common.timeCalc()
    print 'Start Multi-Media Test'
    # Create Folders To Save Imgs Of Result
    ImagePath = common.CreateFolder('5.1.7')
    common.ShowDeviceMemoryInfo(cdevice)
    # Return to idle
    common.BackToHome(cdevice)

    #add by jianke 03/10
    '''
    cameraPath = "/storage/sdcard1/DCIM/"
    cameraName = "Camera"
    rmFloder(cameraPath,cameraName)
    '''
    #end

    if True:
        print "Record video 30s"
        if Recordvideo(VIDEOTIMES):
            print "Play Back video"
            PlayBackvideo2(VIDEOTIMES)
            print "Delete video"
            Delvideo(VIDEOTIMES)

    if True:
        print "Take Photo " + str(PHOTOTIMES) + " Times"
        number = TakePhoto(PHOTOTIMES)
        print "Open Photo " + str(PHOTOTIMES) + " Times"
        OpenPhoto(PHOTOTIMES)
        print "Del Photo " + str(number) + " Times"
        DelPhoto(number)

    if True:
        print "Record Audio 5s"
        if RecordAudio(AUDIOTIMES):
            print "Play Back Audio"
            PlayBackAudio(AUDIOTIMES)
            print "Delete Audio"
            DelAudio(AUDIOTIMES)

    if True:
        print "Play Streaming " + str(STREAMTIMES) + " Times"
        Streaming(STREAMTIMES)
    
    if True:
        print "Open And Close Musicplayer " + str(OPENCLOSETIMES) + " Times"
        OpenClosePlayer(OPENCLOSETIMES)

    if True:
        print "Play Music " + str(MUSICPLAYTIMES) + " Times"
        PlayMusic(MUSICPLAYTIMES)
        print "Close Musicplayer"
        CloseMusicPlayer(EXITPLAYTIMES)
    
    common.BackToHome(cdevice)

    print "Finished Multi-Media Test"
    common.ShowDeviceMemoryInfo(cdevice)
    
    print "Success Times: ",SucTimes
    Rate = SucTimes/TestTimes*100
    if Rate < 95:
        print 'Result Fail Success Rate Is ' + str(Rate) + '%'
    else:
        print 'Result Pass Success Rate Is ' + str(Rate) + '%'
    timeEnd = common.timeCalc()
    totalTime = timeEnd - time_Start
    print '5.1.07_Multi-Media time = ' + str(totalTime) + 'mins'
    
if __name__ == "__main__":
    main()
#  Scrpit End
