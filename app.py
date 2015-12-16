from flask import Flask
from flask import send_file

app = Flask(__name__, static_url_path='')

@app.route("/")
def index():
    return send_file('templates/index.html')

if __name__ == "__main__":
    app.run(debug=True)
