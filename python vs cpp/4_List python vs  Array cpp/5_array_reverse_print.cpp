#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;  // Input the size of the array

    int ar[n];  // Declare an array of size 'n'

    // Input 'n' values into the array
    for (int i = 0; i < n; i++) {
        cin >> ar[i];
    }

    // Print the array elements in reverse order
    for (int i = n - 1; i >= 0; i--) {
        cout << ar[i] << " ";
    }

    return 0;
}
