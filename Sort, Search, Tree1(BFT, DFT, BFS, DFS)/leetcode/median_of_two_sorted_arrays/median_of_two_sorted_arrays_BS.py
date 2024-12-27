def findMedianSortedArrays(nums1, nums2):
    

    # 이미 정렬된 것을 이용하여 "어떤 수" 찾는다. : binary search
    # mid를 기준으로 찾는게 작으면 왼쪽, 크면 오른쪽
    # 여기서는 "어떤 수" 보다는 "어떤 위치"를 찾는다에 가까움.
    # median을 찾아? 계산! :  median 순서 상 중앙에 있는 친구.(짝수개이면 두 수의 평균, 홀수개면 그 위치)
     # 즉 두 배열을 합쳤을 때, 중간값(파티션)을 중심으로 왼쪽이 작고, 오른쪽은 커야 함.
     # 찾은 위치들 i, j : 파티션 기준 왼쪽 개수
     # i + j = (n + m +1) // 2 그 개수 합은 합쳤을 때, 왼쪽 개수랑 같아야 함.(홀수일 경우, 왼쪽에서 최댓값, 짝수일 경우, 왼쪽 최대 , 오른쪽 최소 평균)
     # 5 -> 2 , 6 -> 3

    # i, j 찾기 원리(조건) : i, j들을 기준으로 왼쪽 오른쪽 대소 비교(하단 조건들)가 일치해야 함.
    # 1. i 오른쪽 최솟값 >= j 왼쪽 최댓값이 되도록 i는 늘려가고(j는 자동으로 줄여감)
    # 2. i 왼쪽 최댓값 <= j 오른쪽 최솟값이 되도록 i를 줄여간다.
    # 3. i는 nums1의 중간에서 시작.

    
    # binary search인 이유 : 이미 정렬된 것(작은 배열)에서 i의 위치를 찾는다. : searching
    # 찾는 위치, index인 i를 nums1에서 조건 만족를 따져가며, 찾는 범위 조정.
    ### 찾는 범위를 left와 right로 조정하면서 조율.(start와 end를 mid로 상황별로 대체시키면서 범위 조절하듯.)
    ## while(start <= end)


    n = len(nums1)
    m = len(nums2)
    if (n> m ):
        return findMedianSortedArrays(nums2, nums1)

    #i를 찾는 초기 범위
    start= 0
    end = len(nums1)


    while(start <= end):

        i = (start+ end) // 2 ## num1의 경계선 왼쪽 개수 : 찾는 위치임.
        j = (n + m +1)//2 -i ## nums2의 경계선 왼쪽 개수

        #index가 경계 밖으로 넘어가는 경우도 생김.
        A_left = nums1[i-1] if i>0 else -float("inf")#i왼쪽 최댓값
        A_right= nums1[i] if i < n else float("inf")# i오른쪽 최솟값
        B_left = nums2[j-1] if j>0 else -float("inf") #j왼쪽 최솟값
        B_right = nums2[j] if j < m else float("inf")#j왼쪽 최댓값

        if (A_right >= B_left and A_left <=B_right): # if array[mid] == target:와 상응

            # 조건 일치 : 반환

            if ((n+m) % 2==1): #홀수개
                # 경계들 왼쪽에서 최댓값
                return max(A_left, B_left)
            else:
                #짝수개
                #왼쪽 최대, 오른쪽 최소의 평균
                return (max(A_left, B_left) + min(A_right, B_right)) /2.0


        elif (A_right < B_left): start = i +1  #elif array[mid] < target:와 상응
        
        else:  end = i-1





if __name__ =="__main__":
    nums1= [1,2]
    nums2 = [3]
    ans = findMedianSortedArrays(nums1, nums2)
    print(ans)