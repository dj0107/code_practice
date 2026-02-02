#include <stdio.h>

int main() {
    int arr[3] = {1, 2, 3};
    int (*parr)[3] = &arr;
    printf("arr[1] : %d \n", arr[1]);
    printf("parr[1] : %d \n", (*parr));
    printf("arr: %d", arr);
    return 0; // 0은 정상적으로 끝났다는걸, 나머지는 아니라는걸 의미. (크게 상관 x)
}