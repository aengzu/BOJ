class Solution {
public:
    int rob(vector<int>& nums) {
        int sz = nums.size();
        vector<int> mon(sz, 0);

        if (sz==1) return nums[0];
        if (sz==2) return max(nums[0], nums[1]);

        mon[0] = nums[0];
        mon[1] = max(nums[0], nums[1]);
        for (int i=2; i<sz; ++i) {
            mon[i] = max(mon[i-2]+nums[i], mon[i-1]);
        }
        return mon[sz-1];
    }
};


