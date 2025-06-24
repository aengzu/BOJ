#include <iostream>
#include <cctype>
using namespace std;

int main() {
    string input_str;
    cin >> input_str;
    // 알파벳 배열 0으로 초기화
    int alpha[26] = {0}; 

    // 1. 모두 소문자로 변환 후 카운팅
    for(char& ch : input_str) {
        ch = toupper(ch); // 대소문자 구분 안하기 위함
        alpha[ch-'A']++; // a의 아스키 코드는 97
    }

    // 2. 최대값 찾기
    int maxCount = 0;
    int maxIndex = -1;
    bool isDuplicated = false;

    for (int i = 0; i < 26; ++i) {
        if (alpha[i] > maxCount) {
            maxCount = alpha[i];
            maxIndex = i;
            isDuplicated = false;
        } else if (alpha[i] == maxCount && maxCount > 0) {
            isDuplicated = true;
        }
    }

    if (isDuplicated) {
        cout << "?\n";
    } else {
        cout << static_cast<char>('A' + maxIndex); 
    }
}