class Test1:
    a = 0

    def __init__(self, a):
        self.a = a
        print('클래스가 생성되었습니다.')
        print('a의 값은' + str(a))


test1 = Test1(10)
