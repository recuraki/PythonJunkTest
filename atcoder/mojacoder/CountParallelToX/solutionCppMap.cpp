#include <iostream>
#include <map>
using namespace std;
#define FOR(i, begin, end) for(int i=(begin),i##_end_=(end);i<i##_end_;i++)
#define REP(i, n) FOR(i,0,n)
int main(){
    map<int, int> cnt;
    int N; cin >> N;
    REP(i, N){
        int x, y; cin >> x >> y;
        ++cnt[x];
    }
    int Q; cin >> Q;
    REP(i, Q){
        int a; cin >> a;
        cout << cnt[a];
        if(i==(Q-1)) cout << endl;
        else cout << " ";
    }
}