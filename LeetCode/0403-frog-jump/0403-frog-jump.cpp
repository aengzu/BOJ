#include <vector>
#include <iostream>
#include <unordered_map>

typedef pair<int, int> state;

using namespace std;

class Solution {
private:
    bool dfs(state st, vector<int>& stones, unordered_map<int, int>& pos_to_idx, map<state, bool>& dp) {
        int now_pos = st.first;
        int k = st.second;

        if (now_pos==stones.back()) return true;
        if (dp.count(st)) return dp[st];
        if (k <= 0) return dp[st] = false;

        for (int i=-1; i<=1; i++) {
            int new_k = k + i;
            int new_pos = now_pos + new_k;

            // cant reach the stone -> SKIP
            if (pos_to_idx.find(new_pos) == pos_to_idx.end()) continue;
            if (dfs(make_pair(new_pos, new_k), stones, pos_to_idx, dp)) 
                return dp[st] = true;
        }
        return dp[st] = false;
    }

public:
    bool canCross(vector<int>& stones) {
        unordered_map<int, int> pos_to_idx;
        map<state,bool> dp;
        if (stones[0]!=0 || stones[1] != 1) return false;

        for (int i=0; i<stones.size(); i++) {
            pos_to_idx[stones[i]] = i;
        }

        return dfs(make_pair(1, 1), stones, pos_to_idx, dp);
    }
};