v = int(input('깊이를 입력해주세요: '))
for i in range(1, v + 1):
    for j in range(i, v):
        print(' ', end='')
    for k in range(0, i + (i - 1)):
        print('*', end='')
    print()
for z in range(1, v):
    for x in range(0, z):
        print(' ', end='')
    for y in range(z, v + (v - z - 1)):
        print('*', end='')
    print()
