#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char **split_word(const char *str, const char *delimiter)
{
    if (str == NULL || delimiter == NULL || delimiter[0] == '\0') {
        return NULL;
    }

    size_t delimiter_len = strlen(delimiter);
    size_t count = 1;

    const char *search = str;

    while ((search = strstr(search, delimiter)) != NULL) {
        count++;
        search += delimiter_len;
    }

    char **ret = malloc(sizeof(char *) * (count + 1));
    if (ret == NULL) {
        return NULL;
    }

    const char *start = str;
    size_t index = 0;

    while (1) {
        const char *end = strstr(start, delimiter);

        size_t token_len;

        if (end == NULL) {
            token_len = strlen(start);
        } else {
            token_len = (size_t)(end - start);
        }

        ret[index] = malloc(token_len + 1);
        if (ret[index] == NULL) {
            for (size_t i = 0; i < index; i++) {
                free(ret[i]);
            }
            free(ret);
            return NULL;
        }

        memcpy(ret[index], start, token_len);
        ret[index][token_len] = '\0';
        index++;

        if (end == NULL) {
            break;
        }

        start = end + delimiter_len;
    }

    ret[index] = NULL;
    return ret;
}

// friends_len은 배열 friends의 길이입니다.
// gifts_len은 배열 gifts의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* friends[], size_t friends_len, const char* gifts[], size_t gifts_len) {
    int answer = 0;

    


    return answer;
}