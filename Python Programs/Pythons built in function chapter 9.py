print(abs(10))
print(abs(-10))
print(abs(3))
print(abs(-3))
steps = -3
if abs(steps) > 0:
    print('Character is moving')
steps = -9
if abs(steps) > 0:
    print('I go to Gibson Ek High School')
steps = -3
if steps < 0 and steps > 0:
    print('Character is moving')
steps = 0
if steps < 0 and steps > 0:
    print('I like cross country and track and field')

print(bool(0))
print(bool(1))
print(bool(1123.23))
print(bool(-500))
print(bool(90))
print(bool(138))
print(bool(20))
print(bool(None))
print(bool('a'))
print(bool('hi'))
print(bool('b'))
print(bool(' '))
print(bool('What do you call a pig doing karate? Pork Chop!'))
my_silly_list = []
print(bool(my_silly_list))
my_silly_list = ['s', 'i', 'l', 'l', 'y']
print(bool(my_silly_list))
year = input('year of birth: ')
if not bool(year.rstrip()):
    print('you need to enter a value for your year of birth')

dir(['a', 'short', 'list'])
passcode = input('enter passcode: ')
if not bool(passcode.rstrip()):
    print('you need to enter your passcode')
dir(1)
popcorn = 'I love popcorn!'
dir(popcorn)
help(popcorn.upper)
eval('10*5')
your_calculation = input('enter a calculation: ')
eval(your_calculation)

andy_calculation = input('Enter a calculation: ')
my_small_program = '''print('ham')
print('sandwhich')'''
exec(my_small_program)
float('12')
float('123.456789')
your_age = input('Enter your age: ')
age = float(your_age)
if age > 14:
    print('you are %s years too old' % (age - 14))
int(123.456)
int('123')
len('this is a test string')
