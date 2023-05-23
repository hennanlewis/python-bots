from datetime import datetime
import pyautogui
import os
from dotenv import load_dotenv
load_dotenv()

BLOG_LINKS = os.environ["BLOG_LINKS"]
LOCAL_PATH = os.getcwd()
os.chdir(LOCAL_PATH)
interval_time = 0.25

def log(log_message): print(f"{datetime.now()} - {log_message}")

def select_browser():
	print()
	while True:
		try:
			browser_options = ["firefox", "edge"]
			print("Qual navegador você usa: ")
			print("1 - Firefox")
			print("2 - Microsoft Edge")
			selected = int(input())
			return browser_options[selected-1]
		except Exception:
			print("\nOcorreu algum erro. Tente novamente.")

def select_blog_link():
	print()
	while True:
		try:
			blog_options = BLOG_LINKS.split(",")
			print("Entre com o número correspondente ao blog: ")
			print("1 - Denki 1")
			print("2 - Denki 2")
			print("3 - Denki 3")
			selected = int(input(""))
			return blog_options[selected-1]
		except Exception:
			print("\nOcorreu algum erro. Tente novamente.")

def chapter_values():
	print()
	while True:
		try:
			post_number = int(input("Entre com o número do primeiro capítulo: "))
			post_limit_number = int(input("Entre com o número do último capítulo: "))
			return post_number, post_limit_number
		except Exception:
			print("\nOcorreu algum erro. Tente novamente.")


def open_browser(browser_name):
	log("Abrindo navegador...")
	pyautogui.hotkey("win")
	pyautogui.typewrite(browser_name, interval=0.03)
	pyautogui.hotkey("backspace", "enter")

def search_image_position(path, region):
	return pyautogui.locateCenterOnScreen(path, region=region)

def search_new_tab(path, blog_link):
	log("Procurando \"Nova aba\"...")
	while True:
		selected_position = search_image_position(f"{path}/new-tab.png", (0, 0, 300, 50))
		if selected_position is not None:
			log("Abrindo link...")
			pyautogui.typewrite(blog_link, interval=0.01)
			pyautogui.hotkey("enter")
			return

def load_blogger(path):
	log("Carregando Blogger...")
	while True:
		selected_position = search_image_position(f"{path}/blogger.png", (0, 0, 300, 50))
		if selected_position is not None:
			log("Blogger carregado")
			return

def click_position(selected_position):
	pyautogui.click(selected_position, duration=interval_time)

def rename_title(click_position):
	pyautogui.click(click_position, duration=interval_time)
	pyautogui.hotkey("ctrl", "v")

