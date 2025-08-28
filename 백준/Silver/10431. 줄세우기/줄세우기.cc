#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int p;
    cin >> p;

    while (p--) {
        int t;
        int cnt = 0;
        cin >> t;
        
        int students[20];
        for (int i=0; i<20; i++) {
            cin >> students[i];
        }

        for (int i=0; i < 20; i++) {
            for (int j=0; j<i; j++) {
                if (students[i] < students[j]) {
                    cnt++;
                }
            }
        }

        cout << t << ' ' << cnt << '\n';
    }
    return 0;
}