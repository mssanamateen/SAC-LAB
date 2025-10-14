'''A set is a collection which is unordered, unindexed, and contains only
unique elements.
Mutability:
The set itself is mutable — you can add or remove elements.
'''
# Creating two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union
print("Union:", set1 | set2)

# Intersection
print("Intersection:", set1 & set2)

# Difference (elements in set1 not in set2)
print("Difference (set1 - set2):", set1 - set2)

# Symmetric Difference (elements in either set but not both)
print("Symmetric Difference:", set1 ^ set2)

'''Union: {1, 2, 3, 4, 5, 6, 7, 8}
Intersection: {4, 5}
Difference (set1 - set2): {1, 2, 3}
Symmetric Difference: {1, 2, 3, 6, 7, 8}
'''
