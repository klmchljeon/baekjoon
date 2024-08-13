#include <iostream>

using namespace std;

int main()
{
    int e,s,m;
    int a,b,c;
    int result = 1;
    cin >> e >> s >> m;
    a = b = c = 1;

    while (1) 
    {
        if (a==e and b==s and c==m) 
        {
            cout << result;
            break;
        }
        a++;
        b++;
        c++;
        result++;
        if (a>15) {a=1;}
        if (b>28) {b=1;}
        if (c>19) {c=1;}
    }
}