n = int(input('Enter Number for Fibonacci Series'))
first = 0
second = 1
print(first)
print(second)
for i in range(n-2):
    print(first + second)
    temp = first
    first = second
    second = temp + first
