# This imports the Flask class from the flask package. Flask is a lightweight web framework in Python that allows you to create web applications quickly and easily.
from flask import Flask

#an instance of the Flask class is created and assigned to the variable app.__name__ is a special Python variable that gets the name of the current module.It's passed to Flask to help the app determine the root path. If your app is imported into another module, __name__ will be different
app = Flask(__name__)

#This is a route decorator. It binds a URL to a Python function.
@app.route("/")
def welcome():
    return "Hello  World"

@app.route("/home")
def home():
    return "Home  World"

# import controller.user_controller as user_controller
# import controller.product_controller as product_controller

# from controller import product_controller, user_controller

from controller import *

#import controller.user_controller as  user_controller