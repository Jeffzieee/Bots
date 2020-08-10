#NOTE!!! This code is for 1080p resolution screen and web browser as half screen

from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *


class Cordinates():
    #All the coordinates mentioned in the code is only for 1080p resolution screen, yours may vary depending on screen resolution, use snipping tool \
    #to take a screenshot and use paint.net to find the resolution
    restartBtn = (480, 400) #Coordinates for replay Button
    dino = (246, 405) #Coorinates of dino
    # x = 320 (cordinate to check for tree)
    # y = 415 (cordinate of half tree


def restart():
    pyautogui.click(Cordinates.restartBtn)

def Jump():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print('Jump')
    pyautogui.keyUp('space')

def Box():
    box = (Cordinates.dino[0]+74,Cordinates.dino[1],Cordinates.dino[0]+100,Cordinates.dino[1]+30) #Coordinates of the box
    img = ImageGrab.grab(box)
    grayImg = ImageOps.grayscale(img)
    arr = array(grayImg.getcolors())
    return arr.sum()

def main():
    restart()
    while True:
        if(Box()!=1027):
            Jump()
            time.sleep(0.1)

main()