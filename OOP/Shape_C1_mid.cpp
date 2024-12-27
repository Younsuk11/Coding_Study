#include <iostream>

using namespace std;


/*
24-1 computing 1 midterm 기출
*/

class Shape{
    
    public:
        
        Shape(){n_shape+=1;};
        virtual ~Shape(){
            n_shape -=1;};
        virtual double get_area(){ 
            return 0.0;
        }; // pure virtual function

        static int n_shape;

        
};

class Rectangle: public Shape{
    public:
        double width;
        double height;
        Rectangle(double width, double height): width(width), height(height){
          
        }
        ~Rectangle()override{
        
        }
        double get_area() override{
            return width * height;
        }
};

class Circle: public Shape{
    public:
        double radius;

        Circle(double radius): radius(radius){
            
        }
        ~Circle() override{
         
        }
        double get_area() override{
            return 3*radius*radius;
        }


};

int Shape::n_shape =0; // 밖에서 선언을 해줘야 함. ouf of definition으로 초기화가 필요함.(constructor 내부에서 불가능.)


int main(void){
    Shape* shape1 = new Rectangle(2, 5);
    Shape* shape2 = new Circle(2);
    Shape* shape3 = new Circle(3);

    cout << shape1->get_area() << endl;
    cout << shape2->get_area() << endl;
    cout << shape3->get_area() << endl;

    cout << Shape::n_shape << endl;

    delete shape1;
    delete shape2;
    delete shape3;
    cout << Shape::n_shape;
    return -1;

}