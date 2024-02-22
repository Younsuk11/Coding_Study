#include <stdio.h>
#include <stdlib.h>

/*
Sample 1)
$ ./divide_linked_list 1 2 3 4 5
odd 1 3 5 
even 2 4 

Sample 2)
$ ./divide_linked_list 2 4 6 8 10
odd
even 2 4 6 8 10 

Sample 3)
$ ./divide_linked_list
odd 
even
*/


/* Linked list node structure */
typedef struct nodeType LinkedNode;
struct nodeType{
    int val;
    LinkedNode *next;
};

typedef struct listType SLList;
struct listType{
    LinkedNode *first;
    int size;
};

/* Linked list node functions */
LinkedNode *createNode(int x);
void addFirst(SLList *LL, int x);


void divideList(LinkedNode *a){

    LinkedNode *odd_head = createNode(-1);
    LinkedNode *even_head = createNode(-1);

    /* 
    Currently, odd_head and even_head point to dummy nodes. 
    In the code you write, odd_head and even_head must never change, and must still point to these dummy nodes at the end of the code. 
    Therefore, create new pointers (for example, odd_curr, even_curr) to use.
    */

    /* Write your code here */
    










    // DO NOT MODIFY BELOW!!!

    odd_head = odd_head->next;
    even_head = even_head->next;

    printf("odd ");
    while (odd_head){
        printf("%d ", odd_head->val);
        odd_head = odd_head->next;
    }
    printf("even ");
    while (even_head){
        printf("%d ", even_head->val);
        even_head = even_head->next;
    }
}


// DO NOT MODIFY BELOW!!!

/* Function to create a new node */
LinkedNode *createNode(int x){
    LinkedNode *newNode = (LinkedNode *)malloc(sizeof(LinkedNode));
    newNode->val = x;
    newNode->next = NULL;
    return newNode;
}

void addFirst(SLList *LL, int x){
    LinkedNode *newFirst = createNode(x);
    newFirst->next = LL->first;
    LL->first = newFirst;
    LL->size++;
}

int main(int argc, char* argv[]){
    SLList LL = {NULL, 0};

    for(int i = argc-1; i > 0; i--){
        addFirst(&LL, atoi(argv[i])); 
    }

    divideList(LL.first);
    
    return 0;
}

