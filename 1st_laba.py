# Задание_1
def print_flag():
    height = 13
    width = 27
    circle_radius = 4
    circle_center_x = 11
    circle_center_y = 6

    for y in range(height):
        for x in range(width):
            if (x - circle_center_x) ** 2 + (y - circle_center_y) ** 2 <= circle_radius ** 2:
                print("\033[41m  ", end="")
            else:
                print("\033[42m  ", end="")
        print("\033[0m")

print('Флаг Бангладеша')
print_flag()

# Задание_2 (простите меня пожалуйста за этот кошмар)
def pattern(repeat_count):

    x = "████████"
    y = "█      █"
    z = "█    ███"
    w = "█    █"
    k = "█    █████"


    for _ in range(repeat_count):
        print(x)
        print(y)
        print(z)
        print(w)
        print(k)


repeat_count = 3
print('Узор')
pattern(repeat_count)

# Задание_3
def plot_function():
    height = 10
    width = 6

    graph = [[" " for _ in range(width)] for _ in range(height)]

    for x in range(width):
        y = 2 * x + 3
        if 0 <= y < height:
            graph[height - y - 1][x] = "*"

    print('График от функции y=2x+3')
    print("   y")
    for i in range(height):
        print(f"{height - i - 1:2} | " + " ".join(graph[i]) + " ")
    print("   " + "--" * (width * 2),'x')
    print("    " + "  ".join(str(i) for i in range(width)))

plot_function()


# Задание_4
with open('/Users/vikon/Documents/python_1sem/sequence.txt') as file:

    numbers = [float(line.strip()) for line in file if line.strip()]

first_125 = numbers[:125]
second_125 = numbers[125:250]

sum_first = sum(abs(num) for num in first_125)
sum_second = sum(abs(num) for num in second_125)

total = sum_first + sum_second
percentage_first = (sum_first / total) * 100 if total != 0 else 0
percentage_second = (sum_second / total) * 100 if total != 0 else 0

print(f"Сумма по модулю первых 125 чисел: {sum_first}")
print(f"Сумма по модулю вторых 125 чисел: {sum_second}")
print(f"Процентное соотношение:")
print(f"Первые 125 чисел: {percentage_first:.1f}%")
print(f"Вторые 125 чисел: {percentage_second:.1f}%")


