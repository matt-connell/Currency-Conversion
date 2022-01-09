from flask import Flask
from views import views

app = Flask(__name__)
#all the routes will be stored in a views.py file by using the following statement
app.register_blueprint(views, url_prefix="/")


if __name__ == '__main__':
    app.run(debug = True, port=5001)  