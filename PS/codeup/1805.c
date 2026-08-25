#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

void bubbleSort(int *arr, int size) {
    for (int i = 0; i < size; i++) {
        for (int j = i + 1; j < size; j++) {
            // compare arr[i] and arr[j]
            if (arr[i] > arr[j]) {
                // swap
                int tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
            }
        }
    }

    return;
}

int main() {
    int n;
    scanf("%d", &n);
    int *arr = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++) {
        int a, b;
        scanf("%d%d", &a, &b);
        arr[i] = a * 100000 + b;
    }

    bubbleSort(arr, n);

    for (int i = 0; i < n; i++) {
        printf("%d %d\n", arr[i] / 100000, arr[i] % 100000);
    }
}