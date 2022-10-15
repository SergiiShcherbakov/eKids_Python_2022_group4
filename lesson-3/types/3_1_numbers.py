count = 2 + 3
print('2+3=' + str(count))

count = 3 - 2
print('3-2=' + str(count))
count = 2 * 3
print('2*3=' + str(count))
count = 3 / 2
print('3/2=' + str(count))
count = 3 ** 2
print('3**2=' + str(count))
count = (2 + 3) * 4
print('(2+3)*4=' + str(count))

message = "\n\ntry floats"
print(message.upper())
floatResult = 0.1 + 0.1
print('0.1 + 0.1 =' + str(floatResult))
floatResult = 0.2 - 0.1
print('0.2 - 0.1 =' + str(floatResult))
floatResult = 2 * 0.1
print('2 * 0.1 =' + str(floatResult))
floatResult = 0.2 + 0.1
print('some interesting result')
print('0.2 + 0.1 =' + str(floatResult))
floatResult = 3 * 0.1
print('3 * 0.1 =' + str(floatResult))

print("3 * 0.1 == 0.3 " + str(3 * 0.1 == 0.3))
print("int(3 * 0.1 * 10 == 3) " + str(int(3 * 0.1 * 10) == 3))


print('\n\n Underscores in Numbers')
long_number = 3_000_000 * 300_000
print('3_000_000 * 300_000 =' + str(long_number))
print(f'{long_number:,}')
