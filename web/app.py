# to run
# export FLASK_APP=app.py
# flask run

import sys
sys.path.append("..")
import lib

from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

DEBUG = False


@app.route('/', methods=['GET'])
def showFry():
    size = 300
    return render_template('main.html', the_fry="<svg height=" + str(size) + ";>" + lib.generate(size, size)) + "</svg>";