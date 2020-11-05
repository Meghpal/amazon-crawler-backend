from flask import Flask
import views

app = Flask(__name__)

app.add_url_rule("/", view_func=views.index)

if __name__ == "__main__":
    app.run()