#include <bits/stdc++.h>
using namespace std;

int main()
{
    int ans[60][60];

    for (int row = 1; row <= 60; row++)
    {
        for (int col = 1; col <= row; col++)
        {
            ans[row][col] = 0;
        }
        cout << endl;
    }

    /*
        1
        1 1
        1 2 1
        1 3 3 1
        */

    for (int row = 1; row <= 60; row++)
    {
        for (int col = 1; col <= row; col++)
        {

            if (col == 1)
                ans[row][col] = 1; // first element
            else if (col == row)
                ans[row][col] = 1; // last element

            else
            {
                ans[row][col] = ans[row - 1][col - 1] + ans[row - 1][col];
            }
        }
    }

    int t;
    cin >> t;

    while (t--)
    {
        int n;
        cin >> n;

        for (int row = 1; row <= n+1; row++)
        {
            for (int col = 1; col <= row; col++)
            {
                cout << ans[row][col] << " ";
            }
            cout << endl;
        }

        cout << endl;
    }
}