#include <iostream>
using namespace std;

int main() {
    int a, b, v;
    cin >> a >> b >> v;
    int days = 0; 
    days = (v-a + (a-b)-1)/(a-b) + 1;
    cout << days << endl;
    return 0;
}