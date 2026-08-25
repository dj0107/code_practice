#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

int arr[7][7];

void dfs(int *count, int x, int y, int color) {
    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (nx < 0 || ny < 0 || nx >= 7 || ny >= 7 || arr[nx][ny] != color) {
            continue;
        }
        arr[nx][ny] = 0; // mark visited
        *count += 1;
        dfs(count, nx, ny, color);
    }
}

int main() {

    for (int i = 0; i < 7; i++) {
        for (int j = 0; j < 7; j++) {
            scanf("%d", &arr[i][j]);
        }
    }
    int answer = 0;
    for (int i = 0; i < 7; i++) {
        for (int j = 0; j < 7; j++) {
            
            if (arr[i][j]) {
                int color = arr[i][j];
                // mark visited
                arr[i][j] = 0;
                int count = 1;
                dfs(&count, i, j, color);
                if (count >= 3)
                    answer++;
                
            }
        }
    }

    printf("%d\n", answer);


    // for (int i = 0; i < 7; i++) {
    //     for (int j = 0; j < 7; j++) {
    //         printf("%d ", arr[i][j]);
    //     }
    //     printf("\n");
    // }
}