#include <bits/stdc++.h>
#define ll long 
using namespace std;

bool checkTriangle(ll a, ll b, ll c)
{
    if ((a + b) > c && (b + c) > a && (c + a) > b)
        return true;
    else
        return false;
}

int main()
{

    int t, tc=0;
    cin >> t;

    while (t--)
    {
        int n, cnt=0;
        cin >> n;

        vector<ll> arr, ans;
        for (ll i = 0; i < n; i++)
        {
            ll x;
            cin >> x;
            arr.push_back(x);
        }

        sort(arr.begin(), arr.end());

        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                int x = lower_bound(arr.begin(), arr.end(), arr[i]+arr[j])-arr.begin();
                cnt += n-x;
                cout << arr[i]+arr[j] << "-> " << cnt <<endl;
                
            }
        }

        cout << "Case " << ++tc << ": " << cnt << endl;
        cnt = 0;
    }
}