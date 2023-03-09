//버블 소트
#include <iostream>
#include <algorithm>
#include <vector>

#define ll long long
using namespace std;

int i;
ll tmp;
int n;
vector<pair<int,ll>> v;

ll d[500001];
ll tree[2000001];

void update(int idx, ll var, int s=1, int e=n, int node=1) {
    if (s==e) {
        tree[node] = var;
        return;
    }

    int mid = (s+e)/2;
    if (idx <= mid) {
        update(idx,var,s,mid,node*2);
    }
    else {
        update(idx,var,mid+1,e,node*2+1);
    }
    tree[node] = tree[node*2] + tree[node*2+1];
    return;
}

ll cal(int l, int r, int s=1, int e=n, int node=1) {
    if (e<l || r<s) {
        return 0;
    }

    if (l<=s && e<=r) {
        return tree[node];
    }

    int mid = (s+e)/2;
    ll left = cal(l,r,s,mid,node*2);
    ll right = cal(l,r,mid+1,e,node*2+1);

    return left + right;
}

bool compare(pair<int,ll> a, pair<int,ll> b) {
    if (a.second == b.second) {
        return a.first < b.first;
    }
    else {
        return a.second < b.second;
    }
}

int main()
{
    ll res;

    cin >> n;
    for (i=1; i<=n; i++) {
        cin >> tmp;
        v.push_back({i,tmp});
    }
    sort(v.begin(),v.end(),compare);
    for (i=0; i<v.size(); i++) {
        d[i+1] = v[i].first;
    }

    res = 0;
    for (i=n; i>0; i--) {
        res += cal(1,d[i]);
        update(d[i],1);
    }
    cout << res << '\n';

    return 0;
}