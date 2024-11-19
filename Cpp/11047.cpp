#include <iostream>
using namespace std;



int main() {
    int N, K;
    cin >> N >> K;
    int A[N];
    int counter = 0;
    for(int i = 0; i < N; i++) {
        cin >> A[i];
    }

    for(int i = N - 1; i >= 0; i--) {

        while(K >= A[i]) {
            K -= A[i];
            counter ++;
        }


    }

    cout << counter << endl;

    return 0;

}