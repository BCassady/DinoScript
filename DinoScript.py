import pyautogui
import time
import PIL.ImageGrab
PIL.ImageGrab.grab().size
start = time.time()
time.sleep(1)
pyautogui.click()
xChanged1 = True
xChanged2 = True
x = 380
y = 654
y2 = 559    
testVar = 0
testVar2 = 0
white = True
pyautogui.moveTo(x, y)
while(time.time()-start<240):
    if(time.time()-start>17 and xChanged1):
        x += 120
        testVar = 100
        pyautogui.moveTo(x, y)
        xChanged1 = False
    if(time.time()-start>35 and xChanged2):
        x += 100
        testVar2 = 200
        pyautogui.moveTo(x, y)
        xChanged2 = False
    image = PIL.ImageGrab.grab().load()
    if(image[24,138][0]<122):
        if(image[x, y][0]>150 or image[x-10, y][0]>150 or image[x-20, y][0]>150 or image[x+10, y][0]>150 or image[x+20, y][0]>150 or image[x-50, y][0]>150 or image[x-testVar, y][0]>150 or image[x-testVar2, y][0]>150):
            pyautogui.press('up')
        if(image[x, y2][0]>150 or image[x-10, y2][0]>150 or image[x-20, y2][0]>150 or image[x+10, y2][0]>150 or image[x+20, y2][0]>150 or image[x-50, y2][0]>150 or image[x-testVar, y2][0]>150 or image[x-testVar2, y2][0]>150):
            pyautogui.keyDown('down')
            keyDown = time.time()
            while(time.time()-keyDown<0.5):
                continue
            pyautogui.keyUp('down')
    else: 
        if(image[x, y][0]<150 or image[x-10, y][0]<150 or image[x-20, y][0]<150 or image[x+10, y][0]<150 or image[x+20, y][0]<150  or image[x-50, y][0]<150 or image[x-testVar, y][0]<150 or image[x-testVar2, y][0]<150):
            pyautogui.press('up')
        if(image[x, y2][0]<150 or image[x-10, y2][0]<150 or image[x-20, y2][0]<150 or image[x+10, y2][0]<150 or image[x+20, y2][0]<150 or image[x-50, y2][0]<150 or image[x-testVar, y2][0]<150 or image[x-testVar2, y2][0]<150):
            pyautogui.keyDown('down')
            keyDown = time.time()
            while(time.time()-keyDown<0.5):
                continue
            pyautogui.keyUp('down')