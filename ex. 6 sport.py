distance_1day = int(input("Введите начальную дистанцию, км: "))
distance_result = int(input("Введите ожидаемую ежедневную дистанцию, км/ч: "))
day = 1

while distance_1day < distance_result:
    distance_1day = (distance_1day / 100 * 10) + distance_1day
    day += 1
else:
    print(day)