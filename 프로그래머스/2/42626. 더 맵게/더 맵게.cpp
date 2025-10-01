#include <string>
#include <vector>
#include <queue>
#include <iostream>

// 모든 음식 스코빌 K 이상으로 
using namespace std;

int calScoville(int large, int small) {
    return small + (large*2);
}

int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int, vector<int>, greater<int>> minHeap;
    
    for (auto s: scoville) {
        minHeap.push(s);
    }
    
    // 힙이 비어있지 않고, 윗 원소 스코빌 지수 k 미만이면 반복
    while (!minHeap.empty() && minHeap.top() < K) {
        int top = minHeap.top(); minHeap.pop();
        if (minHeap.empty()) {
            answer = -1;
            break;
        }
        int top2 = minHeap.top(); minHeap.pop();
        int mixed = calScoville(top2, top);
        minHeap.push(mixed);
        answer++;
    }
    return answer;
}