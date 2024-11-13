#include<bits/stdc++.h>
using namespace std;

int main() {
    int tk;
    cin >> tk;
    if (tk >= 100) {
        cout << "Burger khabo";
    } else if (tk >= 50) {
        cout << "Fuchka khabo";
    } else if (tk >= 20) {
        cout << "Ice cream khabo";
    } else {
        cout << "Khabo na";
    }

    return 0;
}
