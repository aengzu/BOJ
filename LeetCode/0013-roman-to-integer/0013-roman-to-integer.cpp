#include <string>
#include <unordered_map>
#include <queue>
using namespace std;

class Solution {
    unordered_map<string, int> romanMap = {
        {"I", 1}, {"V", 5}, {"X", 10}, {"L", 50},
        {"C", 100}, {"D", 500}, {"M", 1000},
        {"IV", 4}, {"IX", 9}, {"XL", 40}, {"XC", 90},
        {"CD", 400}, {"CM", 900}
    };
public:
    int romanToInt(string s) {
        int answer = 0;
        char cur, next;
        queue<char> str;

        for (char c : s) str.push(c);

        while (!str.empty()) {
            cur = str.front();
            str.pop();

            if (!str.empty()) {
                next = str.front();
                string two;
                two += cur; two += next;
                if (romanMap.count(two)) {
                    answer += romanMap[two];
                    str.pop();
                    continue;
                }
            }

            string one(1, cur);
            if (romanMap.count(one)) {
                answer += romanMap[one];
            }
        }
        return answer;
    }
};
