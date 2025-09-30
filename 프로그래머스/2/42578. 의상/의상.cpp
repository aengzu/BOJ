#include <string>
#include <vector>
#include <unordered_map>

using namespace std;


int solution(vector<vector<string>> clothes) {
    int answer = 1;
    unordered_map<string, int> clothesMap;
    
    for (auto cloth: clothes) {
        clothesMap[cloth[1]]++;
    }

    
     for(pair<string,int> elem : clothesMap){
        answer = answer*(elem.second+1);
    }
    
    
    return answer-1;
}