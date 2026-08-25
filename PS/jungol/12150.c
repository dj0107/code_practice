#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main() {
    typedef struct {
        char name[20];
        int age;
    } person;

    person person1, person2, person3;
    scanf("%s%d%s%d%s%d", &person1.name, &person1.age, &person2.name, &person2.age, &person3.name, &person3.age);

    printf("Name : %s\n", person1.name);
    printf("Age : %d\n", person1.age);
    printf("Name : %s\n", person2.name);
    printf("Age : %d\n", person2.age);
    printf("Name : %s\n", person3.name);
    printf("Age : %d\n", person3.age);
}