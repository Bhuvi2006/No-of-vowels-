#Number of vowels
paragraph=input("Enter your text//paragraph: ")
count=0
for i in paragraph:
    if(i=='a' or i=="e" or i=="i" or i=="o" or i=="u"):
        count+=1
print("The number of vowels are:",count)
