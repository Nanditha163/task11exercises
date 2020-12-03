#Program using zip() and list() and create merged list of tuples from 2 lists
list1=[10,"abc",1000]
list2=[20,"xyz",2000]
print("Merged list of tuples from 2 lists:")
print(list(zip(list1,list2)))

#OUTPUT:
Merged list of tuples from 2 lists:
[(10, 20), ('abc', 'xyz'), (1000, 2000)]

