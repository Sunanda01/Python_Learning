Set1={6,4,9,0,1,1,4}
Set2={3,9,7,5,5,1,0}
Set3={'A','B','C','D'}
s={4,9,0}

#Subset , Superset , Disjoint
print(f"{s} ⊆ {Set1} => {s.issubset(Set1)}")
print(f"{Set3} <= [ 'A','B','C','D','E'] => {Set3<=set([ 'A','B','C','D','E'])}")
print(f"{Set1} ⊇ {s} => {Set1.issuperset(s)}")
print(f"[ 'A','B','C','D','E'] >= {Set3} => {set([ 'A','B','C','D','E'])>=Set3}")
print(f"{Set1} isdisjoint {Set3} => {Set1.isdisjoint(Set3)}")

#Union
Union=Set1.union(Set2,Set3)
print(f"{Set1} ∪ {Set2} =>\t {Union}")
print(f"{Set1} ∪ {Set2} =>\t {Set1 | Set2}")

#Intersection
Intersection=Set1.intersection(Set2,s)
print(f"{Set1} ∩ {Set2} ∩ {s} =>\t {Intersection}")
print(f"{s} ∩ {Set1} =>\t {s & Set1}")

#Difference
Diff=Set1.difference(Set2,s)
print(f"{Set1} - {Set2} - {s} =>\t {Diff}")
print(f"{Set1} - {Set2} =>\t {Set1-Set2}")

#Symmetric Diffrence
Diff=Set1.symmetric_difference(Set2)
print(f"{Set1} symmetric_difference {Set2}  =>\t {Diff}")
print(f"{Set1} ^ {Set2} ^ {s} =>\t {Set1^Set2^s}")

#update
Set1.update(Set3)
print(Set1)

Set1 |= set(['a','b','c'])
print(Set1)

#IntersectionUpdate
print(f"{Set1}.intersection_update({Set2}) => ")
Set1.intersection_update(Set2)
print(Set1)

#clear Set
s.clear()
print(s)

#del set
del s
print(s)