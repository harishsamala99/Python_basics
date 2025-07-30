#for i in range(1,6):# range function goes from 1 to 5.
#   print(i)
 
#for i in range(1,11):
 #    print("5 x",i, "=", 5*(i))
  
  
for i in range(1,30):
    
        print(i)
        if i==10:
            break
       
       
for i in range(1,100):
    print(i)
    if i==10:
        break
    
    rows = 10

rows=5
for i in range(1, rows+1):
    # Print spaces between the double colon makes the pyramid, else it gives line by line.
    print(" " * (rows-i), end="")
    print("*"* (2*i-1))
    