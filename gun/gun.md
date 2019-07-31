<h1>Laser Gun Documentation</h1>

***
<h3>Overview</h3>

The laser gun was designed for use with the scooters segmentation. It allows you to
run the object selection either via the laser pointer alone, or on trigger pull. System
is based of a teensy 3.2 microcontroller, and rosserial. 3D model, wiring schematic, and
code are included in the gun directory. Gun publishes a boolean telling if trigger is 
pulled on /pushed

***
<h3>Installation</h3>
<h5>Recommended installation instructions included below:</h5>
ROSSerial and ROSSerial Arduino

* sudo apt-get install ros-<VERSION>-rosserial-arduino

* sudo apt-get install ros-<VERSION>-rosserial
***

<h4>Optional Installs-If you intend to alter microcontroller</h4>
<h5>Arduino IDE</h5>
follow the instructions on this page

https://www.arduino.cc/en/guide/linux 
***

<h5>ros_lib: a ROS extension for the arduino IDE</h5>
Navigate to Arduino Sketchbook

* cd <sketchbook>/libraries
* rm -rf ros_lib
* rosrun rosserial_arduino make_libraries.py\
\
Additional information can be found here:
http://wiki.ros.org/rosserial_arduino/Tutorials/Arduino%20IDE%20Setup

***
<h5>Teensy-Arduino Requirements</h5>
Follow the instructions below:\
https://www.pjrc.com/teensy/tutorial.html
***
<h3>3D Modeling and Parts</h3>
STL Files are included in the gun directory. Prints where done at 60% infill value. A draw up of
the wiring diagram is included in the directory as well. Parts list linked at end of file.

<h3>Usage</h3>
Prerequisite Steps:

* Ensure The Teensy is properly flashed with gun sketch
* Connect Teensy to USB Port and Ensure everything is properly wired
* Figure out which port the Teensy connects to. It should follow the pattern /dev/ttyACM*
* Ensure that the acount is added to the dialout group for proper communication

Steps To Run Just Gun:
1. rosrun rosserial_python serial_node.py /dev/ttyACM*  (insert proper port number here)
2. python .../ur_scooter/scripts/gun.py

Steps To Run With Scooter:
1. rosrun rosserial_python serial_node.py /dev/ttyACM*  (insert proper port number here)
2. Run scooter as regular with gun branch's code
***

<h3>Misc.</h3>
Any questions feel free to ask\
-Patrick\
Patrick_Hoey1@student.uml.edu
***
<h5>parts List</h5>
* 30 mm M3 Screws (cut to length)
* 2 laser diodes:  
https://www.adafruit.com/product/1054?gclid=Cj0KCQjwov3nBRDFARIsANgsdoGiIkk4k0ZG4ME554u0F5iSnqDx9azqsjbdTmCDVKtSUBYzrG3WIwYaAhJ3EALw_wcB
* Teensy 3.2:\
https://www.amazon.com/PJRC-6485230-Teensy-3-2/dp/B015M3K5NG/ref=sr_1_2?crid=3IWCNK6HYUPVE&keywords=arduino%2Bteensy&qid=1560799316&s=gateway&sprefix=arduino%2Btee%2Caps%2C128&sr=8-2&th=1
* Thread Locks:\
https://www.amazon.com/Uxcell-a16041800ux0833-Knurled-Threaded-Embedded/dp/B01IYWUUH8/ref=asc_df_B01IYWUUH8/?tag=hyprod-20&linkCode=df0&hvadid=194876912818&hvpos=1o2&hvnetw=g&hvrand=9659581371199503507&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9001898&hvtargid=pla-315421880105&th=1
* Switches-They can be easily opened and switched to momentary:
https://www.amazon.com/Uxcell-a12081400ux0273-Momentary-Button-Switch/dp/B0094GP7SQ/ref=zg_bs_5739464011_95?_encoding=UTF8&psc=1&refRID=360714WEBVZN3G7BFQ5X
