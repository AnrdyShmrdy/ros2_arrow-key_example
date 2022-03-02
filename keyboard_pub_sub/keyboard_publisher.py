import rclpy
from pynput import keyboard
from rclpy.node import Node
from pynput.keyboard import Listener
from std_msgs.msg import String

def run_publisher(node):
    def onpress(key):
        msg = String()

        if key == keyboard.Key.up:
            msg.data = 'Up key pressed'
        elif key == keyboard.Key.down:
            msg.data = 'Down key pressed'
        elif key == keyboard.Key.left:
            msg.data = 'Left key pressed'
        elif key == keyboard.Key.right:
            msg.data = 'Right key pressed'
        # if key == keyboard.Key.esc:
        # # Stop listener
        #      return False
        else:
            msg.data = 'Non-arrow key pressed'

        node.publisher_.publish(msg)
    def onrelease(key):
        msg = String()
        if key == keyboard.Key.up:
            msg.data = 'Up key released'
        elif key == keyboard.Key.down:
            msg.data = 'Down key released'
        elif key == keyboard.Key.left:
            msg.data = 'Left key released'
        elif key == keyboard.Key.right:
            msg.data = 'Right key released'
        else:
            msg.data = 'Non-arrow key released'
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
