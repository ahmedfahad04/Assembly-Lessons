#include <bits/stdc++.h>
#define ll long long
using namespace std;
int cnt = 0;



void permute(int arr[], int id, int limit, int size, vector<int> val)
{

    if (val.size() == limit - 1)
    {
        if (id < size)
        {
            val.push_back(arr[id]);

            cout << "\nElements: ";
            for (int el : val)
            {
                cout << el << " ";
            }

            val.clear();
            cnt++;
        }

        return;
    }
    else
    {
        val.push_back(arr[id]);
        id++;

        permute(arr, id, limit, size, val);

        while(id < size) 
        permute(arr, ++id, limit, size, val);
    }
}

int main()
{

    int n;
    cout << "n: ";
    cin >> n;

    int r;
    cout << "r: ";
    cin >> r;

    int arr[100];
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    vector<int> ans;

    for (int i = 0; i < n; i++)
    {
        cout << "\nPermutation of " << arr[i] << " is: " << endl;
        permute(arr, i, r, n, ans);
    }

    cout << "Total Combination: " << cnt << endl;
}