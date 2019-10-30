#!/usr/bin/env python
# coding: utf8
# author: Mess
# createTime: 2019-09-02 16:58:56
# updateTime: 2019-10-22 10:52:11

import os
import time
import random

# 模拟滑动
def initlocal():
    time.sleep(2)   # 滑动前休息2秒，避免网络不好
    os.system('.\\adb.exe shell input swipe 900 1200 900 500')  # 模拟从下往上滑动
    time.sleep(2)   # 滑动后休息2秒，避免开始计时延迟

# 返回上一页面
def goback():
    os.system('.\\adb.exe shell input keyevent KEYCODE_BACK')  # 返回


def shopping():
    #多两次避免已逛过该店
    for i in range(1, 21):
        print('===== 逛*****店({}/18) ======'.format(i))
        os.system('.\\adb.exe shell input tap 900 1620')   # 进入逛店
        initlocal()
        print('进入店铺，浏览中，请等待 16 秒')
        time.sleep(16)
        goback()
        time.sleep(1)
    print('已完成逛店任务')
    
def task1():
    print('====== 浏览主会场 ======')
    os.system('.\\adb.exe shell input tap 900 1150')   # 点击去浏览
    initlocal()
    print('进入主会场，浏览中，请等待 16 秒')
    time.sleep(16)
    goback()
    print('已完成浏览主会场任务')
    print('====== 浏览其他会场 ======')
    for i in range(1, 4):
        os.system('.\\adb.exe shell input tap 900 1300')   # 点击去浏览1
        time.sleep(2)   # 滑动前休息2秒，避免网络不好
        initlocal()
        print('进入会场，浏览中，请等待 16 秒')
        time.sleep(16)
        goback()

def task2():
    print('====== 浏览会场 ======')
    # for i in range(1, 4):
    os.system('.\\adb.exe shell input tap 900 1500')   # 点击去浏览
    time.sleep(2)   # 滑动前休息2秒，避免网络不好
    initlocal()
    print('进入会场，浏览中，请等待 16 秒')
    time.sleep(16)
    goback()
    print('已完成浏览会场任务')
    print('====== 浏览其他会场 ======')
    for i in range(1, 4):
        os.system('.\\adb.exe shell input tap 900 1600')   # 点击去浏览1
        time.sleep(2)   # 滑动前休息2秒，避免网络不好
        initlocal()
        print('进入会场，浏览中，请等待 16 秒')
        time.sleep(16)
        goback()
 
os.system('.\\adb.exe shell input tap 900 1700')   # 点击领喵币，弹出任务菜单
time.sleep(1)
task1()
task2()
os.system('.\\adb.exe shell input swipe 900 1600 900 1200')    # 下拉任务列表
time.sleep(1)
shopping()
print('全部任务已完成')
os.system("pause")
