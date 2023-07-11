#include <bits/stdc++.h>

#define ll long long
using namespace std;

map<pair<int,int>,int> mp;
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
        if (cnt.find(d[i]) == cnt.end()) {
            cnt.insert({d[i],0});
        }
    }

    e = 0;
    for (s=0; s<n; s++) {
        while (e<n) {
            if (cnt[d[e]] != 0) {
                mp.erase({-cnt[d[e]],d[e]});
            } 
            
            if (mp.size() == k+1) {
                break;
            }
            
            cnt[d[e]]++;

            mp.insert({{-cnt[d[e]],d[e]},0});
            e++;
        }

        for (auto i:mp) {
            res = max(res,-i.first.first);
            break;
        }

        mp.erase({-cnt[d[s]],d[s]});
        cnt[d[s]]--;
        if (cnt[d[s]] != 0) {
            mp.insert({{-cnt[d[s]],d[s]},0});
        }
    }

    cout << res;

    return 0;
}