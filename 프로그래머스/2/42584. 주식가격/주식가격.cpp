#include <string>
#include <vector>
#include <stack>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer(prices.size());
    stack<int> stk;
    int priceNum = prices.size();
    
    for (int i=0; i<priceNum; i++) {
        while (!stk.empty() && prices[stk.top()] > prices[i]) {
            // 가격 떨어짐
            answer[stk.top()] = i - stk.top();
            stk.pop();
        }
        stk.push(i);
    }
    while (!stk.empty()) {
        // 아지갂지 남아있다면 
        answer[stk.top()] = priceNum - stk.top() - 1;
        stk.pop();     
    }

    return answer;
}