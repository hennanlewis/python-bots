from time import sleep
import pyautogui
import pyperclip
import signal
import sys

import bot_funcs

def handle_interrupt(signal, frame):
	bot_funcs.log("There might have been an error, or the robot was interrupted :(")
	bot_funcs.create_log_file()
	sys.exit(0)

def initialize_bot(selected_browser, blog_link, initial_post, final_post):
	interval_time = 0.25
	pyautogui.PAUSE = interval_time
	screen_width, screen_height = pyautogui.size()

	path = f"images/{selected_browser}"
	selected_position = None

	print()
	bot_funcs.log("Initializing bot")
	bot_funcs.open_browser(selected_browser)
	bot_funcs.search_new_tab(path, blog_link)
	bot_funcs.load_blogger(path)

	while initial_post <= final_post:
		option = 0
		retryTime = preview_retry_time = 0
		post_title = "Post " + str(current_post).zfill(2)
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
				bot_funcs.log(f"Creating post: Post {current_post}")
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
		current_post += 1

	bot_funcs.log("Automation process completed.")
	bot_funcs.create_log_file()

def bot_behavior(browser, blog, initial_post, final_post, current_item):
	print(browser, blog)
	sleep(2)
	browser = "opera"
	sleep(2)
	blog = "blog x"
	sleep(2)
	for i in range(initial_post, final_post + 1):
		current_item += 1
		sleep(0.1)
		print({ "current_blog": blog, "current_item": current_item, "total_quantity": 300})

signal.signal(signal.SIGINT, handle_interrupt)