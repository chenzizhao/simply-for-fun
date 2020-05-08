// template-function.cpp by Bill Weinman <http://bw.org/>
// updated 2018-08-18
#include <iostream>
#include <string>
using namespace std;

template <typename T> // "typename" or "class" both work. 
T maxof ( const T & a, const T & b ) {
    return ( a > b ? a : b );
} // This is the "definition" of the template. 

int main() {
    int a = 7;
    int b = 9;
    
    cout << "max is " << maxof<int>( a, b ) << endl;
    cout << "max is " << maxof<short int>( a, b ) << endl;
    cout << "max is " << maxof<long int>( a, b ) << endl;
    cout << "max is " << maxof<long long int>( a, b ) << endl;
    // This is a "specialization" of the template.

    // The complier can deduct argument type
    // i.e. the programmer need not pass in the type(s) of input(s).
    cout << "Argument deduction: max is " << maxof( a, b ) << endl;
    
    return 0;
}
// The use of template is a compile time abstraction. 
// Templates are useful in generic programming. 