#include <iostream>
#include <algorithm>
#include <climits>

class Solution {
    static constexpr int INF = 1e9;
    const vector<vector<int>>* tri = nullptr;
    vector<vector<int>> memo;
    int n = 0;
private:
    int dfs(int r, int c) {
        if (r==n-1) return (*tri)[r][c];
        int &ret = memo[r][c];
        if (ret != INF) return ret;
        int a = dfs(r+1, c);
        int b = dfs(r+1, c+1);
        return ret = (*tri)[r][c] + min(a, b);
    }
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        tri = &triangle;
        n = (int)triangle.size();
        if(n==0) return 0;
        memo.assign(n, {});

        for (int r = 0; r < n; ++r) 
            memo[r].assign((int)(*tri)[r].size(), INF);


        return dfs(0, 0);      
    }
};

