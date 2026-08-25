#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>

int main() {
    int fd = open("data.txt", O_RDONLY);

    if (fd == -1) {perror("open"); return 1;}

    char buffer[256];
    ssize_t bytes_read;
    while ((bytes_read == 1))


    return 0;
}