import pyautogui

pyautogui.PAUSE = 2.5
pyautogui.moveTo(0, 1)

pyautogui.hotkey('winleft', 'r', interval=0.1)
pyautogui.typewrite('cmd\n')
pyautogui.typewrite('py -3.8\n')
pyautogui.typewrite('import pyautogui\n')
pyautogui.typewrite('pyautogui.displayMousePosition()\n')
