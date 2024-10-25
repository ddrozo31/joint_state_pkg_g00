import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import math
import time

class JointStatePublisher(Node):
    def __init__(self):
        super().__init__('joint_state_publisher')
        self.publisher_ = self.create_publisher(JointState, 'joint_states', 10)
        self.timer = self.create_timer(0.1, self.publish_joint_states)  # 10 Hz
        self.joint_state = JointState()
        self.joint_state.name = ['world2odom_joint', 'odom2base_joint', 'joint3']
        self.joint_state.position = [0.0, 0.0, 0.0]
        self.start_time = time.time()

    def publish_joint_states(self):
        current_time = time.time() - self.start_time

        # Update the joint positions (e.g., a sine wave for joint1)
        self.joint_state.header.stamp = self.get_clock().now().to_msg()
        self.joint_state.position[0] = math.sin(current_time)  # joint1
        self.joint_state.position[1] = math.cos(current_time)  # joint2
        self.joint_state.position[2] = math.sin(2 * current_time)  # joint3

        # Publish the message
        self.publisher_.publish(self.joint_state)
        self.get_logger().info(f'Publishing: {self.joint_state.position}')

def main(args=None):
    rclpy.init(args=args)
    node = JointStatePublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
