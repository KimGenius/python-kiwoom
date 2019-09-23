import random

n = int(input('최솟값을 입력해주세요: '))
m = int(input('최댓값을 입력해주세요: '))

randNum = random.randrange(n, m + 1)  # m + 1을 하는 이유는 randrange 함수가 m - 1 까지만 가져오기 때문

print('입력하신 범위(' + str(n) + ' ~ ' + str(m) + ')내의 랜덤한 값이 정해졌습니다!')
# print(randNum)
answer = int(input('이제 값을 맞춰주세요 '))

x = randNum - answer
if x == 0:
    print('정답!')
else:
    print(str(x) + '만큼 차이가 났습니다')
