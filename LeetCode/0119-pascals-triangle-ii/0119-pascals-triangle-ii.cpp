class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<vector<int>> triangle;
        triangle.assign(rowIndex+1, {});

        if (rowIndex==0) return {1};
        if (rowIndex==1) return {1, 1};

        for (int i=0; i<rowIndex+1; i++) {
            triangle[i].assign(rowIndex+1, 1);
            for (int j=1; j<i; ++j) {
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j];
            }
        }

        return triangle[rowIndex];
    }
};