from time import sleep
from flask import Flask, render_template, request, jsonify
from multiprocessing import Process, Value
import webview

from main_bot import bot_behavior, initialize_bot

app = Flask(__name__, static_folder="./assets", template_folder="./templates")

is_creating_post = False
current_item = Value("i", 0)
current_item_position = Value("i", 0)
total_quantity = 0
data = []

def main_func(data, current_item, current_item_position):
	global is_creating_post

	for index, element in enumerate(data):
		current_item_position.value = index
		browser = element["browser"]
		current_blog = element["blog_url"]
		initial_post = element["initial_post"]
		final_post = initial_post + element["post_quantity"] - 1
		initialize_bot(browser, current_blog, initial_post, final_post, current_item)

	print("Proccess finished successfully")


@app.route("/")
def hello_world():
	return render_template("index.html")


@app.route("/createfile", methods=["POST"])
def create_file():
	global is_creating_post, total_quantity, data
	is_valid_data = True

	if current_item.value == total_quantity:
		is_creating_post = False

	if is_creating_post:
		return jsonify(
			{
				"current_blog": data[current_item_position.value]["blog_url"],
				"current_item": current_item.value,
				"total_quantity": total_quantity,
			}
		)

	data = request.get_json()
	for item in data:
		if not all(
			key in item
			for key in ["blog_url", "initial_post", "post_quantity", "browser"]
		):
			is_valid_data = False
			break

	for element in data:
		total_quantity += element["post_quantity"]

	if is_valid_data:
		is_creating_post = True
		current_item.value = 0
		process = Process(target=main_func, args=(data, current_item, current_item_position))
		process.start()
		print(current_item_position.value)

		return jsonify({"message": "Function is started"})

	return jsonify({"error": "Invalid request body"}), 400


if __name__ == "__main__":
	app.run(debug=True)

# webview.create_window("Hello world", app)
# webview.start()
