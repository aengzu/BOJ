#include <vector>

class Solution {
    private:
        int calSteps(int n, vector<int> &dp) {
            if (n<=2) return dp[n] = n;
            if (dp[n]!=-1) return dp[n];
            return dp[n] = calSteps(n-1, dp) + calSteps(n-2, dp);
        }
public:
    int climbStairs(int n) {
        vector<int> dp(n+1, -1);
        return calSteps(n, dp);
    }
};