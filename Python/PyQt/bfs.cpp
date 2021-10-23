#include <bits/stdc++.h>
using namespace std;

const int N = 50;

vector<int> adj[N];
int parent[N];
int dis[N];

int bfs(int n, int src, int dest){

    //initialize
    for(int i=0; i<n; i++) dis[i] = -1;

    // make the queue
    queue<int> q;
    q.push(src);
    dis[src] = 0;

    while(!q.empty()){

        int u = q.front();
        q.pop();

        if (u == dest) return dis[u];

        for(int i=0; i<adj[u].size(); i++){
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
    
    int node, m;

    while(m--){
        int u,v;
        cin >> u >> v;

        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int distance = bfs(node, 0, 2);

    cout << "Distance: " << distance << endl;

    
}
