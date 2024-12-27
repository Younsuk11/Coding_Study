#include <iostream>
#include <vector>
#include <memory>

/* dynamic memory allocation
1. in runtime : memory allocation
2. data 크기를 모르거나, 계속해서 변하는 경우. ex) string & vector

heap : dynamically = manually or smart pointer(아래로, 커지는 방향으로)
    smart pointers : unique_ptr, shared pointer(알아서 free)
stack : aumatically = static allocation  (위로, 작아지는 방향으로)
*/


void Episode1(){
    std::cout<<"Episode1 : Dynamically memory allocation"<<std::endl;

    int *array; 
    int n;
    std::cin>>n;
    try{
        int* ptr = new int; // int 형 new allocation
        array = new int[n]; // allocation , array는 fixed size라 해당 type에 맞춰 배정된다.

        delete ptr;
        delete[] array; // array라서 이렇게. 지운다.
    }catch(const std::bad_alloc& e){std::cerr<<"Memory allocation failed : "<< e.what() <<std::endl;}
    // std::cerr : no bufferred ,바로 반환시킴.

    //다른 방식도 가능 : exception 반환이 아니라.
    int* array1 = new(std::nothrow) int[n]; // 안되면 null ptr을 반환
    if(array1 == nullptr){std::cerr<<"Memory allocation failed : "<<std::endl;}
    delete[] array1;
}



void Episode2(){


    std::cout<<"Episode2 : vector, also dynamically"<<std::endl;

    // dynamically allocation for class object : new and calling constructor
    std::vector<int> * vecptr = new std::vector<int>(); // constructor을 통해서 만들어낸다.

    //arrow operator
    vecptr -> push_back(10);

    //dereference
    (*vecptr).push_back(100);

    //iteration
    //1. range based
    for (int e : *vecptr){
        std::cout<<e<<std::endl;
    }

    //2. iterator
    for(std::vector<int>::iterator it = vecptr->begin(); it !=(*vecptr).end(); ++it){
        std::cout<<*it<<std::endl;
    }

    delete vecptr; // 이게 무조건 필요하다. : 1. memory leaks, 2. dangling pointers문제 때문에.
    /*
    1. memory leaks : not free하는 문제
    2. dangling pointers : 이미 free된것을 아직도 가리키고 있는 문제.*/
}


void Episode3(){
    std::cout<<"Episode3 : other pointers : smart pointers"<<std::endl;
    // 동적 메모리가 필요없을 때, 알아서  free 해주는 smart pointer
    // #include<memory>

    //1. unique_ptr : exclusive ownership , cannot be copied , 다른 것으로 할당 불가. 이것만 가지고 접근할 수 있음., scope 벗어나면 알아서 free
    //unique_ptr<type> name (raw pointer)
    //사용은 raw pointer랑 같은 방식으로
    std::unique_ptr<std::vector<int>> vecptr(new std::vector<int>());
    // auto other_vecptr = std::make_unique<std::vector<int>>(); // for c++14 :  raw pointer없이 단순 생성 가능.
    vecptr -> push_back(10);
    (*vecptr).push_back(100);
    (*vecptr)[0] = 30;


    //2.shared_ptr : allow shared ownership, copy, assign가능, 메모리 release 자동으로하는데, 메모리 share하는 모든 pointer가 사라질 때.
    std::shared_ptr<std::vector<int>> vecptr1(new std::vector<int>());
    std::shared_ptr<std::vector<int>> vecptr2 = vecptr1; //sharing
    auto vecptr3 = std::make_shared<std::vector<int>>(); // for c++11 :  raw pointer없이 단순 생성 가능.
    vecptr1 -> push_back(10);
    vecptr2 ->push_back(100);
    for (int e : *vecptr1){std::cout<<e<<std::endl;} // 10, 100
    
}


int main(){

    Episode1();
    std::cout<<std::endl;
    Episode2();
    std::cout<<std::endl;
    Episode3();
    return 0;
}