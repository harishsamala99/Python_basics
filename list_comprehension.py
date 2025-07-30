#a=5
#table=[]
#for i in range(1,11):
 #   table.append(5*i)
table=[5*i for i in range(1,11)] #list comprehension this is the short version of the code in this format.
print(table)

squared=[x**2 for x in range(5)]
print(squared)