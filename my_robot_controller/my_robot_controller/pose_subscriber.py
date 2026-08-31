#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim_msgs.msg import Pose


class posesubscriber(Node):

    def __init__(self):
        super().__init__("pose_subscriber")
        self.pose_subscriber_=self.create_subscription(
            Pose,
            "/turtle1/pose",
            self.pose_callback,
            10
            )

    def pose_callback(self,msg: Pose):
        self.get_logger().info("("+str(msg.x)+", "+str(msg.y) + ")")

def main(args=None):
    rclpy.init(args=args)
    node=posesubscriber()
    rclpy.spin(node)


    rclpy.shutdown()
if __name__ == "__main__":
    main()