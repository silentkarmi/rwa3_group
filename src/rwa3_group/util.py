from math import sqrt
import rospy


def compute_distance(x1, y1, x2, y2):
    return sqrt(((x2-x1)**2) + ((y2-y1)**2))

def print_partition():
    rospy.loginfo("="*11)
