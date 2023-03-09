//좌표 정렬하기 2
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int i;
int x,y;
int n;
vector<pair<int,int>> v;

bool compare(pair<int,int> a, pair<int,int> b) {
    if (a.second == b.second) {
        return a.first < b.first;
    }
    else {
        return a.second < b.second;
    }
}

int main()
{
    cin >> n;
    for (i=0; i<n; i++) {
        cin >> x >> y;
        v.push_back({x,y});
    }
    sort(v.begin(),v.end(),compare);

    for (int i=0; i<v.size(); i++) {
        cout << v[i].first << ' ' << v[i].second << '\n';
    }

    return 0;
}