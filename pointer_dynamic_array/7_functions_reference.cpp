#include<iostream>
#include <map>
#include <string>


void swap_by_pointer(int *x , int *y){ // pass pointer as argument , eg. address of variables
    int temp = *x; 
    *x = *y;
    *y = temp;

}


//using function overloading
void swap_by_reference(int& x, int& y){ // using reference parameters : 변수 자체를 활용하는 것. 별명을 이용하는 것일 뿐, x,y가 따로 만들어지지는 않는다.
    int temp = x;
    x = y; 
    y = temp;  // 이렇게 직접 변수를 그대로 사용하는 것이기에, 바로 직접적인 수정이 되는 것. : unintended modification유발 가능성 높음.
}

// 그래서 사용하는 것이 const : 그럼 수정을 못함. : compile error
// void swap_by_reference(const int& x, const int& y){
//     int temp = x;
//     x = y; 
//     y = temp;  
// }




//reference return : 직접 return using *this : 이것때문에 chain operation이 가능해지는 것임.
int& middleElement(std::map<std::string, int>&m) { // take reference parameters
    int index = m.size() / 2;
    auto it = m.begin();
    for(int i =0; i<index; i++){
        it ++;
    }
    // 가장 가운데 위치하는 element 찾기
    return it->second; // value of map // return reference of value
}


std::map<std::string, int>::iterator middleElement2(std::map<std::string, int>&m) { // take reference parameters
    int index = m.size() / 2;

    auto it = m.begin();
    for(int i =0; i<index; i++){
        it ++;
    }
    // 가장 가운데 위치하는 element 찾기

    return it; // value of map // return reference of value
}





int main(){

    //call by reference  : pointer를 활용
    int a= 10, b = 20;
    std::cout << "[Before] a: " << a << ", b: " << b << std::endl;
    swap_by_pointer(&a, &b);
    std::cout << "[After] a: " << a << ", b: " << b << std::endl;


    //call by reference : reference를 활용 : 문제는 unintended modification 이 있을 수도...
    int a1= 10, b1 = 20;
    swap_by_reference(a1, b1);
    std::cout << "[After] a: " << a1 << ", b: " << b1 << std::endl;
    
    


    //reference return
    std::map<std::string, int> m = {{"A", 1}, {"B", 2}, {"C", 3}};

    std::cout<<middleElement(m)<<std::endl;
    //return by reference
    middleElement(m) = 10; // 그 값 자체에 할당.allocation을 위해서 reference return을 하는 것임.
    for (auto& p : m){std:: cout<<p.first << " : " <<p.second <<std::endl;} // 여기서도 auto&로 copy를 쓰지 않고,.
    // a:1, b: 10, c : 3


    // iteraotr로 접근하는 것도 가능. pointer이니까.
    (middleElement2(m))->second = 100;
    for (auto& p : m){std:: cout<<p.first << " : " <<p.second <<std::endl;}
    return 0; 
}