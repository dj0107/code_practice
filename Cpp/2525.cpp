#include <iostream>
using namespace std;

void adjust(int& A, int& B, const int C)
{
    //분 더하기
    B += C;

    //60분을 넘기지 않도록 시간으로 넘기기
    A += B / 60;
    B %= 60;

    //24시를 넘기지 않도록 조정하기
    A %= 24;
}

int main() 
{
    //입력 받기
    int A, B;
    cin >> A >> B;
    int C;
    cin >> C;

    //함수 실행
    adjust(A, B, C);

    cout << A << " " << B << endl;
    

    return 0;
}