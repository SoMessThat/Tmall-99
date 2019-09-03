#!/usr/bin/env python
# coding: utf8
# author: Mess 2019-09-02 16:58:56

import os
import time
import random

# 初始化上个页面位置
def initlocal():
    os.system('adb shell input swipe 900 500 900 800')  # 从上往下滑动，回到页面初始位置
    os.system('adb shell input tap 900 1670')   # 点击小聚星任务，弹出任务菜单


# 返回上一页面
def goback():
    os.system('adb shell input keyevent KEYCODE_BACK')  # 返回


def task1():
    print('===== 聚划算店铺 ======')
    for i in range(1, 51):
        initlocal()
        print('第 {} 次去逛店'.format(i))
        time.sleep(1)
        os.system('adb shell input tap 900 1500')   # 聚划算店铺
        rtime = random.randint(12, 15)  # 随机等待12-15秒
        print('进入店铺，浏览中，请等待 {} 秒'.format(rtime))
        time.sleep(rtime)
        goback()
        time.sleep(1)
    print('已完成聚划算店铺任务')
    
def task2():
    print('====== 逛天猫预售主会场 ======')
    initlocal()
    time.sleep(1)
    os.system('adb shell input tap 900 1188')   # 点击去浏览
    print('进入会场，浏览中，请等待 13 秒')
    time.sleep(13)
    goback()
    time.sleep(1)
    print('已完成逛天猫预售主会场任务')
    print('====== 逛聚划算预售主会场 ======')
    initlocal()
    print('第 1 次去浏览')
    time.sleep(1)
    os.system('adb shell input tap 900 1350')   # 点击去浏览1
    print('进入会场，浏览中，请等待 13 秒')
    time.sleep(13)
    goback()
    time.sleep(1)
    print('已完成逛聚划算预售主会场任务')

def task3():
    print('====== 逛天天特卖频道（1/2） ======')
    initlocal()
    time.sleep(1)
    os.system('adb shell input tap 900 1600')   # 点击去浏览
    print('进入天天特卖频道，浏览三个商品')
    time.sleep(1)
    os.system('adb shell input swipe 900 900 900 100')   # 下滑
    time.sleep(1)
    print('点击第一个商品')
    os.system('adb shell input tap 290 700')   # 点击第一个商品
    time.sleep(1)
    goback()
    print('点击第二个商品')
    os.system('adb shell input tap 290 1000')   # 点击第二个商品
    time.sleep(1)
    goback()
    print('点击第三个商品')
    os.system('adb shell input tap 290 1700')   # 点击第三个商品
    time.sleep(1)
    goback()
    print('完成第一个任务，现在返程')
    time.sleep(1)
    goback()
    time.sleep(1)
    initlocal()
    time.sleep(1)
    print('====== 摇摇钱树（2/2） ======')
    os.system('adb shell input tap 900 1600')   # 点击去浏览
    time.sleep(1)
    os.system('adb shell input tap 800 1300')   # 点击摇一摇
    time.sleep(1)
    goback()
    time.sleep(1)
    goback()
    
def task4():
    print('====== 查看南北PK情况 ======')
    time.sleep(1)
    for i in range(1, 7):
        initlocal()
        print('第{}次查看南北PK情况'.format(i))
        time.sleep(1)
        os.system('adb shell input tap 900 1800')   # 点击去浏览
        print('进入情况，浏览中，请等待 13 秒')
        time.sleep(13)
        goback()
        time.sleep(1)
    print('查看南北PK情况任务')
 
 
task2()
task3()
task4()
task1()
print('全部任务已完成')
