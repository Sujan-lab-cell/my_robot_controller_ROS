#!usr/bin.env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
class DrawCircle(Node):

    def __init__(self):
        super().__init__('draw_circle')
        #this is publisher that will publish to the cmd_vel topic
        self.cmd_vel_pub_=self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        #This is a timer that will call the send_velocity function every 0.5 seconds
        self.timer=self.create_timer(0.5, self.send_velocity)
        self.get_logger().info("Draw circle node has been started.")

    #This function will send a velocity command to the turtle to make it move in a circle
    def send_velocity(self):
        msg=Twist()
        msg.linear.x=2.0
        msg.angular.z=1.0
        self.cmd_vel_pub_.publish(msg)
    

def main(args=None):
    rclpy.init(args=args)
    node=DrawCircle()
    rclpy.spin(node)
    rclpy.shutdown()
