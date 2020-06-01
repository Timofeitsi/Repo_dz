rating = [7, 5, 3, 3, 2]
a = input("Введите число - ")
for i in range(len(rating), 0, -1):
    if int(a) > rating[0]:
        rating.insert(0, int(a))
        break
    else:
        if int(a) <= rating[i-1]:
            rating.insert(i, int(a))
            break

print("Пользователь ввел число -", a, " Результат:", (rating))