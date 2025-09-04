#include <bits/stdc++.h>

using namespace std;

int parent[4000]; 
vector<int> v;

int idx[(1<<20)+1];

int dp[4000][2001];
int p[4000][2001];

map<int,int> mp;

int find(int x) {
    if (parent[x] == x) return x;
    return parent[x] = find(parent[x]);
}

void merge(int a, int b) {
    int pa = find(a);
    int pb = find(b);

    if (pa < pb) {
        parent[pb] = pa;
    }
    else if (pa > pb) {
        parent[pa] = pb;
    }
}

int main() {
    int n,tmp;
    cin >> n;
    for (int i = 0; i < 2*n; i++) {
        cin >> tmp;
        v.push_back(tmp);
        idx[tmp] = i;
    }
    
    for (int i = 0; i < 2*n; i++) {
        parent[i] = i;
    }

    for (int i = 0; i < 2*n-1; i++) {
        for (int j = i+1; j < 2*n; j++) {
            if (((v[i]^v[j])&((v[i]^v[j])-1)) == 0) {
                merge(i,j);
            }
        }
    }

    vector<vector<int>> vi;
    for (int i = 0; i < 2*n; i++) {
        if (mp.find(find(i)) == mp.end()) {
            mp.insert({find(i),mp.size()});
            
            vector<int> vtmp;
            vi.push_back(vtmp);
        }

        vi[mp[find(i)]].push_back(i);
    }

    dp[0][0] = 1;
    p[0][0] = 0;

    dp[0][vi[0].size()] = 1;
    p[0][vi[0].size()] = 1;

    for (int i = 0; i < vi.size(); i++) {
        for (int j = 0; j < n+1; j++) {
            if (!dp[i][j]) continue;

            dp[i+1][j] = 1;
            p[i+1][j] = 0;

            if (j+vi[i+1].size() < n+1) {
                dp[i+1][j+vi[i+1].size()] = 1;
                p[i+1][j+vi[i+1].size()] = 1;
            }
        }
    }

    if (!dp[vi.size()-1][n]) {
        cout << -1;
        return 0;
    }

    vector<int> a;
    vector<int> b;
    int val = n;
    for (int i = vi.size()-1; i > -1; i--) {
        if (p[i][val]) {
            for (int j = 0; j < vi[i].size(); j++) {
                a.push_back(vi[i][j]);
            }
            
            val -= vi[i].size();
        }
        else {
            for (int j = 0; j < vi[i].size(); j++) {
                b.push_back(vi[i][j]);
            }      
        }
    }

    for (int i = 0; i < n; i++) {
        cout << v[a[i]] << ' ';
    }
    cout << '\n';
    
    for (int i = 0; i < n; i++) {
        cout << v[b[i]] << ' ';
    }
    
    return 0;
}