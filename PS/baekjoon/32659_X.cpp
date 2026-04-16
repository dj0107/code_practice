#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main()
{
    string S;
    cin >> S;
    int leng = S.length();
    vector<int> grundyVec;
    for(int i = 0; i < leng; i++)
    {
        if(S[i] == 'B')
        {
            grundyVec.push_back(0);
            if(i > 0 && S[i - 1] == '.') {grundyVec[grundyVec.size() - 1] += 1;}
            if(i < leng - 1 && S[i + 1] == '.') {grundyVec[grundyVec.size() - 1] += 1;}
        }
    }

    if(S[0] == '.') 
    {
        for(int i = 1; i < leng; i++)
        {
            if(S[i] == 'B')
            {
                grundyVec[0] -= 1;
                break;
            }
            else if(S[i] == 'W')
            {
                break;
            }
        }
    }

    if(S[leng - 1] == '.') 
    {
        for(int i = leng - 2; i > 0; i--)
        {
            if(S[i] == 'B')
            {
                grundyVec[grundyVec.size() - 1] -= 1;
                break;
            }
            else if(S[i] == 'W')
            {
                break;
            }
        }
    }

    int grundy = 0;
    for(int i = 0; i < grundyVec.size(); i++)
    {
        grundy ^= grundyVec[i];
    }

    if(grundy == 0) {cout << "Lose";}
    else {cout << "Win";}

    


}