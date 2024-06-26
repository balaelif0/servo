import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
servo = GPIO.PWM(11,50)
try:
    start_time = time.time()  
    while time.time() - start_time < 60:
        servo.start(2)
        time.sleep(1)
        servo.ChangeDutyCycle(4)
        time.sleep(1)
        servo.ChangeDutyCycle(6)
        time.sleep(1)
        servo.ChangeDutyCycle(8)
        time.sleep(1)
        servo.ChangeDutyCycle(10)
        time.sleep(1)
        servo.ChangeDutyCycle(12)
        time.sleep(1)
        servo.ChangeDutyCycle(14)
        time.sleep(1)

except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()
