#include <iostream>
using namespace std;

int main() {
    int Q;
    cin >> Q;

    for(int i = 0; i < Q; i++) {
        int ta, tb, va, vb;
        cin >> ta >> tb >> va >> vb;

        int remain = va - (tb * vb / ta);
        // B 작업 총 시간이 더 길 때
        if(remain <= 0) {
            cout << tb * vb << endl;
        } 
        // 남은 A 작업 개수가 짝수일 때 
        else if(remain % 2 == 0) {
            cout << (tb * vb) + (remain / 2 * ta) << endl;
        }
        // 남은 A 작업 개수가 홀수일 때
        else if(remain % 2 == 1) {
            int additional = ta - (tb * vb % ta); 
            cout << (tb * vb) + (remain / 2 * ta) + additional << endl;
        }
    }
}