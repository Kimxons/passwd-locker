from flask import Flask
# from main import *


app = Flask(__name__)

@app.route('/')
def main():
    return "Hello World"