import pyautogui, time

for _ in range(4):
    server_click = (1324, 798)
    server_delete = (1351, 1009)
    server_confirm_delete = (1243, 409)
    idle_position = (1398, 594)

    pyautogui.moveTo(idle_position)
    pyautogui.scroll(-100)

    pyautogui.moveTo(server_click)
    pyautogui.click()

    pyautogui.moveTo(server_delete)
    pyautogui.click()

    pyautogui.moveTo(server_confirm_delete)
    pyautogui.click()

