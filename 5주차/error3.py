def checkOdd(num):
    return num / 2 == 0


a = int(input('숫자를 입력해주세요: '))

if checkOdd(a):
    print('a는 짝수 입니다!')
else:
    print('a는 홀수 입니다!')
