def threenexttothree(nums):
    for i in range(len(nums)-1):
        if nums[i] == 3:
            if nums[i+1] == 3:
                return True
    return False
print(threenexttothree([1, 3, 3]))
