#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int mini(int x, int y, int z){
	int t = x < y ? x : y;
	return t < z ? t : z;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t, n, x, y, k;
    vector<int> c;
    cin >> t;

    int r;
    int candidates;
    int ans;
    int replace;
    vector<pair<int, int>> inter;
    while(t--){
        cin >> n >> x >> y >> k;
        c.clear();
        for(int i = 0; i < n; i++){
            cin >> r;
            c.push_back(r);
        }
        inter.clear();
        candidates = 0;
        ans = 1;
        sort(c.begin(), c.end());
        for(int i = 1; i < n; i++){
            if(c[i]==c[i-1]) {
                candidates++;
            } else {
                ans++;
                if(c[i]!=c[i-1]+1) {
                    inter.push_back(make_pair(c[i-1]+1, c[i]-1));
                }
            }
        }
        //process viable replace colors
        replace = 0;
        for(int i = 0; i < inter.size(); i++) {
            if(inter[i].first > y || inter[i].second < x) {
                continue;
            }
            inter[i].first = inter[i].first > x ? inter[i].first : x ;
            inter[i].second = inter[i].second < y ? inter[i].second : y ;
            replace += (inter[i].second - inter[i].first + 1);
        }
		//inserting additional off constraint replaces
		if(x < c[0]) {
			if(y < c[0]) {
				replace += y - x + 1;
			} else {
				replace += c[0] - x;
			}
		}
		if(y > c[n-1]) {
			if(x > c[n-1]){
				replace += y - x + 1;
			}
			else {
				replace += y - c[n-1];
			}
		}
        ans += mini(candidates, replace, k);
        cout << ans << endl;
    }
}