#include <iostream>
using namespace std;

typedef long long LL;

int main() {
    LL t, w, l, m, x, y;
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> t;
    while (t--)
    {
        cin >> w >> l >> m >> x >> y;
        if(x < y) {
            if(w <= m - y) {
            cout << "JUMP\n";
        } else {
            cout << "FALL\n";
        }

        } else {
            if(w <= m - x) {
            cout << "JUMP\n";
        } else {
            cout << "FALL\n";
        }
        }
        
    }
    
}