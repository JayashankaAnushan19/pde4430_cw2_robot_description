#!/usr/bin/env python3

import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

def publish_gripper_command(given_position):
    right_position = given_position * -1
    left_position = given_position
    # Initialize the ROS node
    rospy.init_node('gripper_control_node', anonymous=True)

    # Create a publisher for the /robot_gripper_controller/command topic
    pub = rospy.Publisher('/robot_gripper_controller/command', JointTrajectory, queue_size=10)
    rospy.loginfo("Publisher created for /robot_gripper_controller/command")

    # Wait for subscribers to connect
    while pub.get_num_connections() == 0:
        rospy.loginfo("Waiting for subscribers to connect...")
        rospy.sleep(0.5)

    # Create a JointTrajectory message
    traj_msg = JointTrajectory()
    traj_msg.header.stamp = rospy.Time.now() + rospy.Duration(0.1)
    traj_msg.header.frame_id = 'chassy'

    # Set the joint names for the grippers
    traj_msg.joint_names = ['right_gripper_joint', 'left_gripper_joint']  # Update these names if necessary
    rospy.loginfo("Using joint names: %s", traj_msg.joint_names)

    # Create a JointTrajectoryPoint for the grippers
    point = JointTrajectoryPoint()
    point.positions = [right_position, left_position]  # Positions for right and left grippers
    point.time_from_start = rospy.Duration.from_sec(0.05)  # Time for the grippers to move (0.01 seconds)

    # Add the point to the trajectory message
    traj_msg.points.append(point)

    # Publish the message
    rospy.loginfo("Publishing gripper command: right=%f, left=%f", right_position, left_position)
    pub.publish(traj_msg)

if __name__ == '__main__':
    try:
        # x = 0.2
        # # Example: Publish a command to set right gripper to 0.5 and left gripper to -0.5
        # publish_gripper_command(x)
        # rospy.sleep(1)
        # publish_gripper_command(x*-1)

        x = 0.5
        publish_gripper_command(x)
        rospy.sleep(1)
        publish_gripper_command(0.0)
        rospy.sleep(1)
        publish_gripper_command(x)
        rospy.sleep(1)
        publish_gripper_command(-0.2)
        rospy.sleep(1)
        publish_gripper_command(x)
        rospy.sleep(1)
        publish_gripper_command(-0.5)

    except rospy.ROSInterruptException:
        pass
