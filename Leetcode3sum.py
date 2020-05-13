nums = []
result = []

for a in range(len(nums)-2):
    for B in range(len(nums)-1):
        if not B == a:
            c_exp = -nums[a]-nums[B]
            if c_exp in nums:
                result.append(tuple(sorted([nums[a], nums[B], c_exp])))

res = [list(block) for block in set(result)]
print(res)
