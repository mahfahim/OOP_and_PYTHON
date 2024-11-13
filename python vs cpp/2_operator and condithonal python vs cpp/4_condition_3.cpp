#include<bits/stdc++.h>
using namespace std;

int main() {
    int tk;
    cin >> tk;
    if (tk >= 5000) {
        cout << "Cox's Bazar jabo" << endl;
        if (tk >= 10000) {
            cout << "Saint Martin jabo" << endl;
        } else {
            cout << "Ferot chole jabo" << endl;
        }
    } else {
        cout << "Kothao jabo na" << endl;
    }
    return 0;
}
