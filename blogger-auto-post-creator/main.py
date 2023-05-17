from dotenv import load_dotenv
from time import sleep
import pyautogui
import pyperclip
import os


load_dotenv()

LOCAL_PATH = os.getcwd()
os.chdir(LOCAL_PATH)

BLOG_LINK = os.environ["BLOG_LINK"]
screen_position_x = screen_position_y = 0
post_number = 1
post_limit_number = 100


def search_target(image_path, log_message=""):
	retryTime = 2

	if log_message != "":
		print(log_message)

	while True:
		sleep(1)
		try:
			return pyautogui.locateCenterOnScreen(image_path)
			break
		except Exception as e:
			print(f"{e}. Retrying in {retryTime} seconds")
			sleep(retryTime)
			retryTime += 2

pyautogui.hotkey("win","1")
search_target("images/firefox-window-icon.png", "Aguarde, carregando Firefox...")
pyautogui.hotkey("ctrl","n")
search_target("images/new-tab.png", "Aguarde, carregando nova aba...")
pyautogui.typewrite(BLOG_LINK)
pyautogui.hotkey("enter")
search_target("images/blog-loaded.png", "Aguarde, blogger carregando...")
screen_position_x, screen_position_y = search_target("images/new-post.png", "Procurando botão para novo post...")
pyautogui.click(screen_position_x, screen_position_y)

while post_number <= post_limit_number:
	print(f"Criando novo post: Post número {post_number}")
	post_title = "Mangá " + str(post_number).zfill(2)
	pyperclip.copy(post_title)
	retryTime = 0

	while True:
		try:
			screen_position_x, screen_position_y = pyautogui.locateCenterOnScreen("images/new-post.png")
			pyautogui.click(screen_position_x, screen_position_y)
			sleep(1)
			pyautogui.locateOnScreen("images/return-button.png")
			screen_position_x, screen_position_y = pyautogui.locateCenterOnScreen("images/empty-title-post.png")
			pyautogui.click(screen_position_x, screen_position_y)
			break
		except Exception:
			print(f"Tentando novamente em {retryTime} segundos")
			sleep(retryTime)
			retryTime += 2

	post_number += 1
	pyautogui.hotkey("ctrl", "v")
	search_target("images/title-updated.png", "Página criada com sucesso")
	sleep(2.5)
	pyautogui.hotkey("alt", "left")
