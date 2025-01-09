#include <bits/stdc++.h>
#include <iostream>

using namespace std;

vector<pair<int,int>> v;
set<int> st;

bool func(pair<int,int> a, pair<int,int> b) {
    if (a.first != b.first) {
        return a.first < b.first;
    }
    return a.first < b.first;
}

int main()
{
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);

    int n,k;
    int a,b;
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        cin >> a >> b;
        v.push_back({a,b});
    }

    sort(v.begin(), v.end(), func);

    //for (auto i:v) {
    //    cout << i.first << ' ' << i.second << '\n';
    //}

    int prev = v[0].first;
    vector<int> p;

    int m = -2 * 1e9 - 1;
    int res = m;
    for (auto i:v) {
        if (i.first == prev) {
            p.push_back(i.second);
            continue;
        }

        if (!st.empty()) {
            for (int num:p) {
                auto it = st.upper_bound(k-num);
                if (it != st.begin()) {
                    it--;
                    
                    if (num + *it <= k) {
                        res = max(res,num + *it);
                    }
                }
            }
        }

        for (int num:p) {
            st.insert(num);
        }

        p.clear();
        p.push_back(i.second);

        prev = i.first;
    }

    if (!st.empty()) {
        for (int num:p) {
            auto it = st.upper_bound(k-num);
            if (it != st.begin()) {
                it--;
                if (num + *it <= k) {
                    res = max(res,num + *it);
                }
            }
        }
    }

    if (res != m) {
        cout << res;
    }
    else {
        cout << "NO";
    }

    return 0;
}
