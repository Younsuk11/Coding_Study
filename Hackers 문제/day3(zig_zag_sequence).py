#debug the existing code to successfully execute all provided test files.

#A sequence will be called a zig zag sequence if the first  elements in the sequence are in increasing order and the last  elements are in decreasing order
# k = (n+1)/2 , n is odd

#You can modify at most three lines in the given code. You cannot add or remove lines of code.

def findZigZagSequence(a, n):
    a.sort() #ascending order
    mid = int((n + 1)/2) -1  # 4 (changed here)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1 # 5
    ed = n - 2 # 7 #(last one n-1 already min1) (changed here)
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1 #(change here)

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)



