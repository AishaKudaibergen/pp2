# Implement a generator that returns all numbers from (n) down to 0.
def down(n):
    value = n
    while value >= 0:
        yield value
        value -= 1

n = int(input())
for i in down(n):
    print(i, end = " ")