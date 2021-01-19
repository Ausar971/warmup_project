#!/usr/bin/env python3

import rospy

from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from math import radians


class DriveInSquare(object):
	""" This node walks the robot to wall and stops """
	
	def __init__(self):
		rospy.init_node('drive_in_square')
		self.move = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
		
	
	def drive(self):

		
		#forward.linear.x = 0.5  #move forward really slowly
		stop = Twist(linear=Vector3(0, 0, 0), angular=Vector3(0, 0, 0))    #don't move 
		forward = Twist(linear=Vector3(.1, 0, 0), angular=Vector3(0, 0, 0))
		turnRight = Twist(linear=Vector3(0, 0, 0), angular=Vector3(0, 0, 0.3))
		#turnRight = Twist()
		#turnRight.angular.z = .2 #turn but in place not in while moving
		
		#r = rospy.Rate(10)
		
		
		while self.move.get_num_connections() < 1: #found on ros website to help with connections, otherwise spins in circle
            		pass
		
		#self.move.publish(forward)  #move car forward
		#rospy.sleep(10) # is tis the correct way to get duration?
		
		
		
		for i in range(4):
		
			self.move.publish(forward) #move forward
			rospy.sleep(6)
			self.move.publish(stop) #stop car
			#rospy.sleep(2)
			
			self.move.publish(turnRight) #turn car right 
			rospy.sleep(5)
			self.move.publish(stop) 
		

		
			
if __name__ == '__main__':
	moveSquare = DriveInSquare()
	moveSquare.drive()
