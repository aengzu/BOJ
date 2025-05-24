#include <iostream>
#include <cmath>
#include <numeric>

using namespace std;

int f_gcd(int a, int b) {
    int ans;
    while (b != 0) {
        ans = a % b;
        a = b;
        b = ans;
    }
    return a;
}

int main() {
    int a, b;
    cin >> a >> b;
    int gcd = f_gcd(a,b);
    int lcm = (a * b) / gcd;
    cout  << gcd << endl << lcm << endl;
    return 0;
}