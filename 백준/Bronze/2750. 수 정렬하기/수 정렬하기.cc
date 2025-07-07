#include <iostream>
#include <algorithm>
using namespace std;

int nums[1001];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    sort(nums, nums+n);

    for (int i=0; i<n; i++) {
        cout << nums[i] << "\n";
    }
    return 0;
}