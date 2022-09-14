import time
import pyautogui
import random

def sendInput():
   keys = ['w', 'a', 's', 'd', 'space']
   time.sleep(5)
   while True:
        rand_0_4 = random.randint(0, 4) #Chooses what key that gets pressed
        rand_0_1 = random.uniform(0, 1) #Chooses how long the key should be pressed (0-1 seconds)
        rand_wait = random.uniform(1, 670) #Chooses when the key will be pressed (between 1-670 seconds)
        print(keys[rand_0_4]) #Printing data
        pyautogui.keyDown(keys[rand_0_4]) #press down key
        print(rand_0_1) #Printing data
        time.sleep(rand_0_1) #Time it uses from press to release of button
        pyautogui.keyUp(keys[rand_0_4]) #Release key
        print(rand_wait) #Printing data
        time.sleep(rand_wait) #How long it waits before pressing down a new key
sendInput()
