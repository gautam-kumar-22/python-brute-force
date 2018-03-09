import itertools
import time

import pyautogui

Alphabet = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_.!@#$")

CharLength = 1
MAX_LENGTH = 4
for Index in range(100000):
    passwords = (itertools.product(Alphabet, repeat = Index))
    for i in passwords:
        if(len(i)) > MAX_LENGTH-1:
            i = str(i)
            i = i.replace("[", "")
            i = i.replace("]", "")
            i = i.replace("'", "")
            i = i.replace(" ", "")
            i = i.replace(",", "")
            i = i.replace("(", "")
            i = i.replace(")", "")
            pyautogui.typewrite(i)
            pyautogui.keyDown("enter")
            pyautogui.keyUp("enter")
        Index += 1
