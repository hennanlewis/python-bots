from dotenv import load_dotenv
from time import sleep
import pyautogui
import pyperclip
import os

from functions import search_target
from functions import target_to_click

load_dotenv()

LOCAL_PATH = os.getcwd()
os.chdir(LOCAL_PATH)

BLOG_LINK = os.environ["BLOG_LINK"]
screen_position_x = screen_position_y = 0
post_number = 2
# pyautogui.PAUSE = 0.2

pyautogui.hotkey("win","1")

print("Aguarde, carregando Firefox...")
search_target('images/firefox-window-icon.png')

pyautogui.hotkey("ctrl","n")

print("Aguarde, carregando nova aba...")
search_target('images/new-tab.png')

pyautogui.typewrite(BLOG_LINK)
pyautogui.hotkey('enter')

print("Aguarde, página do blogger carregando...")
search_target('images/blog-loaded.png')

print("Procurando botão para novo post...")
target_to_click('images/new-post.png')

while post_number <= 100:
	retryTime = 0
	print("Criando novo post: Post", post_number)
	while True:
		try:
			target_to_click('images/new-post.png')
			search_target('images/return-button.png')
			sleep(1)
			target_to_click('images/empty-title-post.png')
			break
		except Exception:
			print("Tentando novamente em", retryTime, "segundos")
			sleep(retryTime)
			retryTime += 2

	if post_number < 10:
		postTitle = "Post " + str(post_number).zfill(2)
	else:
		postTitle = "Post " + str(post_number)
	post_number += 1
	pyperclip.copy(postTitle)
	pyautogui.hotkey("ctrl", "v")

	sleep(1)
	search_target('images/title-updated.png')
	
	sleep(2.5)
	pyautogui.hotkey("alt", "left")	
