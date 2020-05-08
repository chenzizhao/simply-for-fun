// modify.cpp by Bill Weinman <http://bw.org/>
// 2018-11-06 for CppSTL
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

template <typename T>
void disp_v(const T & v) {
    if(!v.size()) return;
    for(auto e :  v) { cout << e << " "; }
    cout << endl;
}

int main() {
    // prime numbers < 100
    vector<int> v1 = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 };
    vector<int> v2(v1.size(), 0);
    disp_v(v1);
    disp_v(v2);

    // copy_n
    copy_n(v1.begin(), 10, v2.begin());
    disp_v(v2);

    // copy
    copy(v1.begin(), v1.end(), v2.begin());
    disp_v(v2);

    // copy_backward: the result is the same but internally, the elements are copied back to front. 
    copy_backward(v1.begin(), v1.end(), v2.end());
    disp_v(v2);

    // reverse_copy: put the last element of v1 to the first position of v2
    reverse_copy(v1.begin(), v1.end(), v2.begin());
    disp_v(v2);

    // reverse: in place
    reverse(v2.begin(), v2.end());
    disp_v(v2);

    // fill
    fill(v2.begin(), v2.end()-10, 100);
    disp_v(v2);

    // fill_n
    fill_n(v1.begin(), 2, 100);
    disp_v(v1);

    // generate, with lambda function
    generate(v2.begin(), v2.end(), []()->int {return rand()%100;});
    disp_v(v2);

    // random shuffle: in place, can also use you own shuffle generator
    random_shuffle(v1.begin(), v1.end());
    disp_v(v1);
    // random shuffle is deprocated since C++ 17
    // So an alternative approach is recommended. 
    // See randomize.cpp file for more info. 
    // Use function "shuffle" and always provide your own random number generator. 

    return 0;
}
