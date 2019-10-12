import time


def countDown(sec):
    print(sec)
    time.sleep(1)
    if sec == 0:
        return print('땡!')
    return countDown(sec - 1)


sec = int(input('몇 초로 하실건가요?'))
print(str(sec) + '초간 스탑워치 작동합니다.')
countDown(sec)
