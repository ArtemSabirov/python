income = int(input("Введите размер выручки фирмы: "))
expenses = int(input("Введите размер издержек фирмы: "))
money = abs(income - expenses)
increase = income / expenses * 100

if income > expenses:
    print("Ваша фирма приносит доход в размере", money)
    print("Рентабельность Вашей фирмы составила", increase, "%")
    q_employees = int(input("Введите количество Ваших сотрудников: "))
    print("Прибыль на одного сотрудника составила", money / q_employees)
elif income == expenses:
    print("Вы не потеряли, но и не заработали")
else:
    print("Ваша фирма работает в убыток. Его размер составляет", money)
    print("Ваша фирма нерентабельна, соотношение прибыли к издержкам составляет -", increase, "%")