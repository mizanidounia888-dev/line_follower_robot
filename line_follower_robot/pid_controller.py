import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import numpy as np
import cv2

class PIDController(Node):
    def __init__(self):
        super().__init__('pid_controller')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.control_loop)

        # Paramètres PID
        self.kp = 0.01
        self.ki = 0.0
        self.kd = 0.005

        self.prev_error = 0.0
        self.integral = 0.0
        self.image_center = 320

        self.get_logger().info('PID Controller démarré !')

    def control_loop(self):
        # Simuler position de la ligne
        line_x = 320

        # Calcul erreur
        error = self.image_center - line_x
        self.integral += error
        derivative = error - self.prev_error
        self.prev_error = error

        # Calcul correction PID
        correction = (self.kp * error +
                      self.ki * self.integral +
                      self.kd * derivative)

        # Publier commande
        msg = Twist()
        msg.linear.x = 0.2
        msg.angular.z = correction
        self.publisher.publish(msg)

        self.get_logger().info(
            f'Erreur={error:.2f} Correction={correction:.4f}'
        )

def main(args=None):
    rclpy.init(args=args)
    node = PIDController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    
