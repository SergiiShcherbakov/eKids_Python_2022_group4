# # For example
print("------ For example-------")
numbers = [0,1,2,3,4,5]
i = 1

for num in numbers:
    i = i + 1
    print(f"i дорівнює {i}")
    if num == 0:
        print(f"{num} - Це нуль!")

    elif num % 2 == 0:
        print(f"{num} - Це число парне!")

    else:
        print(f"{num} - Це число непарне!")


# # # While example  ------------------------------------------------------
# print("\n\n------ While example-------")
# numbers = [7,5,2,1,4,13]
# i = 0
#
# while i < len(numbers):
#     print(f"i = {i}, len(numbers) = {len(numbers)}, numbers[i] = {numbers[i]}")
#     i = i + 1




# # Break example  ------------------------------------------------------
# print("\n\n------Break example-------")
# print("пошукаємо мої помилки!")
# numbers = [0,1,2,3,4,5]
# i = 1
#
# while i > len(numbers):
#     print(f"i = {i}, numbers[i] = {numbers[i]}, len(numbers) = {len(numbers)}")
#     if i > 3:
#         break
#     i = i + 1





# # continue example ------------------------------------------------------
# print("\n\n------continue example-------")
# print("пошукаємо мої помилки!")
# numbers = [0,1,2,3,4,5]
# i = 1
#
# while i < len(numbers):
#     if i % 2 == 0:
#         print("continue - відпрацювало!!!! Це досить часто може призвести до проблем!!!!")
#         continue
#     print(f"i = {i}, numbers[i] = {numbers[i]}, len(numbers) = {len(numbers)}")
#     i = i + 1




# # # while else example ------------------------------------------------------
# print("\n\n------while else example-------")
# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("зараз і < 6")




# # range example ------------------------------------------------------
# print("\n\n------range example-------")
# for index in range(50, 100, 10):
#     print(index)
#
# print("Теж саме що:")
# index = 50
# while index < 100:
#     print(index)
#     index = index + 10
