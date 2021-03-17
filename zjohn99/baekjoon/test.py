import itertools

# arr = [0,1,2,3,0,1,2,3]

# a = itertools.permutations(arr,3)
# itertools.permutations

arr = [0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3]
a = itertools.permutations(arr,5)
a = set(a)
print(list(a))