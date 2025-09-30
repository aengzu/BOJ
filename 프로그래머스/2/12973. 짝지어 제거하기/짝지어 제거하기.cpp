#include <iostream>
#include <string>
#include <stack>
using namespace std;

bool isValid(string &s) {
    unsigned int sz = s.size();
    stack<int> stk;
    
    for (int i=0; i<sz; i++) {
        char c = s[i];
        if (!stk.empty() && c==stk.top())
            stk.pop();
        else
            stk.push(c);
    }
    return stk.empty();
}

int solution(string s)
{
    int answer = -1;
    if (isValid(s))
        answer = 1;
    else 
        answer = 0;
    return answer;
}