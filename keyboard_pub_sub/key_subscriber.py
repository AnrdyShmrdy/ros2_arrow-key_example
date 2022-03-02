#!/usr/bin/env python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# # #function for printing the message on terminal
# # def callback(data):
# #     rospy.loginfo("%s", data.data)
    
# # def listener():
# #     rospy.init_node('key_subscriber_node', anonymous=True)    #initialising subscriber node
# #     rospy.Subscriber("keylogger_topic", String, callback)
# #     # spin() simply keeps python from exiting until this node is stopped
# #     rospy.spin()
   
# # if __name__ == '__main__':
# #     listener()

# #function for printing the message on terminal
# def callback(data):
#     #rclpy.loginfo("%s", data.data)
#     print("success")
    
# def listener():
#     rclpy.init()
#     node = rclpy.create_node("key_subscriber_node")
#     node.create_subscription(String, 'keylogger_topic', callback, 10)
#     # spin() simply keeps python from exiting until this node is stopped
#     rclpy.spin(node)
   
# # if __name__ == '__main__':
# #     listener()
# listener()

class KeyboardSubscriber(Node):

    def __init__(self):
        super().__init__('keyboard_subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    keyboard_subscriber = KeyboardSubscriber()

    rclpy.spin(keyboard_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    keyboard_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
