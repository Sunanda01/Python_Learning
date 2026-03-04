from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat
# product
l1=(1,2)
l2=(3,4)
print(list(product(l1,l2)))

# permutations
l3=(1,2,3)
print(list(permutations(l3,2)))
# combinations, combinations_with_replacement
print(list(combinations(l3,2)))
print(list(combinations_with_replacement(l3,2)))

# accumulate
l4=(1,2,3)
print(l4)
print(list(accumulate(l4)))

# groupby
l5=(1,2,3,4,5)
group_obj=groupby(l5,lambda x:x<3)
for key,val in group_obj:
    print(key,list(val))

# count
for i in count(10):
    print(i)
    if i == 20:
        break

# cycle
l5=(1,2,3,4,5)
for j in cycle(l5):
    print(j)
    if j==5:
        break

#repeat
for k in repeat(1,5):
    print(k)

# Main Categories of itertools Functions
# Infinite Iterators – Keep producing values endlessly.
# count(start=0, step=1) → Infinite counting.
# cycle(iterable) → Repeats an iterable forever.
# repeat(object, times=None) → Repeats a value.

# Iterators that Terminate – Stop after a certain point.
# accumulate(iterable, func=operator.add) → Running totals.
# chain(iter1, iter2, ...) → Concatenate iterables.
# compress(data, selectors) → Filter elements.
# dropwhile(predicate, iterable) → Drop until predicate is false.
# takewhile(predicate, iterable) → Take while predicate is true.
# filterfalse(predicate, iterable) → Opposite of filter().

# Combinatorics – Generate permutations, combinations, products.
# product(iterable, repeat) → Cartesian product.
# permutations(iterable, r) → All possible arrangements.
# combinations(iterable, r) → Unique combinations.
# combinations_with_replacement(iterable, r) → With repeats.