import RPi.GPIO as GPIO
import time

#Must run container
#docker run --privileged -d whatever


gpioPin = 12
##########################################################################
##########################################################################
def Run_Pump(gpioPin, pumpDuration):
    GPIO.setwarnings(False)

    if pumpDuration is "default":
        pumpDuration = 5

    for _ in range(2):
        #Sets GPIO gpioPins by board location number.
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(gpioPin, GPIO.OUT)

        #Activate Pump
        GPIO.output(gpioPin, GPIO.HIGH)

        #Run pump for this duration.
        time.sleep(pumpDuration)

        #Turn off pump.
        GPIO.output(gpioPin, GPIO.LOW)

        #GPIO Cleanup
        GPIO.cleanup()
##########################################################################
##########################################################################

Run_Pump(gpioPin, 10)
