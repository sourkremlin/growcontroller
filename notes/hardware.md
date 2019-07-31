Grow Controller Hardware
=======================

 * Raspberry Pi - https://www.adafruit.com/product/3775
 * Raspbian SD Card - https://www.adafruit.com/product/4266
 * RPi Power Supply - https://www.adafruit.com/product/1995
 * Jumper Cables
 * Relay Power Supply
 * Touch Screen - https://www.adafruit.com/product/2718
 * Keyboard - https://www.adafruit.com/product/4112

Raspberry Pi
------------

Version 4 is the latest. Released in June 2019 so many accessories do not support it yet -- verify accessories when choosing parts. Alternatively could just use RPi version 3 -- it is more than powerful enough.

Raspbian SD Card
----------------

RPi boots from an attached SD card. Raspbian is a RPi specific linux distribution. Buying the card preloaded with Raspbian will eliminate the annoying step of imaging the SD card. 

RPi Power Supply
----------------

RPi is powered via microUSB. It's a power-only connection that utilizes the 5V and ground wires. The current draw on most 5V microUSB power supplies will drop the voltage below 5V, so this particular power supply is actually 5.25V and intended to be ~5V under load.

Touch Screen
------------

The RPI supports a couple different options for driving a screen,

 * Composite video (NTSC and PAL) via an RCA plug (the yellow socket on your TV) or SCART socket.
 * HDMI 1.3a standard output.
 * Display Serial Interface (DSI) - via unpopulated 15-way flat flex connector.

Keyboard
--------

The keyboard is wired because I don't want to mess with wireless keyboard drivers without keyboard capability. The keyboard includes a USB splitter so that it can be daisy chained with other peripherals.

Relay Power Supply
------------------

Need something that will switch mains power from low voltage/amp GPIO pins on the RPi (at least 3 connectors, more and ability to expand are desirable). This is likely the most challenging part of this device.
