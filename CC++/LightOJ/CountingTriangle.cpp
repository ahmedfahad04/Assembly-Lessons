#include <bits/stdc++.h>
#define ll long long
using namespace std;
int cnt = 0;

bool checkTriangle(int a, int b, int c)
{
    if ((a + b) > c && (b + c) > a && (c + a) > b)
        return true;
    else
        return false;
}

void permute(vector<int> arr, int id, int size, vector<int> val)
{

    if (val.size() == 2)
    {
        if (id < size)
        {
            val.push_back(arr[id]);

            if(checkTriangle(val[0], val[1], val[2])) cnt++;

            val.clear();
            
        }

        return;
    }
    else
    {
        val.push_back(arr[id]);
        id++;

        permute(arr, id, size, val);

        while (id < size)
            permute(arr, ++id, size, val); //01787697583
    }
}

int main()
{

    int t, tc=0;
    cin >> t;

    while (t--)
    {
        int n;
        cin >> n;

        vector<int> arr, ans;
        for (int i = 0; i < n; i++)
        {
            int x;
            cin >> x;
            arr.push_back(x);
        }

        for (int i = 0; i < n; i++)
        {
            permute(arr, i, n, ans);
        }

        cout << "Case " << ++tc << ": " << cnt << endl;
        cnt = 0;
    }
}