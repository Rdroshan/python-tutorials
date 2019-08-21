def double_out(old_function):
	def new_function(a,b):
		return 2*a*b
	return new_function

# Decorators --> Allows you to make simple modifications

@double_out
def multiply(a,b):
	return a*b

# The decorator double_out evaluates to --
# multiply = double_out(multiply)
# print(multiply(5,4))
# We have made a simple change to the multiply function that it will double
# the multiplication of two numbers	
print(d(2,3))