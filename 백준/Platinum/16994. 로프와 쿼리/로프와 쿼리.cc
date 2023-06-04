//로프와 쿼리
#include<iostream>
#include<ext/rope>
#include<string>
using namespace std;
using namespace __gnu_cxx;

int q,n,x,y;
string a;
rope<char> r;
rope<char> tmp;

int main()
{
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);

    cin >> a;

    for (auto i:a) {
        r.push_back(i);
    }

    cin >> q;
    while (q--) {
        cin >> n >> x;
        if (n==1) {
            cin >> y;
            tmp = r.substr(x,y-x+1);
            r.erase(x,y-x+1);
            r = tmp + r;
        }
        else if (n==2) {
            cin >> y;
            tmp = r.substr(x,y-x+1);
            r.erase(x,y-x+1);
            r = r + tmp;
        }
        else {
            cout << r.substr(x,1) << '\n';
        }
    }
}