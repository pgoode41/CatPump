import RPi.GPIO as GPIO
import time

#Must run container
#docker run --privileged -d whatever



##########################################################################
##########################################################################
def Run_Pump(dataDict):
    gpioPin = int(dataDict['gpio_pin_number'])
    pumpDuration = int(dataDict['pump_run_duration'])
    
    GPIO.setwarnings(False)

    if pumpDuration is "default":
        pumpDuration = 5

    for _ in range(1):
        #Sets GPIO gpioPins by board location number.
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(gpioPin, GPIO.OUT)

        #Activate Pump
        GPIO.output(gpioPin, GPIO.HIGH)
        print('Pump Activated.')

        #Run pump for this duration.
        time.sleep(pumpDuration)

        #Turn off pump.
        GPIO.output(gpioPin, GPIO.LOW)
        print('Pump Deactivated.')

        #GPIO Cleanup
        GPIO.cleanup()

        returnString = 'Pump Cycle Complete.'
    return returnString
##########################################################################
##########################################################################
'''
sampleData = {
    "gpio_pin_number": 12,
    "pump_run_duration": 10,
}

Run_Pump(sampleData)
'''
