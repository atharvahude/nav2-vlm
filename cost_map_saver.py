import rclpy
from rclpy.node import Node
import numpy as np
import cv2
from nav_msgs.msg import OccupancyGrid

class CostmapSaver(Node):
    def __init__(self):
        super().__init__('costmap_saver')

        # Subscribe to the global costmap
        self.subscription = self.create_subscription(
            OccupancyGrid,
            '/global_costmap/costmap',  # Ensure the topic name is correct
            self.costmap_callback,
            10)

        self.get_logger().info("Subscribed to /global_costmap/costmap, waiting for message...")

    def costmap_callback(self, msg):
        self.get_logger().info("Received costmap, processing...")

        # Convert occupancy grid data to numpy array
        width = msg.info.width
        height = msg.info.height
        costmap_data = np.array(msg.data, dtype=np.int8).reshape((height, width))

        # Normalize costmap values to 0-255 for visualization
        image = np.uint8((costmap_data + 1) * 127)  # Shift -1 to 0 and 100 to 255
        image = cv2.flip(image, 0)  # Flip to match coordinate system

        # Save image
        cv2.imwrite('global_costmap.png', image)
        self.get_logger().info("Saved global costmap image as global_costmap.png")

        # Unsubscribe from topic
        self.destroy_subscription(self.subscription)
        self.get_logger().info("Unsubscribed from /global_costmap/costmap")

        # Shutdown ROS after saving
        self.get_logger().info("Shutting down node after saving the image.")
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = CostmapSaver()
    executor = rclpy.executors.SingleThreadedExecutor()
    executor.add_node(node)

    try:
        executor.spin_once()  # Process only one message
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        # rclpy.shutdown()

if __name__ == '__main__':
    main()
