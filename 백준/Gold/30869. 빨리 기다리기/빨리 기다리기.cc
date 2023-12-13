#include <iostream>
#include <bits/stdc++.h>

using namespace std;

const int inf = 1e9;

int n,m,k;
int s,e,t,g;
int c,x,nx,st;
int res;

pair<int,int> tmp;
vector<pair<pair<int,int>,int>> d[501];
int dis[501][501];
priority_queue<pair<int,int>> pq;

int main()
{
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m >> k;
    for (int i=0; i<m; i++) {
        cin >> s >> e >> t >> g;
        d[s].push_back({{e,t},g});
    }

    for (int i=1; i<n+1; i++) {
        for (int j=0; j<k+1; j++) {
            dis[i][j] = inf;
        }
    }
    dis[1][0] = 0;

    pq.push({0,1});
    while (pq.size()) {
        tmp = pq.top();
        pq.pop();

        c = -tmp.first;
        x = tmp.second;
        if (dis[x][0] < c) continue;

        s = dis[x][0];
        for (auto a:d[x]) {
            nx = a.first.first;
            t = a.first.second;
            g = a.second;

            st = s%g;
            if (st > 0) st = g - st;

            if (dis[nx][0] > s + st+t) {
                dis[nx][0] = s + st+t;
                pq.push({-dis[nx][0],nx});
            }
        }
    }

    for (int p=1; p<k+1; p++) {
        for (int i=1; i<n+1; i++) {
            for (auto a:d[i]) {
                nx = a.first.first;
                t = a.first.second;
                
                dis[nx][p] = min(dis[nx][p], dis[i][p-1]+t);
            }
        }

        for (int i=1; i<n+1; i++) {
            if (dis[i][p] != inf) {
                pq.push({dis[i][p],i});
            }
        }

        while (pq.size()) {
            tmp = pq.top();
            pq.pop();

            c = -tmp.first;
            x = tmp.second;
            if (dis[x][p] < c) continue;

            s = dis[x][p];
            for (auto a:d[x]) {
                nx = a.first.first;
                t = a.first.second;
                g = a.second;

                st = s%g;
                if (st > 0) st = g - st;

                if (dis[nx][p] > s + st+t) {
                    dis[nx][p] = s + st+t;
                    pq.push({-dis[nx][p],nx});
                }
            } 
        }
    }

    res = inf;
    for (int j=0; j<k+1; j++) {
        res = min(res,dis[n][j]);
    }
    
    if (res == inf) res = -1;

    cout << res;

    return 0;
}