#include <stdio.h>
// int getDouble(int n) {
//     return n * 2;
// }
// void makeItDouble(int *n) {
//     *n = *n * 2;
//     return;
// }
int multi(int (*arr)[3][2][5]) {
    arr[1][1][1][1] = 1;
    return 0;
}
int add1(int (*arr)[2]) {
    (*(arr + 1))[1] = 999;
    return 0;
}
int getGCD(int a, int b) {
    int tmp;
    while (a != 0 && b != 0) {
        if (a >= b) {
            a = a % b;
        } else {
            b = b % a;
        }

    }
    if (a >= b) {return a;}
    else {return b;}

}

int *getGCDS(int (*arr1), int (*arr2)) {
    static int ans[5] = {0, 0, 0, 0, 0};
    for(int i = 0; i < 5; i++) {
        ans[i] = getGCD(arr1[i], arr2[i]);
    }
    return ans;
}


int main() {
    // int arr1[5] = {12, 15, 33, 39, 49};
    // int arr2[5] = {4, 127, 121, 7, 21};
    // int (*arr3);
    // arr3 = getGCDS(arr1, arr2);
    // printf("1: %d, 2: %d, 3: %d, 4: %d, 5: %d\n", arr3[0], arr3[1], arr3[2], arr3[3], arr3[4]);
    // return 0; // 0은 정상적으로 끝났다는걸, 나머지는 아니라는걸 의미. (크게 상관 x)
    int arr[] = {1, 2, 3};
    printf("%d", arr[1]);
}