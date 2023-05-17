import pyautogui
from time import sleep

def search_target(image_path):
	retryTime = 2
	while True:
		try:
			pyautogui.locateCenterOnScreen(image_path)
			break
		except Exception as e:
			print(f"{e}. Retrying in {retryTime} seconds")
			sleep(retryTime)
			retryTime += 2

def target_to_click(image_path):
	retryTime = 2
	while True:
		try:
			screen_position_x, screen_position_y = pyautogui.locateCenterOnScreen(image_path)
			pyautogui.click(screen_position_x, screen_position_y)
			break
		except Exception as e:
			print(f"{e}. Retrying in {retryTime} seconds")
			sleep(retryTime)
			retryTime += 2