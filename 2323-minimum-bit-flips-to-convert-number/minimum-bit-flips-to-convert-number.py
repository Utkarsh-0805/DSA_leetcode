class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        c=0
        i=0
        x=list(format(start,'030b'))
        y=list(format(goal,'030b'))
        while(i!=30):
            if(x[i]==y[i]):
                i+=1
            else:
                c+=1
                i+=1
        return c    