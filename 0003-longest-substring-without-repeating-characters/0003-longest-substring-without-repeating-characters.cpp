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
                nowLen = 0;
                int sIdx = hmap[c]+1;
                hmap.clear();
                //전체 클리어말고 그러면 해당 인덱스 전에 잇ㅇ는 녀석들 삭제는?
                for (int j=sIdx; j<i; j++) {
                    hmap[s[j]] = j;
                    nowLen++;
                }
            }
                
            hmap.insert({c, i});
            nowLen++;
            answer = max(answer, nowLen);
        }

        answer = max(answer, nowLen);
        return answer;
    }
};