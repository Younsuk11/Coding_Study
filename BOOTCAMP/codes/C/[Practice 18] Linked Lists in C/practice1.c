#include <stdio.h>
#include <stdlib.h>

/*
[Practice] Merge Two Sorted Linked List

Get two sorted linked lists, merge two into one sorted linked list and return its head node.

Sample 1)
./run 1 3 5 7 2 4 6 8
output : 1 2 3 4 5 6 7 8

Sample 2)
./run 1 5 8 3 6 9
output : 1 3 5 6 8 9
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

LinkedNode* mergeTwoLists(LinkedNode *a, LinkedNode *b){

    /* Write your code here */








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
    SLList list_a = {NULL, 0};
    SLList list_b = {NULL, 0};
    for(int i = 0; i < (argc-1)/2; i++){
        addFirst(&list_a, atoi(argv[(argc-1)/2-i])); 
    }
    for(int i = 0; i < argc/2; i++){
        addFirst(&list_b, atoi(argv[(argc-1)-i]));
    }
    LinkedNode *c;
    c =  mergeTwoLists(list_a.first, list_b.first);

    while (c){
        printf("%d ", c->val);
        c = c->next;
    }
    
    return 0;
}

