#include<stdlib.h>
#include<stdio.h>

typedef struct MinStack {
    int value;
    int min;
    struct MinStack* next; // next node

    // obj is sentinel for top
} MinStack;


MinStack* minStackCreate() {
    /*
    linked list 구현
    head가 항상 last element
    */
    MinStack* stack = (MinStack*)malloc(sizeof(MinStack));
    stack->next = NULL;
    return stack;

}

void minStackPush(MinStack* obj, int val) {

    //obj은 sentinel? : yes
    
    MinStack* new = (MinStack*)malloc(sizeof(MinStack));

    new->value = val;


    if (obj->next == NULL){
        //nothing in stack
        new->min = val;
    }
    else{
        //minimum till now
        // 현재 이 노드를 추가할 때, 지금까지 본 노드들의 minimum을 새롭게 추가해서 저장.
        // 이 최근 노드가 사라진다면(from top) 다음 노드에는 그 해당 노드를 추가할 때까지 본 최소가 저장되어 있음.
        new->min = (val < obj->next->min) ?  val : obj->next->min; 
    }

    new->next = obj->next;
    obj->next = new;
    
}

void minStackPop(MinStack* obj) {
    
    //get from sentinel's next
    // always called on non-empty stacks

    MinStack* temp = obj->next;
    obj->next = obj->next->next;
    free(temp);

    //min update는 어차피 들어갈 때 있으므로 상관 없음?
    

}

int minStackTop(MinStack* obj) {
    // get from sentinel's next
    // always called on non-empty stacks
    
    int top = (obj->next != NULL) ? obj->next->value : -1;
    return top;

    
}

int minStackGetMin(MinStack* obj) {
    // always called on non-empty stacks
    //retrieves the minimum element in the stack.

    return obj->next->min;
}

void minStackFree(MinStack* obj) {
    
  
    //free all of them
    MinStack* cur =obj;
    while(cur != NULL){
        MinStack* temp = cur;
        cur = cur->next;
        free(temp);
    }
}

/**
 * Your MinStack struct will be instantiated and called as such:
 * MinStack* obj = minStackCreate();
 * minStackPush(obj, val);
 
 * minStackPop(obj);
 
 * int param_3 = minStackTop(obj);
 
 * int param_4 = minStackGetMin(obj);
 
 * minStackFree(obj);
*/


int main(){

    MinStack* obj = minStackCreate();
    minStackPush(obj, -2);
    minStackPush(obj, 0);
    minStackPush(obj, -3);
    printf("%d\n", minStackGetMin(obj)); //-3
    minStackPop(obj);
    printf("%d\n", minStackTop(obj)); // 0
    printf("%d\n", minStackGetMin(obj)); //-2
    minStackFree(obj);

    return 0;

}