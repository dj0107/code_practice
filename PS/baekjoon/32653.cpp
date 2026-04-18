#include <iostream>
#include <vector>
using namespace std;

long long lcm(vector<int> arr)
{
    int N = arr.size();
    long long left = 1; //최소공배수 구하는 그림에서 왼쪽의 곱
    vector<int> divisors = {2, 3, 5, 7, 11, 13, 17, 19, 23}; // xi <= 25임 
    int counter = 0;
    
    while(counter < 9)
    {
        bool is_dividable = false;
        for(int i = 0; i < N; i++)
        {
            if(arr[i] % divisors[counter] == 0) //스테이크들 중 하나라도 해당되는 약수로 나눠진다면 나눠 줌 
            {
                is_dividable = true;
                arr[i] /= divisors[counter];
            }
        }
        if(is_dividable == true) {left *= divisors[counter];} //나눠진다면 left를 해당하는 약수로 곱해줌
        else if(is_dividable == false) {counter++;} //안된다면 다음 약수로 시도하기


    }

    return left;
}

int main()
{
    int N; //스테이크 개수
    cin >> N;
    vector<int> steak(N);

    for(int i = 0; i < N; i++)
    {
        cin >> steak[i];
    }

    cout << lcm(steak) * 2 << endl; //단순한 최소공배수가 아니라 양면 굽기도 고려해야 하기 때문에 2를 곱함
}