for i in range(0,20):
    print(i)
    if i==10:
        break # stops the execution of the loop at what number you mentioned.
    


vowel=['a','e','i','o','u']
words= "harish"
count=0 # it checks how many words are in vowel
for character in words:
    if character in vowel: #checks if there any character in vowels
        count+=1 #increases the count whenever a vowel is found.
print(count)
    