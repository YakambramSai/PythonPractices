tuple = ('ansible', 1111, 89.67, 'GIT', 'Aws')
list = ['ansible', 1111, 89.67, 'GIT', 'Aws']
# update tuple with index number
# tuple(3) = "Hello"  # invalid syntax with tuple   can't assign to function call
tuple[3] = "Hello"  # invalid syntax with tuple tuple' object does not support item assignment
list[3] = "Hello"  # valid syntax fwith list

