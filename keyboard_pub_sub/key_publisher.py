#!/usr/bin/env python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from pynput.keyboard import Listener

# rclpy.init()
# node = rclpy.create_node('key_publisher_node')
# pub = node.create_publisher(String, 'keylogger_topic', 10)

# #function called each time a key is presssed
# def writetofile(key):
#     msg = String()
#     msg.data = "key pressed"
#     #function responsible for publishing the pressed key
#     print("pressed key is {}".format(key))
#     pub.publish(msg)

# #initialising Listener object   
# with Listener(on_press = writetofile) as l:
#     l.join()

def run_publisher(node):
    def writetofile(key):
        msg = String()
        #msg.data = "key pressed"
        #function responsible for publishing the pressed key
        msg.data = "pressed key is {}".format(key)
        node.publisher_.publish(msg)
    #initialising Listener object   
    with Listener(on_press = writetofile) as l:
        l.join()
class KeyboardPublisher(Node):
    def __init__(self):
        super().__init__('key_publisher_node')
        self.publisher_ = self.create_publisher(String, 'topic', 10)

def main(args=None):
    rclpy.init(args=args)

    keyboard_publisher = KeyboardPublisher()
    run_publisher(keyboard_publisher)
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    keyboard_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
