// template-variable.cpp by Bill Weinman <http://bw.org/>
// created 2018-09-08
#include <iostream>
using namespace std;


// definition of a template variable
// available in C++ 14
template<typename T>
constexpr T pi = T(3.1415926535897932385L);

template<typename T>
T area_of_circle(const T& r){
    return r*r*pi<T>;
}

int main()
{
    cout.precision(20);
    cout << pi<long double> << " " << area_of_circle<long double>(3) << endl;
    return 0;
}

// constexpr is available at compile time.
// in contrast, const is available at run time. 