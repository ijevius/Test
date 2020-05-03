memory = dict()
memory[0] = 0
memory[1] = 1
memory[2] = 2

def num(n):
    if n in memory.keys():
        return memory[n]
    else:
        res = num(n-1)+num(n-3)
        memory[n] = res
    return res

n = int(input())
nums = input().split()
for i in nums:
    print(num(int(i)), end=" ")
