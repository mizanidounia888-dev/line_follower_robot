import rclpy
from rclpy.node import Node
import cv2
import numpy as np

class LineDetector(Node):
    def __init__(self):
        super().__init__('line_detector')
        self.get_logger().info('Line Detector démarré !')
        self.timer = self.create_timer(1.0, self.detect)
        self.count = 0

    def detect(self):
        frame = np.ones((480, 640, 3), dtype=np.uint8) * 255
        cv2.rectangle(frame, (290, 0), (350, 480), (0, 0, 0), -1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY_INV)
        moments = cv2.moments(thresh)
        if moments['m00'] > 0:
            cx = int(moments['m10'] / moments['m00'])
            cy = int(moments['m01'] / moments['m00'])
            cv2.circle(frame, (cx, cy), 10, (0, 0, 255), -1)
            self.get_logger().info(f'Ligne détectée à x={cx}, y={cy}')
        cv2.imwrite(f'/tmp/detection_{self.count}.png', frame)
        self.get_logger().info(f'Image sauvegardée : /tmp/detection_{self.count}.png')
        self.count += 1

def main(args=None):
    rclpy.init(args=args)
    node = LineDetector()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
