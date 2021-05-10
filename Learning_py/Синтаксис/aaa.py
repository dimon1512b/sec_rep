def move(x, y, nap):
    if nap == 0:
        y += 1
    if nap == 1:
        x += 1
    if nap == 2:
        y -= 1
    if nap == 3:
        x -= 1
    return x, y

n = int(input())
a = [[0] * n for i in range(n)]
x, y, nap = 0, 0, 0
for i in range(n ** 2):
    xx = x
    yy = y
    a[x][y] = i + 1
    x, y = move(x, y, nap)
    if x < 0 or y < 0 or x >= n or y >= n or a[x][y] != 0:
        x = xx
        y = yy
        nap = (nap + 1) % 4
        x, y = move(x, y, nap)
for i in range(n):
    print(*a[i])
