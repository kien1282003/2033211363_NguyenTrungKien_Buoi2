#include <stdio.h>

int isMultipleOf7(int num) {
    return (num % 7 == 0);
}
void printMultiplesOf7() {
    printf("Cac so nguyen co 2 chu so va la boi cua 7:\n");
    for (int i = 10; i < 100; i++) {
        if (isMultipleOf7(i)) {
            printf("%d ", i);
        }
    }
    printf("\n");
}

int main(void) {
    printMultiplesOf7();
    return 0;

}
