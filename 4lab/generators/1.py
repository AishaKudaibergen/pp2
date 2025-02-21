# Create a generator that generates the squares of numbers up to some number N.
def generate_squares(n):
    value = 1
    while value<=n:
        yield value**2
        value += 1

n = int(input())
it = iter(generate_squares(n))
for i in range(n):
    print(next(it), end= " ")