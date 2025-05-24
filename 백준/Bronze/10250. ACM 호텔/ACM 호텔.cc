#include <iostream>

using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int h, w, n;
        cin >> h >> w >> n;
        int ans = 0;
        int tmp = n % h;
        if (tmp == 0) {
            tmp = h;
            ans = (n / h) + tmp * 100;
        }
        else {
            ans = (1 + n / h) + tmp * 100;
        }
        cout << ans << endl;
    }
    return 0;
}