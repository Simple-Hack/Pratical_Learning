# -*- coding:utf-8 -*-

import copy     # 注意对象的深拷贝和浅拷贝的使用！！！
import numpy as np
class GameNode:
    '''博弈树结点数据结构
    成员变量：
    map - list[[]] 二维列表，三子棋盘状态
    val - int  该棋盘状态对执x棋子的评估值，1表示胜利，-1表示失败，0表示平局
    deepID - int 博弈树的层次深度，根节点deepID=0
    parent - GameNode，父结点
    children - list[GameNode] 子结点列表
    '''
    def __init__(self, map, val=0, deepID=0, parent=None, children=[]):
        self.map = map
        self.val = val
        self.deepID = deepID
        self.parent = parent
        self.children = children

class GameTree:
    '''博弈树结点数据结构
    成员变量：
    root - GameNode 博弈树根结点
    成员函数：
    buildTree - 创建博弈树
    '''
    def __init__(self, root):
        self.root = root                # GameNode 博弈树根结点

    def buildTree(self, root):
        '''递归法创建博弈树
        参数：
        root - GameNode 初始为博弈树根结点
        '''
        #请在这里补充代码，完成本关任务
        #********** Begin **********#
        if self.isTerminal(root):
            return
        for i in range(3):
            for j in range(3):
                if root.map[i][j]=='_':
                    new_map=copy.deepcopy()
        
        

            

        #********** End **********#

class MinMax:
    '''博弈树结点数据结构
    成员变量：
    game_tree - GameTree 博弈树
    成员函数：
    minmax - 极大极小值算法，计算最优行动
    max_val - 计算最大值
    min_val - 计算最小值
    get_val - 计算某棋盘状态中:执x棋子的评估值，1表示胜利，-1表示失败，0表示平局
    isTerminal - 判断某状态是否为最终状态:无空闲棋可走
    '''
    def __init__(self, game_tree):
        self.game_tree = game_tree      # GameTree 博弈树

    def minmax(self, node):
        '''极大极小值算法，计算最优行动
        参数：
        node - GameNode 博弈树结点
        返回值：
        clf - list[map] 最优行动，即x棋子的下一个棋盘状态GameNode.map
              其中，map - list[[]] 二维列表，三子棋盘状态
        '''
        #请在这里补充代码，完成本关任务
        #********** Begin **********#


        #********** End **********#


    def max_value(self, node):
        '''计算最大值
        参数：
        node - GameNode 博弈树结点
        返回值：
        clf - int 子结点中的最大的评估值
        '''
        #请在这里补充代码，完成本关任务
        #********** Begin **********#
        if self.isTerminal(node):
            return self.get_value(node)
        res=-114514
        for chi in node.children:
            res=max(res,self.min_value(chi))

        #********** End **********#


    def min_value(self, node):
        '''计算最小值
        参数：
        node - GameNode 博弈树结点
        返回值：
        clf - int 子结点中的最小的评估值
        '''
        #请在这里补充代码，完成本关任务 
        #********** Begin **********#
        if self.isTerminal(node):
            return self.get_value(node)
        res=114514
        for chi in node.children:
            res=min(res,self.max_value(chi))
        return res

        #********** End **********#


    def get_value(self, node):
        '''计算某棋盘状态中:执x棋子的评估值，1表示胜利，-1表示失败，0表示平局
        参数：
        node - GameNode 博弈树结点
        返回值：
        clf - int 执x棋子的评估值，1表示胜利，-1表示失败，0表示平局
        '''
        #请在这里补充代码，完成本关任务
        #********** Begin **********#
        

        #********** End **********#


    def isTerminal(self, node):
        '''判断某状态是否为最终状态:无空闲棋可走
        参数：
        node - GameNode 博弈树结点
        返回值：
        clf - bool 是最终状态，返回True，否则返回False
        '''
        #请在这里补充代码，完成本关任务
        #********** Begin **********#
        array=node.map
        def row_and_col_check(row):
            data_1=array[row][0]
            if data_1!='_' and all([array[row][i]==data_1 for i in range(1,3)]):
                return True
            data_2=array[0][row]
            if data_2!='_' and all([node[i][row]== data_2 for i in range(1,3)]):
                return True
            return False

        def lean_check():
            if array[0][0]!='_' and array[0][0]==array[1][1]==array[2][2]:
                return True
            if array[0][2]==array[1][1]==array[2][0]:
                return True
            return False
        
        if any([row_and_col_check(i) for i in range(0,3)]) or lean_check():
            return True
        
        return False

        #********** End **********#

