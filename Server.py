from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/',methods = ['POST', 'Get'])
def root():
    return render_template("index.html")


@app.route('/health')
def health():
    return "OK"

if __name__=='__name__':
    app.run(debug="true")    