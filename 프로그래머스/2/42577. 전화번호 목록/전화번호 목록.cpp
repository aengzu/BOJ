#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    
    unordered_map<string, int> phoneMap;
    
    for(auto pNum: phone_book) {
        phoneMap[pNum]++;
    }
    
    for (int i=0; i<phone_book.size(); i++) {
        string nowNum = "";
        for (int j=0; j<phone_book[i].size(); j++) {
            nowNum += phone_book[i][j];
            if (phoneMap[nowNum] && nowNum != phone_book[i])
                answer = false;
        }
    }
    
    return answer;
}