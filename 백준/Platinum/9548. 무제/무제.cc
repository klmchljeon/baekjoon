//로프와 쿼리
#include<iostream>
#include<ext/rope>
#include<string>
using namespace std;
using namespace __gnu_cxx;

int t,x,y;
string s,r,q;
rope<char> res;
rope<char> tmp;

int main()
{
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);

    cin >> t;

    while (t--) {
        cin >> s;
        for (auto i:s) {
            res.push_back(i);
        }

        while (1) {
            cin >> q;

            if (q=="I") {
                cin >> r >> x;
                tmp.clear();
                for (auto i:r) {
                    tmp.push_back(i);
                }
                res.insert(x,tmp);
            }
            else if (q=="P") {
                cin >> x >> y;
                for (auto i:res.substr(x,y-x+1)) {
                    cout << i;
                }
                cout << '\n';
            }
            else {
                res.clear();
                break;
            }
        }
    }
}