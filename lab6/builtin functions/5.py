#Write a Python program with builtin function that returns True if all elements of the tuple are true.
def all_true(t):
    return all(t)

values = tuple(map(int, input("input: ").split()))

print("output:", all_true(values))
