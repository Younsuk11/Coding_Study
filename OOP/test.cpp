#include<iostream>

using namespace std;


class Base
{
    public :
        int val;

        Base() { val = 4; cout<< "Base constructor default"<<endl;}
        Base(int param) {val = param; cout<<"Base constructor int"<<endl;}
        ~Base(){cout<<"Bye Base"<<endl;}

        int bar1() { return val +1;}
        virtual int bar2() {return val +2;}


};

class Derived : public Base{

    public:
        Derived() :Base(10){cout<<"Derived constructor"<<endl;}
        ~Derived(){cout<<"Bye Derived"<<endl;}
        int bar1(){return val +11;}
        virtual int bar2(){return val +12;}

};


int main(){
    Base b;
    Derived d;
    Base* ptr = &d;

    cout<<"First: "<<b.bar1()<<endl;
    cout<<"Second : " <<b.bar2()<<endl;
    cout<<"Third : "<<ptr->bar1()<<endl;
    cout<<"Fourth : "<<ptr->bar2()<<endl;
}