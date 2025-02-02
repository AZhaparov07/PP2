def unique(nums):
    nums1 = []
    for num in nums:
        if num not in nums1:
            nums1.insert(len(nums1),num)
    nums2 = sorted(nums1)
    return nums2
print(unique([5,6,7,4,3,5,7]))