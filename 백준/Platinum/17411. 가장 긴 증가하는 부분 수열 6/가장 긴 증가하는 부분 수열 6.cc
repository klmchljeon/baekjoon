//가장 긴 증가하는 부분 수열 6
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

#define ll long long
using namespace std;

int mod = 1e9+7;
int tmp;
int n,sqn;
pair<int,int> sum;

vector<pair<ll,int>> v;
pair<int,int> tree[4000001];

pair<int,int> cal(int l, int r, int s=1, int e=n, int node=1) {
    if (e<l || r<s) {
        return {0,0};
    }

    if (l<=s && e<=r) {
        return tree[node];
    }

    int mid = (s+e)/2;
    pair<int,int> left = cal(l,r,s,mid,node*2);
    pair<int,int> right = cal(l,r,mid+1,e,node*2+1);

    if (left.first > right.first) {
        return left;
    }
    else if (left.first < right.first) {
        return right;
    }
    else {
        return {left.first, (left.second+right.second)%mod};
    }
}

void update(int idx, pair<int,int> val, int s=1, int e=n, int node=1) {
    if (s==e) {
        if (val.first) {
            tree[node] = {val.first+1, val.second};
        }
        else {
            tree[node] = {1,1};
        }
        return;
    }

    int mid = (s+e)/2;
    if (idx <= mid) {
        update(idx,val,s,mid,node*2);
    }
    else {
        update(idx,val,mid+1,e,node*2+1);
    }

    pair<int,int> left = tree[node*2];
    pair<int,int> right = tree[node*2+1];

    if (left.first > right.first) {
        tree[node] = left;
    }
    else if (left.first < right.first) {
        tree[node] = right;
    }
    else {
        tree[node] = {left.first, (left.second+right.second)%mod};
    }
    return;
}

bool compare(pair<ll,int> a, pair<ll,int> b) {
    if (a.first == b.first) {
        return b.second < a.second;
    }
    else {
        return a.first < b.first;
    }
}

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;
    sqn = (int)sqrt(n) + 1;
    for (int i=1; i<n+1; i++) {
        cin >> tmp;
        v.push_back({tmp,i});
    }
    
    sort(v.begin(),v.end(),compare);
    for (int i=0; i<n; i++) {
        sum = cal(1,v[i].second-1);
        update(v[i].second,sum);
    }

    pair<int,int> ans = cal(1,n);
    cout << ans.first << ' ' << ans.second << '\n';
}