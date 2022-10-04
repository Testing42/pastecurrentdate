from datetime import date
import pyperclip as pc
import pyautogui

now = date.today()

date = now.strftime("%m/%d/%y")

pc.copy(date)
pyautogui.click()
pc.paste(date)

