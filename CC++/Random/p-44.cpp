#include <bits/stdc++.h>
using namespace std;
#define ll long long

ll fact(ll n)
{
    if (n == 0 or n == 1)
        return 1;
    return n * fact(n - 1);
}

ll nCr(ll n, ll r)
{
    ll nominator = fact(n);
    ll denominator = fact(r) * fact(n - r);

    return nominator / denominator;
}

int main()
{
    int tc;
    cin >> tc;

    while (tc--)
    {
        int n;
        cin >> n;

        int x = 1;

        if (n == 0)
        {
            cout << 1 << endl;
        }
        else
        {

            cout << 1 << endl;

            for (int i = 0; i < n; i++)
            {
                for (int r = 0; r < i + 1; r++)
                {
                    cout << nCr(x, r) << " ";
                }

                cout << 1 << endl;
                x++;
            }

        }

        cout << endl;
    }
}