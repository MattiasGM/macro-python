
import time
import pyautogui

pyautogui.hotkey('winleft', '0')
time.sleep(1)
pyautogui.hotkey('ctrlleft', '2')
time.sleep(5)
pyautogui.hotkey('tab')
time.sleep(1)

while True:
    locate1 = pyautogui.locateOnScreen('img1.png', confidence=0.9)
    while (locate1 == None):
        locate1 = pyautogui.locateOnScreen('img1.png', confidence=0.9)

    time.sleep(1)
    pyautogui.hotkey('enter')

    locate2 = pyautogui.locateOnScreen('img2.jpeg', confidence=0.9)  
    while (locate2 == None):
        locate2 = pyautogui.locateOnScreen('img2.jpeg', confidence=0.9) 
    
    time.sleep(1)
    pyautogui.hotkey('ctrlleft', 'w')  