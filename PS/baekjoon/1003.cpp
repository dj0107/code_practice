#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;

    int memory0[41] = {0,};
    int memory1[41] = {0,};

    memory0[0] = 1;
    memory1[0] = 0;
    memory0[1] = 0;
    memory1[1] = 1;

    for(int i = 2; i < 41; i++) {
        memory0[i] = memory0[i - 1] + memory0[i - 2];
        memory1[i] = memory1[i - 1] + memory1[i - 2];
    }

    int N[T];
    for(int i = 0; i < T; i++) {
        cin >> N[i];
    }

    for(int i = 0; i < T; i++) {
        cout << memory0[N[i]] << " " << memory1[N[i]] << endl;
    }

}