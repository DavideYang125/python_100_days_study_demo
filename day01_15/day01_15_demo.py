# s1 = r'\'hello, world!\''
# s2 = r'\n\\hello, world!\\\n'
# print(s1, s2, end='')

# s1 = '\'hello, world!\''
# s2 = '\n\\hello, world!\\\n'
# print(s1, s2, end='')
# s4 = 'hello python. ' * 2
# print(s4)
# print('he2'in s4)


#a, b = 5, 10
# print('{0} * {1} = {2}'.format(a, b, a * b))
#print(f'{a}*{b}={a*b}')

firstList=['hello','world']
fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
# 列表切片
fruits2 = fruits[1:4]
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)
set1 = {1, 2, 3, 3, 3, 2}
print(set1)