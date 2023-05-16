from dotenv import load_dotenv
from time import sleep
import pyautogui
import pyperclip
import os

os.chdir (os.environ["PATH"])

load_dotenv()

blogLink = os.environ["BLOG_LINK"]
screenPositionX = screenPositionY = 0
postCounter = 1
# pyautogui.PAUSE = 0.2

# 1 é a posição na barra de tarefas do ícone do navegador firefox
pyautogui.hotkey("win","1")

print("Aguarde, carregando firefox...")
while True:
	try:
		pyautogui.locateOnScreen('images/firefox-window-icon.png')
		break
	except Exception as e:
		print("Erro:", e)

pyautogui.hotkey("ctrl","n")

print("Aguarde, carregando nova aba...")
while True:
	try:
		pyautogui.locateOnScreen('images/new-tab.png')
		break
	except Exception:
		continue

pyautogui.typewrite(blogLink)
pyautogui.hotkey('enter')

print("Aguarde, página do blogger carregando...")
while True:
	try:
		pyautogui.locateOnScreen('images/blog-loaded.png')
		break
	except Exception:
		continue

print("Procurando botão para novo post...")
while True:
	try:
		screenPositionX, screenPositionY = pyautogui.locateCenterOnScreen('images/new-post.png')
		break
	except Exception:
		continue

while postCounter <= 100:
	retryTime = 0
	print("Criando novo post: Post", postCounter)
	while True:
		try:
			screenPositionX, screenPositionY = pyautogui.locateCenterOnScreen('images/new-post.png')
			pyautogui.click(screenPositionX, screenPositionY)
			pyautogui.locateOnScreen('images/return-button.png')
			sleep(1)
			screenPositionX, screenPositionY = pyautogui.locateCenterOnScreen('images/empty-title-post.png')
			pyautogui.click(screenPositionX, screenPositionY)
			break
		except Exception:
			print("Tentando novamente em", retryTime, "segundos")
			sleep(retryTime)
			retryTime += 2

	if postCounter < 10:
		postTitle = "Post " + str(postCounter).zfill(2)
	else:
		postTitle = "Post " + str(postCounter)
	postCounter += 1
	pyperclip.copy(postTitle)
	pyautogui.hotkey("ctrl", "v")

	while True:
		sleep(1)
		try:
			pyautogui.locateOnScreen('images/title-updated.png')
			break
		except Exception:
			continue
	
	sleep(2.5)
	pyautogui.hotkey("alt", "left")	
