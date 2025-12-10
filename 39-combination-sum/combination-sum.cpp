class Solution {
public:
    set<vector<int>>s;
    void acb(vector<int>& c,vector<int> &cmb,vector<vector<int>>&a, int i,int t){
    if (i==c.size() || t<0){
        return ;
    }
    if(t==0){
        if(s.find(cmb)==s.end()){
            a.push_back(cmb);
            s.insert(cmb);
        }
        return ;}
        cmb.push_back(c[i]);
        acb(c,cmb,a,i+1,t-c[i]);
        acb(c,cmb,a,i,t-c[i]);
        cmb.pop_back();
        acb(c,cmb,a,i+1,t);

    }
    vector<vector<int>> combinationSum(vector<int>& c, int t) {
        vector<int>cmb;
        vector<vector<int>>a;
        acb(c,cmb,a,0,t);
        return a;
    }
};