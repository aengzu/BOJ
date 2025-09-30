#include <string>
#include <vector>
#include <climits>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int maxLong = 0, maxShort = 0;

    for (const auto& s : sizes) {
        int a = s[0], b = s[1];
        int longer = max(a, b);
        int shorter = min(a, b);
        maxLong = max(maxLong, longer);
        maxShort = max(maxShort, shorter);
    }
    return maxLong * maxShort;
}

