// iterator.cpp by Bill Weinman <http://bw.org/>
// 2018-09-18 for CppSTL
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> vi1 = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
    vector<int>::iterator it1;   // iterator object
    // Type of iterator is bound to the type of class (vector<int>)
    vector<int>::iterator ibegin = vi1.begin();
    vector<int>::iterator iend = vi1.end();
    // The use of "auto" is recommended. 
    // auto ibegin = viq.begin();
    for(it1 = ibegin; it1 < iend; ++it1) {
        // Iterators can be incremented/decremented like a pointer. 
        cout << *it1 << " ";
    }
    cout << endl;
    
    return 0;
}

// Works a lot like a pointer.
// Can be dereferenced. 