cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print('\n\nConditional tests')
print(cars[0] == 'bmw')
print(cars[0] == 'audi')


print('\n\nConditional tests ignoring tests')
print(cars[0] == 'AUDI')
print(cars[0] == 'AUDI'.lower())


print('\n\nChecking for Inequality')
print(cars[0] != 'audi')
print(cars[0] != 'bmw')


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
print('age_0 >= 21 and age_1 >= 21, ' + str(age_0 >= 21 and age_1 >= 21))
age_1 = 22
print('age_0 >= 21 and age_1 >= 21, ' + str(age_0 >= 21 and age_1 >= 21))

print('\n\nUsing and to Check Multiple Conditions, more readable')
age_0 = 22
age_1 = 18
print('(age_0 >= 21) and (age_1 >= 21), ' + str((age_0 >= 21) and (age_1 >= 21)))
age_1 = 22
print('(age_0 >= 21) and (age_1 >= 21), ' + str((age_0 >= 21) and (age_1 >= 21)))


print('\n\nUsing or to Check Multiple Conditions')
age_0 = 22
age_1 = 18
result = age_0 >= 21 or age_1 >= 21
print('age_0 >= 21 or age_1 >= 21, ' + str(result))
age_0 = 18
result = age_0 >= 21 or age_1 >= 21
print('age_0 >= 21 or age_1 >= 21, ' + str(result))


print('\n\nChecking Whether a Value Is in a List')
requested_toppings = ['mushrooms', 'onions', 'pineapple']
result = 'mushrooms' in requested_toppings
print('contains "mushrooms",' + str(result))
result = 'pepperoni' in requested_toppings
print('contains "pepperoni",' + str(result))


print('\n\nChecking Whether a Value Is Not in a List')
requested_toppings = ['mushrooms', 'onions', 'pineapple']
result = 'mushrooms' not in requested_toppings
print('does not contain "mushrooms",' + str(result))
result = 'pepperoni' not in requested_toppings
print('does not contain "pepperoni",' + str(result))


print('\n\nBoolean Expressions')
true_value = True
false_value = False

print(true_value)
print(false_value)



print('\n\nif Statements')
true_value = True
false_value = False

if true_value:
    print(':)')

if false_value:
    print(':(')


print('\n\nother examples')
age = 14
if age >= 10:
    print('You are older than 10')


print('\n\nif-else Statements')
age = 14
if age >= 18:
    print('You are older than 18')
else:
    print('You younger than 18')


print('\n\nThe if-elif-else Chain')
age = 14
if age >= 18:
    print('You are older than 18')
elif age == 12:
    print("You are 12")
elif age == 14:
    print("You are 14")
else:
    print('You younger than 18')


print('\n\nconditional with lists:\n')
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")
