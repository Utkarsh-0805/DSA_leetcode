class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        s1=0
        s2=0
        i=1
        while(i<n+1):
            if(i%m==0):
                s1=s1+i
            else:
                s2=s2+i
            i+=1
        return (s2-s1)

        