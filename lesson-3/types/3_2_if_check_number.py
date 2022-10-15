input1 = input("Введи int число: ")

try:
    num = int(input1)
    if num > 100:
        print("Чісло більше ста")

    elif num > 50:
        print("Чісло більше пятидесяти")

    elif num > 25:
        print("Чісло більше двадцяти пяти")

    else:
        print("Чісло меньше двадцяти пяти")

except:
    print(f"{input1} це не інт число")

print("Кінець!")
