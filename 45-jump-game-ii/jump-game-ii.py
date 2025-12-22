class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        cs=0
        ms=0
        i=0
        while i<len(nums)-1:
            ms=max(ms,nums[i]+i)
            if cs==i:
                c+=1
                
                cs=ms
            i+=1
        return c