//Copy and Paste
#include<iostream>
#include<ext/rope>
#include<string>
using namespace std;
using namespace __gnu_cxx;

int m,n,a,b,c;
string s;
rope<char> res;
rope<char> tmp;

int main()
{
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);

    cin >> m >> s >> n;
    for (auto i:s) {
        res.push_back(i);
    }

    while (n--) {
        cin >> a >> b >> c;
        tmp = res.substr(a,b-a);
        res.insert(c,tmp);

        if (res.size() > m) {
            res.erase(m,res.size()-m);
        }
    }

    for (auto i:res) {
        cout << i;
    }
    cout << '\n';

}