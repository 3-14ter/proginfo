def navigacio(a):
    nums = sorted(a)
    b = 0
    for x in nums:
        if x > b + 1:
            return b + 1
        b += x
    return b + 1
print(navigacio({1, 2, 3, 4, 5, 7}))