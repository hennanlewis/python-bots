from datetime import datetime
from dotenv import load_dotenv
from time import sleep
import pyautogui
import pyperclip
import cv2
import os

load_dotenv()
LOCAL_PATH = os.getcwd()
os.chdir(LOCAL_PATH)


browser_options = ["firefox", "edge", "edge-dark"]
print("Qual navegador você usa: ")
print("1 - Firefox")
print("2 - Edge")
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

intervaltime = 1
pyautogui.PAUSE = intervaltime
screen_width, scr = pyautogui.size()
path = f"images/{selected_browser}"

def search_image(image_path, log_message="", validate=False, x0=0, y0=0, width=screen_width, height=350):
	log(log_message)
	retryTime = 0
	return locateOnScreen(image_path, validate, retryTime, x0, y0, width, height)


def log(log_message):
	print(f"{datetime.now().time()} - {log_message}")


def locateOnScreen(image_path, validate, retryTime, x0, y0, width, height):
	sleep(retryTime)
	if validate is False:
		return image_match(image_path, x0, y0, width, height)

	try:
		return image_match(image_path, x0, y0, width, height)
	except Exception as e:
		log(f"{e}. Retrying in {retryTime} seconds")
		retryTime += 2
		locateOnScreen(image_path, validate, retryTime, x0, y0, width, height)

def image_match(image_path, x0, y0, width, height):
	screenshot = pyautogui.screenshot(region=(x0, y0, width, height))
	screenshot.save("screenshot.png")
	total_frame = cv2.imread("screenshot.png")
	section_img = cv2.imread(image_path)
	result = cv2.matchTemplate(total_frame, section_img, cv2.TM_CCOEFF_NORMED)

	_, _, _, position = cv2.minMaxLoc(result)
	left, top = position

	log(f"Encontrado a {left}px da esquerda e {top}px do topo")
	center_x = left + width/2
	center_y = top + height/2
	return (center_x, center_y)


log("")
pyautogui.hotkey("win","1")

pyautogui.locateOnScreen(f"{path}/browser-window-icon.png")

pyautogui.hotkey("ctrl","n")
search_image(f"{path}/new-tab.png", "Abrindo nova aba", width=200, height=80, validate=True)

sleep(1)
pyautogui.typewrite(selected_blog)
pyautogui.hotkey("enter")
search_image(f"{path}/blog-loaded.png", "Carregando Blogger", width=200, height=80, validate=True)


while post_number <= post_limit_number:
	log(f"Criando novo post: Post {post_number}")
	post_title = "Post " + str(post_number).zfill(2)
	pyperclip.copy(post_title)
	retryTime = 0

	while True:
		try:
			screen_position_x, screen_position_y = search_image(f"{path}/new-post.png",
				"Procurando botão \"Nova Postagem\"", y0=200, width=200, height=80, validate=True)
			pyautogui.click(110, 240)
			pyautogui.locateCenterOnScreen(f"{path}/return-button.png")
			log("Página de edição de post carregada")
			title_screen_position_x, title_screen_position_y = search_image(f"{path}/empty-title-post.png",
				"Renomeando post", validate=True)
			pyautogui.click(title_screen_position_x, title_screen_position_y)
			break
		except Exception as e:
			log(f"{e}. Retrying in {retryTime} seconds")
			sleep(retryTime)
			retryTime += 2

	pyautogui.hotkey("ctrl", "v")
	search_image(f"{path}/title-updated.png", "Página criada com sucesso")
	pyautogui.hotkey("alt", "left")
	post_number += 1
