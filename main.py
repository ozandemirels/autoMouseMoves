import pyautogui
import time
from random import randint
from random import uniform

'''pyautogui.moveTo(5,176)
pyautogui.moveTo(1908,990)
'''

time.sleep(3)
a = 0
b = 0

for i in range(5,56):
    x = randint(5,1908)
    y = randint(176,990)
    if((abs(x-a)+abs(y-b))<666):
        z = uniform(0.00,0.33)
        print(str(z) +" in way 1")
    elif((abs(x-a)+abs(y-b))<1332):
        z=uniform(0.33,0.66)
        print(str(z) + " in way 2")
    else:
        z=uniform(0.66,1)
        print(str(z) +" in way 3")

    pyautogui.moveTo(x,y,z)
    pyautogui.click()
    a = x
    b = y
    time.sleep(3)
