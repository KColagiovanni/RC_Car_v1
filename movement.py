from time import sleep
import RPi.GPIO as GPIO


class Movement:

    def __init__(self):
        self.MOTOR_1_PIN_1 = 26
        self.MOTOR_1_PIN_2 = 19
        self.MOTOR_2_PIN_1 = 13
        self.MOTOR_2_PIN_2 = 6
        self.RED_LED_PIN = 16
        self.BLUE_LED_PIN = 20

        self.lights = False
        self.flash_duration = 0.5
        self.flash_count = 0
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
        flash_count = 0
        while flash_count < 25:
            print('Flash Red')
            GPIO.output(self.RED_LED_PIN, True)
            GPIO.output(self.BLUE_LED_PIN, False)
            sleep(self.flash_duration)
            print('Flash Blue')
            GPIO.output(self.BLUE_LED_PIN, True)
            GPIO.output(self.RED_LED_PIN, False)
            sleep(self.flash_duration)
            flash_count += 1

    # def toggle_lights(self):
    #     # print(f'lights is {self.lights}')
    #     # if not self.lights:
    #     self.flash_count += 1
    #     print(f'self.flash_count is {self.flash_count}')
    #     if self.flash_count % 2 != 0:
    #         print('Turning lights On')
    #         self.flashing_lights(True)
    #     else:
    #         print('Turning lights Off')
    #         self.flashing_lights(False)
    #
    # def flashing_lights(self, lights_on):
    #     print('Flashing Lights')
    #     print(f'lights_on is {lights_on}')
    #     while lights_on:
    #         print('Flash Red')
    #         # GPIO.output(self.RED_LED_PIN, True)
    #         # GPIO.output(self.BLUE_LED_PIN, False)
    #         sleep(self.flash_duration)
    #         print('Flash Blue')
    #         # GPIO.output(self.BLUE_LED_PIN, True)
    #         # GPIO.output(self.RED_LED_PIN, False)
    #         sleep(self.flash_duration)
