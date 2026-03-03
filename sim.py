import pybullet as p 
import pybullet_data
import numpy as np 
import time

# Plan 
# 1. Load the plane, panda, and 2 cubes, set the gravity, set the cubes's friction and positions, open up the gripper
# 2. Design get_cube, open_gripper, close_gripper, stack()
# 3. Panda opens its gripper, gets the first cube and places it in a place, then it gets teh second cubes and places it on the first cube
# 4. 