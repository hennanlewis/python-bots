from time import sleep
from flask import Flask, render_template, request, jsonify
from threading import Thread
import webview

from main_bot import test

app = Flask(__name__, static_folder="./assets", template_folder="./templates")

is_creating_post = False
current_item = 0
total_quantity = 0
current_blog = ""


def main_func(data):
    global is_creating_post, current_item, total_quantity, current_blog
    current_item = 0
    total_quantity = 0
    for element in data:
        total_quantity += element["post_quantity"]

    for element in data:
        browser = element["browser"]
        print(element["blog_url"])
        current_blog = element["blog_url"]
        initial_post = element["initial_post"]
        final_post = initial_post + element["post_quantity"] - 1
        test(browser, current_blog, initial_post, final_post, current_item)

    is_creating_post = False


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/createfile", methods=["POST"])
def create_file():
    global is_creating_post, current_item, total_quantity, current_blog
    is_valid_data = True

    if is_creating_post:
        return jsonify({ "current_blog": current_blog, "current_item": current_item, "total_quantity": total_quantity})

    data = request.get_json()
    for item in data:
        if not all(
            key in item
            for key in ["blog_url", "initial_post", "post_quantity", "browser"]
        ):
            is_valid_data = False
            break

    if is_valid_data:
        is_creating_post = True
        thread = Thread(target=main_func, args=(data,))
        thread.start()

        return jsonify({"message": "Function is started"})

    return jsonify({"error": "Invalid request body"}), 400


if __name__ == "__main__":
    app.run(debug=True)

# webview.create_window("Hello world", app)
# webview.start()
