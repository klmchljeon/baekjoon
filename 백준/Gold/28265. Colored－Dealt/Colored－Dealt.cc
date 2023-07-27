#include <string>
#include "colored_dealt.h"

using namespace std;

string guess(int N)
{
    string res;
    int i,j;
    int num = 3*N;
    int x,dif;

    for (i=1; i<N+1; i++) {
        string s;
        for (j=0; j<i; j++) {
            s += 'R';
        }
        for (j=i; j<N; j++) {
            s += 'B';
        }

        x = design(s);
        dif = num-x;
        if (dif == 0) {
            res += 'B';
        }
        else if (dif == 1) {
            res += 'G';
        }
        else {
            res += 'R';
        }
        num = x;
    }

    return res;
}
