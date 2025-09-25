#include <iostream>
#include <vector>
#include <string>
#include <limits>

using namespace std;


int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N = 0;
	cin >> N;
	cin.ignore(numeric_limits<streamsize>::max(), '\n');

	vector<string> board;
	board.reserve(N);

	for (int i = 0; i < N; i++) {
		string row;
		getline(cin, row);
		board.push_back(row);
	}

	pair<int, int> heart = { 0, 0 };
	bool found = false;
	for (int i = 0; i < N && !found; i++) {
		for (int j = 0; j < N; j++) {
			if (board[i][j] == '*') {
				{
					heart = { i + 1, j };
					found = true;
					break;
				}
			}
		}
	}

	// 좌 우 하 
	int dr[5] = { 0, 0, 1, 1, 1};
	int dc[5] = { -1, 1, 0, 0, 0};

	// 허 좌팔 우팔 좌다리 우다리
	vector<int> v(5, 0);
	pair<int, int> wai = { 0,0 };


	// 심장 기준 팔, 허리, 
	for (int d_num = 0; d_num < 3; d_num++)
	{
		int r = heart.first;
		int c = heart.second;

		while (true) {
			int n_r = r + dr[d_num];
			int n_c = c + dc[d_num];


			if (n_r >= N || n_r < 0 || n_c < 0 || n_c >= N)
			{
				break;
			}

			if (board[n_r][n_c] == '*') {
				v[d_num]++;
				r = n_r;
				c = n_c;
			}
			else {
				if (d_num == 2)
					wai = { n_r - 1, n_c };
				break;
			}
		}
	}

	// 허리 기준 왼달, 우달
	for (int d_num = 3; d_num < 5; d_num++)
	{
		int r = wai.first;
		int c = wai.second;

		if (d_num == 3)
		{
			r = r + 1;
			c = c - 1;
		}
		else {
			r = r + 1;
			c = c + 1;
		}
		v[d_num]++;

		while (true) {
			int n_r = r + dr[d_num];
			int n_c = c + dc[d_num];
			if (n_r < 0 || n_c < 0 || n_r >= N || n_c >= N)
			{
				break;
			}

			if (board[n_r][n_c] == '*') {
				v[d_num]++;
				r = n_r;
				c = n_c;
			}
			else {
				break;
		}
	}
	}

	cout << heart.first+1 << ' ' << heart.second+1 << '\n';

	for (auto const& i : v)
	{
		cout << i << ' ';
	}
	return 0;
}