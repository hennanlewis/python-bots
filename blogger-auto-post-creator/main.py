from datetime import datetime
from dotenv import load_dotenv
from time import sleep
import pyautogui
import pyperclip
import os

load_dotenv()
LOCAL_PATH = os.getcwd()
os.chdir(LOCAL_PATH)

browser_options = ["firefox", "edge"]
print("Qual navegador você usa: ")
print("1 - Firefox")
print("2 - Microsoft Edge")
selected = int(input())
selected_browser = browser_options[selected-1]


blog_options = [""]

print("\nEntre com o número correspondente ao blog: ")
print("1 - Denki 1")
print("2 - Denki 2")
print("3 - Denki 3")
selected = int(input(""))
selected_blog = blog_options[selected-1]


post_number = int(input("Entre com o número do primeiro capítulo: "))
post_limit_number = int(input("Entre com o número do último capítulo: "))


screen_width, screen_height = pyautogui.size()
interval_time = 0.25
pyautogui.PAUSE = interval_time
screen_width, scr = pyautogui.size()
path = f"images/{selected_browser}"
selected_position = None

def log(log_message): print(f"{datetime.now()} - {log_message}")

locateCenterOnScreen = pyautogui.locateCenterOnScreen
typewrite = pyautogui.typewrite
hotkey = pyautogui.hotkey
click = pyautogui.click

print()
log("Iniciando o robô")
log("Abrindo navegador...")
pyautogui.hotkey("win")

pyautogui.typewrite(selected_browser, interval=0.03)
pyautogui.hotkey("backspace", "enter")

log("Procurando \"Nova aba\"...")
while True:
	selected_position = pyautogui.locateCenterOnScreen(f"{path}/new-tab.png", region=(0, 0, 300, 50))
	if selected_position is not None:
		log("Abrindo link")
		image_position = selected_position
		pyautogui.typewrite(selected_blog, interval=0.03)
		pyautogui.hotkey("enter")
		selected_position = None
		break

log("Carregando Blogger...")
while True:
	selected_position = pyautogui.locateCenterOnScreen(f"{path}/blogger.png", region=(0, 0, 300, 50))
	if selected_position is not None:
		selected_position = None
		break

while post_number <= post_limit_number:
	post_title = "Mangá " + str(post_number).zfill(2)
	pyperclip.copy(post_title)
	retryTime = 0
	preview_retry_time = retryTime
	option = 0

	while True:
		selected_position = pyautogui.locateCenterOnScreen(f"{path}/new-tab.png", region=(0, 0, 300, 50))
		if selected_position is not None:
			log("Retornando a página")
			image_position = selected_position
			pyautogui.hotkey("alt", "right")
			selected_position = None

		selected_position = pyautogui.locateCenterOnScreen(f"{path}/new-post.png", region=(0, 120, 300, 150))
		if selected_position is not None:
			log(f"Iniciando novo post...")
			image_position = selected_position
			pyautogui.click(image_position, duration=interval_time)
			retryTime += 2
			selected_position = None
			option = 1

		selected_position = pyautogui.locateCenterOnScreen(f"{path}/edit-post.png", region=(0, 0, 300, 50))
		if selected_position is not None and option == 1:
			log(f"Criando novo post: Post {post_number}")
			image_position = selected_position
			selected_position = None
			option = 2

		selected_position = pyautogui.locateCenterOnScreen(f"{path}/empty-title.png", region=(0, 100, 60, 130))
		if selected_position is not None and option == 2:
			log("Renomeando título...")
			image_position = selected_position
			pyautogui.click(image_position, duration=interval_time)
			pyautogui.hotkey("ctrl", "v")
			selected_position = None
			option = 3

		region = (screen_width-370, 90, 100, 130)
		selected_position = pyautogui.locateCenterOnScreen(f"{path}/edited-post.png", region=region)
		if selected_position is not None and option == 3:
			log("Post renomeado")
			selected_position = None
			option = 4

		selected_position = pyautogui.locateCenterOnScreen(f"{path}/return.png", region=(0, 80, 70, 40))
		if selected_position is not None and option == 4:
			log("Retornando às postagens")
			image_position = selected_position
			pyautogui.click(image_position, duration=interval_time)
			selected_position = None
			break

		if retryTime != preview_retry_time:
			log(f"Tentando novamente em {retryTime} segundos")
			preview_retry_time = retryTime
			sleep(retryTime)

	log(f"{post_title} inserido com sucesso!")
	post_number += 1

log("Automação chegou ao fim")