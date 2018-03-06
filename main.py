import itertools
import time

import pyautogui

Alphabet = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_.@#!$")

CharLength = 1

for Index in range(25):
    passwords = (itertools.product(Alphabet, repeat = Index))
	if len(i) > 5:
        for i in passwords:
            i = str(i)
            i = i.replace("[", "")
            i = i.replace("]", "")
            i = i.replace("'", "")
            i = i.replace(" ", "")
            i = i.replace(",", "")
            i = i.replace("(", "")
            i = i.replace(")", "")
            pyautogui.typewrite(i)
        Index += 1
