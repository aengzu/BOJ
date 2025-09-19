#include <iostream>
#include <vector>
using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	static int n;

	cin >> n;
	vector<int> candidates(n);

	for (int i = 0; i < n; i++)
		cin >> candidates[i];

	int b, c;
	cin >> b >> c;

	long long int ans = 0;


	for (int i = 0; i < candidates.size(); ++i)
	{
		candidates[i] -= b;
		ans++;
		if (candidates[i] > 0)
		{
			ans += (candidates[i] + c - 1) / c;
		}
	}

	cout << ans << '\n';
	return 0;
}