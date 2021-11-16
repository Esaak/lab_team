import spidev
import time
import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import numpy as np

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


directionPin = 27
enablePin = 22
stepPin = 17

spi = spidev.SpiDev()

try:
    s=[]
    initSpiAdc()
    for i in range(1000):
        s.append(getAdc())
finally:
    deinitSpiAdc()
    s_str=[str(item) for item in s]
    with open('70_Pa.txt', 'w') as f:
        f.write("- Jet Lab \n\n")
        f.write('- Experiment date = {}\n'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
        f.write("- Number of samples in measure = 100\n")
        f.write("- Number of motor steps between measures = 0 \n")
        f.write("- Measures count = 1000 \n")
        f.write("\n")
        f.write("- adc12bit\n")
        f.write("\n".join(s_str))