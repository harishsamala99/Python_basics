fib=[0,1]
n=10
for i in range(n-2):
    fib.append(fib[-1]+fib[-2])
print(','.join(str(e) for e in fib))


