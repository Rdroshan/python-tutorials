# Class multiple

class Multiple:
	def __init__(self, number, maximum):
		self.number = number
		self.maximum = maximum
		self.counter = 0

#	To create the class as iterable define __iter__ method.
	def __iter__(self):
		return self

#	To iterate over the elements of the iterator
	def __next__(self):
		self.counter += 1

		if self.counter > self.maximum:
			raise StopIteration
		else:
			return self.number * self.counter

m = Multiple(5, 10)

print(next(m))
print(next(m))
print(next(m))

# I can't call this because the object is not iterable
# To make it iterable we need to create a method named __iter__ which returns an iterator..
# Either it's own object or other object
# iter(m)


# A for loop requires a iterable object which it converts to iterator and performs next method on them.
for it in m:
	print(it)

