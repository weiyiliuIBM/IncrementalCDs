# coding: utf-8

import sys, os

def LPA(filename):
    # 功能:
    #   LPA 社团发现算法的Wrapper
    # 输入: 
    #   filename --- 需要进行社团发现的网络名称 
    # 输出:
    #   <输出到文件> filename.com --- 社团发现的结果
    os.system("./LPA %s"%filename) # --- 此为最简单的方案 ^_^



# JUST FOR TEST
filename = "2004-04"
LPA(filename)