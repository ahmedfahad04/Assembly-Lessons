#include <bits/stdc++.h>
using namespace std;

const int N = 1e+7;

vector<int> adj[N];
int parent[N];
int dis[N];

int bfs(int n, int src, int dest){

    for(int i=0; i<n; i++) dis[N] = -1;

    queue<int> q;
    q.push(src);
    dis[src] = 0;
    

    while(!q.empty()){

        int u = q.front();
        q.pop();

        if (u == dest) return dis[u];

        for(int i=0; i<(int)adj[u].size(); i++){
            
            int v = adj[u][i];

            if(dis[v] == -1 or dis[v] > dis[u]+1){
                dis[v] = dis[u] + 1;
                parent[v] = u;
                q.push(v);
            }

        }
    }
    
    return -1;
}

int main(){

    int n,m;

    cin >> n >> m;

    while(m--){

        int u,v;
        cin >> u >> v;

        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int d = bfs(n, 0, 3);

    cout << "Distance of " << n-1 << " from 0: " << d << endl;

}