import itertools
def tabulate(f, start=0, step=0):
	return map(f, itertools.count())
sqgen = tabulate(lambda x: x ** 2)
print(next(sqgen)) # => 0
print(next(sqgen)) # => 1
print(next(sqgen)) # => 2
print(next(sqgen)) # => 4
print(next(sqgen)) # => 9