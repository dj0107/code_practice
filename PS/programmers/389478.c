#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool check_upper(int curr, int n, int w, int right, int left) { // return true if there is box above current box, false otherwise.
    if (((curr - 1) / w) % 2 == 0 && curr + 2 * right + 1 <= n) { // right direction
        return true;
    } else if (((curr - 1) / w) % 2 == 1 && curr + 2 * left + 1 <= n) {
        return true;
    }
    return false;
}

int solution(int n, int w, int num) {
    int answer = 1; // itself

    int right, left;
    int curr = num;
    left = (num - 1) % w;
    right = w - left - 1;
    if (((num - 1) / w) % 2 == 1) { // swap left and right
        int tmp = left;
        left = right;
        right = tmp;
    }

    while (check_upper(curr, n, w, right, left)) {
        answer++;
        if (((curr - 1) / w) % 2 == 0) { // right direction
            curr += 2 * right + 1;
        } else {curr += 2 * left + 1;}

    }


    return answer;
}

int main() {
    printf("%d\n", solution(6, 5, 4));
}