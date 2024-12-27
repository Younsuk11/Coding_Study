'''
from collections import deque
result = deque()

deque.append(item): item을 데크의 오른쪽 끝에 삽입한다.
deque.appendleft(item): item을 데크의 왼쪽 끝에 삽입한다.
deque.pop(): 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
deque.popleft(): 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
deque.extend(array): 주어진 리스트를 데크의 오른쪽에 추가한다.
deque.extendleft(array): 주어진 리스트를 데크의 왼쪽에 추가한다.
deque.remove(item): item을 데크에서 찾아 삭제한다. (제일 처음 나온 해당 string만 제거됨)
deque.clear(): 해당 deque 전체 삭제
deque.reverse(): 말그대로 역순으로 정렬한다.
deque.rotate(num): 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽).



baseline : circular queue(array implementation)
'''

class deque:
    rear = 0
    front = 0
    max_size = 10
    deq = list()
    ## 자동 초기화. like member variables in C++



    def __init__(self):
        self.rear = 0
        self.front = 0 # 항상 빈 공간을 가리키고 있음. (circular queue와 동일)
        self.deq = [0 for _ in range(self.max_size)]

    def is_empty(self):
        if (self.front == self.rear):
            return True
        return False
    
    def is_full(self):
        if ((self.rear+1) % self.max_size == self.front):
            return True
    
        return False

    def get_front(self): 
        ## same as dequeue in circular queue
        # but not remove, just return

        if (not self.is_empty()):
            front = (self.front +1) % self.max_size 
            ## front는 항상 빈 공간을 가리키고 있어서 값을 가져오려면 이렇게 해야 함.
            return self.deq[front]

        return -1
    
    def get_rear(self):
        if(not self.is_empty()):
            return self.deq[self.rear]
        return -1
    
    def add_rear(self, x):
        ## same as enqueue in circular queue

        if (self.is_full()):
            print("queue is full")
            ## resize
            return
        self.rear = (self.rear+1) %self.max_size
        self.deq[self.rear] = x


    def add_front(self, x):
        if (self.is_full()):
            print("queue is full")
            return
    
        self.deq[self.front]
        '''
        self.front = (self.front -1) % self.max_size 
        이 계산을 하면 안되는데, 
        front 가 0이면 벗어난다. 그걸 방지해주고자 한바퀴를 더 돌린 +max_size를 해준다.
        '''
        self.front(self.front -1 + self.max_size) % self.max_size


    def del_front(self):
        ## same as dequeu in circular queue

        if (self.is_empty()):
            print("queue is empty")
            return

        self.front  = (self.front + 1) % self.max_size ## 여기서는 변화가 있음.
        return self.deq[self.front]
    
    def del_rear(self):
        if (self.is_empty()):
            print("queue is empty")
            return
    
        ## del_front와 순서가 다르다. : 불러오고, 인덱스 업로드 : rear 는 front와 다르게 실제 값을 가리키고 잇으니가
        temp = self.deq[self.rear]

        ## add front와 마찬가지로 index가 0을 벗어나는 것을 방지해주기 위해 + max_size
        self.rear = (self.rear - 1 + self.max_size) % self.max_size
        return temp
    

    #추가한 함수
    def reverse(self):
        pass


    def rotate(self):
        pass

    
    def print_deque(self):
        i = (self.front + 1) % self.max_size ## nothing in self.front

        if (self.is_empty()):
            print("queue is empty")
            return
        while (i != self.rear):
            print("value : ", self.deq[i])
            i = (i+1) % self.max_size
        
        print(self.deq[i]) ## for i == self.rear