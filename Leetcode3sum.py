#TODO optimize it 

nums = []
result = []

for a in range(len(nums)-2):
    for B in range(len(nums)-1):
        if not B == a:
            for c in range(len(nums)):
                if (not c == a and not c == B) and (nums[a]+nums[B]+nums[c] == 0):
                    result.append(tuple(sorted([nums[a], nums[B], nums[c]])))                    

print([list(block) for block in set(result)])
