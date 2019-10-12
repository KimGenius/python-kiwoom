def calculator(num1, num2, type):
    if type == 'sum':
        return num1 + num2
    elif type == 'min':
        return num1 - num2
    elif type == 'mul':
        return num1 * num2
    elif type == 'div':
        return num1 / num2
    else:
        return '정확한 type을 입력해주세요.'


print(calculator(int(input('숫자1을 입력해주세요: ')), int(input('숫자2을 입력해주세요: ')), input('type을 입력해주세요.')))
