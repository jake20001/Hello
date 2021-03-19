# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/5 16:37
# FileName : day7.2
# Description : 
# --------------------------------
import logging


class DB(object):

    def _query(self,query,type,logger):
        logger('done')

    def execute(self,query,logger=logging.info):
        self._query(query,'EXECUTE',logger)


# DB().execute('my query')

DB().execute('my query',logging.warning)