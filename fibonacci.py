fib=[0,1]
n=10
for i in range(n-1):
    fib.append(fib[-1]+fib[-2])
print(','.join(str(a) for a in fib))
# or print(fib)
#using".join" makes the the numbers seperated by comas and ".join" can only works with strings which makes it more readable.


