import spidev
import time
import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import numpy as np

directionPin = 27
enablePin = 22
stepPin = 17

spi = spidev.SpiDev()

def initSpiAdc():
    spi.open(0, 0)
    spi.max_speed_hz = 1600000
    print ("SPI for ADC has been initialized")


def deinitSpiAdc():
    spi.close()
    print ("SPI cleanup finished")


def getAdc():
    adcResponse = spi.xfer2([0, 0])
    adc = ((adcResponse[0] & 0x1F) << 8 | adcResponse[1]) >> 1

    return adc


def getMeanAdc(samples):
    sum = 0
    for i in range(samples):
        sum += getAdc()
    
    return int(sum / samples)


def initStepMotorGpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup([directionPin, enablePin, stepPin], GPIO.OUT)
    print ("GPIO for step motor have been initialized")


def deinitStepMotorGpio():
    GPIO.output([directionPin, enablePin, stepPin], 0)
    GPIO.cleanup()
    print ("GPIO cleanup finished")


def step():
    GPIO.output(stepPin, 0)
    time.sleep(0.005)
    GPIO.output(stepPin, 1)
    time.sleep(0.005)
    

def stepForward(n):
    GPIO.output(directionPin, 1)
    GPIO.output(enablePin, 1)

    for i in range(n):
        step()

    GPIO.output(enablePin, 0)


def stepBackward(n):
    GPIO.output(directionPin, 0)
    GPIO.output(enablePin, 1)

    for i in range(n):
        step()

    GPIO.output(enablePin, 0)


def saveMeasures(measures, samplesInMeasure, motorSteps, count):
    filename = '50_mm.txt'

    with open(filename, "w") as outfile:
        outfile.write('- Jet Lab\n\n')
        outfile.write('- Experiment date = {}\n'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
        outfile.write('- Number of samples in measure = {}\n'.format(samplesInMeasure))
        outfile.write('- Number of motor steps between measures = {}\n'.format(motorSteps))
        outfile.write('- Measures count = {}\n\n'.format(count))
        
        outfile.write('- adc12bit\n')
        np.savetxt(outfile, np.array(measures).T, fmt='%d')


def showMeasures(measures, samplesInMeasure, motorSteps, count):
    print('\nExperiment date = {}'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
    print('Number of samples in measure = {}'.format(samplesInMeasure))
    print('Number of motor steps between measures = {}'.format(motorSteps))
    print('Measures count = {}\n'.format(count))
    
    plt.plot(measures)
    plt.show()


try:
    s=[]
    

    initSpiAdc()
    initStepMotorGpio()
    step()

    for i in range(100):

        s.append(getMeanAdc((100)))
        
        
        stepForward(4)

    stepBackward(400)
finally:
    deinitSpiAdc()
    deinitStepMotorGpio()
    saveMeasures(s, 100, 10, 100)
    showMeasures(s, 100, 10, 100)
