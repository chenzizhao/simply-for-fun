// replace.cpp by Bill Weinman <http://bw.org/>
// 2018-09-30 for CppSTL
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

template <typename T>
bool is_even(const T & n) {
    return ((n % 2) == 0);
}

template <typename T>
void disp_v(const T & v) {
    if(!v.size()) return;
    for(auto e :  v) { cout << e << " "; }
    cout << endl;
}

int main() {
    // prime numbers < 100
    vector<int> v1 = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 };
    // No constant identifier because replace happens in place. 
    disp_v(v1);

    // Replace all occurrences if applicable, in place. 
    replace(v1.begin(), v1.end(), 47, 99);
    replace_if(v1.begin(), v1.end(), is_even<int>, 99);

    disp_v(v1);

    // Remove 
    auto it = remove(v1.begin(), v1.end(), 99);
    // just pass the last iterator
    if (it==v1.end()) cout << "no element was removed." <<endl;
    else v1.resize(it-v1.begin()); // Note need to resize the vector. 
    disp_v(v1);

    // Unique (set-ify)
    it = unique(v1.begin(), v1.end());
    if (it==v1.end()) cout << "no element was removed due to duplicates." <<endl;
    else v1.resize(it-v1.begin()); // Note need to resize the vector. 
    disp_v(v1);

    return 0;
}
