import json
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
	return "welcome!"

@app.route("/git")
def git():
	with open('kiransukumaran.json') as json_data:
		d = json.load(json_data)
		print d

if __name__ == "__main__":
    app.run()
