#include <iostream>
#include <vector>
#include <queue>
using namespace std;

void dfs(vector<vector<int>>& dfsVec, int size, int start, vector<int>& orderVec)
{
    dfsVec[0][start] = 1;
    orderVec.push_back(start);
    

    for(int i = 1; i <= size; i++)
    {
        if(dfsVec[start][i] == 1 && dfsVec[0][i] == 0)
        {
            dfs(dfsVec, size, i, orderVec);
        }
    }
    return;
}

void bfs(vector<vector<int>>& bfsVec,  int size, int start, vector<int>& orderVec)
{
    queue<int> q;
    q.push(start);
    while(!q.empty())
    {
        start = q.front();
        orderVec.push_back(start);
        q.pop();
        bfsVec[0][start] = 1;
        for(int i = 1; i <= size; i++)
        {
            if(bfsVec[start][i] == 1 && bfsVec[0][i] == 0)
            {
                q.push(i);
                bfsVec[0][i] = 1;
            }
        }
    }
    return;
}


int main()
{
    int n, m, v;
    cin >> n >> m >> v;
    vector<vector<int>> dfsVec; // dfs(or bfs)Vec[a][b] means the existence of edge. [0][a] means the whether it was visited. 
    vector<int> hollowVec(n + 1);
    for(int i = 0; i < n + 1; i++)
    {
        dfsVec.push_back(hollowVec);
    }

    int a, b;

    for(int i = 0; i < m; i++)
    {
        cin >> a >> b;
        dfsVec[a][b] = 1;
        dfsVec[b][a] = 1;
    }

    vector<vector<int>> bfsVec = dfsVec;
    vector<int> orderVecDfs;
    dfs(dfsVec, n, v, orderVecDfs);
    for(int i = 0; i < orderVecDfs.size() - 1; i++)
    {
        cout << orderVecDfs[i] << " ";
    }
    cout << orderVecDfs[orderVecDfs.size() - 1] << "\n";
    
    vector<int> orderVecBfs;
    bfs(bfsVec, n, v, orderVecBfs);

    for(int i = 0; i < orderVecBfs.size() - 1; i++)
    {
        cout << orderVecBfs[i] << " ";
    }

    cout << orderVecBfs[orderVecBfs.size() - 1];
}