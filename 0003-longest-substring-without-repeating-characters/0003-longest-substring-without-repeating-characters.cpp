#include <iostream>
#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(const string& s) {
        unordered_map<char, int> last; // 문자 -> 마지막 인덱스
        int start = 0;                  // 윈도우 왼쪽
        int ans = 0;

        for (int i = 0; i < (int)s.size(); ++i) {
            char c = s[i];
            if (last.count(c)) {
                // start는 뒤로만 이동해야 함
                start = max(start, last[c] + 1);
            }
            ans = max(ans, i - start + 1);
            last[c] = i; // 현재 위치로 갱신
        }
        return ans;
    }
};
