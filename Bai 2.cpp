#include <stdio.h>
#include <math.h>
int isPerfectSquare(int a) {
    int squareRoot = sqrt(a);
    return (squareRoot * squareRoot == a);
}

void countandPrintPerfectSquare(int n) {
    printf("\nCac so chinh phuong nho hon %d la: ", n);
    int count = 0;
    for (int i = 1; i < n; i++) {
        if (isPerfectSquare(i)) {
            printf("%d  ", i);
            count++;
        }
    }
    printf("\nSo luong so chinh phuong la : %d ", count);
}

int main(void) {
    int n;
    printf("Nhap so N");
    scanf_s("%d", &n);
    countandPrintPerfectSquare(n);

}
