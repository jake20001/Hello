# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/7/9 14:16
# FileName : imgvideo
# Description : 
# --------------------------------


import cv2
import glob
import os
from datetime import datetime

scriptspath = os.path.dirname(__file__)

imagepath = os.path.join(scriptspath,'imagesave')

def frames_to_video(fps, save_path, frames_path):
    # XVID
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    videoWriter = cv2.VideoWriter(save_path, fourcc, fps, (1920, 720))
    imgs = glob.glob(frames_path + "/*.jpg")
    frames_num = len(imgs)
    for i in range(1,frames_num+1):
        if os.path.isfile("%s/%d.jpg"%(frames_path, i)):
            frame = cv2.imread("%s/%d.jpg"%(frames_path, i))
            videoWriter.write(frame)
    videoWriter.release()
    return


if __name__ == '__main__':
    t1 = datetime.now()
    frames_to_video(23.9, "result.mp4", imagepath)
    t2 = datetime.now()
    print("Time cost = ", (t2 - t1))
    print("SUCCEED !!!")
