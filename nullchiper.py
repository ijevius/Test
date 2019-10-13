line = "".split() #without dot at end, via spaces. Allowed commas
       
x = max(line, key=len)
if x[len(x)-1] == ",": x = x[:len(x)-1]
for i in range(2, len(x)+1):
    print(" ".join(line[i::i+1]))
