# Documentação pyautoGUI
# https://pyautogui.readthedocs.io/en/latest/install.html


import pyautogui
import time

pyautogui.alert('O código vai começar, Não mexa em nada!')
pyautogui.PAUSE = 2.5

# fe
pyautogui.press('winleft')
pyautogui.write('onedrive')
pyautogui.press('enter')

# chaves = pyautogui.KEYBOARD_KEYS
# print(chave)

# entrando na area de trabalho
pyautogui.hotkey('winleft', 'd')

# posição do mouse
# print(pyautogui.position()) # descobrir a posição onde está seu mouse

# pyautogui.position()
pyautogui.moveTo(x=727, y=529)

# Precionando botão do mouse esquerdo
pyautogui.mouseDown()

# movendo arquivo
pyautogui.moveTo(x=869, y=361)
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.mouseUp()

pyautogui.alert('Terminou')
