from time import sleep
from flask import Flask, render_template, request, jsonify
from threading import Thread
import random
import webview

app = Flask(__name__, static_folder="./assets", template_folder="./templates")

is_creating_post = False
initial_number = 0
final_number = 0
link_counter = 0

def main_func():
	global initial_number, final_number, is_creating_post
	while initial_number <= final_number:
		sleep(2)
		print(f"Creating Post {initial_number}")
		initial_number += 1
	is_creating_post = False
		
@app.route("/")
def hello_world():
	return render_template("index.html", link_counter=link_counter)

@app.route("/createfile", methods=["POST"])
def create_file():
	global is_creating_post, initial_number, final_number

	if is_creating_post:
		return jsonify({
			"current_post": initial_number,
			"final_post": final_number
		})

	data = request.get_json()
	if "initial_number" in data and "final_number" in data:
		initial_number = data["initial_number"]
		final_number = data["final_number"]

		is_creating_post = True
		thread = Thread(target=main_func)
		thread.start()

		return jsonify({"message": "function is started"})

	return jsonify({"error": "Invalid request body"}), 400


if __name__ == "__main__":
	app.run(debug=True)

# webview.create_window("Hello world", app)
# webview.start()
