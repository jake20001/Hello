# coding: utf-8
"""
    @author: zhangjk
    @file: md5test.py
    @date: 2019-09-27
    说明：MD5
"""
import hashlib
import json
import os
import time
import zipfile

scriptspath = os.path.dirname(__file__)
gzipslog = os.path.join(scriptspath,'gzips')
ungziplog = os.path.join(scriptspath,'ungzips')
myjsonlog = os.path.join(scriptspath,'myjson')

class MD5Test(object):

    def __init__(self):
        pass

    # 打包 gzip
    def zip_dir(self,dirname,zipfilename):
        filelist = []
        if os.path.isfile(dirname):
            filelist.append(dirname)
        else:
            for root, dirs, files in os.walk(dirname):
                for name in files:
                    filelist.append(os.path.join(root, name))

        zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
        for tar in filelist:
            arcname = tar[len(dirname):]
            #print arcname
            zf.write(tar,arcname)
        zf.close()

    # 解包 gzip
    def unzip_file(self,zipfilename, unziptodir):
        if not os.path.exists(unziptodir):
            os.mkdir(unziptodir, '0777')
        zfobj = zipfile.ZipFile(zipfilename)
        for name in zfobj.namelist():
            name = name.replace('\\','/')

            if name.endswith('/'):
                os.mkdir(os.path.join(unziptodir, name))
            else:
                ext_filename = os.path.join(unziptodir, name)
                ext_dir = os.path.dirname(ext_filename)
                if not os.path.exists(ext_dir):
                    os.mkdir(ext_dir,'0777')
                outfile = open(ext_filename, 'wb')
                outfile.write(zfobj.read(name))
                outfile.close()

    # 加密方式
    def encryption(self,mypath,KeyEncry):
        if KeyEncry=='md5':
            value = hashlib.md5(open(mypath,'rb').read()).hexdigest()
        elif KeyEncry=='sha-1':
            value = hashlib.sha1(open(mypath,'rb').read()).hexdigest()
        elif KeyEncry=='sha-256':
            value = hashlib.sha256(open(mypath,'rb').read()).hexdigest()
        elif KeyEncry=='sha-512':
            value = hashlib.sha512(open(mypath,'rb').read()).hexdigest()
        else:
            value = "请输入正确的加密algorithm"
        return value


class JsonTest(object):

    def __init__(self):
        pass

    # 格式化成2016-03-20-11-45-39形式
    def get_format_now_time(self):
        return time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())

    # 把词典写入json
    def produceJson(self):
        test_dict = {'bigberg': [7600, {'timestamp':self.get_format_now_time(),1: [['iPhone', 6300], ['Bike', 800], ['shirt', 300]]}]}
        # dumps 将数据转换成字符串
        json_str = json.dumps(test_dict)
        # loads: 将 字符串 转换为 字典
        new_dict = json.loads(json_str)
        # dump: 将数据写入json文件中
        with open(os.path.join(myjsonlog,'j1.json'),"w") as f:
            json.dump(new_dict,f)
            print("加载入文件完成...")

    # 分析新json，生成新的json
    def newJson(self):
        with open(os.path.join(myjsonlog,'j1.json'),'r') as load_f:
            load_dict = json.load(load_f)
            print(load_dict)
            print(type(load_dict))
        # 增加某个项
        # load_dict['smallberg'] = [8200,{1:[['Python',81],['shirt',300]]}]
        # print(load_dict)

        # 删除timestamp项
        load_dict['bigberg'][1].pop('timestamp')
        print(load_dict)

        with open(os.path.join(myjsonlog,'new_j1.json'),"w") as dump_f:
            json.dump(load_dict,dump_f)



def main():
    mMD5Test = MD5Test()
    # mygzip = os.path.join(scriptspath,'mylog.gzip')
    mygzip2 = os.path.join(scriptspath,'mylog2.gzip')
    # # mMD5Test.zip_dir(gzipslog,mygzip)
    # 打包gzip
    mMD5Test.zip_dir(gzipslog,mygzip2)
    # # 解包gzip
    # mMD5Test.unzip_file(mygzip,ungziplog)
    # # mygzip md5
    # value = mMD5Test.encryption(mygzip,'md5')
    # print(value)
    # # mygzip2 md5
    # value2 = mMD5Test.encryption(mygzip2,'md5')
    # print(value2)
    # print(value2==value)
    # mJsonTest = JsonTest()
    # mJsonTest.produceJson()
    # mJsonTest.newJson()

if __name__ == '__main__':
    main()