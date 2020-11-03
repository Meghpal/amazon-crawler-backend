from flask import Flask
from time import sleep

app = Flask(__name__)


@app.route("/")
def home():
    print("started")
    sleep(5)
    print("done")
    return {"a": "1"}


if __name__ == "__main__":
    app.run()