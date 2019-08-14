def freq(lists):
    keys = set()
    f = dict()
    for array in lists:
        keys.update(array)
    for key in keys: f.update({key: 0})
    for key in keys:
        for arr in lists:
            if key in arr: f[key] += 1
    print(max(f, key=f.get))


n = int(input())
w, h = 2, n
t = [[0 for x in range(w)] for y in range(h)]
for i in range(n):
    t[i][0] = int(input())
    t[i][1] = int(input())+1

a = [list(range(m[0], m[1])) for m in t]
freq(a)
