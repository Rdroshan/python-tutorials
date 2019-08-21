#def myFun(*argv):
#	for arg in argv:
#		print(arg)

#myFun('Hello', 'world', 'looking', 'into', 'asdfa')

# def myFun(**kwargs):
# 	for key, value in kwargs.items():
# 		print("%s == %s" %(key, value))

# myFun(first='roshan', last='dawande')

class Dog:
	def __init__(self, name, age):
		self.name = name
		self.age = age


a = Dog('chia', 5)
b = Dog('cherry', 2)
c = Dog('jainny', 10)


def get_biggest_number(*args):
	max = 0
	for age in args:
		if max < age:
			max = age
	return max

print(get_biggest_number(a.age, b.age, c.age))

