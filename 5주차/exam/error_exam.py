# price = input('물건의 가격을 입력하세요:')
# money = input('건네받은 돈을 입력하세요:')
price = int(input('물건의 가격을 입력하세요:'))
money = int(input('건네받은 돈을 입력하세요:'))

change = money - price
resultList = []

for i in [10000, 1000, 100, 10, 1]:
    result = money // i
    resultList.append(result)
    money = money - result * i
# print(resultList
print(resultList)
