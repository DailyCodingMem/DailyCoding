def solution(sizes):
    w, h = 0, 0
    for size in sizes:
        x, y = min(size), max(size)
        if w * h == 0:
            w, h = x, y
        else:
            w, h = max(x, w), max(y, h)
    return w*h
