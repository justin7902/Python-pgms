dict1 = {2:"orange",3: "banana",1: "grape"}
print(f"Dictionary 1: {dict1}")
l = list(dict1.items())
l.sort()
print("Asceding order is:", l)
l = list(dict1.items())
l.sort(reverse=True)
print("Descending Order is:",l)
dict2 = {4:"Plum",5:"Cherry"}
print(f"Dictonary 2: {dict2}" )
dict1.update(dict2)
print(f"Dictonary after merging:{dict1}")
