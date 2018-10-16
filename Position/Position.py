# -*- coding: UTF-8 -*-
import pyautogui as pag
import time
def getCurrentPosition():
    currentMouseX, currentMouseY = pag.position()
    positionStr = 'currentMouseX: ' + str(currentMouseX) + ' currentMouseY: ' + str(currentMouseY) + '\n'
    return positionStr
if __name__ == '__main__':
    print('Press q to quit.')
    for i in range(1000):
        positionStr = getCurrentPosition()
        print(positionStr)
        time.sleep(1)