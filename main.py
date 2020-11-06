from flask import Flask
from views import index, fetch_reviews

app = Flask(__name__)

app.add_url_rule("/", methods=["GET", "POST"], view_func=index)

app.add_url_rule("/fetch_reviews", methods=["GET", "POST"], view_func=fetch_reviews)

if __name__ == "__main__":
    app.run(debug=True)