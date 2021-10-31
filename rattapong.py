#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def main():
    pub = rospy.Publisher('rattapong', String, queue_size=10)
    sys.stdout.write("My name is Rattapong")
    rate = rospy.Rate(5) # 5hz
    
if __name__ == '__main__':
    main()
