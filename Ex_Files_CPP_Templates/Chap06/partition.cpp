// partition.cpp by Bill Weinman <http://bw.org/>
// 2018-10-01 for CppSTL
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// Partition reorder the elements, 
// such that the elements that meet certain criteria are at the beginning of the container. 

template <typename T>
bool is_even_tens(T & n) {
    if(n < 10) return false;
    return ((n / 10) % 2) == 0;
}

template <typename T>
void disp_v(const T & v) {
    if(!v.size()) return;
    for(auto e :  v) { cout << e << " "; }
    cout << endl;
}

int main() {
    // prime numbers > 10 & < 100
    vector<int> v1 = { 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 };
    disp_v(v1);
    
    partition(v1.begin(), v1.end(), is_even_tens<int>);
    // stable_partition(v1.begin(), v1.end(), is_even_tens<int>);
    // "stable_partition" maintains the original order, takes more time&space. 

    size_t sz = count_if(v1.begin(), v1.end(), is_even_tens<int>);
    vector<int> v2(sz), v3(v1.size()-sz); // v2: meet the criteria, v3: does not meet the criteria
    partition_copy(v1.begin(), v1.end(), v2.begin(), v3.begin() ,is_even_tens<int>);
    disp_v(v1);
    disp_v(v2);
    disp_v(v3);

    return 0;
}
