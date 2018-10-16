# -*- coding: UTF-8 -*-
import pyautogui as pag
import time
import ConfigParser
import string

def  partOne(cfg):
    '''新建模拟器'''
    print("create a new simulator")
    moveToX=int(cfg.get("新建模拟器", "moveToX"))
    moveToY=int(cfg.get("新建模拟器", "moveToY"))
    pag.mouseDown(x=moveToX, y=moveToY, button='left')
    pag.mouseUp(x=moveToX, y=moveToY, button='left')
    '''模拟器版本选择'''
    print("simulator Version ")
    moveToX=int(cfg.get("模拟器版本选择", "moveToX"))
    moveToY=int(cfg.get("模拟器版本选择", "moveToY"))
    pag.mouseDown(x=moveToX, y=moveToY, button='left')
    pag.mouseUp(x=moveToX, y=moveToY, button='left')
    t =  int(cfg.get("模拟器版本选择", "time"))
    time.sleep(t)
    '''模拟器设置'''
    print("Settings")
    moveToX=int(cfg.get("模拟器设置", "moveToX"))
    moveToY=int(cfg.get("模拟器设置", "moveToY"))
    pag.mouseDown(x=moveToX, y=moveToY, button='left')
    pag.mouseUp(x=moveToX, y=moveToY, button='left')
    t = int(cfg.get("模拟器设置", "time"))
    time.sleep(t)
    '''分辨率选择'''
    print("resolutions")
    moveToX=int(cfg.get("分辨率选择", "moveToX"))
    moveToY=int(cfg.get("分辨率选择", "moveToY"))
    pag.mouseDown(x=moveToX, y=moveToY, button='left')
    pag.mouseUp(x=moveToX, y=moveToY, button='left')
    time.sleep(0.5)
    '''选择手机模式'''
    print("Phone sheet")
    moveToX=int(cfg.get("选择手机模式", "moveToX"))
    moveToY=int(cfg.get("选择手机模式", "moveToY"))
    pag.mouseDown(x=moveToX, y=moveToY, button='left')
    pag.mouseUp(x=moveToX, y=moveToY, button='left')
    time.sleep(0.5)
    '''保存设置'''
    print("save")
    moveToX=int(cfg.get("保存设置", "moveToX"))
    moveToY=int(cfg.get("保存设置", "moveToY"))
    pag.mouseDown(x=moveToX, y=moveToY, button='left')
    pag.mouseUp(x=moveToX, y=moveToY, button='left')
    time.sleep(0.5)
    '''确定'''
    print("OK")
    moveToX=int(cfg.get("确定", "moveToX"))
    moveToY=int(cfg.get("确定", "moveToY"))
    pag.mouseDown(x=moveToX, y=moveToY, button='left')
    pag.mouseUp(x=moveToX, y=moveToY, button='left')
    t = int(cfg.get("确定", "time"))
    time.sleep(t)
def partTwo(cfg):
    '''启动模拟器'''
    print("starting a simulator")
    moveToX=int(cfg.get("启动模拟器", "moveToX"))
    moveToY=int(cfg.get("启动模拟器", "moveToY"))
    pag.doubleClick(x=moveToX, y=moveToY,interval=0.2, button='left')
    t = int(cfg.get("启动模拟器", "time"))
    time.sleep(t)
    '''进入主页面'''
    print("Home page")
    moveToX=int(cfg.get("进入主页面", "moveToX"))
    moveToY=int(cfg.get("进入主页面", "moveToY"))
    pag.mouseDown(x=moveToX, y=moveToY, button='left')
    pag.mouseUp(x=moveToX, y=moveToY, button='left')
    t = int(cfg.get("进入主页面", "time"))
    time.sleep(t)
    '''将app拖入模拟器中进行安装'''
    print("drag app to simulator")
    srcX = int(cfg.get("将app拖入模拟器中进行安装", "srcX"))
    srcY = int(cfg.get("将app拖入模拟器中进行安装", "srcY"))
    pag.moveTo(srcX, srcY, duration=0.25)
    dstX = int(cfg.get("将app拖入模拟器中进行安装", "dstX"))
    dstY = int(cfg.get("将app拖入模拟器中进行安装", "dstY"))
    pag.dragTo(dstX,dstY,5)
    t = int(cfg.get("将app拖入模拟器中进行安装", "time"))
    time.sleep(t)
    '''app位置'''
    print("app position")
    moveToX=int(cfg.get("app位置", "moveToX"))
    moveToY=int(cfg.get("app位置", "moveToY"))
    pag.doubleClick(x=moveToX, y=moveToY,interval=0.2, button='left')
    t = int(cfg.get("app位置", "time"))
    time.sleep(t)
    '''双击deny'''
    print("double click deny")
    moveToX=int(cfg.get("双击deny", "moveToX"))
    moveToY=int(cfg.get("双击deny", "moveToY"))
    pag.doubleClick(x=moveToX, y=moveToY,interval=0.3, button='left')
    t = int(cfg.get("双击deny", "time"))
    time.sleep(t)

    '''随机关键词'''
    print("random key words")
    moveToX=int(cfg.get("随机关键词", "moveToX"))
    moveToY=int(cfg.get("随机关键词", "moveToY"))
    pag.mouseDown(x=moveToX, y=moveToY, button='left')
    pag.mouseUp(x=moveToX, y=moveToY, button='left')
    '''点击广告'''
    print("click ad")
    moveToX=int(cfg.get("点击广告", "moveToX"))
    moveToY=int(cfg.get("点击广告", "moveToY"))
    pag.mouseDown(x=moveToX, y=moveToY, button='left')
    pag.mouseUp(x=moveToX, y=moveToY, button='left')
    t = int(cfg.get("点击广告", "time"))
    time.sleep(t)
    '''点击其中的一个广告'''
    print("click a ad")
    moveToX=int(cfg.get("点击其中的一个广告", "moveToX"))
    moveToY=int(cfg.get("点击其中的一个广告", "moveToY"))
    pag.doubleClick(x=moveToX, y=moveToY,interval=0.2, button='left')
    time.sleep(1)
    '''浏览广告--滚轮'''
    print("browser ad")
    moveToX=int(cfg.get("浏览广告--滚轮", "moveToX"))
    moveToY=int(cfg.get("浏览广告--滚轮", "moveToY"))
    pag.moveTo(moveToX, moveToY, duration=0.05)
    for i in range(20):
        amount_to_scroll = -1200
        pag.scroll(clicks=amount_to_scroll, x=moveToX, y=moveToY)
        time.sleep(1)
    for i in range(20):
        amount_to_scroll = 1200
        pag.scroll(clicks=amount_to_scroll, x=moveToX, y=moveToY)
        time.sleep(1)

def partThree(cfg):
    '''关闭模拟器'''
    print("close simulator")
    moveToX=int(cfg.get("关闭模拟器", "moveToX"))
    moveToY=int(cfg.get("关闭模拟器", "moveToY"))
    pag.doubleClick(x=moveToX, y=moveToY, button='left')
    time.sleep(1)
    '''确定关闭模拟器'''
    print("close simulator")
    moveToX=int(cfg.get("确定关闭模拟器", "moveToX"))
    moveToY=int(cfg.get("确定关闭模拟器", "moveToY"))
    pag.mouseDown(x=moveToX, y=moveToY, button='left')
    pag.mouseUp(x=moveToX, y=moveToY, button='left')
    t = int(cfg.get("确定关闭模拟器", "time"))
    time.sleep(t)
    '''删除镜像'''
    print("delete the image")
    moveToX=int(cfg.get("删除镜像", "moveToX"))
    moveToY=int(cfg.get("删除镜像", "moveToY"))
    pag.mouseDown(x=moveToX, y=moveToY, button='left')
    pag.mouseUp(x=moveToX, y=moveToY, button='left')
    '''确定删除镜像'''
    print("OK")
    moveToX=int(cfg.get("确定删除镜像", "moveToX"))
    moveToY=int(cfg.get("确定删除镜像", "moveToY"))
    pag.mouseDown(x=moveToX, y=moveToY, button='left')
    pag.mouseUp(x=moveToX, y=moveToY, button='left')
if __name__ == '__main__':
    print("hello world")
    config = ConfigParser.ConfigParser()
    config.read("./app1.ini")
    '''启动延时'''
    t = int(config.get("start", "time"))
    print("staring------")
    time.sleep(t)
    partOne(config)
    partTwo(config)
    partThree(config)
    print("finished------")