#include <iostream>

using namespace std;

int main() {
    int n, p;
    cin >> n;
    while (n--) {
        cin >> p;
        int mvp_value = 0;
        string mvp_name;
        while (p--) {
            int value;
            string name;
            cin >> value >> name;
            if (mvp_value <= value) {
                mvp_value = value;
                mvp_name = name;
            }
        }
        cout << mvp_name << endl;
    }
    return 0;
}