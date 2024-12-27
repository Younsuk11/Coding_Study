#include <iostream>
#include <string>
#include <initializer_list>

using namespace std;

/*
24-1 computing 1 midterm 기출
*/


template <typename T>
class MyVector{
    public:

        T* array;
        int size;
        int capacity;

        MyVector(std::initializer_list<T> elements);
        ~MyVector(){
            delete[] array;
        };
        void push_back(T element);
        void resize();
        T* begin();
        T* end();
        int getsize() const;
        T& operator[](int index) const;


        friend std::ostream& operator<<(std::ostream& os, MyVector<T>& vec); // 객체 출력가능한 friend operator
        // MyVector의 구성내용을 접근이 가능하게한다.

        friend std::istream& operator>>(std::istream& is, MyVector<T>& vec);

};

template <typename T>
MyVector<T>::MyVector(std::initializer_list<T> elements) : size(0), capacity(elements.size()){
    array = new T[capacity];
    for (auto element : elements){
        push_back(element);
    }
}

template<typename T>
int MyVector<T>::getsize() const{
    return size;
}


template <typename T>
void MyVector<T>::push_back(T element){
    if(size == capacity){
        resize();
    }
    array[size] = element;
    size ++;
}
template <typename T>
void MyVector<T>::resize(){
    capacity *=2;
    T* newarray = new T[capacity];
    for (int i= 0 ; i<size; i++){
        newarray[i] = array[i];
    }
    delete[] array;
    array = newarray;
}

//prob2-a : ranged-based iteration을 위한 위한 구현
template <typename T>
T* MyVector<T>::begin(){
    return array;
}
template <typename T>
T* MyVector<T>::end(){
    return array + size;

}

//prob2-b : operator overloading
/*
<< 연산자. 출력하는 연산자임.
std::ostream에 벡터 내용을 출력하기 위함.
friend operator로 선언.
*/

template <typename T>
T& MyVector<T>::operator[](int index) const{ // 값 자체를 "복사"가 아니라 call by reference
    return array[index];
}

template<typename T>
std::ostream& operator<<(std::ostream& os, MyVector<T>& vec){

    os<<"[";
    for (int i = 0; i<vec.getsize(); ++i){
        os<<vec[i];
        if (i < (vec.getsize() -1)){
            os<<", ";
        }
    }
    os<<"]";
    return os;
}

template<typename T>
MyVector<T>& operator>>(std::istream& is, MyVector<T>& vec){}



int main(void){
    MyVector<int> intVec{1, 2, 3};
    for (auto e : intVec) std::cout << e << " ";
    cout<<endl;

    MyVector<std::string> strVec = {"apple", "bee", "cake"};
    for (auto e : strVec) std::cout << e << " ";
    cout<<endl;

    strVec.push_back("dog");
    for (auto e : strVec) std::cout << e << " ";
    cout<<endl;


    std::cout << intVec;
    std::cout << std::endl;
    std::cout << strVec ;


    // int x, y, z;
    // intVec >> x >> y >> z;
    return -1;
}