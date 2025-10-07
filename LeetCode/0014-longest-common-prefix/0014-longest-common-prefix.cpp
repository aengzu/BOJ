#include <algorithm>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string answer = "";
        int sz = strs.size();
        int min_str = 1e9;

        for (int i=0; i<sz; i++) {
            min_str = min((int)strs[i].length(), min_str);
        }


        for (int i=0; i<min_str; i++) {
            bool this_char_ok = true;
            char cur = strs[0][i];
            for (int j=1; j<sz; j++) {
                if (cur != strs[j][i])
                    this_char_ok = false;
                cur = strs[j][i];
            }
            if (this_char_ok)
                answer += strs[0][i];
            else
                break;
        }
        
        return answer;
    }
};