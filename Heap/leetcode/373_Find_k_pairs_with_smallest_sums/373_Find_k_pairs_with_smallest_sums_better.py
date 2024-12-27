
import heapq
from typing import List
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        heap = []

        for i in range(min(k , len(nums1))): # 둘 중 작은 것을 기준으로 , 만약 k가 더 작으면 먼저 다 돌리고, 나중에 업데이트 ,k가 더 크면 더 넣어주기.
            heap.append((nums1[i] + nums2[0], i, 0)) # sum을 기준으로 min heap



        #K개만 생각하고 계속 업데이트

        results = []
        while heap and len(results) <k:

            '''
            heap 크기가 k보다 작을 때, 계속해서 새로운 pair를 추가해야 한다.
            heap 크기가 k보다 클 때, 새로운 pair를 추가할 때마다 가장 작은 pair를 제거해야 한다.

            검사 대상 : num1[0] + nums2[j]가 지금 heap 구성성분보다 큰지 작은지.
            '''
            s, i, j = heapq.heappop(heap)
            results.append([nums1[i], nums2[j]]) # 앞에서부터 하나씩 뺴기 (어차피 계속 제일 작은것으로 업데이트 됨.)

            # 추가 : 지금보다 "한 단계"만 더 큰 것을 넣어주기.
            if j +1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))

            #i에 대해서는 이미 heap에 모든 i들이 들어가 있기 때문.
        
        return results
            

