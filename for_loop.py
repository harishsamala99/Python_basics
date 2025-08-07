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
    
    
    
for i in range(0,15):
    if i==8:
        continue # or continue  #the difference between the continue and break is when using continue it Skip printing 8 because of the continue statement and starts from next number and using break statement it stops the loop at 7.
        # if you mention (0,15) starts at 1 and stops at 14.
    print(i)
    
    
for a in range(2):
    for b in range(4):
        print(a,b)
        
    # so for every value of a in range(2) (0 to 1), it loops through b in range(4) (0 to 4).
    