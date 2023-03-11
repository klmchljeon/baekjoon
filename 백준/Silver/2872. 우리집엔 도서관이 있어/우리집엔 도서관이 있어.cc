//우리집엔 도서관이 있어
#include <iostream>

using namespace std;

int i,n;
int arr[300000];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int cnt,idx;

    cin >> n;
    for (i=0; i<n; i++) {
        cin >> arr[i];
        if (arr[i] == n) {
            idx = i;
        }
    }

    cnt = n;
    for (i=idx; i>-1; i--) {
        if (arr[i] == cnt) {
            cnt--;
        }
    }

    cout << cnt << '\n';

    return 0;
}