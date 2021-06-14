from flask import Flask, render_template, flash, redirect, url_for
from main import *


app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")