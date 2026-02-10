#include <stdio.h>
#include <stdlib.h>
// #include "plus.h"

int compare(char *a,char *b) {
    int i = 0;
    int matched = 1;
    while (b[i]) {
        if (!a[i]) {
            matched = 0;
            break;
        }
        if (b[i] != a[i]) {
            matched = 0;
            break;
        }
        i++;
    }
    if (a[i]) {matched = 0;}
    return matched;

}
struct name {
    char *first;
    char *last;
};

struct human {
    int age;
    float height;
    float kg;
    struct name myname;
};


int main() {
    int **arr;
    int row, col;
    scanf("%d%d", &row, &col);
    arr = (int **)malloc(sizeof(int*) * row);
    for(int i=0; i<row; i++) {
        arr[i] = (int *)malloc(sizeof(int) * col);
    }
    int cnt = 0;
    for (int i=0; i<row; i++) {
        for(int j=0; j<col; j++) {
            arr[i][j] = cnt;
            cnt++;
        }
        
    }

    for (int i=0; i<row; i++) {
        for(int j=0; j<col; j++) {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }

    int *pt = &arr[0][1];


    for(int i=0; i<row; i++){
        free(arr[i]);
    }
    free(arr);

    printf("%d\n", *pt);


    return 0;
}

