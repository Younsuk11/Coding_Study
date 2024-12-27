#include <stdio.h>
#include <stdlib.h>

/*
 * 이중 연결 리스트 노드
 * 각 노드는 큐의 요소를 저장
 */
typedef struct QueueNode {
    int data;
    struct QueueNode *prev;
    struct QueueNode *next;
} QueueNode;

/*
 * 큐와 이중 연결 리스트를 결합한 자료 구조
 */
typedef struct Deque {
    QueueNode *front;   // 큐의 앞쪽 포인터
    QueueNode *rear;    // 큐의 뒤쪽 포인터
    int size;           // 현재 큐의 크기
} Deque;

/* 
 * 함수 프로토타입 
 */

// 큐 초기화
Deque* create_deque();

// 큐가 비어있는지 확인
int is_empty(Deque *deque);

// 큐의 크기 반환
int get_size(Deque *deque);

// 큐의 앞에 요소 추가 (enqueue_front)
void enqueue_front(Deque *deque, int value);

// 큐의 뒤에 요소 추가 (enqueue_rear)
void enqueue_rear(Deque *deque, int value);

// 큐의 앞에서 요소 제거 및 반환 (dequeue_front)
int dequeue_front(Deque *deque);

// 큐의 뒤에서 요소 제거 및 반환 (dequeue_rear)
int dequeue_rear();

// 큐의 앞 요소 확인
int peek_front(Deque *deque);

// 큐의 뒤 요소 확인
int peek_rear(Deque *deque);

// 큐 메모리 해제
void free_deque(Deque *deque);

/* 
 * 함수 구현 
 * 아래는 함수의 기본 스켈레톤으로, 실제 구현은 필요에 따라 추가하세요.
 */

// 큐 초기화
Deque* create_deque() {
    // 메모리 할당 및 초기화
    return NULL;
}

// 큐가 비어있는지 확인
int is_empty(Deque *deque) {
    // 빈 경우 1, 아니면 0 반환
    return 0;
}

// 큐의 크기 반환
int get_size(Deque *deque) {
    // 현재 크기 반환
    return 0;
}

// 큐의 앞에 요소 추가
void enqueue_front(Deque *deque, int value) {
    // 새로운 노드 생성 및 앞쪽에 삽입
}

// 큐의 뒤에 요소 추가
void enqueue_rear(Deque *deque, int value) {
    // 새로운 노드 생성 및 뒤쪽에 삽입
}

// 큐의 앞에서 요소 제거 및 반환
int dequeue_front(Deque *deque) {
    // 앞쪽 노드 제거 및 값 반환
    return -1;
}

// 큐의 뒤에서 요소 제거 및 반환
int dequeue_rear(Deque *deque) {
    // 뒤쪽 노드 제거 및 값 반환
    return -1;
}

// 큐의 앞 요소 확인
int peek_front(Deque *deque) {
    // 앞쪽 노드의 값 반환
    return -1;
}

// 큐의 뒤 요소 확인
int peek_rear(Deque *deque) {
    // 뒤쪽 노드의 값 반환
    return -1;
}

// 큐 메모리 해제
void free_deque(Deque *deque) {
    // 모든 노드와 큐 자체의 메모리 해제
}



int main() {
    Deque *deque = create_deque();

    enqueue_rear(deque, 10);
    enqueue_rear(deque, 20);
    enqueue_front(deque, 5);

    printf("Front element: %d\n", peek_front(deque));
    printf("Rear element: %d\n", peek_rear(deque));

    printf("Dequeued from front: %d\n", dequeue_front(deque));
    printf("Dequeued from rear: %d\n", dequeue_rear(deque));

    printf("Queue size: %d\n", get_size(deque));

    free_deque(deque);
    return 0;
}
