// string-transform.cpp by Bill Weinman <http://bw.org/>
// 2018-09-25 for CppSTL
#include <iostream>
#include <string>
#include <algorithm>
#include <locale>
#include "title-case.h"
using namespace std;

// Understand that string is a container of characters. 

int main()
{
    string s1 = "this is a string";
    cout << s1 << endl;
    
    string s2(s1.size(), '.');
    transform(s1.begin(), s1.end(), s2.begin(), ::toupper);
    cout << s2 << endl;
    // :: is the scope resolution operator.
    // It distinguishes the function with the colon macro in the standard library. 
    
    // pass in the function
    transform(s1.begin(), s1.end(), s2.begin(), title_case());
    cout << s2 << endl;

    // pass in an instance of the function, also works
    title_case t;
    transform(s1.begin(), s1.end(), s2.begin(), t);    
    cout << s2 << endl;

    // You can also create user-defined transformations with functors/"function object". 
    return 0;
}
