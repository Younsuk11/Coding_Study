#include <cstdio>
#include <iostream>
#include <ostream>
#include <cmath>


class Number {
public:
  Number() {}
  Number(int val):val(val){}
  ~Number(){}
  Number add (Number n){
    Number new_n;
    int new_val = val + n.val; 
    new_n.val = new_val;
    return new_n;
  }
  int get_number(){
    return val;
  }

private:
  int val;
};