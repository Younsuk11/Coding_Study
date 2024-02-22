#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 15:27:19 2023

@author: yeomss
"""

#Binary search

#정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
#데이터가 가정되어 있어야 한다.
#변수 3개(start, end, mid)를 사용하여 탐색한다. 
#찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 것이 이진 탐색의 과정이
#O(logN)

#%% 재귀함수 구현
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    # 원하는 값 찾은 경우 인덱스 반환
    if array[mid] == target:
        return mid
    # 원하는 값이 중간점의 값보다 작은 경우 왼쪽 부분(절반의 왼쪽 부분) 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 원하는 값이 중간점의 값보다 큰 경우 오른쪽 부분(절반의 오른쪽 부분) 확인
    else:
        return binary_search(array, target, mid + 1, end)






n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1) # arrary, target, start, end
if result is None:
    print('원소가 존재 X')
else:
    print(result + 1)







#%% 반복문 구현

# 반복문으로 구현한 이진 탐색
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        # 원하는 값 찾은 경우 인덱스 반환
        if array[mid] == target:
            return mid
        # 원하는 값이 중간점의 값보다 작은 경우 왼쪽 부분(절반의 왼쪽 부분) 확인
        elif array[mid] > target:
            end = mid - 1
        # 원하는 값이 중간점의 값보다 큰 경우 오른쪽 부분(절반의 오른쪽 부분) 확인
        else:
            start = mid + 1

    return None


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result is None:
    print('원소가 존재 X')
else:
    print(result + 1)



#%% 라이브러리





from bisect import bisect_left, bisect_right
#bisect_left(a,x) : x를 a에 넣을 때, 가장 왼쪽에 해당하는 경우(인덱스) 반환
#bisect_right(a,x) : x를 a에 넣을 때, 가장 오른쪽에 해당하는 경우(인덱스) 반환



# '정렬된 리스트'에서 `특정 값들 사이에 속하는 원소의 개수`를 구할 때 좋다.


def count_by_range(b, left_value, right_value):
    right_index = bisect_right(b, right_value)
    left_index = bisect_left(b, left_value)
    print('right : ', right_index, 'left :', left_index)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(a, -1, 3))
# 리스트 a에 -1~3사이의 값은 총 6개 존재한다.







