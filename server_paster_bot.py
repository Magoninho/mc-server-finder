# This script will automatically click on the screen to add the servers to minecraft
# Place minecraft window on the right side of a 1920x1080 monitor
# I know it's very inefficient, but it's fun to see 
# (and I don't know how to edit the servers.dat file in .minecraft)

import pyautogui
import time
import keyboard

with open("open_servers.txt", 'r') as f:
	servers = f.read().splitlines()

time.sleep(3)

for i in range(30):
	pyautogui.moveTo(1628, 955)
	pyautogui.click()

	pyautogui.moveTo(x=1357, y=263)
	pyautogui.click()

	pyautogui.typewrite(servers[i])

	pyautogui.moveTo(x=1531, y=529)
	pyautogui.click()

	if keyboard.is_pressed('b'):
		print("coisou")
		exit()