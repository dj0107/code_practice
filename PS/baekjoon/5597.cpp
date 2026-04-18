#include <iostream>
using namespace std;

int main() 
{
    int arr[31];

    for(int i = 0; i < 31; i++)
    {
        arr[i] = 0;
    }

    int num;
    // 입력받아서 제출자 체크
    for(int i = 0; i < 28; i++)
    {
        cin >> num;
        arr[num] = 1;
    }
    // 출력
    for(int i = 1; i < 31; i++)
    {
        if(arr[i] == 0) {cout << i << endl;}
    }

}