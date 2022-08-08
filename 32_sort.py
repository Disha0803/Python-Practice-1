from audioop import reverse


str=input("Enter a string: ")
str=str.lower()
asc=list(str)
astr=''.join(sorted(asc))
dstr=''.join(sorted(asc,reverse=True))
print("In ascending order: ",astr)
print("In descending order: ",dstr)