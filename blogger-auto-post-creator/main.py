from time import sleep
import pyautogui
import pyperclip

from functions import log, select_browser, select_blog_link, chapter_values, search_new_tab, open_browser, search_image_position, load_blogger, click_position, rename_title

interval_time = 0.25
pyautogui.PAUSE = interval_time
screen_width, scr = pyautogui.size()
screen_width, screen_height = pyautogui.size()


selected_browser = select_browser()
selected_blog = select_blog_link()
post_number, post_limit_number = chapter_values()

path = f"images/{selected_browser}"
selected_position = None

print()
log("Iniciando o robô")
open_browser(selected_browser)
search_new_tab(path, selected_blog)
load_blogger(path)

while post_number <= post_limit_number:
	option = 0
	retryTime = 0
	preview_retry_time = retryTime
	post_title = "Post " + str(post_number).zfill(2)
	pyperclip.copy(post_title)

	while True:
		search_image_position(f"{path}/new-tab.png", (0, 0, 300, 50))

		selected_position = search_image_position(f"{path}/new-post.png", (0, 120, 300, 150))
		if selected_position is not None:
			log(f"Iniciando novo post...")
			click_position(selected_position)
			selected_position = None
			retryTime += 2
			option = 1

		selected_position = search_image_position(f"{path}/edit-post.png", (0, 0, 300, 50))
		if selected_position is not None and option == 1:
			log(f"Criando novo post: Post {post_number}")
			selected_position = None
			option = 2

		selected_position = search_image_position(f"{path}/empty-title.png", (0, 100, 60, 130))
		if selected_position is not None and option == 2:
			log("Renomeando título...")
			rename_title(selected_position)
			selected_position = None
			option = 3

		## region = (screen_width-370, 90, 100, 130)
		selected_position = search_image_position(f"{path}/edited-post.png", (screen_width-370, 90, 100, 130))
		if selected_position is not None and option == 3:
			log("Post renomeado")
			selected_position = None
			option = 4

		selected_position = search_image_position(f"{path}/return.png", (0, 80, 70, 50))
		if selected_position is not None and option == 4:
			log("Retornando às postagens")
			click_position(selected_position)
			selected_position = None
			break

		if retryTime != preview_retry_time:
			log(f"Tentando novamente em {retryTime} segundos")
			preview_retry_time = retryTime
			sleep(retryTime)

	log(f"\"{post_title}\" inserido com sucesso!")
	post_number += 1

log("Automação chegou ao fim")