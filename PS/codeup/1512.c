#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
int dist(int x, int y, int tx, int ty) {
    int distx = tx - x < 0 ? x - tx : tx - x;
    int disty = ty - y < 0 ? y - ty : ty - y;
    return distx + disty;
}
int main() {
    int n, x, y;
    scanf("%d", &n);
    scanf("%d%d", &x, &y);

    x--;
    y--;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int distance = dist(i, j, x, y);
            printf("%d ",distance + 1);

        }
        printf("\n");
    }
}