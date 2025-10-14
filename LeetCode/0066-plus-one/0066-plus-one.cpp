#include <vector>
using namespace std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        for (int i = digits.size() - 1; i >= 0; i--) {
            if (digits[i] < 9) {     // 올림 없이 끝남
                digits[i]++;
                return digits;
            }
            digits[i] = 0;           // 9 → 0, carry 발생
        }
        // 모든 자리가 9였다면 앞에 1 추가
        digits.insert(digits.begin(), 1);
        return digits;
    }
};
