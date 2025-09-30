#include<string>
#include <iostream>
#include <stack>

using namespace std;

bool solution(string s)
{
    bool answer = true;
    stack<int> stk;
    
    for (char c: s) {
        if (c==')') {
            if (stk.empty() || stk.top()!='(')
                answer = false;
            else
                stk.pop();
        } else {
            stk.push('(');
        }
    }
    
    if (!stk.empty())
        answer = false;

    return answer;
}