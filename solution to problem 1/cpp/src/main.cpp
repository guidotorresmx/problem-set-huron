#include "../include/shared.hpp"
#include "analytical.cpp"
#include "programmatical.cpp"
using namespace std;


int main(){
    cout << "====================================" << endl;
    cout << "Programmatical solution in c++" << endl;
    programmatical();
    cout << "====================================" << endl;
    cout << "Analytical solution in c++" << endl;
    analytical();
    cout << "====================================" << endl;

    return 0;
}