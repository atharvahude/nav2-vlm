#!/bin/bash
gnome-terminal -- bash -i -c "sleep 3; ros2 launch turtlebot3_gazebo turtlebot3_apartment_1.launch.py; exec bash"
sleep 10
gnome-terminal -- bash -i -c "sleep 3; ros2 launch nav2_bringup localization_launch.py map:=maps/apartment.yaml; exec bash"
sleep 10
gnome-terminal -- bash -i -c "sleep 3; ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True map:=maps/apartment.yaml; exec bash"


