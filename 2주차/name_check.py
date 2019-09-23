# 이름 길이
name = input('이름을 입력해주세요: ')
nameLen = len(name)
if nameLen < 2 or nameLen > 5:
    print('이름으로 쓰기엔 조금 힘들지 않을까요?')
else:
    print('이름으로 쓰기 좋네요')
