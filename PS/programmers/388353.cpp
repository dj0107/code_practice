// SOLVED
#include <string>
#include <deque>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;
/**
 * 외곽에 해당하는 2차원 벡터를 받아서 갱신해줌
 */
void recalc_outer(vector<vector<bool>>& outer, vector<string> storage) {
    int n = outer.size();
    int m = outer[0].size();
    // 네 변을 보면서 빈 공간을 넣고 시작
    deque<int> dqx;
    deque<int> dqy;
    vector<vector<bool>> visited(n, vector<bool>(m, false));

    for (int i=0; i<n; i++) {
        outer[i][0] = true; outer[i][m-1] = true;
        if (storage[i][0] == '0') {
            dqx.push_back(i);
            dqy.push_back(0);
        }
        if (storage[i][m-1] == '0') {
            dqx.push_back(i);
            dqy.push_back(m-1);
        }
    }
    for (int i=1; i< m-1; i++) {
        outer[0][i] = true; outer[n-1][i] = true;
        if (storage[0][i] == '0') {
            dqx.push_back(0);
            dqy.push_back(i);
        }
        if (storage[n-1][i] == '0') {
            dqx.push_back(n-1);
            dqy.push_back(i);
        }
    }
    int dx[4] = {0, 0, -1, 1};
    int dy[4] = {-1, 1, 0, 0};
    // dqx, dqy의 각 지점 (바깥과 연결된 빈 공간)에 대해 BFS
    while (!dqx.empty()) {
        int x = dqx.front(); dqx.pop_front();
        int y = dqy.front(); dqy.pop_front();
        // 해당 지점이 이미 있으면 skip
        if (visited[x][y]) continue;
        // 이제 그 지점을 visited 처리하기
        visited[x][y] = true;
        // 4방향을 보면서 outer에 넣고 비었다면 dq에도 넣기
        for (int i=0; i<4; i++) {
            int nx = x + dx[i], ny = y + dy[i];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            outer[nx][ny] = true;
            if (storage[nx][ny] == '0') {
                // 탐색한 공간이 빈 공간이면 dq에 넣기
                dqx.push_back(nx); dqy.push_back(ny);
            }
        }
        
    }
    // 끝
}

int solution(vector<string> storage, vector<string> requests) {
    
    int n = storage.size();
    int m = storage[0].size();
    int answer = n * m;
    vector<vector<bool>> outer;
    vector<bool> temp;
    for (int i=0; i<m; i++) temp.push_back(false);
    for (int i=0; i<n; i++) outer.push_back(temp);
    recalc_outer(outer, storage); // 초기화
    
    int req_len = requests.size();
    for (int i=0; i<req_len; i++) {
        if (requests[i].size() == 1) { // 한 글자인 경우 -> 지게차
            for (int x=0; x<n; x++) {
                for (int y=0; y<m; y++) {
                    if (outer[x][y] && (storage[x][y] == requests[i][0])) {
                        // 지게차로 내릴 수 있으면 빼기
                        storage[x][y] = '0';
                        answer--;
                    }
                }
            }
        }
        else { // "BB" 처럼 두 글자인 경우---> 크레인
            for (int x=0; x<n; x++) {
                for (int y=0; y<m; y++) {
                    if (storage[x][y] == requests[i][0]) {
                        // 빼기
                        storage[x][y] = '0';
                        answer--;
                    }
                }
            }
        }
        // 이제 outer 벡터 갱신
        recalc_outer(outer, storage);
    }
    return answer;
}

