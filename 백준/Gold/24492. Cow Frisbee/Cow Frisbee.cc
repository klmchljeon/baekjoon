//Cow Frisbee
#include <iostream>
#include <stack>
#include <vector>

#define ll long long
using namespace std;

int n;
int a,idx;
ll res;

stack<pair<int,int>> st;

int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;
    for (int i=0; i<n; i++) {
        cin >> a;
        while (!st.empty() && st.top().first < a) {
            idx = st.top().second;
            st.pop();
            res += i-idx+1;
        }

        if (!st.empty()) {
            res += i-st.top().second+1;
        }

        st.push({a,i});
    }

    cout << res;

    return 0;
}