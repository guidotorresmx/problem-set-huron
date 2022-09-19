//#include "utils.h"
#include <iostream>
#include <cmath>
#include <set>
#include <map>
#include <vector>

using namespace std;
//map<int, float> get_probs_analytically(s: Set, r: int) -> Dict:

uint32_t nCr( uint16_t n, uint16_t r )
{
    if (r > n) return 0;
    if (r * 2 > n) r = n-r;
    if (r == 0) return 1;

    int result = n;
    for( int i = 2; i <= r; ++i ) {
        result *= (n-i+1);
        result /= i;
    }
    return result;
}

void get_probs_analytically(set<uint16_t> &s, uint16_t r){
    map<uint16_t, float> probs;
    uint16_t sSize = s.size();
  
    for (auto i=s.begin(); i!=s.end(); ++i){
        probs.insert({*i,0.0});
    }

  
  
  
    for(auto it=probs.begin(); it!=probs.end(); ++it){
        cout << it->first << " => " << it->second << endl;
    }
    cout << "set size: " << sSize;
    
}

int main(){
    set<uint16_t> s{49, 8, 48, 15, 47, 4, 16, 23, 43, 44, 42, 45, 46};
    uint16_t r=6;
    get_probs_analytically(s, r);
    cout << endl << r << endl;

}