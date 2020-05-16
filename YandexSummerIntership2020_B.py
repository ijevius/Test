import sys

n = int(input())
pods = []
num = 0
res = -1

i = 0

for m in range(n):
    line = next(sys.stdin)
    d = [int(line[0]), int(line[2])]
    pods.append(d)

    #print(pods)

for p in range(len(pods)-2):
    for k in range(p+1, len(pods)-1):
        if (pods[k][0] > pods[p][0]) and (pods[k][1] > pods[p][1]):
            num += 1
                #break #дальше можно не проверять

res = n-num

if num == 0: res = 1

print(res)
