#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <sstream>
#include <typeinfo>
#include <fstream>


template<typename T,size_t X>
struct BinaryTrie{
    struct Node{
        bool f;
        size_t cnt;
        Node *p,*l,*r;
        Node(bool f,Node* p):f(f),cnt(0),p(p){l=r=nullptr;}
    };

    T acc;
    Node *root;
    BinaryTrie():acc(0){root=emplace(0,nullptr);}

    inline Node* emplace(bool f,Node* p){
        return new Node(f,p);
    }

    inline size_t count(Node* a){
        return a?a->cnt:0;
    }

    void add(const T b,size_t k=1){
        const T nb=b^acc;
        Node* a=root;
        for(int i=X-1;i>=0;i--){
            bool f=(nb>>i)&1;
            if(!f&&!a->l) a->l=emplace(f,a);
            if( f&&!a->r) a->r=emplace(f,a);
            a=f?a->r:a->l;
        }
        a->cnt+=k;
        while((a=a->p)) a->cnt=count(a->l)+count(a->r);
    }

    inline void update(const T b){acc^=b;}

    Node* find(const T b){
        const T nb=b^acc;
        Node* a=root;
        for(int i=X-1;i>=0;i--){
            bool f=(nb>>i)&1;
            a=f?a->r:a->l;
            if(!a) return a;
        }
        return a;
    }

    Node* check(Node *a){
        if(!a||count(a)) return a;
        delete(a);
        return nullptr;
    }

    void sub(Node* a,size_t k=1){
        assert(a&&a->cnt>=k);
        a->cnt-=k;
        while((a=a->p)){
            a->l=check(a->l);
            a->r=check(a->r);
            a->cnt=count(a->l)+count(a->r);
        }
    }

    Node* xmax(const T b){
        assert(count(root));
        const T nb=b^acc;
        Node* a=root;
        for(int i=X-1;i>=0;i--){
            bool f=(nb>>i)&1;
            a=(!a->l||(!f&&a->r))?a->r:a->l;
        }
        return a;
    }

    int xmin(const T b){
        return xmax(~b&((T(1)<<X)-1));
    }

    Node* ge(Node *a){
        if(a&&(a->r||a->l)) return a->l?a->l:a->r;
        return a;
    }

    Node* next(Node* a){
        while(a->p){
            if(a->p->l==a) return ge(a->p->r);
            a=a->p;
        }
        return nullptr;
    }

    Node* lower_bound(const T b){
        const T nb=b^acc;
        Node* a=root;
        for(int i=X-1;i>=0;i--){
            bool f=(nb>>i)&1;
            if(!f&&a->l){a=a->l;continue;}
            if( f&&a->r){a=a->r;continue;}
            if(f) return next(a);
            return ge(a->r);
        }
        return a;
    }

    int upper_bound(const T b){
        return lower_bound(b+1);
    }

    T val(Node* a){
        T res(0);
        for(int i=0;i<(int)X;i++){
            bool f=(acc>>i)&1;
            res|=(T(a->f)<<i)^f;
            a=a->p;
        }
        return res^acc;
    }

    Node* find_by_order(size_t k){
        Node *a=root;
        if(count(a)<=k) return nullptr;
        for(int i=X-1;i>=0;i--){
            bool f=(acc>>i)&1;
            if(count(f?a->r:a->l)<=k){
                k-=count(f?a->r:a->l);
                a=f?a->l:a->r;
            }else{
                a=f?a->r:a->l;
            }
        }
        return a;
    }

    size_t order_of_key(const T b){
        const T nb=b^acc;
        Node *a=root;
        size_t res=0;
        for(int i=X-1;i>=0;i--){
            bool f=(nb>>i)&1;
            if(f) res+=count(a->l);
            a=f?a->r:a->l;
            if(!a) break;
        }
        return res;
    }
};

using namespace std;

class YetAnotherGraphColoring {
    public:
    int minColors(int n, int a1, int a2, int x, int y, int z, int m) {
        return 0;
    }
};

// CUT begin
ifstream data("YetAnotherGraphColoring.sample");

string next_line() {
    string s;
    getline(data, s);
    return s;
}

template <typename T> void from_stream(T &t) {
    stringstream ss(next_line());
    ss >> t;
}

void from_stream(string &s) {
    s = next_line();
}

template <typename T>
string to_string(T t) {
    stringstream s;
    s << t;
    return s.str();
}

string to_string(string t) {
    return "\"" + t + "\"";
}

bool do_test(int n, int a1, int a2, int x, int y, int z, int m, int __expected) {
    time_t startClock = clock();
    YetAnotherGraphColoring *instance = new YetAnotherGraphColoring();
    int __result = instance->minColors(n, a1, a2, x, y, z, m);
    double elapsed = (double)(clock() - startClock) / CLOCKS_PER_SEC;
    delete instance;

    if (__result == __expected) {
        cout << "PASSED!" << " (" << elapsed << " seconds)" << endl;
        return true;
    }
    else {
        cout << "FAILED!" << " (" << elapsed << " seconds)" << endl;
        cout << "           Expected: " << to_string(__expected) << endl;
        cout << "           Received: " << to_string(__result) << endl;
        return false;
    }
}

int run_test(bool mainProcess, const set<int> &case_set, const string command) {
    int cases = 0, passed = 0;
    while (true) {
        if (next_line().find("--") != 0)
            break;
        int n;
        from_stream(n);
        int a1;
        from_stream(a1);
        int a2;
        from_stream(a2);
        int x;
        from_stream(x);
        int y;
        from_stream(y);
        int z;
        from_stream(z);
        int m;
        from_stream(m);
        next_line();
        int __answer;
        from_stream(__answer);

        cases++;
        if (case_set.size() > 0 && case_set.find(cases - 1) == case_set.end())
            continue;

        cout << "  Testcase #" << cases - 1 << " ... ";
        if ( do_test(n, a1, a2, x, y, z, m, __answer)) {
            passed++;
        }
    }
    if (mainProcess) {
        cout << endl << "Passed : " << passed << "/" << cases << " cases" << endl;
        int T = time(NULL) - 1619180140;
        double PT = T / 60.0, TT = 75.0;
        cout << "Time   : " << T / 60 << " minutes " << T % 60 << " secs" << endl;
        cout << "Score  : " << 400 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT)) << " points" << endl;
    }
    return 0;
}

int main(int argc, char *argv[]) {
    cout.setf(ios::fixed, ios::floatfield);
    cout.precision(2);
    set<int> cases;
    bool mainProcess = true;
    for (int i = 1; i < argc; ++i) {
        if ( string(argv[i]) == "-") {
            mainProcess = false;
        } else {
            cases.insert(atoi(argv[i]));
        }
    }
    if (mainProcess) {
        cout << "YetAnotherGraphColoring (400 Points)" << endl << endl;
    }
    return run_test(mainProcess, cases, argv[0]);
}
// CUT end
