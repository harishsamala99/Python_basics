age=int(input("enter your age:"))
if(age>18):
    print("you can drive")
elif(age==18):
    print("schedule and interview")
elif(age<18):
    print("you cant even ask this question")
else:
    print('you cant drive')
    
print("end of program")



age=int(input("Show me your ID: "))
if age==21:
    print("You are elgible to buy anything in the store")
elif age==18:
    print("You can get in but can't buy anything")
else:
    print("Wait until you turn 21")
    