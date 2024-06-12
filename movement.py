# import RPi.GPIO as GPIO

class Movement():

    def __init__(self):
        MOTOR_1_PIN_1 = 14
        MOTOR_1_PIN_2 = 15
        MOTOR_2_PIN_1 = 13
        MOTOR_2_PIN_2 = 12

    def forward(self):
        print('Move Forward')

    def backwards(self):
        print('Move Backwards')

    def left(self):
        print('Turn Left')

    def right(self):
        print('Turn Right')

    def stop(self):
        print('Stop!')
