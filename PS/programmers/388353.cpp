#include <string>
#include <vector>

using namespace std;
/**
 * 외곽에 해당하는 2차원 벡터를 받아서 갱신해줌
 */
void recalc_outer(vector<vector<bool>>& outer, vector<string> storage) {
    int n = outer.size();
    int m = outer[0].size();
    // 네 변을 보면서 시작
}

int solution(vector<string> storage, vector<string> requests) {
    int answer = 0;
    int n = storage.size();
    int m = storage[0].size();
    vector<vector<bool>> outer;
    vector<bool> temp;
    for (int i=0; i<m; i++) temp.push_back(false);
    for (int i=0; i<n; i++) outer.push_back(temp);
    recalc_outer(outer, storage);
}

