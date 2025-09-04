class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        p1=abs(z-x)
        p2=abs(z-y)
        if p1>p2:
            return 2
        elif (p1==p2):
            return 0
        else:
            return 1
        