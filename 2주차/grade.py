# 점수 측정 프로그램
grade = int(input('점수를 입력해주세요: '))

if grade > 100 or grade < 0:
    print('올바른 점수를 입력해주세요.')
elif grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
elif grade >= 50:
    print('E')
else:
    print('측정불가')
