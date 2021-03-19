# coding: utf-8
"""
    @author: zhangjk
    @file: monkeyrunnertest.py
    @date: 2020-02-29
    说明：monkeyrunner
"""

import os,sys
crruntpath = sys.path[0]
axpath = crruntpath.split(':')

scriptspath = axpath[1] + ':' + axpath[2]

from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
from com.android.monkeyrunner.easy import EasyMonkeyDevice
from com.android.monkeyrunner.easy import By

# device=MonkeyRunner.waitForConnection()
# device.startActivity(component="com.yftech.vehiclecenter/com.yftech.vehiclecenter.ui.MainActivity")
# result = device.takeSnapshot()
# result.writeToFile(os.path.join(scriptspath,'opennote.png'),'png')

def ConnectClientDevice():
    device=MonkeyRunner.waitForConnection(5,'1912119056000004')
    hierarchyviewer=device.getHierarchyViewer()
    easy_device=EasyMonkeyDevice(device)
    return device,hierarchyviewer,easy_device


def isExitId(device,hierarchyviewer,easy_device):
    while True:
        # call_time_node = hierarchyviewer.findViewById('id/call_page_time_txt')
        # if call_time_node==None:
        #     print('call_time_node')
        call_page_hangup_id = hierarchyviewer.findViewById('id/call_page_hangup')
        if call_page_hangup_id!=None:
            easy_device.touch(By.id('id/call_page_hangup'),MonkeyDevice.DOWN_AND_UP)
            MonkeyRunner.sleep(1)
            print("call_page_hangup_id")
            break
        # 无法定位到call log点(89, 125)
        device.touch(90,125,MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)

        # flow_calling_bg_id = hierarchyviewer.findViewById('id/flow_calling_bg')
        # if flow_calling_bg_id!=None:
        #     easy_device.touch(By.id('id/flow_calling_bg'),MonkeyDevice.DOWN_AND_UP)
        #     MonkeyRunner.sleep(1)
        #     print("flow_calling_bg_id")
    print("Hang up OK")




def main():
    device,hierarchyviewer,easy_device = ConnectClientDevice()
    isExitId(device,hierarchyviewer,easy_device)




if __name__ == '__main__':
    main()

