# consider itertools for working with iterators and generators
#

import itertools

# linking iterators together
#
it = itertools.chain([1, 2, 3], [4, 5, 6])

print(list(it))


# repeat

it = itertools.repeat("hello", 3)

print(list(it))


# cycle
it = itertools.cycle([1, 2])
result = [next(it) for _ in range(10)]

print(result)


# tee
#
it1, it2, it3 = itertools.tee(["first", "second"], 3)
print(list(it1))
print(list(it2))
print(list(it3))


# product
single = itertools.product([1, 2], repeat=2)
print("Single: ", list(single))

multiple = itertools.product([1, 2], ["a", "b"])
print("Multiple: ", list(multiple))


# permuiations
#
it = itertools.permutations([1, 2, 3, 4], 2)
print("permutation list", list(it))


it = itertools.combinations([1, 2, 3, 4], 2)
print("combination list", list(it))
