# warmup_project
## drive_in_square project

### High-level overview
I used a time approach to have the robot drive in a circle. It drives forward for 6 seconds and then turns right for 5 seconds. This is because the car is set to move forward at .1 and turn at .3 radians/sec. After completing four turns the robot stops. 

I am running into a bug right now where the initial drive forward and turn work perfectly but for the subsequent ones the robot does not move. It moces forward very slightly and turns very slightly. I am currently trying to fix this problem but I am stuck. I just realized that this is working correctly, but I think my internet was not good enough to update the screen/send requests so it looked stuck. Will need to work on this in the future. Due to this internet problem I was not able to fine tune my turns as much and will improve them in future updates. 

### Code Overview 

First the code creates a new node and publisher to /cmd_vel in the __init__ section. In the drive method, the code creates three different movement states. Forward, Stop, and TurnRIght. Then the code checks to make sure there is a connection and the robot is subscribed to the /cmd_vel topic that was initiated in def __init__ portion of the code (found on ROS stack overflow as my robot would spin in circles over and over with out it).  Finally, the code loops 4 times and has the robot move forward and then turn right by sending messages using the publisher. Finally the robot is halted. 


### Drive in Square Demo

![gif of robot test](/driveinsquarenew.gif)
