number = int(input('Enter a number'))
l = []


def max_divisor(arg):
    if arg == 1:
        l.append(arg)
        return 1
    if number % arg == 0:
        l.append(arg)
        print(l)
        max_divisor(arg-1)

max_divisor(number)
print(l)
