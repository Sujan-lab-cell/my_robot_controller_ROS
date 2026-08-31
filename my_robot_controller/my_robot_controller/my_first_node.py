#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):

    def __init__(self):
        #here we are calling the constructor of the Node class and passing the name of the node as an argument
        super().__init__("First_Node")
        self.counter_=0
        self.create_timer(1.0,self.timer_callback)
        #self get the Node name and print it in the terminal

        #self.get_logger().info("Hello from ROS2")
    def timer_callback(self):
        self.get_logger().info("Hello "+str(self.counter_))
        self.counter_+=1
def main(args=None):
    #initializing the Ros2 comunication
    rclpy.init(args=args)
    node=MyNode()
    #this will make node  t0 run inifitly
    rclpy.spin(node)
    #to stop the node
    rclpy.shutdown()
if __name__=='__main__':
    main()
