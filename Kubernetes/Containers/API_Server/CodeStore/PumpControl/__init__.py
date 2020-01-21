import RPi.GPIO as GPIO
import time

#Must run container
#docker run --privileged -d whatever



##########################################################################
##########################################################################
def Run_Pump(dataDict):
    gpioPin = int(dataDict['gpio_pin_number'])
    pumpDuration = int(dataDict['pump_run_duration'])
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(gpioPin, GPIO.OUT)
    
    GPIO.setwarnings(False)

    GPIO.output(gpioPin, GPIO.LOW)

    if pumpDuration is "default":
        pumpDuration = 5

    for _ in range(1):


        #Activate Pump
        GPIO.output(gpioPin, GPIO.LOW)
        print('Pump Activated.')

        #time.sleep(0.5)

        GPIO.output(gpioPin, GPIO.HIGH)

        #Run pump for this duration.
        time.sleep(pumpDuration)

        #Turn off pump.
        GPIO.output(gpioPin, GPIO.LOW)
        print('Pump Deactivated.')



        returnString = 'Pump Cycle Complete.'
        #GPIO Cleanup
        GPIO.cleanup()

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
'''
import RPi.GPIO as GPIO
import time

gpio_pin_number = 21
pump_run_duration = 5

GPIO.setmode(GPIO.BOARD)
GPIO.setup(gpio_pin_number, GPIO.OUT)

#Activate Pump
GPIO.output(gpioPin, GPIO.LOW)
GPIO.output(gpioPin, GPIO.LOW)
print('Pump Activated.')

#time.sleep(0.5)

GPIO.output(gpio_pin_number, GPIO.HIGH)

#Run pump for this duration.
time.sleep(pumpDuration)

#Turn off pump.
GPIO.output(gpio_pin_number, GPIO.LOW)
print('Pump Deactivated.')

#GPIO Cleanup
GPIO.cleanup()
'''