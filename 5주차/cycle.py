class cycle:
    wheel = 0
    speed = 5

    def __init__(self, wheel, speed):
        self.wheel = wheel
        self.speed = speed

    def run(self, sec):
        return self.speed * sec

    def getType(self):
        return (str(self.wheel) + '발 자전거')


one = cycle(1, 10)
print(one.run(5))
print(one.getType())
