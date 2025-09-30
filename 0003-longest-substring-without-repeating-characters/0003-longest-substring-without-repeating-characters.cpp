#include <iostream>
#include <unordered_map>
#include <algorithm>

/// z z a b k c a
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int answer = (s.size()>0 ? 1 : 0);
        int nowLen = 0;
        unordered_map<char, int> hmap;
        for (int i=0; i<s.size(); i++) {
            char c = s[i];
            if (hmap.count(c)) {
                answer = max(answer, nowLen);
                nowLen = 0;
                int sIdx = hmap[c]+1;
                hmap.clear();
                for (int j=sIdx; j<i; j++) {
                    hmap[s[j]] = j;
                    nowLen++;
                }
            }
                
            hmap.insert({c, i});
            nowLen++;
        }

        answer = max(answer, nowLen);
        return answer;
    }
};