def new_elm(arr):
    res = []
    for i in arr:
        res.append(i)
        res.append(i)
    return res

n = int(input("Введите размер массива >> "))
arr = []
print("Введите значения:")  # Запрашиваем половину значений
for i in range(n // 2):
    el = input(f"Введите значение {i + 1} >> ")
    arr.append(el)

arry = new_elm(arr)

print("Результат:", arry)