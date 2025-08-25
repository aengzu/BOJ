#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;

    vector<pair<int, int>> items;
    items.reserve(n); // n 개 공간 미리 확보

    // 입력받기
    for (int i=0; i<n; i++) {
        int w, v;
        cin >> w >> v;
        items.push_back({w, v});
    }

    // DP 채우기 k+1개 0으로 채워둠 일단
    vector<int> dp(k+1, 0);
    
    for (auto &p: items) {
        int w = p.first;
        int v = p.second;

        for (int W=k; W>=w; --W){
            dp[W] = max(dp[W], dp[W-w]+v);
        }
    }
    
    cout << dp[k] << '\n';
    return 0;
}