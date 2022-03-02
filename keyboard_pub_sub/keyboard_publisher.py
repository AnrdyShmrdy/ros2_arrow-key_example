# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from pynput import keyboard
from rclpy.node import Node
from pynput.keyboard import Listener
from std_msgs.msg import String

# def on_press(key):
#     if key == keyboard.Key.up:
#         print('key {0} pressed'.format(key))

#         #self.msg.data = 'Key.up pressed'
#     if key == keyboard.Key.down:
#         print('key {0} pressed'.format(key))
#         #self.msg.data = 'Key.down pressed'
#     if key == keyboard.Key.left:
#         print('key {0} pressed'.format(key))
#         #self.msg.data = 'Key.left pressed'
#     if key == keyboard.Key.right:
#         print('key {0} pressed'.format(key))
#         #self.msg.data = 'Key.right pressed'
#     else:
#         print('No Key Pressed')
#         #self.msg.data = 'No key pressed'

# def on_release(key):
#     if key == keyboard.Key.up:
#         print('{0} released'.format(key))
#         #self.msg.data = 'Key.up released'
#     if key == keyboard.Key.down:
#         print('{0} released'.format(key))
#         #self.msg.data = 'Key.down released'
#     if key == keyboard.Key.left:
#         print('{0} released'.format(key))
#         #self.msg.data = 'Key.left released'
#     if key == keyboard.Key.right:
#         print('{0} released'.format(key))
#         #self.msg.data = 'Key.right released'
#     if key == keyboard.Key.esc:
#             # Stop listener
#             return False
#     else:
#         print('No Key relesed')
#         #self.msg.data = 'No key released'

def run_publisher(node):
    def onpress(key):
        msg = String()
        #msg.data = "key pressed"
        #function responsible for publishing the pressed key
        msg.data = "pressed key is {}".format(key)
        node.publisher_.publish(msg)
    def onrelease(key):
        msg = String()
        #msg.data = "key released"
        #function responsible for publishing the released key
        msg.data = "released key is {}".format(key)
        node.publisher_.publish(msg)
    #initialising Listener object   
    with Listener(on_press = onpress, on_release = onrelease) as l:
        l.join()
class KeyboardPublisher(Node):
    def __init__(self):
        super().__init__('keyboard_publisher')
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
