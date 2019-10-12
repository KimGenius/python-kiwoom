def checkValue(value):
    if value == '가위' and value == '바위' or value == '보':
        print('정확한 값을 입력해주세요!')
    # if not (value == '가위' or value == '바위' or value == '보'):
    #     return print('정확한 값을 입력해주세요!')
    return print('정확한 값 입니다')


checkValue(input('가위, 바위, 보 중 하나를 입력해주세요: '))
