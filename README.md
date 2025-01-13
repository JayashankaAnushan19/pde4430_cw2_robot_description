# PDE4430 Coursework-02 _ Robot Creation and achive the task (Middlesex Universityssss)

## <u>Task</u>
As per the task, we are instructed to design a robot to move around the area (world) and there will be three size of spres around the area. Robot need to bring these spres to the special goal. Robot can design any determinded desin and there is no any specific standard to design the robot.

## <u>Planning</u>
As per the coursework, i have being to develop a robot that can move towards the spheres in the area (world) and need to bring all of them to the designated place (to the Goal). In this case robot should be able to move and there should be a related gripping mechanism to catch spheres. 

## <u>Robot Creation</u>
For create the robot, I used Solid works 2021 and exported as a URDF file using a Solid work export plugin tool.
![Solidworks](https://www.rickyjordan.com/wp-content/uploads/2011/04/SolidWorksNewLogo.jpg)
**First experiment demostration in Rviz** can be view via below link;
[![Video Title](https://img.youtube.com/vi/gdx-bQXcAog/hqdefault.jpg)]([video.mp4](https://www.youtube.com/watch?v=gdx-bQXcAog))

## <u>Move the Robot</u>
Robot can be move using keyboard control (`W`,`A`,`S`,`D`) and gripper also can be conrol using keyboard (`0 - Open Gripper`, `1 - Close gripper for bigger sphere`, `2 - Close gripper for medium size sphere`, etc).

## <u>How to establish the project</u>
For establish the project need to have ROS1, Gazebo installed.
- For install ROS;
https://wiki.ros.org/ROS/Installation

- For install Gazebo
```
sudo apt install gazebo11 libgazebo11-dev
```
```
sudo apt install ros-noetic-gazebo-ros-pkgs ros-noetic-gazebo-ros-control
```

- For install Rviz
```
sudo apt install ros-noetic-rviz
```

- For Install Necessary ROS Packages
```
sudo apt install ros-noetic-ros-control ros-noetic-ros-controllers
```

- For Install Navigation Stack (for autonomous navigation)
```
sudo apt install ros-noetic-navigation
```

- For Install Robot State Publisher (for robot model and joint state)
```
sudo apt install ros-noetic-robot-state-publisher
```

- For Install Teleoperation (keyboard control for robot):
```
sudo apt install ros-noetic-teleop-twist-keyboard
```

## <u>Run the program</u>
Need to run the launch file using below command;
`roslaunch pde443_cw2_robot_description myrobot.launch`. 
World, robot and all the controllers will be start with this. It will open in Gazebo envorinment.

## <u>RQT Graph</u>
We can see the rqt graph using below command;
`rosrun rqt_graph`.

Below is the RQT Graph of this process.
![RQT_graph](img.jpg)

## <u>Demostration Video</u>
Demostration can be watch in below link.

[![Video Title](thumbnail_image_url)](video.mp4)

## <u>Title</u>
## <u>Title</u>

## <u>Further more...</u>
Program under development for mapping and automation the process with sensors (Lidar) `robot_mapping.launch`, SLAM and Rviz.