from flask import Flask, render_template, request, redirect, jsonify
from movement import Movement

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/forward')
def forward():
    mv = Movement()
    mv.forward()


@app.route('/backwards')
def backwards():
    mv = Movement()
    mv.backwards()


@app.route('/left')
def left():
    mv = Movement()
    mv.left()


@app.route('/right')
def right():
    mv = Movement()
    mv.right()


@app.route('/stop')
def stop():
    mv = Movement()
    mv.stop()


if __name__ == '__main__':
    app.run(debug=True)
