from flask import Flask
app = Flask(__name__)

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
