#include "../include/analytical.h"
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

void get_probs_analytically(
        set<uint16_t> &s, 
        uint16_t r, 
        map<uint16_t, float> &probs
    ){
    uint16_t n = s.size();
  
    uint32_t denominator = nCr(n, r);
    uint16_t i = 0;
    for (auto key=s.begin(); key!=s.end(); ++key){
        i++;
        uint32_t numerator = nCr(n-i,r-1);
        float val = 
            static_cast<float>(numerator)/
            static_cast<float>(denominator);
        probs.insert({*key,val});
    }
}

int analytical(){
    set<uint16_t> s{49, 8, 48, 15, 47, 4, 16, 23, 43, 44, 42, 45, 46};
    uint16_t r=6;

    map<uint16_t, float> probs;
    get_probs_analytically(s, r, probs);

    for(auto i=probs.begin(); i!=probs.end(); ++i){
        printf("%d : %.3f \n", i->first, i->second);   
    }
}