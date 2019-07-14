def d(a, b):
    if len(a) > len(b):
        b.extend([None] * len(a) - len(b))
    return dict((a[i], b[i]) for i in range(len(a)))
