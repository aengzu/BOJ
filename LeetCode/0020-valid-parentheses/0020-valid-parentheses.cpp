#include <stack>

class Solution {
    unordered_map<char, char> paren_map = {
        {'(', ')'}, {'[', ']'}, {'{', '}'}
    };
public:
    bool isValid(string s) {
        stack<char> parentheses;
        for (auto c: s) {
            if (paren_map.find(c) != paren_map.end()) {
                parentheses.push(c);
            } else {
                if (parentheses.empty()) return false;
                char target = parentheses.top();
                if (paren_map[target] != c) return false;
                parentheses.pop(); 
            }
        }
        if (!parentheses.empty()) return false;

        return true;
    }
};