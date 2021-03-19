# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2021/1/15 20:28
# FileName : day1.1
# Description : 
# --------------------------------

class Node(object):

    def __init__(self,data):
        self.data = data
        self.next = None
        self.pre = None


class Ring(object):

    def __init__(self,node):
        self.node = node
        node.next = node
        self.cot = set()

    def add_next_node(self,node):
        self.node.next = node
        node.pre = self.node
        self.node = node

    def visit(self,root,nodes_list,length):
        print(root.data)
        index = list(root.data.values())[0]
        if len(nodes_list)==1:
            print(nodes_list[0].data)
            return nodes_list
        nodes_list.remove(root)
        if index%2==0:
            self.remove_cur_node(root)
            # self.cot.remove(root)
        else:
            length = length+1
            root.data = {list(root.data.keys())[0]:length}
            nodes_list.append(root)
        self.visit(root.next,nodes_list,length)


    def remove_cur_node(self,node):
        print("remove",node.data)
        node.next.pre = node.pre
        node.pre.next = node.next



def main():
    nodes_list = []
    list_all = [{1:1},{2:2},{3:3},{4:4},{5:5}]
    begin_node = Node(list_all[0])
    mRing = Ring(begin_node)
    nodes_list.append(begin_node)

    for i in range(1,len(list_all)):
        node2 = Node(list_all[i])
        mRing.add_next_node(node2)
        nodes_list.append(node2)

    mRing.add_next_node(begin_node)
    mRing.visit(begin_node,nodes_list,len(list_all))


if __name__ == '__main__':
    main()