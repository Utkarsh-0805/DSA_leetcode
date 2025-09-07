class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        l=[]
        i=0
        for i in range(1,n//2+1):
            l.append(i)
            l.append(-1*(i))
        if(n%2==1):
            l.append(0)
        return l
        