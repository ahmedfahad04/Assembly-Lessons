#include <bits/stdc++.h>
using namespace std;

const int N = 1e+7;

vector<int> adj[N];
int parent[N];
int dis[N];

void bfs(int n, int src, int dest){

    for(int i=0; i<n; i++) dis[N] = -1;

    queue<int> q;
    q.push(src);
    dis[src] = 0;
    

    while(!q.empty()){

        int u = q.front();
        q.pop();

        cout << u << ":";

        // if (u == dest) return dis[u];

        for(int i=0; i<(int)adj[u].size(); i++){
            
            int v = adj[u][i];

            cout << " " << v;

            if(dis[v] == -1 or dis[v] > dis[u]+1){
                dis[v] = dis[u] + 1;
                parent[v] = u;
                q.push(v);
            }
        }

        cout << "\nAFTER: " << q.front() << " ";
    }
}

int main(){

    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int n,m;

    cin >> n >> m;

    while(m--){

        int u,v;
        cin >> u >> v;

        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    for(int i=0; i<n; i++){
        cout << i << ":";
        for(int j=0; j<(int)adj[i].size(); j++){
            cout << " " << adj[i][j];
        }

        cout << endl;
    }

    cout << "\n\nAfter applying BFS.\n";
    bfs(n, 0, 3);

    cout << "\n\nDistance of " << 3 << " from 0: " << dis[3] << endl;

}