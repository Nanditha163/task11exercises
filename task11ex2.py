#Program to create range from 1-8 and using zip() merge list and range to create new list of tuples
listn=["Rain","Icecream","Happiness","Python","Technology","Forest","Maldives","Mountain"]
rangen=list(range(1, 8))
print("New list of tuples:")
print(list(zip(listn, rangen)))


#OUTPUT:
New list of tuples:
[('Rain', 1), ('Icecream', 2), ('Happiness', 3), ('Python', 4), ('Technology', 5), ('Forest', 6), ('Maldives', 7)]
