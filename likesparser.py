def likes(s):
    return " and ".join(s) + " like this" if len(s) == 2 else 'No one likes this' if len(s) == 0 else f"{', '.join(s[:2])} and {s[2]} like this" if len(s)==3 else str(s[0])+" likes this" if len(s)==1 else ", ".join(s[:2]) + f" and {len(s)-2} others like this"
