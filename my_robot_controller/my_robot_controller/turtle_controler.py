#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim_msgs.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim_msgs.srv import SetPen
from functools import partial

class Turtle_controler(Node):

    def __init__(self):
        super().__init__("turtle_controller")
        self.previous_x=0
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

        if pose.x>5.5 and self.previous_x<=5.5:
            self.previous_x=pose.x
            self.get_logger().info("Set color to red")
            self.call_set_pen_service(255,0,0,3,0)
        elif pose.x<=5.5 and self.previous_x>5.5:
            self.previous_x=pose.x
            self.get_logger().info("set color to green")
            self.call_set_pen_service(0,255,0,3,0)
        
    #request
    def call_set_pen_service(self,r,g,b,width,off):
        client = self.create_client(SetPen, '/turtle1/set_pen')
        while not client.wait_for_service(1.0):
            self.get_logger().info("Waiting for service.....")
        request=SetPen.Request()
        request.r=r
        request.g=g
        request.b=b
        request.width=width
        request.off=off

        future=client.call_async(request)
        future.add_done_callback(partial(self.callback_set_pen))
#   Response
    def callback_set_pen(self,future):
        try:
            response=future.result()
        except Exception as e:
            self.get_logger().error("Service call failed: %r"%(e,))



def main(args=None):
    rclpy.init(args=args)
    node=Turtle_controler()
    rclpy.spin(node)
    rclpy.shutdown()
