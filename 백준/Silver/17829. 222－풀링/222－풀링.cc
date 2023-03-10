//222-풀링
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int dx[4] = {0,0,1,1};
int dy[4] = {0,1,0,1};

int n;
int nx,ny;
int arr[1024][1024];

int find(int size, int x=0, int y=0) {
    if (size == 1) {
        return arr[x][y];
    }

    size/=2;
    vector<int> v;
    for (int i=0; i<4; i++) {
        nx = x + size*dx[i];
        ny = y + size*dy[i];

        v.push_back(find(size,nx,ny));
    }

    sort(v.begin(),v.end());
    return v[2];
}

int main()
{
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cin >> arr[i][j];
        }
    }

    int res = find(n);
    cout << res << '\n';

    return 0;
} 