#include <iostream>
#include <set>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int m;
    cin >> m;
    set<int> s;
    while(m--) {
        string cmd;
        cin >> cmd;
        if (cmd=="all"){
            s = {1,2,3,4,5,6,7,8,9,10,
           11,12,13,14,15,16,17,18,19,20};
        } else if (cmd=="empty") {
            s.clear();
        }
        else {
            int n;
            cin >> n;
            if (cmd=="add") {
                s.insert(n);
            } else if (cmd=="check") {
                cout << (s.count(n) ? 1: 0) << '\n';
            } else if (cmd=="toggle") {
                 if (s.count(n)) {
                        s.erase(n);
                    } else {
                        s.insert(n);
                    }
            } else {
                 if (s.count(n)) {
                        s.erase(n);
                    }
            }
            }
        }
    return 0;
}