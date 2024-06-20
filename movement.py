from time import sleep
import RPi.GPIO as GPIO


class Movement:

    def __init__(self):
        self.MOTOR_1_PIN_1 = 26
        self.MOTOR_1_PIN_2 = 19
        self.MOTOR_2_PIN_1 = 13
        self.MOTOR_2_PIN_2 = 6
        self.RED_LED_PIN = 20
        self.BLUE_LED_PIN = 21
        self.YELLOW_LED_PIN = 1
        self.GREEN_LED_PIN = 7

        self.total_number_of_flashes = 5

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.MOTOR_1_PIN_1, GPIO.OUT)
        GPIO.setup(self.MOTOR_1_PIN_2, GPIO.OUT)
        GPIO.setup(self.MOTOR_2_PIN_1, GPIO.OUT)
        GPIO.setup(self.MOTOR_2_PIN_2, GPIO.OUT)
        GPIO.setup(self.RED_LED_PIN, GPIO.OUT)
        GPIO.setup(self.BLUE_LED_PIN, GPIO.OUT)
        GPIO.setup(self.YELLOW_LED_PIN, GPIO.OUT)
        GPIO.setup(self.GREEN_LED_PIN, GPIO.OUT)

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

    def sequential_flashing(self, flash_speed, flash_duration):
        flash_count = 0
        while flash_count < flash_duration:

            print('Flash Red')
            GPIO.output(self.BLUE_LED_PIN, False)
            GPIO.output(self.RED_LED_PIN, True)
            sleep(flash_speed)

            print('Flash Yellow')
            GPIO.output(self.RED_LED_PIN, False)
            GPIO.output(self.YELLOW_LED_PIN, True)
            sleep(flash_speed)

            print('Flash Green')
            GPIO.output(self.YELLOW_LED_PIN, False)
            GPIO.output(self.GREEN_LED_PIN, True)
            sleep(flash_speed)

            print('Flash Blue')
            GPIO.output(self.GREEN_LED_PIN, False)
            GPIO.output(self.BLUE_LED_PIN, True)
            sleep(flash_speed)

            flash_count += 1
        else:
            print('Flash Off')
            GPIO.output(self.BLUE_LED_PIN, False)
            GPIO.output(self.RED_LED_PIN, False)
            GPIO.output(self.YELLOW_LED_PIN, False)
            GPIO.output(self.GREEN_LED_PIN, False)

    def police_lights(self, flash_speed, flash_duration):
        flash_count = 0
        while flash_count < flash_duration:
            print('Flash Red')
            GPIO.output(self.RED_LED_PIN, True)
            GPIO.output(self.BLUE_LED_PIN, False)
            sleep(flash_speed)
            print('Flash Blue')
            GPIO.output(self.BLUE_LED_PIN, True)
            GPIO.output(self.RED_LED_PIN, False)
            sleep(flash_speed)
            flash_count += 1
        else:
            print('Flash Off')
            GPIO.output(self.BLUE_LED_PIN, False)
            GPIO.output(self.RED_LED_PIN, False)

    def paired_flashing(self, flash_speed, flash_duration):
        flash_count = 0
        while flash_count < flash_duration:

            print('Flash Red and Green')
            GPIO.output(self.BLUE_LED_PIN, False)
            GPIO.output(self.YELLOW_LED_PIN, False)
            GPIO.output(self.RED_LED_PIN, True)
            GPIO.output(self.GREEN_LED_PIN, True)
            sleep(flash_speed)

            print('Flash Yellow and Blue')
            GPIO.output(self.RED_LED_PIN, False)
            GPIO.output(self.GREEN_LED_PIN, False)
            GPIO.output(self.YELLOW_LED_PIN, True)
            GPIO.output(self.BLUE_LED_PIN, True)
            sleep(flash_speed)

            flash_count += 1
        else:
            print('Flash Off')
            GPIO.output(self.BLUE_LED_PIN, False)
            GPIO.output(self.RED_LED_PIN, False)
            GPIO.output(self.YELLOW_LED_PIN, False)
            GPIO.output(self.GREEN_LED_PIN, False)
