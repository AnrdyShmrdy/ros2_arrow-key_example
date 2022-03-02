#!/usr/bin/env python
import rclpy
from std_msgs.msg import String
from pynput.keyboard import Listener
rclpy.init()
node = rclpy.create_node('key_publisher_node')
pub = node.create_publisher(String, 'keylogger_topic', 10)

#function called each time a key is presssed
def writetofile(key):
    msg = String()
    msg.data = "key pressed"
    #function responsible for publishing the pressed key
    print("pressed key is {}".format(key))
    pub.publish(msg)

#initialising Listener object   
with Listener(on_press = writetofile) as l:
    l.join()

