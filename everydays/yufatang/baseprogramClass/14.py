# coding: utf-8
"""
    @author: zhangjk
    @file: 14.py
    @date: 2020-02-29
    说明：xxxx
"""
import pickle

from django import db


class Course(db.Model):
    dept_code = db.StringProperty()
    number = db.IntegerProperty()
    title = db.StringProperty()
    raw_pre_reqs = db.StringProperty(multiline=True)
    original_description = db.StringProperty()

    def getPreReqs(self):
        return pickle.loads(str(self.raw_pre_reqs))

    def __repr__(self):
        title_msg = self.title if self.title else "Untitled"
        return "%s %s: %s" % (self.dept_code, self.number, title_msg)

    def __attrs(self):
        return (self.dept_code, self.number, self.title, self.raw_pre_reqs, self.original_description)

    def __eq__(self, other):
        return isinstance(other, Course) and self.__attrs() == other.__attrs()

    def __hash__(self):
        return hash(self.__attrs())
