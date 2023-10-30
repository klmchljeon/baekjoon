#include <bits/stdc++.h>
using namespace std;

int p,t,a;
vector<int> v;
int res;

int main() {
    cin >> p;
    for (int i=0; i<p; i++) {
        cin >> t;
        v.push_back(t);
    }

    cin >> a;
    res = 0;
    for (int i=0; i<p; i++) {
        if (v[i] == a) {
            res++;
        }
    }
    cout << res;
}