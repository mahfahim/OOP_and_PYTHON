#include<bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;  // Input the size of the array

    int ar[n];  // Declare an array of size 'n'

    // Input 'n' values into the array
    for (int i = 0; i < n; i++) {
        cin >> ar[i];
    }

    int sum = 0;
    // Calculate the sum of the array elements
    for (int i = 0; i < n; i++) {
        sum += ar[i];
    }

    // Output the sum
    cout << sum;

    return 0;
}
