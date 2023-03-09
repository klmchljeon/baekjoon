//숫자 카드 2
#include <iostream>
#include <unordered_map>

using namespace std;

unordered_map <int,int> map;
int i,tmp;
int n,m;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

    cin >> n;
    for (i=0; i<n; i++) {
        cin >> tmp;
        map[tmp]++;
    }

    cin >> m;
    for (i=0; i<m; i++) {
        cin >> tmp;
        cout << map[tmp] << ' ';
    }
    cout << '\n';

    return 0;
}