//linked list에서는 header를 알려주는 sentinel(none)의 유무가 중요했는데,
//C로 넘어오면 malloc을 통해서 heap에 dynamic memory를 할당해주어,
//크기가 동적으로 변하는 linked list를 구현할 수 있다.

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

//linkned list in C (no sentinel)
typedef struct nodeType LinkedNode;

struct nodeType{
    int val;
    LinkedNode *next; // 다음 노드를 가리키는 pointer
};


//공간 할당 및 값 할당
LinkedNode *createNode(int x) // __init__함수가 없으니 만들어줘야함. 앞에 *이 있는 이유는 newNode라는 pointer(메모리)를 return 하므로
{
    LinkedNode *newNode;
    newNode = (LinkedNode *) malloc(sizeof(LinkedNode)); //void pointer also linkednode type
    // 메모리를 할당해주고 만들어진 메모리 내 내용을 채워넣는다고 생각하면 됨.

 
    newNode ->val = x;
    newNode->next = NULL;

    return newNode;

}


// single linked list in C no sentinel


typedef struct listType SLlist;
struct listType{
    LinkedNode *first;
    int size;
};


//functions declaration
void addFirst(SLlist *LL, int x); // insert first
void addBack(SLlist *LL, int x);
int getFirst(SLlist*LL); // return first node
int getSize(SLlist *LL);
void printSLlist(SLlist *LL);
LinkedNode *searchNode(SLlist *LL, int x);
void DeleteNode(SLlist *LL, int x);
LinkedNode* mergeTwoLists(LinkedNode* a, LinkedNode* b);
LinkedNode* reverse_LL(LinkedNode* head);
bool hasCycle(LinkedNode* head);
LinkedNode* addTwoNum( LinkedNode* l1, LinkedNode* l2);
LinkedNode* partition(LinkedNode* head, int x);




// functions definition
void addFirst(SLlist *LL, int x)
{
    LinkedNode *newFirst;

    newFirst = createNode(x); // 메모리 만들어서 저장

    newFirst->next = LL -> first; // NULL값
    LL -> first = newFirst;

    LL->size++;// size up

}

void addBack(SLlist *LL, int x){

    LinkedNode* newnode;
    newnode = createNode(x);

    
    if (LL->first == NULL){
        LL->first = newnode;
        LL->size++;
        return;
    }
    
    LinkedNode* curnode = LL->first;
    //find last
    while(curnode->next !=NULL){
        curnode = curnode->next;
    }

    curnode->next = newnode;
    LL->size++;
}



int getFirst(SLlist *LL)
{
    if (LL->first !=NULL)
    {
        return LL ->first ->val;

    }
    return 0;
}

int getSize(SLlist *LL)
{
    return LL -> size;
}

void printSLlist(SLlist *LL)
{
    LinkedNode *curr = LL -> first;

    printf("size : %d, firstVal : %d, allVals : ", getSize(LL) , getFirst(LL));

    while(curr !=NULL)
    {
        printf("%d ->", curr->val);
        curr = curr ->next;
    }

    printf("END\n");

}


LinkedNode *searchNode(SLlist *LL, int x)
{
    LinkedNode *curr = LL->first;

    while(curr!=NULL)
    {
        if (curr->val == x)
            return curr;
        curr = curr->next;
    }
    return NULL;
}

void DeleteNode(SLlist *LL, int x)
{
    LinkedNode *curr = LL -> first;
    LinkedNode *prev = NULL;


    while(curr != NULL)
    {
        if (curr ->val == x){
            if(curr == LL ->first)
            {
                LL->first = LL->first->next; // 가장 처음에서 찾을 때

            }
        
            else{
                prev->next = curr->next; // 하다가 찾을 경우
            }

            //지우고 buffer은 지우기
            free(curr); // deallocation
            LL->size--;
            return;
        }
        else /// 못찾을 경우, 넘어가기
        {
            prev = curr;
            curr = curr -> next;
        }


    }

}


LinkedNode* mergeTwoLists(LinkedNode* a, LinkedNode* b){
    /*
    합치고 first node 반환
    node : next & val
    */

    LinkedNode dummy;
    LinkedNode* new_head = &dummy; // sentinel
    new_head->next = NULL;

    while(a != NULL && b!=NULL){
        if (a->val <= b->val){
            new_head->next = a;
            a = a->next;
        }
        else{
            new_head->next = b;
            b = b->next;
        }
        new_head = new_head->next;
    }

    if(a!=NULL){
        new_head->next = a; // first node를 이어주면 되는 거라. a는 넘어가지 않아도 됨.
    }

    if(b!=NULL){
        new_head->next = b;
    }

    // return new_head->next;// 이거는 이미 끝까지 도달한 pointer를 반환할 것임.
    return dummy.next; // 첫번째 위치는 계속 별도로 지정을 해두어야 함.

}


LinkedNode* reverse_LL(LinkedNode* head)
{
    LinkedNode* prev = NULL;
    LinkedNode* next = NULL;
    LinkedNode* curnode = head;

    while(curnode !=NULL){
        next = curnode->next;
        curnode->next = prev;
        prev = curnode;
        curnode = next;
    }

    return prev;

}


bool hasCycle(LinkedNode* head)
{   

    /*
    
    Given head, the head of a linked list, 
    determine if the linked list has a cycle in it.

    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
    Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
    Note that pos is not passed as a parameter.

    return true if there is a cycle in the linked list. Otherwise, return false.

    앞에서부터 순회하다 이미 지나온 곳이 나오면 그때 cycle 감지. : two pointer

    Floyd's Tortoise and Hare Algorithm : slow pointer & fast pointer : 만나면 무조건 cycle
    */

   if (head == NULL){
    return false;
   }
   LinkedNode* slow = head;
   LinkedNode* fast = head -> next;

   while(fast != NULL && fast ->next != NULL){ // 다음 한칸이 NULL 일수도, 두칸을 건너와서 NULL 일수도.
        if (slow == fast){

            return true;
        }
        slow = slow -> next;
        fast = fast ->next -> next;

   }




    return false;
}


LinkedNode* addTwoNum(LinkedNode* l1, LinkedNode* l2) {
    /*
    You are given two non-empty linked lists representing two non-negative integers. 
    The digits are stored in reverse order, and each of their nodes contains a single digit. 
    Add the two numbers and return the sum as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.

    Input: l1 = [0], l2 = [0]
    Output: [0]

    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]

    Traverse both lists, add corresponding digits, and handle carry.
    */

    LinkedNode dummy;
    LinkedNode* newnode = &dummy; // sentinel
    newnode->next = NULL;
    int carry = 0;

    while (l1 != NULL || l2 != NULL || carry) {
        int sum = carry;
        if (l1 != NULL) {
            sum += l1->val;
            l1 = l1->next;
        }
        if (l2 != NULL) {
            sum += l2->val;
            l2 = l2->next;
        }

        carry = sum / 10;
        LinkedNode* temp = (LinkedNode*)malloc(sizeof(LinkedNode));
        temp->val = sum % 10;
        temp->next = NULL;
        newnode->next = temp;
        newnode = newnode->next;
    }

    return dummy.next;
}



LinkedNode* partition(LinkedNode* head, int x){

    /*
    Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

    You should preserve the original relative order of the nodes in each of the two partitions.


    Input: head = [1,4,3,2,5,2], x = 3
    Output: [1,2,2,4,3,5]
    Example 2:

    Input: head = [2,1], x = 2
    Output: [1,2]
        
    */

    LinkedNode dummy1; // for less than x
    LinkedNode dummy2; // for greater than  x
    LinkedNode* cur1 = &dummy1;
    LinkedNode* cur2 = &dummy2;
    cur1->next = NULL;
    cur2->next = NULL;


    LinkedNode* cur = head;
    while(cur != NULL){

        LinkedNode* temp = (LinkedNode*)malloc(sizeof(LinkedNode));
        temp->next = NULL;
        temp->val = cur->val;
        if (cur->val < x){
            cur1->next = temp;
            cur1= cur1->next;
        }
        else{
            cur2->next = temp;
            cur2 =cur2->next;
        }
    
        cur = cur->next;
    }

    cur1->next = dummy2.next;
    return dummy1.next;
    
}









void Episode1()
{
    SLlist myLL = {NULL, 0};

    addFirst(&myLL, 10);

    printf("%d\n", getFirst(&myLL));
    getSize(&myLL);
    printSLlist(&myLL);
}

void Episode2(int argc, char* argv[]){
    
    SLlist list_a = {NULL, 0};
    SLlist list_b = {NULL, 0};
    

    // 절반씩, Merge two sorted linked list
    for(int i = 0; i < (argc-1)/2; i++){
        addFirst(&list_a, atoi(argv[(argc-1)/2-i]));  // 뒤에서 부터 넣기.
    }
    for(int i = 0; i < argc/2; i++){
        addFirst(&list_b, atoi(argv[(argc-1)-i]));
    }


    //print
    printSLlist(&list_a);
    printSLlist(&list_b);

    LinkedNode *c;
    c =  mergeTwoLists(list_a.first, list_b.first);
    SLlist list_c = {NULL, 0};

    while (c){
        printf("%d ", c->val);
        addBack(&list_c, c->val);
        c = c->next;
    }

    printSLlist(&list_c);
    
    

    
}


void Episode3(int argc, char* argv[])
{  
    int length = argc - 1;

    /* Create a linked list from input integers */
    LinkedNode *head = NULL;
    LinkedNode *prev = NULL;
    LinkedNode *curr = NULL;

    for (int k = 1; k <= length; k++) {
        LinkedNode *temp = createNode(atoi(argv[k]));
        if (k > 1){
            prev->next = temp;
        }
        else {
            head = temp;
        }
        prev = temp;
    }

    /* Write your code here */	
    // Since printing starts at 'LinkedNode *head', it must point to the first node of the linked list.
    LinkedNode* newhead = reverse_LL(head);
    SLlist newssl = {NULL, 0};
    // DO NOT MODIFY BELOW!!!
    
    curr = newhead;
    while (curr){
        printf("%d ", curr->val);
        addBack(&newssl, curr->val);
        
        curr = curr->next;
    }

    printSLlist(&newssl);


}



int main(int argc, char*argv[]){

    //argc : int
    // argv : 배열의 pointer
    Episode1();



    /*
    Sample 1)
    ./run 1 3 5 7 2 4 6 8
    output : 1 2 3 4 5 6 7 8

    Sample 2)
    ./run 1 5 8 3 6 9
    output : 1 3 5 6 8 9

    */
    Episode2(argc, argv);




    /*
    Sample 1)
    ./run 1 2 3 4 5
    output : 5 4 3 2 1

    Sample 2)
    ./run 10 20 30
    output : 30 20 10
    */
    Episode3(argc, argv);

    return 0;
}







