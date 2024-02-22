#include <stdio.h>
#include <stdlib.h>

/* define structures - Point, Rectangle */
/* Write your code here */
struct structPoint;
struct structPoint
{
    float x;
    float y;

};
typedef struct structPoint Point;

struct structRectangle;
struct structRectangle
{
    Point a;
    Point b;
};
typedef struct structRectangle Rectangle;


//////////////////////////

/* declare functions*/
float area(Rectangle rect);
float width(Rectangle rect);
float height(Rectangle rect);
Point centroid(Rectangle rect);

int main() {
    Point a = {10, 40}; // a.x = 10, a.y = 40
    Point b = {55, 10}; // b.x = 55, b.y = 10

    /* Write your code here */

    // declaration Rectalge
    Rectangle rect;
    rect.a = a;
    rect.b = b;
    Point c;
    float w;
    float h;
    float A;


    c = centroid(rect);
    w = width(rect);
    h = height(rect);
    A = area(rect);

    printf("Bounding Box : (%.1f, %.1f, %.1f, %.1f)\n", c.x, c.y, w, h);
    printf("Area : %.1f\n", A);
    //////////////////////////    

    return 0;
}

/* define functions - area, width, height, centroid */
/* Write your code here */
float area(Rectangle rect)
{
    float w;
    float h;
    w = width(rect);
    h = height(rect);

    return w *h;
}

float width(Rectangle rect)
{
    return rect.b.x - rect.a.x;
}
float height(Rectangle rect)
{
    return rect.a.y - rect.b.y;
}
Point centroid(Rectangle rect)
{
    Point result;
    result.x = (rect.a.x + rect.b.x) /2;
    result.y = (rect.a.y + rect.b.y) /2;
    return result;
}
//////////////////////////