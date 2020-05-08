// auto.cpp by Bill Weinman <http://bw.org/>
// updated 2018-11-02
#include <iostream>
#include <typeinfo>
#include <string>
using namespace std;

template <typename lt, typename rt>
auto tf(const lt lhs, const rt rhs){
    return lhs+rhs;
}
// auto is useful in creating template functions. 


int main() {
    int i = 47;
    const char * cstr = "this is a c-string";
    const string sclass = string("this is a string class string");
    
    auto x = "this is a c-string";
    // let the compiler to decide what type to use
    decltype(x) y;
    // declare y as the same type of x
    cout << "type of i is " << typeid(i).name() << endl;
    cout << "type of cstr is " << typeid(cstr).name() << endl;
    cout << "type of sclass is " << typeid(sclass).name() << endl;
    cout << "type of x is " << typeid(x).name() << endl;
    cout << "type of y is " << typeid(y).name() << endl;
    // typeid() outputs depend on the platform

    for (auto it=sclass.begin(); it!=sclass.end(); ++it){
        cout << *it << " ";
    }
    cout << endl;
    // iterator based loop

    for (auto c : sclass){
        cout << c << " ";
    }
    cout << endl;
    // range based loop

    // auto is useful when the type is error-prone but inferable. 

    // Let's use template function with "auto" return type
    auto z = tf<string, const char *>(sclass, cstr);
    cout << z << endl;
    cout << "The type of auto return z is: " << typeid(z).name() << endl;

    return 0;
}
