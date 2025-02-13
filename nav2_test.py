#!/usr/bin/env python3

import rclpy
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped 
import tf_transformations
from agent import ai_planner

def create_pose_stamped(navigator : BasicNavigator,x, y, orientation_z ):
    qx,qy,qz,qw = tf_transformations.quaternion_from_euler(0,0,orientation_z)
    pose = PoseStamped()
    pose.header.frame_id = 'map'
    pose.header.stamp = navigator.get_clock().now().to_msg()
    pose.pose.position.x = x
    pose.pose.position.y = y
    pose.pose.position.z = 0.0
    pose.pose.orientation.x = qx
    pose.pose.orientation.y = qy
    pose.pose.orientation.z = qz
    pose.pose.orientation.w = qw
    return pose


def main():
    
    # Initialize the rclpy library
    rclpy.init()
    navigiator = BasicNavigator()
    
    # Set initial pose
    
    # Quaternion from euler
    qx,qy,qz,qw = tf_transformations.quaternion_from_euler(0,0,0)
    
    initial_pose = PoseStamped()
    initial_pose.header.frame_id = 'map'
    initial_pose.header.stamp = navigiator.get_clock().now().to_msg()

    initial_pose.pose.position.x = 0.0
    initial_pose.pose.position.y = 0.0
    initial_pose.pose.position.z = 0.0

    initial_pose.pose.orientation.x = qx
    initial_pose.pose.orientation.y = qy
    initial_pose.pose.orientation.z = qz
    initial_pose.pose.orientation.w = qw


    navigiator.setInitialPose(initial_pose)
    navigiator.waitUntilNav2Active()

    response_dict = ai_planner()
    print('Goal: ',response_dict['goal'])
    print('Reasoning: ',response_dict['reasoning'])

    _ = input("Press enter to continue ...")

    waypoint_coordinates = response_dict['goal']

    waypoints = []
    for i in waypoint_coordinates:
        x_coord = i[0]/20
        y_coord = (198-i[1])/20
        waypoints.append(create_pose_stamped(navigiator,x_coord,y_coord,0))

    navigiator.followWaypoints(waypoints)

    while not navigiator.isTaskComplete():  
        feedback = navigiator.getFeedback()
        print(feedback)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
