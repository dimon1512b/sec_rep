objects = [1, 2, 1, 5, True, False, True, 'false', [], [1,2], [1,2]]
a = 0
o_k = 0
i_k = 0
for obj in objects:
    for i in objects:
        if (obj is i) and o_k != i_k:
            i_k = 0
            break
        elif (i is objects[-1]) and obj is not i:
            a += 1
        i_k += 1
    o_k += 1
print(a)
