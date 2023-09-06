/*
    C언어 Hello, World! 예제
*/
#include <stdio.h>

int arr[10001];

int main(int argc, char *argv[])
{
    int n,x;
    scanf("%d",&n);
    scanf("%d",&x);
    for (int i=1; i<n+1; i++) {
        scanf("%d",&arr[i]);
    }

    for (int i=1; i<n+1; i++) {
        if (arr[i] < x) {
            printf("%d ",arr[i]);
        }
    }

    return 0;
}