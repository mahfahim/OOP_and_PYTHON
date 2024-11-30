#include<bits/stdc++.h>
using namespace std;

int main() {
    long long int sum = 0;
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        sum += i;
    }
    cout << sum << endl;
    return 0;
}
