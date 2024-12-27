'''
bubble sort
1. 순회 하면서 현재 위치보다 다음 위치의 값이 더 작을 경우 둘의 위치를 바꾼다.
2. time complexity
'''

def bubblesort_ascending(arr):
    n = len(arr)


    # 오른쪽 끝을 먼저 가장 큰 것으로 만들기 위해서 왼쪽에서 bubble up한다는 느낌.
    for i in range(n-1, -1, -1): ## 역순으로 순회
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr


def bubblesort_descending(arr):
    n = len(arr)


    #이번엔 왼쪽으로 올리니까 반대로.
    for i in range(n):
        for j in range(n-1, i , -1):
            if arr[j] >arr[j-1]:
                arr[j] , arr[j-1] = arr[j-1], arr[j]
    
    return arr



def main():
    L = [2,5,6,8,2,10]
    print(L)

    print("Ascending : ", bubblesort_ascending(L))
    print("Descending : ", bubblesort_descending(L))


if __name__ == "__main__":
    main()