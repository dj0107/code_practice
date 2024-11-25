#include <iostream>
#include <string>
using namespace std;

int main()
{
    string S;
    cin >> S;
    int len = S.length();
    int numOfspaces = 0; //돌 사이에 빈 공간의 수(두 돌 사이에 빈 공간이 2개 있어도 +1만 카운트함)

    for(int i = 1; i < len; i++) 
    {
        if((S[i - 1] == 'B' || S[i - 1] == 'W') && S[i] == '.' )
        {
            numOfspaces++;
        }
    }

    if(S[len - 1] == '.') {numOfspaces--;}

    if(numOfspaces % 2 == 0) {cout << "Lose";}
    else {cout << "Win";}

}