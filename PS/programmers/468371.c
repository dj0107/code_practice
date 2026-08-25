#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>


// signals_rows는 2차원 배열 signals의 행 길이, signals_cols는 2차원 배열 signals의 열 길이입니다.
int solution(int** signals, size_t signals_rows, size_t signals_cols) {
    int answer = -1;
    int total_period = 1;
    int *T = (int *)malloc(sizeof(int) * signals_cols);
    for (int i = 0; i < signals_cols; i++) {
        T[i] = signals[i][0] + signals[i][1] + signals[i][2];
        total_period *= T[i];
    }
    for (int t = 1; t <= total_period; t++) {
        bool found = true;
        for (int i = 0; i < signals_cols; i++) {
            if (t % T[i] > signals[i][0] && t % T[i] <= signals[i][0] + signals[i][1]) {
                found = false;
                break;
            }
        }
        if (found) {
            answer = t;
            printf("found!\n");
            break;
        }
    }


    return answer;
}

int main() {
    int **signals[2][3] = {{2, 1, 2}, {5, 1, 1}};
    size_t signals_rows, signals_cols;
    signals_rows = 2;
    signals_cols = 3;
    printf("answer: %d\n", solution(signals, signals_rows, signals_cols));
}

/*
연습지
RYG에서 
노란불은 R+1초부터 시작해서 Y초간 반복하고 주기는 R+Y+G마다

*/