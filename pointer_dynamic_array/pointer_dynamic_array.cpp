#include<iostream>
#include<string>

using namespace std;



void Episode1(){
    std::cout<<"Episode1 : Dynamically memory allocation"<<std::endl;

    //int
    int* aptr = new int(5); // 5값을 가지는 동적메모리 형성.(heap) //aptr은 stack에 저장
    cout<<"aptr : "<<aptr <<" *aptr : "<<*aptr<<" &aptr : " <<&aptr <<endl;
    //aptr : 0x14b606f20(heap 내 주소) *aptr : 5 &aptr : 0x16d05ede8(stack 내 주소)
    delete aptr;


    //array
    int *arr = new int[3]{1,2,3}; //initialization
    //arr은 arr[0]의 주소값과 같음. , 주소는 int형을 따라 4byte 씩 늘어남. (heap 이므로 중가방향)
    cout<<"arr[0] == *arr  : "<<arr[0]<<endl; // arr[0] == *arr  : 1
    cout<<"arr == &arr[0] = &(*arr) : " <<arr<< endl; // arr == &arr[0] = &(*arr) : 0x14b606f20
    cout<<"arr + 1 = &arr[1] : " <<arr+ 1<<endl; // arr + 1 = &arr[1] : 0x14b606f24
    cout<<"*(arr + 1) = *(&arr[1]) = arr[1] : " <<*(arr+ 1)<<endl; // *(arr + 1) = *(&arr[1]) = arr[1] : 2
    
    for (int i =0; i<3; ++i){
        cout<< &arr[i]<<endl;
        /*
        heap에서 주소가 증가하는 방향은 아래로다.
        int형이라 4byte씩 증가.
        0x123606f20
        0x123606f24
        0x123606f28
        */


    }



    delete[] arr;
    //string
    string *strptr = new string("new string"); // initialization

    delete strptr;

    

}

void Episode2(){
    std::cout<<"Episode2 :multi-dimensional(dynamic)"<<std::endl;


    int nRows = 2, nCols = 3;
    int** arr = new int*[nRows]; 
    // arr = 각 행에 해당하는 array(즉 pointer)들을 가리키는 pointer 변수
    // arr[0]의 주소를 갖고 있음., 즉 pointer의 pointer
    for (int i =0; i <nRows ; i++){
        arr[i] = new int[nCols]{1,2,3};
    } // [[1,2,3], [1,2,3]]
    
    // arr은 pointer를 담는 array,즉, array를 담는 array, array의 기본 단위는 8byte
    cout<<"arr + 1 = arr + 8byte = &(arr[1]) : " <<arr +1<<endl;
    cout<<"*(arr +1) = arr[1] = &(arr[1][0]) : " <<*(arr +1)<<endl;
    cout<<"*((*arr +1)+2) = *(arr[1] +2) = *(arr[1] + int byte *2) = arr[1][2] : "<<*((*arr + 1)+2)<<endl;



}



void Episode3(){
    std::cout<<"Episode3 :static allocation: stack"<<std::endl;

    //fixed size, contiguous memory block
    int arr[3] = {1,2,3};
    // arr이라는 것은 pointer는 아니지만,  arr[0]의 pointer처럼 작동한다. 
    // dynamic allocation떄처럼. : int *arr = new int[3]{1,2,3}; 조금 차이는 있다.

    cout<<"arr[0] : "<<arr[0] <<" *arr : " <<*arr<<endl; // 1
    cout<<" arr : " <<arr<<" &arr[0] : " <<&arr[0] <<" &(*arr) : "<<&(*arr)<<endl; // arr : 0x16d7f2dd8 &arr[0] : 0x16d7f2dd8 &(*arr) : 0x16d7f2dd8
    cout<<"arr + 1 = &arr[1] : " <<arr+ 1<<endl; // arr + 1 = &arr[1] : 0x16d7f2ddc
    cout<<"*(arr + 1) = *(&arr[1]) = arr[1] : " <<*(arr+ 1)<<endl; // *(arr + 1) = *(&arr[1]) = arr[1] : 2

    //비슷하지만 차이점.(사용은 비슷한데 개념이 다름.)
    /*
    1. array 그자체임. static arr은. address를 바꿀 수는 없음. 동적이 아니니까
    2. arr이라는 변수 이름은 pointer처럼 주소를 담고 있는 변수가 아님., 주소를 담고 있는 별도의 공간도 없고.
    3. &arr : 전체 array의 주소를 말함.
    */

}

void Episode4(){
    std::cout<<"Episode4 :static multidimensional array: stack"<<std::endl;

    //마찬가지로 fixed size, contiguous memory block
    //(arr[0][0], arr[0][1], arr[1][0], arr[1][1]차례대로 아래로 stack에.), arr은 arr[0][0]을 
    int arr[2][2] = {1,2,3,4};
    cout<<arr[0][0]<<arr[0][1]<<arr[1][0]<<arr[1][1]<<endl;
    cout<<&arr<<endl;
    cout<<&arr[0][0]<<endl;
    cout<<&arr[0]<<endl;
    // 다같은 주소 가리킴. arr그자체이기 때문.
}









int main(){
    Episode1();
    cout<<endl;
    Episode2();
    cout<<endl;
    Episode3();
    cout<<endl;
    Episode4();

    return 0;
}