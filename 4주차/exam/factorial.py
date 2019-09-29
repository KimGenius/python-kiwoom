def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)


x = int(input('팩토리얼을 계산할 수를 입력하세요: '))
print(factorial(x))
