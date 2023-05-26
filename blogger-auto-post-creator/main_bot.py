from time import sleep
import pyautogui
import pyperclip
import signal
import sys

import bot_funcs

interval_time = 0.25
pyautogui.PAUSE = interval_time
screen_width, scr = pyautogui.size()
screen_width, screen_height = pyautogui.size()


selected_browser = bot_funcs.select_browser()
selected_blog = bot_funcs.select_blog_link()
post_number, post_limit_number = bot_funcs.chapter_values()

path = f"images/{selected_browser}"
selected_position = None

def handle_interrupt(signal, frame):
	bot_funcs.log("There might have been an error, or the robot was interrupted :(")
	bot_funcs.create_log_file()
	sys.exit(0)

signal.signal(signal.SIGINT, handle_interrupt)

print()
bot_funcs.log("Init bot")
bot_funcs.open_browser(selected_browser)
bot_funcs.search_new_tab(path, selected_blog)
bot_funcs.load_blogger(path)

while post_number <= post_limit_number:
	option = 0
	retryTime = 0
	preview_retry_time = retryTime
	post_title = "Post " + str(post_number).zfill(2)
	pyperclip.copy(post_title)

	while True:
		bot_funcs.search_image_position(f"{path}/new-tab.png", (0, 0, 300, 50))

		selected_position = bot_funcs.search_image_position(f"{path}/new-post.png", (0, 120, 300, 150))
		if selected_position is not None:
			bot_funcs.log(f"Initiating a new post...")
			bot_funcs.click_position(selected_position)
			selected_position = None
			retryTime += 2
			option = 1

		selected_position = bot_funcs.search_image_position(f"{path}/edit-post.png", (0, 0, 300, 50))
		if selected_position is not None and option == 1:
			bot_funcs.log(f"Creating post: Post {post_number}")
			selected_position = None
			option = 2

		selected_position = bot_funcs.search_image_position(f"{path}/empty-title.png", (0, 100, 60, 130))
		if selected_position is not None and option == 2:
			bot_funcs.log("Renaming title...")
			bot_funcs.rename_title(selected_position)
			selected_position = None
			option = 3

		selected_position = bot_funcs.search_image_position(f"{path}/edited-post.png", (screen_width-370, 90, 100, 130))
		if selected_position is not None and option == 3:
			bot_funcs.log("Post renamed")
			selected_position = None
			option = 4

		selected_position = bot_funcs.search_image_position(f"{path}/return.png", (0, 80, 70, 50))
		if selected_position is not None and option == 4:
			bot_funcs.log("Back to Blogger main page")
			bot_funcs.click_position(selected_position)
			selected_position = None
			break

		if retryTime != preview_retry_time:
			bot_funcs.log(f"Trying it again in {retryTime} seconds")
			preview_retry_time = retryTime
			sleep(retryTime)

	bot_funcs.log(f"\"{post_title}\"  inserted successfully!")
	post_number += 1

bot_funcs.log("Automation process completed.")
bot_funcs.create_log_file()
