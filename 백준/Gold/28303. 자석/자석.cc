#include <iostream>

#define ll long long
using namespace std;

const ll INF = 98765432123;

int i;
int n,m,k;
ll a,b;
ll c;

ll d[500001];
ll ltree[2000001];
ll rtree[2000001];

ll linit(int s=1, int e=n, int node = 1) {
    if (s==e) {
        ltree[node] = d[s] + s*k;
        return ltree[node];
    }

    int mid = (s+e)/2;
    ll left = linit(s,mid,node*2);
    ll right = linit(mid+1,e,node*2+1);

    ltree[node] = min(left,right);
    return ltree[node];
}

ll rinit(int s=1, int e=n, int node = 1) {
    if (s==e) {
        rtree[node] = d[s] + (n+1-s)*k;
        return rtree[node];
    }

    int mid = (s+e)/2;
    ll left = rinit(s,mid,node*2);
    ll right = rinit(mid+1,e,node*2+1);

    rtree[node] = min(left,right);
    return rtree[node];
}

ll lcal(int l, int r, int s=1, int e=n, int node=1) {
    if (e<l || r<s) {
        return INF;
    }

    if (l<=s && e<=r) {
        return ltree[node];
    }

    int mid = (s+e)/2;
    ll left = lcal(l,r,s,mid,node*2);
    ll right = lcal(l,r,mid+1,e,node*2+1);

    return min(left,right);
}

ll rcal(int l, int r, int s=1, int e=n, int node=1) {
    if (e<l || r<s) {
        return INF;
    }

    if (l<=s && e<=r) {
        return rtree[node];
    }

    int mid = (s+e)/2;
    ll left = rcal(l,r,s,mid,node*2);
    ll right = rcal(l,r,mid+1,e,node*2+1);

    return min(left,right);
}

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> k;
    for (i=1; i<n+1; i++) {
        cin >> d[i];
    }

    linit();
    rinit();

    ll res = -INF;

    for (i=1; i<n+1; i++) {
        a = lcal(i+1,n); a -= i*k;
        b = rcal(0,i-1); b -= (n+1-i)*k;

        res = max(res,d[i]-min(a,b));
    }

    cout << res;

    return 0;
}