# WRITTEN BY JEREMY JUNG
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
class Button_Handler:

    def __init__(self, pin_num, init_value):
        '''
        inputs
        ------
        pin_num: number
            number of the GPIO pin where the button is connected
        init_value: string
            initial value to read of the button. accepts "down" or "up". 
        '''
        init_value_map = {
            'down': GPIO.PUD_DOWN, #off
            'up': GPIO.PUD_UP #on
        }
        GPIO.setwarnings(False) # Ignore warning for now
        GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
        # Set input pin and initial value
        GPIO.setup(pin_num, GPIO.IN, pull_up_down=init_value_map[init_value.lower()]) 
        self.times_called = 0
    def button_event_main_callback(self, first_callback, second_callback):
        if (self.times_called % 2 == 0):
            # this is either the first or third or etc. times this event was detected
            self.times_called+=1
            first_callback()
        else: 
            # this is either the second or fourth or etc. times this event was detected
            self.times_called+=1
            second_callback()
        
    def set_button_event (self, edge, first_callback, second_callback):
        '''
        inputs
        ------
        edge: string
            What type of edge to catch events for. Either RISING, FALLING or BOTH.
        first_callback: function
            function to call the first time event is caught (and every other time)
        second_callback: function
            function to call the second time event is caught (and every other time)
        '''
        edge_map = {
            'RISING': GPIO.RISING,
            'FALLING': GPIO.FALLING,
            'BOTH': GPIO.BOTH,
        }
        GPIO.add_event_detect(10,edge_map[edge.lower()], callback = self.button_event_main_callback(first_callback, second_callback))

# do sudo apt-get install python-rpi.gpio python3-rpi.gpio
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

"""
while True: # Run forever
    if GPIO.input(10) == GPIO.HIGH:
        print("Button was pushed!")
"""
def button_callback(channel):
    print("Button was pushed!")

GPIO.add_event_detect(10,GPIO.RISING, callback = button_callback)
message = input("press enter to quit \n\n")
GPIO.cleanup()
