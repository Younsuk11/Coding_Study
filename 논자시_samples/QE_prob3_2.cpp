#include <cstdio>
#include <iostream>
#include <ostream>
#include <cmath>
using namespace std;

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


int main(){
  Number n1(1), n2(2);
  Number n3  = n1.add(2);
  cout<<n3.get_number()<<endl;
  cout<<n1.get_number()<<endl;
  cout<<n2.get_number()<<endl;
}