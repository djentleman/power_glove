#power_glove
===========

proof of concept usb peripheral - inspired by the [power glove of old](http://en.wikipedia.org/wiki/Power_Glove)

###Hardware

####Microprocessor

The glove is powered by an ATMEL ATMEGA 328P, as it is compatible with the arduino IDE for easy code load.

The processor is clocked at 16MHz with a quartz crystal.

####Gyroscope

I'm using a MPU6050 Accelerometer/Gyroscope to measure the position of the glove. This communicates with the microprocessor via an I<sup>2</sup>C bus, using the standard ATMEGA 328 SCL/SDA puns (A5, A4 respectively)

####Usb Interface

As you may have noticed from the code, rather than using USB HID protocol, I am using RS232 serial over usb.
The conversion is done using a FT232R chip, the glove is connected to the hosting computing via the mini usb port on this breakout.


###Firmware



###Software
