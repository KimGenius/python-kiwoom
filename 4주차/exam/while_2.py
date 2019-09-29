total = 0
count = 0
while True:
    grade = input('점수를 입력해주세요: ')
    if grade == 'exit':
        break
    total += int(grade)
    count += 1

print('평균은 : ', total / count)
