#include <iostream>
#include <string.h>
#include <vector>
using namespace std;

// Implement definition of all classes and the member functions in this file.

class Container{
    protected:
        float size;
        float capacity; 
        string capacity_code;
        string* container_code;

    public: 
        //constructor
        Container(float size) : size(size){
            container_code = new string("");
        }
        //destructor
        ~Container(){
            delete container_code;
        }

        float get_size(){
            return size;
        }
        virtual void set_capacity()=0; // pure virtual function  ; Container = abstract class
        
        float get_capacity(){
            return capacity;
        }
        
        void set_container_code(){

            

            if (capacity < 100){
                capacity_code = "1";
            }
            else if((capacity >= 100) &&(capacity <200)){
                capacity_code = "2";
            }
            else{
                capacity_code = "3";
            }

            *container_code +=capacity_code;
        }

        string* get_container_code(){
        
            return container_code;
        }


};

class Box: public Container{
    public :

        
        //constructor
        Box(float size) : Container(size){
        } 

        void set_capacity() override{
            capacity = size * 1; 
        }
        
};

class PaperBox: public Box{
    public:

        
        PaperBox(float size) : Box(size){
            *container_code += "PaB";
        }
        
        
        void set_capacity() override{
            capacity = size * 1.3;
        }
};

class PlasticBox: public Box{

    public:
        PlasticBox(float size) : Box(size) {
            *container_code += "PlB";
        }

        
        void set_capacity() override{
            capacity = size * 1.1;
        }

};

class Bag: public Container{
    public : 
        Bag(float size) : Container(size){
            *container_code += "B";
        }
        
        void set_capacity() override{
            capacity = size * 3;
        }
};

class Carrier: public Container{
    public:

        std::vector<Box*> aux_vec;


        Carrier(float size) : Container(size){
            *container_code += "C";
        }
        ~Carrier() {
         
            for(auto v : aux_vec){
                delete v;
            }
        }
        void set_capacity() override{
            capacity = size*5;
        }

        void add_aux(Box* aux){
            if (aux_vec.size() ==2){
                return;
            }
        
            else{
                aux_vec.push_back(aux);
            }
            float aux_capacity = aux ->get_capacity();
            capacity += 1.1*aux_capacity;
        }

        Box* get_aux(int n){
            if(n > aux_vec.size()){
                return nullptr;
            }

            else{
                return aux_vec.at(n-1);
            }
       
        }



};