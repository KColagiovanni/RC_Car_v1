from flask import Flask, render_template
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


@app.route('/policeLights')
def flash_police_lights():
    print('flash_police_lights')
    mv = Movement()
    mv.police_lights(.25)
    return render_template('index.html')

# @app.route('/flashingLights')
# def flashingLights():
#     mv = Movement()
    # if light_count % 2 == 0:
    #     toggle = True
    #     light_count += 1
    # else:
    #     toggle = False
    # mv.toggle_lights(toggle)
    # if light_count % 2 == 0:
    #     toggle = True
    #     light_count += 1
    # else:
    #     toggle = False
    # mv.toggle_lights()
    # return render_template('index.html')


if __name__ == '__main__':
    app.run(
        debug=True,
        # host='192.168.0.221',  # Use for RPi
        host='0.0.0.0',  # Use for local debugging
        port=5000
    )
