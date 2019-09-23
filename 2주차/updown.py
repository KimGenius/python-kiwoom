# 업 다운 게임
import random

n = int(input('최대값을 입력해주세요: '))
randValue = random.randrange(1, n)

userValue = int(input('랜덤값이 셋팅되었습니다. 정답을 맞춰주세요: '))
if randValue == userValue:
    print('Correct!')
elif randValue < userValue:
    print('Down!')
else:
    print('Up!')
