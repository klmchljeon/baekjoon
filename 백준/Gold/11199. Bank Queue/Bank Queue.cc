//Bank Queue
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

int n,t;
int a,b;
int res;

priority_queue<int> pq;
vector<pair<int,int>> v;

int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> t;
    for (int i=0; i<n; i++) {
        cin >> a >> b;
        v.push_back({b,a});
    }

    sort(v.begin(),v.end());

    for (auto i:v) {
        pq.push(-i.second);

        if (i.first+1 < pq.size()) {
            pq.pop();
        }
    }

    res = 0;
    while (!pq.empty()) {
        res += -pq.top();
        pq.pop();
    }

    cout << res;

    return 0;
}