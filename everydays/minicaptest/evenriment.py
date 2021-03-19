# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/7/9 10:14
# FileName : evenriment
# Description : 
# --------------------------------
import os
import re
import time

scriptspath = os.path.dirname(__file__)


utilspath = os.path.join(scriptspath,'utils')

class Everiment(object):

    def __init__(self,utilspath):
        self.utilspath = utilspath

    def push_data_local_tmp(self):
        # push  minicap  /data/local/tmp
        sorminicap = os.path.join(self.utilspath,'minicap')
        sorminicapso = os.path.join(self.utilspath,'minicap.so')
        s1 = os.popen('adb push ' + sorminicap + ' /data/local/tmp').read()
        s2 = os.popen('adb push ' + sorminicapso + ' /data/local/tmp').read()
        # print('s1',s1,'s2',s2)
        return (s1,s2)

    def chmod_minicap(self):
        # chmod 755 /data/local/tmp/minicap
        local_minicap = '/data/local/tmp/minicap'
        local_minicapso = '/data/local/tmp/minicap.so'
        c1 = os.popen('adb shell chmod 755 ' + local_minicap).read()
        c2 = os.popen('adb shell chmod 755 ' + local_minicapso).read()
        print('c1',c1,'c2',c2)

    # adb shell ls -l /data/local/tmp/minicap | busybox awk '{print $1}'
    def check_chomd(self,mode,file):
        md = {mode:'rwxr-xr-x'}
        m1 = os.popen('adb shell "ls -l /data/local/tmp/%s | busybox awk \'{print $1}\'"' %(file)).read()
        # print(m1)
        if m1.find(md[mode])!=-1:
            return True
        return False

    def repattern(self,iline):
        pattern = r'.*file pushed.*skipped.*'
        result = re.findall(pattern,iline)
        # print(result)
        return result

    # 建立连接  adb forward tcp:1313 localabstract:minicap
    def create_connection(self,port):
        cc = os.popen('adb forward tcp:' + port + ' localabstract:minicap').read()
        print(cc,type(cc))
        return cc

    def check_tcp_port(self,port):
        cc = os.popen('adb forward --list').read()
        print('cc',cc)
        pattern = r'tcp:(\d{4}).*'
        resp = re.findall(pattern,cc)
        print(resp)
        if resp[0]==port:
            return True
        return False


    def get_window_size(self):
        size = os.popen('adb shell wm size').read()
        lc_w_size = size.split(':')[1].strip('\n').strip()
        print(lc_w_size)
        return lc_w_size

    # adb shell LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/minicap -P 1920x720@1920x720/0
    def get_window_idle(self,lc_w_size):
        cc = os.popen('adb shell LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/minicap -P %s@%s/0'%(lc_w_size,lc_w_size)).read()
        print(cc,type(cc))
        if len(cc):
            return True
        return False


    def init_condition(self):
        ss = self.push_data_local_tmp()
        r1 = self.repattern(ss[0])
        r2 = self.repattern(ss[1])
        # print(r1)
        # print(r2)
        isOK = False
        for i in range(5):
            if r1 and r2:
                isOK = True
                break
            time.sleep(1)
        # 给权限
        if not isOK:
            return
        print("OKKKKK")
        self.chmod_minicap()
        isChmod1 = self.check_chomd(755,'minicap')
        isChmod2 = self.check_chomd(755,'minicap.so')
        if not (isChmod1 and isChmod2):
            return
        print("OKKKKKK2222")
        # 建立车机和PC连接; 检查port
        port = '1313'
        rep = self.create_connection(port)
        if not (rep==port or self.check_tcp_port(port)):
            return
        print("OKKKKK33333")
        sz = self.get_window_size()
        if self.get_window_idle(sz):
            print("Init OK")
        else:
            print("Init FAIL")


def main():
    mEveriment = Everiment(utilspath)
    mEveriment.init_condition()





if __name__ == '__main__':
    main()




