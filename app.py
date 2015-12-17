import os
from flask import Flask
from flask import send_file

STATIC_FOLDER = os.path.join(os.getcwd(), 'front_end/dist')

app = Flask(__name__, static_folder=STATIC_FOLDER, static_url_path='')

@app.route("/")
def index():
    return send_file('front_end/dist/index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
