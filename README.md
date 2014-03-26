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

####I<sup>2</sup>C

In order to read the gyroscope I am using the Wire, I2Cdev and MPU6050 arduino libraries.

####Serial

After reading the data from the I<sup>2</sup> device, I am scaling the data to a more manageable size, and formatting it into an unsigned 5 bit integer. The data is sent to the host machine in one byte packets, made up of a 3 bit ID 'header', and a 5 bit data 'body'. For instance the 'y' value from the gyroscope has an ID of 1, and if the data read from the accelerometer happened to be 18 (-14 if it were a signed integer), then the data packet would be:

    001 10010



###Software
