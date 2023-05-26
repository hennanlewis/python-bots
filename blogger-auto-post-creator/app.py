from flask import Flask, render_template

app = Flask(__name__, static_folder="./assets", template_folder="./templates")

counter = 0
@app.route("/")
def hello_world():
	return render_template("index.html", counter=counter)

if __name__ == "__main__":
	app.run(debug=True)
