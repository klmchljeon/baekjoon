#include <iostream>
#include <vector>

using namespace std;

int i,tmp;
int n,k;
vector<int> v;

bool check(int num) {
    int cnt = 0;
    int tmp = 0;
    for (i=0; i<v.size(); i++) {
        tmp += v[i];
        if (tmp >= num) {
            tmp = 0;
            cnt++;
        }
    }
    return (cnt >= k);
}

int main() {
    int s,e,mid;

    cin >> n >> k;
    for (i=0; i<n; i++) {
        cin >> tmp;
        v.push_back(tmp);
    }

    s = 0;
    e = 20e5+1;
    while (s+1<e) {
        mid = (s+e)/2;

        if (check(mid)) {
            s = mid;
        }
        else { 
            e = mid;
        }
    }
    cout << s << '\n';

    return 0;
}