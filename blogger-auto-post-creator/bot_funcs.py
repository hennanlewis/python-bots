from datetime import datetime
import pyautogui
import pyscreeze

interval_time = 0.25
log_file_text = ""
file_name = ""


def log(log_message):
    global log_file_text
    text = f"{datetime.now()} - {log_message}"
    print(text)
    log_file_text = f"{text}" if log_file_text == "" else f"{log_file_text}\n{text}"


def create_log_file():
    time_log = datetime.now()
    date_numbers = (
        str(time_log).replace("-", "").replace(":", "").replace(" ", "").split(".")[0]
    )
    with open(f"log/{date_numbers}", "w", encoding="utf-8") as file:
        file.write(log_file_text)
        file.close()


def select_browser():
    print()
    while True:
        try:
            browser_options = ["firefox", "edge"]
            print("Select the browser: ")
            print("1 - Firefox")
            print("2 - Microsoft Edge")
            selected = int(input())
            return browser_options[selected - 1]
        except Exception:
            print("\nAn error occurred. Please try again.")


def chapter_values():
    print()
    while True:
        try:
            post_number = int(input("Insert the initial chapter of the range: "))
            post_limit_number = int(input("Insert the last chapter of the range: "))
            return post_number, post_limit_number
        except Exception:
            print("\nAn error occurred. Please try again.")


def open_browser(browser_name):
    log("Opening browser...")
    pyautogui.hotkey("win")
    pyautogui.typewrite(browser_name, interval=0.03)
    pyautogui.hotkey("backspace", "enter")


def search_image_position(path, region):
    return pyscreeze.locateCenterOnScreen(path, region=region)


def search_new_tab(path, blog_link):
    log('Searching "New tab" icon...')
    while True:
        selected_position = search_image_position(
            f"{path}/new-tab.png", region=(0, 0, 300, 50)
        )
        if selected_position is not None:
            log("Opening link...")
            pyautogui.typewrite(blog_link, interval=0.01)
            pyautogui.hotkey("enter")
            return


def load_blogger(path):
    log("Loading Blogger...")
    while True:
        selected_position = search_image_position(
            f"{path}/blogger.png", (0, 0, 300, 50)
        )
        if selected_position is not None:
            log("Blogger loaded")
            return


def click_position(selected_position):
    pyautogui.click(selected_position, duration=interval_time)


def rename_title(click_position):
    pyautogui.click(click_position, duration=interval_time)
    pyautogui.hotkey("ctrl", "v")
