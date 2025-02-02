def spy_game(nums):
    spy = [0,0,7]
    el = 0
    for i in nums:
        if i == spy[el]:
            el += 1
        if el == 3:
            return True
    else:
        return False
print(spy_game([1,2,4,0,0,7,5]))