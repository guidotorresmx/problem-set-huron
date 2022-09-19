#include "../include/shared.hpp"
using namespace std;


void get_combinations_recursive(
        uint16_t n, 
        uint16_t k, 
        uint16_t i, 
        vector<uint16_t> combination, 
        vector<vector<uint16_t>> &combinations
    ){
    
    if(combination.size() == k){
        combinations.push_back(combination);
        return;
    }
    for(auto j=i; j<=n; j++){
        combination.push_back(j);
        get_combinations_recursive(n, k, j+1, combination, combinations);
        combination.pop_back();
    }
}

void normalize_vector(vector<float> &values){
    float total = 0;
    for (auto& n : values)
         total += n;

    for (auto& n : values)
         n = n/total;
}

void get_probs_programmatically(
        set<uint16_t> &s, 
        uint16_t r,
        map<uint16_t, float> &probs          
    ){

    vector<uint16_t> indexes(s.size());
    vector<uint16_t> keys(s.size());
    vector<float> values(s.size());

    uint16_t n = s.size();
    
    copy(s.begin(), s.end(), keys.begin());

    vector<uint16_t> combination;
    vector<vector<uint16_t>> combinations;
    get_combinations_recursive(n, r, 1, combination, combinations);
    
    for (vector<uint16_t> tCombination: combinations){
        uint16_t min = *min_element(tCombination.begin(), tCombination.end());
        values[min-1]++;
    }
    
    normalize_vector(values);

    for (size_t i = 0; i < keys.size(); ++i)
        probs[keys[i]] = values[i];
    
}

void programmatical(){
    set<uint16_t> s{49, 8, 48, 15, 47, 4, 16, 23, 43, 44, 42, 45, 46};
    uint16_t r=6;

    map<uint16_t, float> probs;
    get_probs_programmatically(s, r, probs);

    for(auto i=probs.begin(); i!=probs.end(); ++i){
        printf("%d : %.3f \n", i->first, i->second);   
    }
}