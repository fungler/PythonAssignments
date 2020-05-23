from flask import Flask
import func

app = Flask(__name__)


@app.route('/display')
def displayValues():
    return func.displayInfo()