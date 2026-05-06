# 🤖 Line Follower Robot - ROS2

Robot autonome suiveur de ligne développé avec ROS2 Jazzy et Gazebo Harmonic.

## 📋 Description

Ce projet implémente un robot différentiel capable de détecter et suivre
une ligne noire sur un sol blanc en utilisant la vision par ordinateur (OpenCV)
et un contrôleur PID.

## 🛠️ Technologies utilisées

- ROS2 Jazzy - Framework robotique
- Gazebo Harmonic - Simulateur physique 3D
- OpenCV 4.6 - Détection de ligne par vision
- Python 3.12 - Langage de programmation
- URDF - Description du robot
- PID Controller - Contrôle de trajectoire

## 📁 Structure du projetline_follower_robot/

├── urdf/
│   └── robot.urdf          # Description du robot
├── launch/
│   └── start.launch.py     # Fichier de lancement
├── worlds/
│   └── line_world.sdf      # Monde Gazebo avec ligne
├── line_follower_robot/
│   ├── line_detector.py    # Nœud détection de ligne
│   └── pid_controller.py   # Nœud contrôle PID
├── setup.py
└── package.xml
## 🚀 Installation

### Prérequis
- Ubuntu 24.04
- ROS2 Jazzy
- Gazebo Harmonic
- Python 3.12

### Cloner le projet
mkdir -p ~/line_follower_ws/src
cd ~/line_follower_ws/src
git clone https://github.com/Amayas420/line_follower_robot.git


### Compiler
cd ~/line_follower_ws
colcon build
source install/setup.bash


## ▶️ Lancement

Terminal 1 - Lancer Gazebo + Robot :
ros2 launch line_follower_robot start.launch.py


Terminal 2 - Lancer la détection de ligne :
ros2 run line_follower_robot line_detector


Terminal 3 - Lancer le contrôle PID :
ros2 run line_follower_robot pid_controller


## 🔧 Architecture ROS2
Gazebo ──► /image_raw ──► line_detector ──► /cmd_vel ──► Robot
│
pid_controller

## 📊 Paramètres PID

| Paramètre | Valeur | Description |
|-----------|--------|-------------|
| Kp | 0.01 | Gain proportionnel |
| Ki | 0.0  | Gain intégral |
| Kd | 0.005| Gain dérivé |
