#Program using filter(),filter even no.s so that only odd no.s are passed to new list
listn=[3,40,77,16,21,12,117,162,85,189]
def filtereven(num):
    if(num%2)!=0:
        return True
    else:
        return False
filterout=filter(filtereven,listn)
print("Passing odd no.s after filtering even no.s:")
print("Filtered seq is as:", list(filterout))

#OUTPUT:
Passing odd no.s after filtering even no.s:
Filtered seq is as: [3, 77, 21, 117, 85, 189]
