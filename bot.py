from PIL import ImageGrab,ImageOps
import pyautogui
import time
from numpy import *

class Coordinates():
    replayBtn = (383,343)
    dinosaur = (175,388)
    #298,387 top left
    #334,434 bottom right
    #to jum x 286
    #lowest y 408

def restartGame():
    pyautogui.click(Coordinates.replayBtn)

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("Jump")

#restartGame()
#time.sleep(1)
#pressSpace()

def imageGrab():
    box = (Coordinates.dinosaur[0]+40,Coordinates.dinosaur[1],Coordinates.dinosaur[0]+80,Coordinates.dinosaur[1]+30 )
    image = ImageGrab.grab(box)
    grayimage = ImageOps.grayscale(image)
    a = array(grayimage.getcolors())
    print(a.sum())
    return a.sum()

def main():
    restartGame()
    while True:
        if(imageGrab()!=1447):
            pressSpace()
            time.sleep(0.1)

main()