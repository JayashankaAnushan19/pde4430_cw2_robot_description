#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import sys, select, termios, tty

# Save the existing terminal settings
settings = termios.tcgetattr(sys.stdin)

def getKey():
    """Function to capture keyboard input"""
    tty.setraw(sys.stdin.fileno())
    select_result = select.select([sys.stdin], [], [], 0.1)
    if select_result[0]:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


def publish_gripper_command(gripper_pub, given_position):
    """Function to publish gripper commands"""
    if given_position == 0:
        given_position = 0.5
        msg_gripper_status = "Gripper Open"
    elif given_position == 1:
        given_position = 0.2
        msg_gripper_status = "Gripper Close for Big sphere"
    elif given_position == 2:
        given_position = -0.3
        msg_gripper_status = "Gripper Close for Medium sphere"
    elif given_position == 3:
        given_position = -0.5
        msg_gripper_status = "Gripper Close for Small sphere"
    else:
        given_position = -0.5
        msg_gripper_status = "Gripper Fully Close"

    right_position = given_position * -1
    left_position = given_position

    # Create a JointTrajectory message
    traj_msg = JointTrajectory()
    traj_msg.header.stamp = rospy.Time.now() + rospy.Duration(0.1)
    traj_msg.header.frame_id = 'chassy'

    # Set the joint names for the grippers
    traj_msg.joint_names = ['right_gripper_joint', 'left_gripper_joint']

    # Create a JointTrajectoryPoint for the grippers
    point = JointTrajectoryPoint()
    point.positions = [right_position, left_position]
    point.time_from_start = rospy.Duration.from_sec(0.05)

    # Add the point to the trajectory message
    traj_msg.points.append(point)

    # Publish the message
    rospy.loginfo("Publishing gripper command: right=%f, left=%f", right_position, left_position)
    rospy.loginfo(msg_gripper_status)
    gripper_pub.publish(traj_msg)


def main():
    """Main function to control the robot"""
    rospy.init_node('my_teleop_cmds')
    pub = rospy.Publisher('/robot_wheel_controller/cmd_vel', Twist, queue_size=10)
    gripper_pub = rospy.Publisher('/robot_gripper_controller/command', JointTrajectory, queue_size=10)

    speed = 1.0
    move_cmd = Twist()

    print("...")
    print("Press '0' to Open Gripper.")
    print("Press '1' to Catch big ball.")
    print("Press '2' to Catch medium ball.")
    print("Press '3' to Catch small ball.")
    print("Press 'w', 's', 'a', 'd' to move the robot.")
    print("Press 'q' or 'e' to rotate the robot.")
    print("Press 'x' to stop.")
    print("Press Ctrl+C to quit.")
    print("...")

    rospy.on_shutdown(lambda: pub.publish(Twist()))  # Stop bot on shutdown

    try:
        while not rospy.is_shutdown():
            key = getKey()
            if key:
                if key == '0':  # Open Gripper
                    publish_gripper_command(gripper_pub, 0)
                elif key == '1':  # Close Gripper for big ball
                    publish_gripper_command(gripper_pub, 1)
                elif key == '2':  # Close Gripper for medium ball
                    publish_gripper_command(gripper_pub, 2)
                elif key == '3':  # Close Gripper for small ball
                    publish_gripper_command(gripper_pub, 3)
                elif key == 'w':  # Move forward
                    move_cmd.linear.x = speed
                    move_cmd.angular.z = 0
                    pub.publish(move_cmd)
                elif key == 's':  # Move backward
                    move_cmd.linear.x = -speed
                    move_cmd.angular.z = 0
                    pub.publish(move_cmd)
                elif key == 'a':  # Turn left
                    move_cmd.linear.x = 0
                    move_cmd.angular.z = speed
                    pub.publish(move_cmd)
                elif key == 'd':  # Turn right
                    move_cmd.linear.x = 0
                    move_cmd.angular.z = -speed
                    pub.publish(move_cmd)
                elif key == 'q':  # Rotate counter-clockwise
                    move_cmd.angular.z = speed
                    pub.publish(move_cmd)
                elif key == 'e':  # Rotate clockwise
                    move_cmd.angular.z = -speed
                    pub.publish(move_cmd)
                elif key == 'x':  # Stop
                    move_cmd = Twist()
                    pub.publish(move_cmd)
                    print("")
                    print("Stop Command !!!.")
                    print("Program Exiting...")
                    break
                else:
                    rospy.loginfo("Unknown key pressed.")
    except Exception as e:
        rospy.logerr(e)


if __name__ == '__main__':
    try:
        settings = termios.tcgetattr(sys.stdin)
        main()
    except rospy.ROSInterruptException:
        pass
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
