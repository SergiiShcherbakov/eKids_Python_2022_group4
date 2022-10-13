print('\n\nIF statements')

car = 'toyota'

if car == 'bmw':
    print(car.upper())
else:
    print(car.title())

print('\n\nIF / ELIF statements')

car = 'honda'

if car == 'bmw':
    print(car.upper())
elif car == 'honda':
    print("It's Honda")
else:
    print(car.title())


print('\n\nNumerical Comparisons')
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

print('\n\nOther conditions')
age = 19
print('age < 21,  ' + str(age < 21))
print('age <= 21, ' + str(age <= 21))
print('age > 21, ' + str(age > 21))
print('age >= 21, ' + str(age >= 21))


print('\n\nUsing and to Check Multiple Conditions')
age_0 = 22
age_1 = 18
result = age_0 >= 21 and age_1 >= 21
print('age_0 >= 21 and age_1 >= 21, ' + str(result))
age_1 = 22
result = age_0 >= 21 and age_1 >= 21
print('age_0 >= 21 and age_1 >= 21, ' + str(age_0 >= 21 and age_1 >= 21))


print('\n\nUsing or to Check Multiple Conditions')
age_0 = 22
age_1 = 18
result = age_0 >= 21 or age_1 >= 21
print('age_0 >= 21 or age_1 >= 21, ' + str(result))
age_0 = 18
result = age_0 >= 21 or age_1 >= 21
print('age_0 >= 21 or age_1 >= 21, ' + str(result))


print('\n\n Boolean variable')
age = 6
print("age = 6")
test = age == 6
print(f"test = age == 6 -> test value is: {test}")
test = age > 6
print(f"test = age > 6 ->test value is: {test}")
test = age < 6
print(f"test = age < 6 ->test value is: {test}")
test = age <= 6
print(f"test = age <= 6 ->test value is: {test}")
test = age >= 6
print(f"test = age >= 6 ->test value is: {test}")
test = age != 6
print(f"test = age != 6 ->test value is: {test}")
print(type(test))
print(type(test) == bool)
