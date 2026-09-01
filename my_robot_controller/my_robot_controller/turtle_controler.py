#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim_msgs.msg import Pose
from geometry_msgs.msg import Twist
class Turtle_controler(Node):

    def __init__(self):
        super().__init__("turtle_controller")
        self.cmd_vel_publislisher_=self.create_publisher(
            Twist,"/turtle1/cmd_vel",10
        )
        self.pose_subscriber=self.create_subscription(
            Pose,
            "/turtle1/pose",
            self.pose_call_back,10
        )
        self.get_logger().info("Trutle controller has been started.")

    def pose_call_back(self,pose:Pose):
        cmd=Twist()
        if pose.x>9.0 or pose.x<2.0 or pose.y>9.0 or pose.y<2.0:
            cmd.linear.x=1.0
            cmd.angular.z=0.9
        else:
            cmd.linear.x=5.0
            cmd.angular.z=0.0
        self.cmd_vel_publislisher_.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node=Turtle_controler()
    rclpy.spin(node)
    rclpy.shutdown()
