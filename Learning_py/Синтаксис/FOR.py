a, b, c, d = int(input()), int(input())  + 1, int(input()), int(input()) + 1
for i in range(c, d):
    print('\t', i, end='')
print()
for i in range(a, b):
    print(i, end='\t' + " ")
    for j in range(c, d):
        print(i * j, end='\t' + " ")
    print()

#Сейчас будет нечто что называется [list comperhention]
#но нужно обратить внимание на работу for со множеством переменных

lst = [["apple", 55, 62, 1], ["orange", 60, 74, 2], ["pineapple", 140, 180, 3], ["lemon", 80, 84, 4]]

print(sum([num for frut, low, high, num in lst]))



