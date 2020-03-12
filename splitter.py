s = "" #str with text
subs = ""
SEPARATOR = " "

i = 0
while i < len(s)-2:
    if s[i] == SEPARATOR:
        if subs != "":
            print(subs)
            subs = ""
        i += 1
    else:
        for k in range(i, len(s)):
            if s[k] != SEPARATOR:
                subs += s[k]
            else:
                break
        print(subs)
        subs = ""
        i = k + 1
