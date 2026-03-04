#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int ki(int a[][3]) {
    return a[0][2];
}

int main() {
    int arr[1][3] = {0, 1, 2};
    cout << ki(arr);
    
    return 0;
}
