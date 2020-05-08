// forward-iterator.cpp by Bill Weinman <http://bw.org/>
// 2018-09-18 for CppSTL
#include <iostream>
#include <forward_list>
using namespace std;

int main() {
    forward_list<int> fl1 = { 1, 2, 3, 4, 5 };
    forward_list<int>::iterator it1;     // forward iterator
    
    for(it1 = fl1.begin(); it1!= fl1.end(); ++it1) {
        cout << *it1 << " ";
    }
    cout << endl;
    // A range-based for-loop uses a forward iterator. 
    // for(int i:fl1){
    //     cout << i << endl;
    // }
    return 0;
}

// A forward iterator is somewhat similar to a singly linked list. 
// - Can not decrement a forward iterator
// - Can both read and write (more flexible than input/output iterator)