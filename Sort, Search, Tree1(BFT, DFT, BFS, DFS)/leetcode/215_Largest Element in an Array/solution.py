'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?


sorting algorithm time complexities
1. selection sort : O(N^2)
2. insertion sort : O(N^2)
3. merge sort : O(N*logN)
4. quick sort : O(N*logN) or O(N^2)
'''

'''
사실상, sort -> find kth index라기 보다는
search에 가까운 것.

정답 : quick_selection

'''


from typing import List
class Solution:


    def merge(self,L, start, mid, last):
        k = start
        sub1 = L[start :mid+1]
        sub2 = L[mid+1 : last + 1]
        
        i = j = 0
        while(i<len(sub1) and j< len(sub2)):
            if (sub1[i] <= sub2[j]):
                L[k] = sub1[i]
                i+=1
            else:
                L[k] = sub2[j]
                j+=1
            k+=1
        
        if (i <len(sub1)):
            L[k:last+1] = sub1[i:]
        if (j<len(sub2)):
            L[k:last + 1] = sub2[j:]

    def mergesort(self,L, first, last):

        if (first == last ): 
            return
        if (first < last):
            mid = first + (last -first)//2

            self.mergesort(L, first, mid)
            self.mergesort(L, mid+1 ,last)
            self.merge(L, first,mid, last)



    def quick_selection_reverse(self,arr, kth):
        if len(arr) ==1:
            return arr[0] # 재귀 종료 시점.

        pivot = arr[len(arr)//2] ## pivot 위치 mid로 설정

        left, mid, right = [], [], []

        for i in range(len(arr)): # 전체를 순환하면서 pitvot기준으로 왼쪽 오른쪽 나누기.
            
            if arr[i] < pivot:
                left.append(arr[i]) # 작은 쪽에 합류
            
            elif arr[i] > pivot:
                right.append(arr[i]) # 큰 쪽에 합류
            else: 
                mid.append(arr[i]) # 같은 경우


        '''
        kth largest 라면 적은 k는 큰 쪽에서 먼저 개수 체크
        '''
        if kth <=len(right): 
            return self.quick_selection_reverse(right, kth)
        
        elif kth<=len(right) + len(mid):

            return mid[0]
        else: 
            #kth >= len(left) + len(mid)
        
            return self.quick_selection_reverse(left, kth - len(right) -len(mid))



    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # # solution 1 : mergesort -> find kth element
        # self.mergesort(nums, 0, len(nums)-1)
        # return nums[-k]

        #solution2 : quick selection -> kth smallest element or largest element
        ans = self.quick_selection_reverse(nums, k)
        return ans




def main():
    L = [3,2,1,5,6,4]
    print(L)
    sol = Solution()
    sol.mergesort(L, 0, len(L)-1)
    print(L)


    k = 2
    ans = sol.findKthLargest(L, k)
    print("Ans : ", ans)

if __name__ =="__main__":
    main()
