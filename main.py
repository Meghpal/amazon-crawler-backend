from flask import Flask
from views import index

app = Flask(__name__)

app.add_url_rule("/", methods=["GET", "POST"], view_func=index)

if __name__ == "__main__":
    app.run(debug=True)