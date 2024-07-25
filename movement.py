from time import sleep
import RPi.GPIO as GPIO


class Movement:
    '''
    This class handles the movement of the car and other accessaries like flashing lights and horn beep.
    
    Attributes: None
    '''

    def __init__(self):
        '''
        This method defines the Raspberry Pi pins that are to be used for the different behaviors.
        
        Parameters:
            self.MOTOR_1_PIN_1(int): The Raspberry Pi pin that controls motor 1, pin 1. It is either high(True) or low(False).
            self.MOTOR_1_PIN_2(int): The Raspberry Pi pin that controls motor 1, pin 2. It is either high(True) or low(False).
            self.MOTOR_2_PIN_1(int): The Raspberry Pi pin that controls motor 2, pin 1. It is either high(True) or low(False).
            self.MOTOR_2_PIN_2(int): The Raspberry Pi pin that controls motor 2, pin 2. It is either high(True) or low(False).
            self.RED_LED_PIN(int): The Raspberry Pi pin that controls the red LED. It is either high(True) or low(False).
            self.BLUE_LED_PIN(int): The Raspberry Pi pin that controls the blue LED. It is either high(True) or low(False).
            self.YELLOW_LED_PIN(int): The Raspberry Pi pin that controls the yellow LED. It is either high(True) or low(False).
            self.GREEN_LED_PIN(int): The Raspberry Pi pin that controls the green LED. It is either high(True) or low(False).
            self.HORN_PIN(int): The Raspberry Pi pin that controls the horn. It is either high(True) or low(False).

            GPIO.setmode(GPIO.BCM): BCM defines referring to the pin by their name as opposed to their actual number.
            GPIO.setup(pin, pin behavior): Defines a pin whether it is going to be used for input or output.
        
        Returns: None
        '''
        self.MOTOR_1_PIN_1 = 26
        self.MOTOR_1_PIN_2 = 19
        self.MOTOR_2_PIN_1 = 13
        self.MOTOR_2_PIN_2 = 6
        self.RED_LED_PIN = 20
        self.BLUE_LED_PIN = 21
        self.YELLOW_LED_PIN = 1
        self.GREEN_LED_PIN = 7
        self.HORN_PIN = 5

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.MOTOR_1_PIN_1, GPIO.OUT)
        GPIO.setup(self.MOTOR_1_PIN_2, GPIO.OUT)
        GPIO.setup(self.MOTOR_2_PIN_1, GPIO.OUT)
        GPIO.setup(self.MOTOR_2_PIN_2, GPIO.OUT)
        GPIO.setup(self.RED_LED_PIN, GPIO.OUT)
        GPIO.setup(self.BLUE_LED_PIN, GPIO.OUT)
        GPIO.setup(self.YELLOW_LED_PIN, GPIO.OUT)
        GPIO.setup(self.GREEN_LED_PIN, GPIO.OUT)
        GPIO.setup(self.HORN_PIN, GPIO.OUT)

    def forward(self):
        '''
        This method moves the car in a forward direction.
        
        Parameters: None
        
        Returns: None
        '''
        print('Move Forward')
        GPIO.output(self.MOTOR_1_PIN_1, True)
        GPIO.output(self.MOTOR_1_PIN_2, False)
        GPIO.output(self.MOTOR_2_PIN_1, True)
        GPIO.output(self.MOTOR_2_PIN_2, False)

    def backward(self):
        '''
        This method moves the car in a backward direction.
        
        Parameters: None
        
        Returns: None
        '''
        print('Move Backwards')
        GPIO.output(self.MOTOR_1_PIN_1, False)
        GPIO.output(self.MOTOR_1_PIN_2, True)
        GPIO.output(self.MOTOR_2_PIN_1, False)
        GPIO.output(self.MOTOR_2_PIN_2, True)

    def left(self):
        '''
        This method turns/rotates the car left.
        
        Parameters: None
        
        Returns: None
        '''
        print('Turn Left')
        GPIO.output(self.MOTOR_1_PIN_1, False)
        GPIO.output(self.MOTOR_1_PIN_2, True)
        GPIO.output(self.MOTOR_2_PIN_1, True)
        GPIO.output(self.MOTOR_2_PIN_2, False)

    def right(self):
        '''
        This method turns/rotates the car right.
        
        Parameters: None
        
        Returns: None
        '''
        print('Turn Right')
        GPIO.output(self.MOTOR_1_PIN_1, True)
        GPIO.output(self.MOTOR_1_PIN_2, False)
        GPIO.output(self.MOTOR_2_PIN_1, False)
        GPIO.output(self.MOTOR_2_PIN_2, True)

    def stop(self):
        '''
        This method stops all motion.
        
        Parameters: None
        
        Returns: None
        '''
        print('Stop')
        GPIO.output(self.MOTOR_1_PIN_1, False)
        GPIO.output(self.MOTOR_1_PIN_2, False)
        GPIO.output(self.MOTOR_2_PIN_1, False)
        GPIO.output(self.MOTOR_2_PIN_2, False)

    def horn(self):
        '''
        This method makes the horn start beeping.
        
        Parameters: None
        
        Returns: None
        '''
        print('Beep!')
        GPIO.output(self.HORN_PIN, True)

    def hornStop(self):
        '''
        This method makes the horn stop beeping.
        
        Parameters: None
        
        Returns: None
        '''
        print('Unbeep!')
        GPIO.output(self.HORN_PIN, False)

    def sequential_flashing(self, flash_speed, flash_duration):
        '''
        This method makes the LED's flash sequentially.
        
        Parameters:
            flash_speed(int): Defines how fast the lights flash.
            flash_duration(int): Defines how many times the lights flash.
        
        Returns: None
        '''
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
            self.lights_off()

    def police_lights(self, flash_speed, flash_duration):
        '''
        This method makes the red and blue LED's will alternate flashing, similar to a police car.
        
        Parameters:
            flash_speed(int): Defines how fast the lights flash.
            flash_duration(int): Defines how many times the lights flash.
        
        Returns: None
        '''
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
            self.lights_off()

    def paired_flashing(self, flash_speed, flash_duration):
        '''
        This method makes the LED's alternate flash in pairs. There are 4 LED's, they will alternate flashing in pairs,
        two on and two off.
        
        Parameters:
            flash_speed(int): Defines how fast the lights flash.
            flash_duration(int): Defines how many times the lights flash.
        
        Returns: None
        '''
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
            self.lights_off()

    def lights_off(self):
        '''
        This method turns off all of the LED's.
        
        Parameters: None
        
        Returns: None
        '''
        print('Lights Off')
        GPIO.output(self.BLUE_LED_PIN, False)
        GPIO.output(self.RED_LED_PIN, False)
        GPIO.output(self.YELLOW_LED_PIN, False)
        GPIO.output(self.GREEN_LED_PIN, False)
