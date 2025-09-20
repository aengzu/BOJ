#include <iostream>
#include <queue>

using namespace std;

// dp[1] = (4, 10)
// dp[2] = (7, 20)
// dp[3] = 
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	static int n;
	cin >> n;

	// n+1일까지 접근(종료 시점이 n+1일 수 있으므로) -> n+2로 확보
	vector<pair<int, int>> plans(n + 2);
	for (int i = 1; i <= n; i++) {
		cin >> plans[i].first >> plans[i].second;
	}

	// dp[day]에 (day, 그 시점까지의 이익)들을 저장
	vector<vector<pair<int, int>>> dp(n + 2);

	int ans = 0;

	for (int i = 1; i <= n; i++) {
		// '해당 일을 안 하는' 기본값(0)을 넣어 두되
		dp[i].push_back(make_pair(i, 0));

		// i일 시작 시점까지의 최대 이익 계산
		int base_dp_i = 0;
		for (auto& st : dp[i]) base_dp_i = max(base_dp_i, st.second);

		//i일의 최대 이익을 i+1로 넘기기 (그날 스킵)
		if (i+1 <= n + 1) {
			dp[i + 1].push_back(make_pair(i + 1, base_dp_i));
		}
		
		// i일에 일해서 끝나는 날로 이익 넘기기
		int next_t = i + plans[i].first;
		int next_p = base_dp_i + plans[i].second;

		if (next_t <= n + 1) {
			dp[next_t].push_back(make_pair(next_t, next_p));
			ans = max(ans, next_p);
		}

		// 현재까지 최댓값 갱신(일을 더 못해도 n 또는 n+1에 도달 가능)
		ans = max(ans, base_dp_i);
	}
	cout << ans << '\n';
	return 0;
}