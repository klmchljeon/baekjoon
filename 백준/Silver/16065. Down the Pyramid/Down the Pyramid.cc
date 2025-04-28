#include <iostream>
#include <vector>

using namespace std;

int main()
{
    //입력변수
    int n;
    int tmp;
    vector<int> v;

    //입력
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        v.push_back(tmp);
    }

    //아래 수열에 대해,
    //위 수열을 한 칸씩 추가하며 가능한 범위를 체크
    
    //위 수열의 1번 칸에 대해, 아래 수열의 2번 칸이 가질 수 있는 범위
    int s = 0;
    int e = v[0];
    for (int i = 1; i < n; i++) {
        //가능한 가장 작은 값인 s도 불가능하다면, 가능한 경우의 수 없음
        if (v[i] - s < 0) {
            cout << 0;
            return 0;
        }

        //이전 칸이 s일 때 다음 칸의 값
        int ns = v[i] - s; 
        ns = min(ns,v[i]); //v[i]를 넘지 못함
        
        //이전 칸이 e일 때 다음 칸의 값
        int ne = v[i] - e;
        ne = max(ne,0); //0 이상이어야 함

        //(s~e) -> (ns~ne)이므로 ne <= ns. 뒤집어줌
        s = ne;
        e = ns;
    }

    //출력
    cout << e-s+1;

    return 0;
}
