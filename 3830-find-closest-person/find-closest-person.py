class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        

        p1=(z-x)
        if p1<0:
            p1=p1*(-1)
        p2=(z-y)
        if p2<0:
            p2=p2*(-1)
        if p1>p2:
            return 2
        elif (p1==p2):
            return 0
        else:
            return 1
        