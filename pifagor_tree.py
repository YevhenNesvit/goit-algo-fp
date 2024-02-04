import turtle


def draw_pifagor_tree(branch_length, recursion_level):
    if recursion_level == 0:
        return
    else:
        # Рисуємо гілку
        turtle.forward(branch_length)
        turtle.left(45)

        # Рекурсивно рисуємо праву частину дерева
        draw_pifagor_tree(0.6 * branch_length, recursion_level - 1)

        # Повертаємося на початковий кут
        turtle.right(90)

        # Рекурсивно рисуємо ліву частину дерева
        draw_pifagor_tree(0.6 * branch_length, recursion_level - 1)

        # Повертаємося на початковий кут
        turtle.left(45)
        turtle.backward(branch_length)


# Введення рівня рекурсії від користувача
recursion_level = int(input("Введіть рівень рекурсії: "))

# Налаштування вікна для візуалізації
turtle.speed(2)
turtle.left(90)
turtle.up()
turtle.backward(100)
turtle.down()

# Виклик функції для малювання дерева Піфагора
draw_pifagor_tree(100, recursion_level)

# Закриваємо вікно при кліку
turtle.exitonclick()
