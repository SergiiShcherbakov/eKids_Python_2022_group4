# range
# https://docs.python.org/3/library/stdtypes.html#ranges
# https://www.w3schools.com/python/ref_func_range.asp
segments = ['a', 'b', 'c', 'd']

# len() = length

# for index in range(1, 10, 1):
#     print('index: ' + str(index))


print("=======    1    =========")
#  start -> len(segments) - 1
#  end -> 0
#  step -> -1
range_list = range(len(segments) - 1, 0, -1)

print('segments:' + str(segments))
print('range_list:' + str(range_list))

for index in range_list:
    print('index: ' + str(index) + '  , letter :' + segments[index])

print("=======    2    =========")
#  start -> 0
#  end -> len(segments) - 1
#  step -> 1
for index in range(0, len(segments) - 1, 1):
    print('index: ' + str(index) + '  , letter :' + segments[index])
