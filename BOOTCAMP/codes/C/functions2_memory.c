// function example
#include <stdio.h>

int main (void)
{
    int a;
    int b;
    b = Watt(a); //main cals Watt first
    b = Volt(a,b);


}

int Watt(int a)
{
    int w;
    w = Volt(w, 10); // Watt calls Volt
    return w;

}

int Volt(int q, int r)
{
    int k;
    int m ;
    return k;
}

// memory stack(LIFO) : run time stack when execution starts
// all local variable -> so stack in run-time stack
// functino memory address  -> frame pointer
/*
stack and pop 순서> 
main -> Watt-> Volt
main -> Watt
main 
main -> Volt*/ 