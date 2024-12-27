#include <iostream>

using namespace std;
/*
array 구현 문제. with OOP
*/

/*
24-1 computing 1 midterm 기출
*/

template <typename T>
class BasicArray {
private:
    T* data;
    int size;

public:
    BasicArray(int initSize) : size(initSize) {
        data = new T[size];
    }

    ~BasicArray() {
        delete[] data; 
    }

    // copy constructor
    BasicArray(const BasicArray<T>& other);

    //copy assignment operator
    BasicArray<T>& operator=(const BasicArray<T>& other);

    //move constructor
    BasicArray(BasicArray<T>&& other) noexcept;

    //move assignment operator
    BasicArray<T>& operator=(BasicArray<T>&& other) noexcept;

    void set(int index, T value) {

        if (index >= 0 && index < size) {
            data[index] = value;
        }
    }

    T& operator[](int index) const { return data[index]; }
};

//copy constructor
template<typename T>
BasicArray<T>::BasicArray(const BasicArray<T>& other):
size(other.size), data(new T[other.size]){
    
    //copy
    for (int i =0; i<other.size; ++i){
        data[i] = other[i];
    }

}

//copy assignment operator
template<typename T>
BasicArray<T>& BasicArray<T>::operator=(const BasicArray<T>& other){
    if (this !=&other){
        delete[] data;

        size = other.size;
        data = new T[size];
        for(int i = 0; i<other.size; ++i){
            data[i] = other[i];
        }
    }
    return *this;
}


//move constructor
template<typename T>
BasicArray<T>::BasicArray(BasicArray<T>&& other) noexcept
: data(other.data), size(other.size){
    other.data = nullptr;
    other.size =0;
}

//move assignment operator
template<typename T>
BasicArray<T>& BasicArray<T>::operator=(BasicArray<T>&& other) noexcept{
    if(this !=&other){
        delete[] data;
        data = other.data; // 복사가 아니라 그대로 가져오는 것.

        size = other.size;
        other.data = nullptr;
        other.size = 0;
    }
    
    return *this;
}


int main(){
    BasicArray <int> arr1(5);
    arr1.set(0,1);
    arr1.set(1,2);
    arr1.set(2,3);

    BasicArray <int> arr2 = arr1; // copy constructor
    arr1.set(3,4);
    arr2.set(3,5);

    cout << "arr1: [";
    for (int i = 0; i < 4; i++) {
        cout << arr1[i];
        if (i < 3) {
            cout << ", ";
        }
    }
    cout << "]" << endl;
    cout << "arr2: [";
    for (int i = 0; i < 4; i++) {
        cout << arr2[i];
        if (i < 3) {
            cout << ", ";
        }
    }
    cout << "]" << endl;
    // Expected result: arr1: [1, 2, 3, 4], arr2: [1, 2, 3, 5]

    arr1 = arr2; // copy assignment operator
    arr1.set(4,6);
    arr2.set(4,7);
    cout << "arr1: [";
    for (int i = 0; i < 5; i++) {
        cout << arr1[i];
        if (i < 4) {
            cout << ", ";
        }
    }
    cout << "]" << endl;
    cout << "arr2: [";
    for (int i = 0; i < 5; i++) {
        cout << arr2[i];
        if (i < 4) {
            cout << ", ";
        }
    }
    cout << "]" << endl;
    // Expected result: arr1: [1, 2, 3, 5, 6], arr2: [1, 2, 3, 5, 7]

    return 0;
    
}