from time import sleep
import RPi.GPIO as GPIO

class Movement():

    def __init__(self):
        self.MOTOR_1_PIN_1 = 26
        self.MOTOR_1_PIN_2 = 19
        self.MOTOR_2_PIN_1 = 13
        self.MOTOR_2_PIN_2 = 6
        self.RED_LED_PIN = 16
        self.BLUE_LED_PIN = 20

        self.lights = False
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.MOTOR_1_PIN_1, GPIO.OUT)
        GPIO.setup(self.MOTOR_1_PIN_2, GPIO.OUT)
        GPIO.setup(self.MOTOR_2_PIN_1, GPIO.OUT)
        GPIO.setup(self.MOTOR_2_PIN_2, GPIO.OUT)
        GPIO.setup(self.RED_LED_PIN, GPIO.OUT)
        GPIO.setup(self.BLUE_LED_PIN, GPIO.OUT)

    def forward(self):
        print('Move Forward')
        GPIO.output(self.MOTOR_1_PIN_1, True)
        GPIO.output(self.MOTOR_1_PIN_2, False)
        GPIO.output(self.MOTOR_2_PIN_1, True)
        GPIO.output(self.MOTOR_2_PIN_2, False)

    def backward(self):
        print('Move Backwards')
        GPIO.output(self.MOTOR_1_PIN_1, False)
        GPIO.output(self.MOTOR_1_PIN_2, True)
        GPIO.output(self.MOTOR_2_PIN_1, False)
        GPIO.output(self.MOTOR_2_PIN_2, True)

    def left(self):
        print('Turn Left')
        GPIO.output(self.MOTOR_1_PIN_1, False)
        GPIO.output(self.MOTOR_1_PIN_2, True)
        GPIO.output(self.MOTOR_2_PIN_1, True)
        GPIO.output(self.MOTOR_2_PIN_2, False)

    def right(self):
        print('Turn Right')
        GPIO.output(self.MOTOR_1_PIN_1, True)
        GPIO.output(self.MOTOR_1_PIN_2, False)
        GPIO.output(self.MOTOR_2_PIN_1, False)
        GPIO.output(self.MOTOR_2_PIN_2, True)

    def stop(self):
        print('Stop!')
        GPIO.output(self.MOTOR_1_PIN_1, False)
        GPIO.output(self.MOTOR_1_PIN_2, False)
        GPIO.output(self.MOTOR_2_PIN_1, False)
        GPIO.output(self.MOTOR_2_PIN_2, False)

    def toggle_lights(self):
        if self.lights == True:
            print('Turning lights On')
            self.flashingLights(True)
        else:
            print('Turning lights Off')
            self.flashingLights(False)

    def flashingLights(self, lights_on):
        print('Flashing Lights')
        while lights_on:
            GPIO.output(self.RED_LED_PIN, True)
            GPIO.output(self.BLUE_LED_PIN, False)
            sleep(100)
            GPIO.output(self.BLUE_LED_PIN, True)
            GPIO.output(self.RED_LED_PIN, False)
            sleep(100)