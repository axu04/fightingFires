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
