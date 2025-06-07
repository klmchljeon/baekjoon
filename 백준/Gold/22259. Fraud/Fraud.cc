#include <iostream>
#include <vector>
using namespace std;

class frac {
    private:
        long long u,d;

    public:
        frac(long long u, long long d) {
            if (d < 0) {
                u = -u;
                d = -d;
            }

            if (u == 0) {
                d = 1;
            }

            this->u = u;
            this->d = d;
        }

    bool operator < (const frac &other) const {
        return u * other.d < other.u * d;
    }

    bool operator == (const frac &other) const {
        return u * other.d == other.u * d;
    }

    bool operator > (const frac &other) const {
        return u * other.d > other.u * d;
    }

    friend ostream& operator<<(ostream& os, const frac& f) {
        os << f.u << "/" << f.d;
        return os;
    }
};

int main() {
    int n;
    long long tmp;
    vector<long long> a,b;

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        a.push_back(tmp);
    }
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        b.push_back(tmp);
    }
    
    frac low = frac(0,1); 
    frac high = frac(1000000000000,1); 

    bool flag = true;
    for (int i = 0; i < n-1; i++) {
        if (a[i] == a[i+1]) {
            if (b[i] == b[i+1]) {
                flag = false;
                break;
            }

            if (b[i] < b[i+1]) {
                flag = false;
                break;
            }

            continue;
        }

        frac k = frac(b[i]-b[i+1],a[i+1]-a[i]);

        if (a[i] > a[i+1]) {
            if (low < k) {
                low = k;
            }
        }
        else {
            if (high > k) {
                high = k;
            }
        }

        //cout << k << '\n';
    }

    if (flag && low < high) {
        cout << "YES";
    }
    else {
        cout << "NO";
    }
    //cout << '\n' << low << ' ' << high;

    return 0;
}
