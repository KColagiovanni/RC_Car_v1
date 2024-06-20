from flask import Flask, render_template, request
from movement import Movement

app = Flask(__name__)
# light_count = 0

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/forward')
def forward():
    mv = Movement()
    mv.forward()
    return render_template('index.html')


@app.route('/backward')
def backward():
    mv = Movement()
    mv.backward()
    return render_template('index.html')


@app.route('/left')
def left():
    mv = Movement()
    mv.left()
    return render_template('index.html')


@app.route('/right')
def right():
    mv = Movement()
    mv.right()
    return render_template('index.html')


@app.route('/stop')
def stop():
    mv = Movement()
    mv.stop()
    return render_template('index.html')


@app.route('/lights', methods=['POST', 'GET'])
def lights():
    if request.method == 'POST':
        type = request.form['type']
        speed = request.form['speed']
        flash_duration = int(request.form['duration'])

        if speed == 'slow':
            flash_speed = 0.5
        elif speed == 'intermediate':
            flash_speed = 0.25
        elif speed == 'fast':
            flash_speed = 0.1
        else:
            print('speed was not defined')
            flash_speed = 0

        mv = Movement()
        if type == 'sequential':
            mv.sequential_flashing(flash_speed, flash_duration)
        elif type == 'police':
            mv.police_lights(flash_speed,flash_duration)
        elif type == 'paired':
            mv.paired_flashing(flash_speed, flash_duration)
        else:
            print('type was not defined')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        debug=True,
        # host='192.168.0.221',  # Use for RPi
        host='0.0.0.0',  # Use for local debugging
        port=5000
    )
