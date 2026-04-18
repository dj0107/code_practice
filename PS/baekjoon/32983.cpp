#include <iostream>
#include <vector>
#include <queue>
using namespace std;

void bfs(vector<vector<int>>& bfsVec,  int sizen, int sizem, int startn, int startm, vector<int>& sumVec)
{
    queue<int> qn, qm;
    int sum = bfsVec[startn][startm];
    bfsVec[startn][startm] = -2;
    qn.push(startn);
    qm.push(startm);
    qn.push(-1);
    qm.push(-1);
    sumVec.push_back(sum);
    while(!qn.empty())
    {
        startn = qn.front();
        startm = qm.front();
        qn.pop();
        qm.pop();

        if(startn > 1 && bfsVec[startn - 1][startm] >= 0) //up
        {
            sum += bfsVec[startn - 1][startm];
            bfsVec[startn - 1][startm] = -2; //-2 means visited that cell
            qn.push(startn - 1);
            qm.push(startm);

        }
        if(startn < sizen && bfsVec[startn + 1][startm] >= 0)//down
        {
            sum += bfsVec[startn + 1][startm];
            bfsVec[startn + 1][startm] = -2; //-2 means visited that cell
            qn.push(startn + 1);
            qm.push(startm);
        }
        if(startm > 1 && bfsVec[startn][startm - 1] >= 0)//left
        {
            sum += bfsVec[startn][startm - 1];
            bfsVec[startn][startm - 1] = -2; //-2 means visited that cell
            qn.push(startn);
            qm.push(startm - 1);
        }
        if(startm < sizem && bfsVec[startn][startm + 1] >= 0)//right
        {
            sum += bfsVec[startn][startm + 1];
            bfsVec[startn][startm + 1] = -2; //-2 means visited that cell
            qn.push(startn);
            qm.push(startm + 1);
        }

        if(qn.front() == -1)
        {
            qn.pop();
            qm.pop();
            sumVec.push_back(sum);
            if(!qn.empty())
            {
                qn.push(-1);
                qm.push(-1);
            }
        }

        
    }
    return;
}

int main()
{
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n, m, c;
    cin >> n >> m >> c;
    int sr, sc;
    cin >> sr >> sc;
    vector<vector<int>> caveVec;
    vector<int> rawVec(m + 1);
    caveVec.push_back(rawVec);
    for(int i = 1; i <= n; i++)
    {
        caveVec.push_back(rawVec);
        for(int j = 1; j <= m; j++)
        {
            cin >> caveVec[i][j];
        }
    }
    vector<int> sumVec;

    bfs(caveVec, n, m, sr, sc, sumVec);
    int ans = 0;
    for(int i = 0; i < sumVec.size(); i++)
    {
        sumVec[i] -= i * c;
        ans = (sumVec[i] > ans) ? sumVec[i] : ans;
    }

    cout << ans;
    
}