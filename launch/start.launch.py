from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg_path = get_package_share_directory('line_follower_robot')
    world_file = os.path.join(pkg_path, 'worlds', 'line_world.sdf')
    urdf_file = os.path.join(pkg_path, 'urdf', 'robot.urdf')

    with open(urdf_file, 'r') as f:
        robot_description = f.read()

    return LaunchDescription([

        # Lancer Gazebo
        ExecuteProcess(
            cmd=['gz', 'sim', world_file],
            output='screen'
        ),

        # Bridge ROS2 <-> Gazebo
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=[
                '/image_raw@sensor_msgs/msg/Image@gz.msgs.Image',
                '/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist',
            ],
            output='screen'
        ),

        # Publier le robot
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{'robot_description': robot_description}],
            output='screen'
        ),

        # Spawner le robot
        Node(
            package='ros_gz_sim',
            executable='create',
            arguments=[
                '-name', 'line_follower',
                '-topic', 'robot_description',
                '-x', '0.0',
                '-y', '0.0',
                '-z', '0.1'
            ],
            output='screen'
        ),

    ])
    
