// functor.cpp by Bill Weinman <http://bw.org/>
// 2018-09-27 for CppSTL
#include <iostream>
using namespace std;

template <typename T>
class multiply_by {
    T _mult = 0;
    multiply_by();
public:
    // constructor
    multiply_by(T n) : _mult(n) {} // simply overwrite value for the attribute _mult
    // reset the attribute _mult
    void mult(T n) { _mult = n; }
    // when not given an argument, return _mult
    T mult() const { return _mult; }
    // overload the operator with the function (what distinguishes a "functor" and a regular class instance)
    T operator() (T n) const { return _mult * n; }
};

int main() {
    // Similar to function classes in Python. 
    multiply_by<int> x(9);
    cout << "x mult is " << x.mult() << endl;
    
    cout << "x(5) is " << x(5) << endl;
    cout << "x(25) is " << x(25) << endl;
    
    // Reset _mult (multiplier) to 7.
    x.mult(7);
    // Call x.mult() to return the reset value for the multiplier. 
    cout << "x mult is " << x.mult() << endl;
    
    cout << "x(5) is " << x(5) << endl;
    cout << "x(25) is " << x(25) << endl;
    
    return 0;
}
