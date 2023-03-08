//구간 합 구하기
#include <iostream>

#define ll long long
using namespace std;

int i;
int n,m,k;
int a,b;
ll c;

ll d[1000001];
ll tree[4000001];

ll init(int s=1, int e=n, int node = 1) {
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

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m >> k;
    for (i=1; i<n+1; i++) {
        cin >> d[i];
    }

    init();

    for (i=0; i<m+k; i++) {
        cin >> a >> b >> c;
        if (a==1) {
            update(b,c);
        }
        else {
            cout << cal(b,c) << '\n';
        }
    }

    return 0;
}