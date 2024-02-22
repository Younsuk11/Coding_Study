#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 13:53:40 2023

@author: yeomss
"""

from collections import deque

deq = deque() #양방향 큐,  리스트는 단방향인데 반면,
deq.appendleft(10) # start에 추가
deq.append(0) # add to the end

deq.popleft() #pop from the start
deq.pop() #pop from the end (가져오고 삭제)

deq = deque([1,2,3,4,5])

deq.extend([6,7]) # 주어진 array를 순회하면서 deq 오른쪽에 추가
deq.extendleft([0,-1]) # 순회하면서 왼쪽에  deque([-1, 0, 1, 2, 3, 4, 5, 6, 7])

deq.remove(1)# deque([-1, 0, 2, 3, 4, 5, 6, 7])
deq.rotate(-1) #숫자만큼 회전, 양수면 오른쪽 음수면 왼(한칸씩 미룬다는 것을 의미) : deque([0, 2, 3, 4, 5, 6, 7, -1])



###리스트처럼 사용하기도, stack처럼 사용하기도 해서 좋다.



#%%
#stack tutorial

#stack이란, 가장 나중에 자료가 가장 먼저 처리되는 자료구조
#Last in First out

#리스트로 흉내내서 만들어준다.
stack = []


stack = [1,2,3]
stack.append(4)
print(stack)

top = stack.pop()
print(top, stack)


#%%
## 백준 7576 토마토 문제

from collections import deque


def solution(m, n, tomatoes):
    count = 0  # Count number of days
    deq = deque()
    # deq = list()
    D = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def search(row, col):
        searched_list = []

        for i, j in D:
            if (row + i < N and col + j < M) and (row + i >= 0 and col + j >= 0):
                if tomatoes[row + i][col + j] == 0:
                    tomatoes[row + i][col + j] = 1
                    searched_list.append((row + i, col + j))

        return searched_list

    # Add all riped tomatoes
    for r in range(N):
        for c in range(M):
            if tomatoes[r][c] == 1:
                deq.append((r, c))

    # Search begin
    while deq:
        for _ in range(len(deq)):
            r, c = deq.popleft()
            for tomato in search(r, c):
                deq.append(tomato)
        count += 1

    # Check unriped tomato(es) after search
    for r in range(N):
        for c in range(M):
            if tomatoes[r][c] == 0:
                return -1

    return count - 1


if __name__ == "__main__":
    M, N = map(int, input().split(" "))
    tomatoes = [[int(n) for n in input().split(" ")] for _ in range(N)]
    print(solution(M, N, tomatoes))
