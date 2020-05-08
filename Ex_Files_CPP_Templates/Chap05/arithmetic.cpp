// arithmetic.cpp by Bill Weinman <http://bw.org/>
// 2018-11-06 for CppSTL
#include <iostream>
#include <functional>
#include <algorithm>
// Note new header ^
#include <vector>
using namespace std;

template <typename T>
void disp_v(vector<T> & v) {
    if(!v.size()) return;
    for(T e :  v) { cout << e << " "; }
    cout << endl;
}

int main() {
    vector<long> v1 = { 26, 52, 79, 114, 183 };
    vector<long> v2 = { 1, 2, 3, 4 ,5 };
    vector<long> v3(v1.size(), 0);
    disp_v(v1);
    disp_v(v2);
    disp_v(v3);
    cout << endl;
    
    plus<long> f;
    // Pass in functions as an object (as in Python).
    // This can be useful when we set up other arguments of the function. 
    // e.g. plus<double> add_4(4); transform(v1.begin(), v1.end(), v2.begin(), v3.begin(), add_4);
    transform(v1.begin(), v1.end(), v2.begin(), v3.begin(), f);
    disp_v(v3);
    
    return 0;
}
