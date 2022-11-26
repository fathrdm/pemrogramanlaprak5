#include <stdio.h>
int reverse(int a){
    int b, 
    x = 0;
    while (a!=0){
        b = a % 10;
        x = x * 10 + b;
        a/=10;}
    return x;}
int main() {
    int A, B;
    scanf("%d %d",&A,&B);
    A=reverse(A);
    B=reverse(B);
    int C = A+B;
    printf("%d",reverse(C));
}