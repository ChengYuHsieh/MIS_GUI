from flask import Flask
from flask import send_file

app = Flask(__name__, static_folder='front_end/dist', static_url_path='')

@app.route("/")
def index():
    return send_file('front_end/dist/index.html')

if __name__ == "__main__":
    app.run(debug=True)
