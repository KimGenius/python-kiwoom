# 가위바위보 게임
import random

randValue = random.randrange(1, 4)
userValue = input('가위, 바위, 보 중에 하나를 입력해주세요: ')
if userValue in ['가위', '바위', '보']:
    if userValue == '가위':
        userValue = 1
    elif userValue == '바위':
        userValue = 2
    elif userValue == '보':
        userValue = 3

    if randValue == userValue:
        print('무승부')
    elif randValue == 1 and userValue == 2 or randValue == 2 and userValue == 3 or randValue == 3 and userValue == 1:
        print('승리')
    else:
        print('패배')
else:
    print('정확한 값을 입력해주세요.')
