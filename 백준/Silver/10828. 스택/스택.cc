// Stack : LIFO 구조 마지막에 넣은게 가장 먼저 빠짐
// include <stack> 을 통해 인클루드
#include <iostream>
#include <stack> 

using namespace std;

stack<int> push(stack<int> st, int x) {
    st.push(x);
    return st;
}

pair<stack<int>, int> pop(stack<int> st) {
    if (st.empty()) {
        throw runtime_error("Stack Empty");
    }
    int top = st.top();
    st.pop();
    return make_pair(st, top);
}

int size(stack<int> st) {
    return st.size();
}

bool empty(stack<int> st) {
    return st.empty();
}

int top(stack<int> st) {
    if (st.empty()) {
        return -1;
    }
    else {
        return st.top();
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    stack<int> st;
    int n;
    cin >> n;
    while (n--) {
        string cmd;
        cin >> cmd;

        if(cmd == "push") {
            int x;
            cin >> x;
            st = push(st, x);
        } else if (cmd == "pop") {
            if (st.empty()) cout << -1 << endl;
            else {
                pair<stack<int>, int> result = pop(st);
                st = result.first;
                cout << result.second << endl;
            }
        } else if (cmd == "empty") {
            cout << empty(st) << endl;
        } else if (cmd == "top") {
            cout << top(st) << endl;
        } else {
            cout << size(st) << endl;
        }
    }
    return 0;
}