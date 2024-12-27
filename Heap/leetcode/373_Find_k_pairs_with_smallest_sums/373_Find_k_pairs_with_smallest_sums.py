'''
Array, Heap


You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

모든 pair 조합의 합을 계산하면서 priority queue에 넣어서 k개의 pair를 뽑아내면 된다.


Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]


Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]


'''

'''
python heap 함수들(기본 min heap)
- heapq.heappush(heap, item)
- heapq.heappop(heap) : 가장 작은 요소를 꺼내고 반환
- heapq.heapify(x) : 이미 있는 리스트를 힙으로 변환
- heapq.nlargest(n, iterable, key=None) : n개의 가장 큰 요소를 반환
- heapq.nsmallest(n, iterable, key=None) : n개의 가장 작은 요소를 반환

max heap으로 바꾸기
- heapq.heappush(heap, -item)

'''



import heapq
from typing import List
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        heap = []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                s = nums1[i] + nums2[j]
                heapq.heappush(heap, (s, nums1[i], nums2[j])) # sum을 기준으로 min heap


        # heapq.heapify(heap)

        # results  = heap[:k]
        # return [[x[1], x[2]] for x in results] # 그대로 꺼내면 안됌.

        results = []
        for _ in range(k):
            if heap:
                results.append(heapq.heappop(heap)[1:]) # pop은 꺼내고 지운다.
            else:
                break   

        return results
    
        # or 
        # return [[x[1], x[2]] for x in heapq.nsmallest(k, heap)]


'''
이 코드의 문제점.
1. 이미 non-decreasing order로 정렬되어 있기 때문에, 불필요한 계산이 많이 일어난다.

제일 작은 것들로 예상되는 거 먼저 넣어주고 그다음을 생각

3. 굳이 모든 조합들을 넣어줄 필요가 없이. 매번 맨 위에서 하나씩 뺀다고 생각하고 heap에만 빼고 추가 빼고 추가를 반복.


'''




if __name__ == "__main__":
    sol = Solution()
    # print(sol.kSmallestPairs([1,7,11], [2,4,6], 3)) # [[1,2],[1,4],[1,6]]
    # print(sol.kSmallestPairs([1,1,2], [1,2,3], 2)) # [[1,1],[1,1]]
    # print(sol.kSmallestPairs([1,2], [3], 3)) # [[1,3],[2,3]]
    print(sol.kSmallestPairs([1,2,4,5,6], [3,5,7,9], 3)) # [[1,3],[2,3],[1,5]]
