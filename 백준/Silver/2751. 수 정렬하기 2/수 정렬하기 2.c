/*
    C: Hello, World!
*/
#include <stdio.h>

void MS(int l, int h, int* A) {
    if (l == h) {
        return;
    }

    int m = (l+h)/2;
    MS(l,m,A);
    MS(m+1,h,A);

    Merge(l,m,h,A);
}

void Merge(int l, int m, int h, int* A) {
    int tmp[1000000];

    int left = l;
    int right = m+1;

    int idx = 0;
    while (left <= m && right <= h) {
        if (A[left] <= A[right]) {
            tmp[idx++] = A[left++];
        }
        else {
            tmp[idx++] = A[right++];
        }
    }

    while (left <= m) {
        tmp[idx++] = A[left++];
    }

    while (right <= h) {
        tmp[idx++] = A[right++];
    }

    for (int i = 0; i < idx; i++) {
        A[l++] = tmp[i];
    }
    return;
}

int main(int argc, char *argv[])
{
    int A[1000000];
    int n;

    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &A[i]);
    }

    MS(0,n-1,A);

    for (int i = 0; i < n; i++) {
        printf("%d\n", A[i]);
    }

    return 0;
}
