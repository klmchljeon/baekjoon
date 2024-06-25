/*
    C++ Hello, World! 예제
*/
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int n,q;
int a,b;
int idx;
set<int> st;


int main()
{
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    
    cin >> n >> q;
    for (int i=0; i<n; i++) {
        cin >> a;
        if (a == 1) st.insert(i);
    }

    for (int i=0; i<q; i++) {
        cin >> a;
        if (a == 1) {
            cin >> b;
            if (st.find(b-1) == st.end()) {
                st.insert(b-1);
            }
            else {
                st.erase(b-1);
            }
        }

        if (a == 2) {
            cin >> b;
            idx = (idx + b)%n;
        }

        if (a == 3) {
            set<int>::iterator it = st.lower_bound(idx);
            if (it == st.end()) {
                it = st.lower_bound(0);
                if (it == st.end()) {
                    cout << -1;
                }
                else {
                    cout << *it - idx + n;
                }
            }
            else {
                cout << *it - idx;
            }

            cout << '\n';
        }

    }

    return 0;
}