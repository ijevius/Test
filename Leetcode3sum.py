nums = []
result = []

for a in range(len(nums)-2):
    for B in range(len(nums)-1):
        if not B == a:
            c_exp = -nums[a]-nums[B]
            c_ins = [i for i,x in enumerate(nums) if x == c_exp]
            if c_exp in nums and (((not a in c_ins) and (not B in c_ins)) or len(c_ins)>2):
                result.append(tuple(sorted([nums[a], nums[B], c_exp])))
            elif (((not a in c_ins) ^ (not B in c_ins))) and len(c_ins)>1:
                result.append(tuple(sorted([nums[a], nums[B], c_exp])))

res = [list(block) for block in set(result)]
print(res)
