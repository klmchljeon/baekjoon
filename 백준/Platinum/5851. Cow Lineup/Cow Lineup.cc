#include <bits/stdc++.h>

#define ll long long
using namespace std;

map<int,int> cnt;

int d[100000];

int i,s,e;
int n,k;
int res = 0;

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> k;
    for (i=0; i<n; i++) {
        cin >> d[i];
    }

    e = 0;
    for (s=0; s<n; s++) {
        while (e<n) {
            if (cnt.find(d[e])==cnt.end()) {
                if (cnt.size() == k+1) {
                    break;
                }
                else {
                    cnt.insert({d[e],0});
                }
            }

            cnt[d[e]]++;

            res = max(res,cnt[d[e]]);
            e++;
        }

        cnt[d[s]]--;
        if (cnt[d[s]] == 0) {
            cnt.erase(d[s]);
        }
    }

    cout << res;

    return 0;
}