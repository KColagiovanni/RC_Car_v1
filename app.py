from flask import Flask, render_template, request
from movement import Movement

app = Flask(__name__)
# light_count = 0

@app.route('/', methods=['POST', 'GET'])
def index():
    '''
    Function and route for the home page.

    Parameters: None

    Returns: Renders the index.html page. 
    '''

    return render_template('index.html')

@app.route('/forward')
def forward():
    '''
    Function and route for forward motion.

    Parameters: None

    Returns: Renders the index.html page. 
    '''
    
    mv = Movement()
    mv.forward()
    return render_template('index.html')

@app.route('/backward')
def backward():
    '''
    Function and route for backward motion.

    Parameters: None

    Returns: Renders the index.html page. 
    '''
    mv = Movement()
    mv.backward()
    return render_template('index.html')

@app.route('/left')
def left():
    '''
    Function and route for left turning motion.

    Parameters: None

    Returns: Renders the index.html page. 
    '''
    mv = Movement()
    mv.left()
    return render_template('index.html')

@app.route('/right')
def right():
    '''
    Function and route for right turning motion.

    Parameters: None

    Returns: Renders the index.html page. 
    '''
    mv = Movement()
    mv.right()
    return render_template('index.html')


@app.route('/stop')
def stop():
    '''
    Function and route to stop all motion.

    Parameters: None

    Returns: Renders the index.html page. 
    '''
    mv = Movement()
    mv.stop()
    return render_template('index.html')

@app.route('/horn')
def horn():
    '''
    Function and route a horn beep.

    Parameters: None

    Returns: Renders the index.html page. 
    '''
    mv = Movement()
    mv.horn()
    return render_template('index.html')

@app.route('/hornStop')
def hornStop():
    '''
    Function and route to stop the beeping horn.

    Parameters: None

    Returns: Renders the index.html page. 
    '''
    mv = Movement()
    mv.hornStop()
    return render_template('index.html')

@app.route('/lights', methods=['POST', 'GET'])
def lights():
    '''
    Function and route to flash the LED lights. It gets the type, speed, and flash_duration form data from the submitted
    form. The flash speed is defined based on the form speed value. Depending on the flash type that is submitted in 
    the form, a corosponding method is called based on the type value, the type and flash_duration are sent as 
    parameters. 

    Parameters: None

    Returns: Renders the index.html page. 
    '''
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
            mv.police_lights(flash_speed, flash_duration)
        elif type == 'paired':
            mv.paired_flashing(flash_speed, flash_duration)
        else:
            print('type was not defined')

    return render_template('index.html')


# Run the Flask app. Define the host and port.
if __name__ == '__main__':
    app.run(
        # Enabling debug mode will show an interactive traceback and console in the browser when there is an error.
        debug=True,
        # host='192.168.0.221',  # Use for RPi
        host='0.0.0.0',  # Use for local debugging
        port=5000  # Define the port to use when connecting.
    )
