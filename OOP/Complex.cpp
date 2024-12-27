#include <cstdio>
#include <iostream>
#include <ostream>
#include <cmath>
#include <iomanip>

using namespace std;

class Complex {
public:
  Complex(){};
  Complex(double real, double imag):real(real), imag(imag){};
  ~Complex(){};

  double getReal() const {return real;};
  double getImag() const {return imag;};
  void setReal(double real_val){real  = real_val;}
  void setImag(double imag_val){imag = imag_val;}
  Complex operator+(const Complex& rhs);
  
  friend Complex operator-(const Complex& complex);

  friend std::ostream& operator<<(std::ostream& os, const Complex& complex);

private:
  double real, imag;
  
};

Complex Complex::operator+(const Complex& rhs){
  Complex new_complex(0, 0);
  new_complex.setReal(real + rhs.getReal());
  new_complex.setImag(imag + rhs.getImag());
  return new_complex;
}

Complex operator-(const Complex& complex){
  Complex new_complex(-complex.getReal(), -complex.getImag());
  return new_complex;
}

std::ostream& operator<<(std::ostream& os, const Complex& complex){
  double real_val = complex.getReal();
  double imag_val = complex.getImag();


  os<<real_val;
  
  if (imag_val>0){
    os<<"+";
    os<<imag_val;
    os<<"i";
  }
  else if(imag_val<0){
    os<<"-";
    os<<abs(imag_val);
    os<<"i";
  }

  return os;

}




int main(){

  cout<<std::fixed<<std::setprecision(2);
  Complex c1(3.3, 2.6);
  Complex c2, c3;
  c2.setReal(7.89);
  c2.setImag(-9.21);
  c3 = c1 + c2;

  cout<<c3.getReal()<<endl;
  cout<<c3.getImag()<<endl;

  cout<<"SUm : "<<c3<<endl;
  
  cout<<"neg c3: "<<-c3<<endl;

  Complex c4(1.0, 0.0);
  Complex c5(0.0, 1.0);

  cout<<c4<<endl;
  cout<<c5<<endl;

  Complex c6(0.0, 6.61);
  cout<<c6<<endl;

  return 0;

}