# This contains all kinds of iterators provided by itertools
import itertools
import operator

l1 = [1, 2, 3]

# accumulate(list, function) function of itertools --> function is performed to the list items
print(list(itertools.accumulate(l1, operator.mul)))


l2 = [4, 5, 6]

# chain(iter1, iter2, iter3...) function of itertools --> function is performed to chain different lists
l3  = list(itertools.chain(l1, l2))
print(l3)

# chain.from_iterable(list) --> same as chain function but takes list of lists or othen iterable container
l4 = [l1, l2]
print(list(itertools.chain.from_iterable(l4)))

# compress(list, selector) --> This function takes selector  which is boolean list 
print(list(itertools.compress(l3, [1, 1, 1, 0, 0, 0])))

#  dropwhile(function, list) --> The function prints all values from the first time the list item return false corresonding to the fucntion applied.
l5 = [2, 4, 5, 6, 7]
print(list(itertools.dropwhile(lambda x: x % 2 == 0, l5)))

# filterfalse(function, list) --> The function prints values of list which returns false corresponding to applied function.
print(list(itertools.filterfalse(lambda x: x % 2 == 0, l5)))