print(f"залишок від ділення це операція %. Наприклад 3%2 буде дорівнювати 1. Ось приклад {3%2}")
input1 = input("Введи int число: ")
try:
    num = int(input1)
    if num == 0:
        print(f"{num} - Це нуль!")

    elif num % 2 == 0:
        print(f"{num} - Це число чотне!")

    else:
        print(f"{num} - Це число нечотне!")

except:
    print(f"{input1} це не інт число")

print("Кінець!")
