// search.cpp by Bill Weinman <http://bw.org/>
// 2018-09-30 for CppSTL
#include <iostream>
#include <functional>
#include <algorithm>
#include <vector>
using namespace std;

template <typename T>
bool is_odd(const T & n) {
    return ((n % 2) == 1);
}

template <typename T>
void disp_v(const T & v) {
    if(!v.size()) return;
    for(auto e :  v) { cout << e << " "; }
    cout << endl;
}

int main() {
    // prime numbers < 100
    const vector<int> v1 = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 };
    const vector<int> v2 = { 31, 37, 41, 43, 47 };
    disp_v(v1);
    
    // e.g. search for single element
    auto it = find(v1.begin(), v1.end(), 41);
    it = find_if(v1.begin(), v1.end(), is_odd<int>);
    it = find_if_not(v1.begin(), v1.end(), is_odd<int>);

    // e.g. search for a sequence, returns the iterator location if found. 
    it = search(v1.begin(), v2.end(), v2.begin(), v2.end());
    
    // If not found, return the end iterator. 
    if(it != v1.end()) {
        size_t index = it - v1.begin();
        cout << "found at index " << index << ": " << *it << endl;
    } else {
        cout << "not found" << endl;
    }

    // Counting
    auto c = count(v1.begin(), v1.end(), 7);
    c = count_if(v1.begin(), v1.end(), is_odd<int>);
    // No count_if_not
    cout << "found " << c << " occurrences." << endl; 

    return 0;
}
