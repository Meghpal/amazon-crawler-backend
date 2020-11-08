from flask import Flask
from views import search, search_next, fetch_reviews

app = Flask(__name__)

app.add_url_rule("/search", methods=["GET"], view_func=search)

app.add_url_rule("/search_next", methods=["GET"], view_func=search_next)

app.add_url_rule("/fetch_reviews", methods=["POST"], view_func=fetch_reviews)

if __name__ == "__main__":
    app.run(debug=True)