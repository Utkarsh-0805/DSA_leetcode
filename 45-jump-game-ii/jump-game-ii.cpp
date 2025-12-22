class Solution {
public:
    int jump(vector<int>& nums) {
        int i=0;
        int cstp=0;
        int mxstp=0;
        int c=0;
        while(i<nums.size()-1){
            mxstp=max(mxstp,nums[i]+i);
            if(cstp==i){
                c+=1;
                cstp=mxstp;
            }
            i+=1;
        }
        return c;
    }
};