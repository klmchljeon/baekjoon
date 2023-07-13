#include <bits/stdc++.h>

#define ll long long
using namespace std;

int i;
int n,m,k;
int q,a,b;
ll c;

ll d[1000001];
ll tree[4000001];
ll lazy[4000001];

void propagate(int s, int e, int node) {
    ll tmp = lazy[node];
    if (tmp != 0) {
        if (s!=e) {
            lazy[node*2] += tmp;
            lazy[node*2+1] += tmp;
        }

        tree[node] += (e-s+1)*tmp;
        lazy[node] = 0;
    }
}

ll init(int s=1, int e=n, int node=1) {
    if (s==e) {
        tree[node] = d[s];
        return d[s];
    }

    int mid = (s+e)/2;
    ll left = init(s,mid,node*2);
    ll right = init(mid+1,e,node*2+1);

    tree[node] = left + right;
    return tree[node];
}

void update(int l,int r, ll val, int s=1, int e=n, int node=1) {
    propagate(s,e,node);

    if (e<l || r<s) {
        return;
    }

    if (l<=s && e<=r) {
        lazy[node] = val;
        propagate(s,e,node);
        return;
    }

    int mid = (s+e)/2;
    update(l,r,val,s,mid,node*2);
    update(l,r,val,mid+1,e,node*2+1);

    tree[node] = tree[node*2] + tree[node*2+1];
    return;
}

ll cal(int l, int r, int s=1, int e=n, int node=1) {
    propagate(s,e,node);

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

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m >> k;
    for (i=1; i<n+1; i++) {
        cin >> d[i];
    }

    init();

    m += k;
    while (m--) {
        cin >> q >> a >> b;
        if (q==1) {
            cin >> c;
            update(a,b,c);
        }
        else {
            cout << cal(a,b) << '\n';
        }
    }

    return 0;
}