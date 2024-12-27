def findMedianSortedArrays(nums1, nums2):
    
    i = j = 0
    nums = []
    while(i < len(nums1) and j < len(nums2)):

        if (nums1[i] <= nums2[j]):
            nums.append(nums1[i])
            i+=1
        else:
            nums.append(nums2[j])
            j+=1
    
    # handling remaining
    if (i< len(nums1)):
        nums+= nums1[i:]
    if (j<len(nums2)):
        nums += nums2[j:]

    # get median
    mid = len(nums)//2
    if (len(nums)%2 == 1):
        return nums[mid]
    else:
        return (nums[mid -1] + nums[mid]) / 2



if __name__ =="__main__":
    nums1= [1,2]
    nums2 = [3]
    ans = findMedianSortedArrays(nums1, nums2)
    print(ans)