# Joint State Node with Launch Configuration and Visualization

This repository provides a complete setup for launching a Joint State Node along with associated tools for robot visualization and state publishing. The configuration uses ROS (Robot Operating System) to process a URDF/XACRO file, publish the robot's state, and visualize the robot in RViz.

## Repository Overview
The repository contains the following essential components:

1. **Joint State Node**: A ROS node that publishes the current joint states of the robot. This is used to track joint positions, velocities, and efforts in real-time.

2. **Launch File**: The launch file coordinates the execution of several nodes and tools, including:

    - The Joint State Node
    - RViz for visualization
    - robot_state_publisher to broadcast the robot's URDF model
    - Xacro processing to generate the URDF dynamically

3. **Xacro/URDF Files**: The robot model is defined using Xacro, which allows for parameterized URDF descriptions. These files are processed during launch to generate a valid URDF for the robot.


### Setup Instructions

1. Clone the repository

´´´bash

https://github.com/ddrozo31/joint_state_pkg_g00.git

´´´


## Presentation

**EIA University**, Mechatronical Eng. - Industrial Robotics Laboratory 
*Professor*: David Rozo Osorio M.Sc. email: david.rozo31@eia.edu.co
