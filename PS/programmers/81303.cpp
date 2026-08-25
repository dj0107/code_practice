#include <string>
#include <vector>

using namespace std;

string solution(int n, int k, vector<string> cmd) {
    
    string arr(n, 'O');
    vector<int> delStack;
    int lastIdx = n - 1;
    int *up = new int[n];
    int *down = new int[n];
    for (int i = 0; i < n; i++) {
        up[i] = i-1;
        down[i] = i+1;
    }
    up[0] = -1;
    down[n-1] = -1;


    int cmds = cmd.size();
    for (int i = 0; i < cmds; i++) {
        char command = cmd[i][0];
        switch(command) 
        {
            case 'U':
            {
                int x = stoi(cmd[i].substr(2));
                while (x > 0) {
                    x--;
                    k = up[k];
                }
                break;
            }
            case 'D':
            {
                int x = stoi(cmd[i].substr(2));
                while (x > 0) {
                    x--;
                    k = down[k];
                }
                break;
            }
            case 'C':
            {
                if (k == lastIdx) {
                    // delete and choose upper one
                    delStack.push_back(k);
                    arr[k] = 'X';
                    lastIdx = up[k];
                    k = lastIdx;
                    down[k] = -1;
                }
                else {
                    // delete and choose lower one
                    delStack.push_back(k);
                    arr[k] = 'X';
                    if (up[k] != -1) down[up[k]] = down[k];
                    else up[down[k]] = -1;
                    up[down[k]] = up[k];

                    k = down[k];
                }
                break;
            }
            case 'Z':
            {
                int val = delStack.back();
                delStack.pop_back();
                arr[val] = 'O';
                if (val > lastIdx) {
                    lastIdx = val;
                    down[up[val]] = val;
                }
                else {
                    down[up[val]] = val;
                    up[down[val]] = val;
                }
                break;
            }
        }

    }


    return arr;
}