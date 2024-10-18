def quad(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    return 0  # Точка на осях

frst = thrd = 0
while True:
    coords = input("Введите координаты точки (x, y) или 'выход' для выхода >> ")
    if coords.lower() == 'выход':
        break
    try:
        x, y = map(float, coords.split(','))
        got_quad = quad(x, y)
        if got_quad == 1:
                print("Точка находится в 1-м квадранте")
                frst += 1
        elif got_quad == 3:
                print("Точка находится в 3-м квадранте")
                thrd += 1
        else:
                print(f"Точка находится в {got_quad} квадранте или на осях")
    except ValueError:
            print("Ошибка при вводе. Пожалуйста, используйте формат 'x, y'")

print(f"\nКоличество точек в 1-м квадранте >> {frst}")
print(f"Количество точек в 3-м квадранте >> {thrd}")