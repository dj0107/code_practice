#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main() {
    int N;
    scanf("%d", &N);
    int arr[1001];
    arr[0] = 1;
    arr[1] = 4;
    for (int i = 2; i <= N; i++) {
        arr[i] = 4 * i + arr[i-2];
    }
    printf("%d", arr[N]);
}