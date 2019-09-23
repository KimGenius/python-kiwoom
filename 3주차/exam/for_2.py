# 구구단 n 단 출력해보기
n = int(input('몇 단을 출력할까요? '))
for i in range(1, 10):
    print(str(n) + ' * ' + str(i) + ' = ' + str(n * i))

