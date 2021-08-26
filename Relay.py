import RPi.GPIO as GPIO
import time, sys
 
R1 = 23
R2 = 24
R3 = 25
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(R1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(R2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(R3, GPIO.OUT, initial=GPIO.LOW)

print("Script will turn on/off relay after every 10 sec")

while True:
    try:
        print("Turning All Relays On")
        GPIO.output(R1, GPIO.HIGH)
        GPIO.output(R2, GPIO.HIGH)
        GPIO.output(R3, GPIO.HIGH)
        time.sleep(10)
        print("Turning All Relays OFF")
        GPIO.output(R1, GPIO.LOW)
        GPIO.output(R2, GPIO.LOW)
        GPIO.output(R3, GPIO.LOW)
        time.sleep(10)
    except KeyboardInterrupt:
        print('Closing')
        GPIO.cleanup()
        sys.exit()