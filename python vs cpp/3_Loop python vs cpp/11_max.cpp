#include<bits/stdc++.h>
using namespace std;

int main() {
    int n, a;
    cin >> n;
    int max = INT_MIN, min = INT_MAX;
    
    for (int i = 1; i <= n; i++) {
        cin >> a;
        if (a > max) {
            max = a;
        }
        if (a < min) {
            min = a;
        }
    }
    
    cout << min << " " << max << endl;
    return 0;
}
