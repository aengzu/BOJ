class Solution {
    vector<vector<int>> triangle;
public:
    vector<vector<int>> generate(int numRows) {
        triangle.assign(numRows, {});
        for (int i = 0; i < numRows; ++i) {
            triangle[i].assign(i+1, 1);  
            for (int j = 1; j < i; ++j) {
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
            }
        }
        return triangle;
    }
};