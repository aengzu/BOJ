#include <iostream>
#include <algorithm>
#include <vector>
#include <climits>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

    static int n;
	cin >> n;

	vector<int> nums(n);
	for (int i = 0; i < n; i++) cin >> nums[i];

    vector<int> opCnt(4);
	cin >> opCnt[0] >> opCnt[1] >> opCnt[2] >> opCnt[3];

    // 연산자 리스트 생성
    vector<char> ops;
    for (int i = 0; i < opCnt[0]; i++) ops.push_back('+');
    for (int i = 0; i < opCnt[1]; i++) ops.push_back('-');
    for (int i = 0; i < opCnt[2]; i++) ops.push_back('*');
    for (int i = 0; i < opCnt[3]; i++) ops.push_back('/');

    // 중복 원소가 있으니 먼저 정렬
    sort(ops.begin(), ops.end());
	int min_result = INT_MAX;
	int max_result = INT_MIN;

    do {
        int now_ans = nums[0];
        for (int now_idx = 0; now_idx < n - 1; now_idx++) {
            int l = now_ans;
            int r = nums[now_idx+1];
            char op = ops[now_idx];

            switch (op) {
                case '+':
                    now_ans = l + r;
                    break;
                case '-':
                    now_ans = l - r;
                    break;
                case '*':
                    now_ans = l * r;
                    break;
                case '/':
                    if (l < 0) now_ans = -(abs(l) / r);
                    else now_ans = l / r;
                    break;
            }
		}
        min_result = min(now_ans, min_result);
        max_result = max(now_ans, max_result);
    } while (next_permutation(ops.begin(), ops.end()));
    
    cout << max_result << '\n' << min_result << '\n';
    return 0;
}