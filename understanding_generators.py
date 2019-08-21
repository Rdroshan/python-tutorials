
# A generator function returns a generator object which can be used 
# directly in the 'for in ' loop or using next() on them.	
def multiple(number, maximum):
	counter = 1

	while counter <= maximum:
		# yield is similar to return but instead of exiting it pauses the execution
		# until next value is required.
		yield number * counter
		counter += 1



for num in multiple(5, 10):
	print(num)

# GENERATOR COMPREHENSIONS OR GENERATOR EXPRESSIONS
# as similar to list comprehensions
# like [i**2 for i in list]

# How to make a generator which takes value?
