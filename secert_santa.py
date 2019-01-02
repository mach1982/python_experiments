import random

secert_user=[]
secert_santa=[]
name=''

#welcome message
print( "\t\t\t\tWelcome to Secert Sanat Generator\n")
print("Enter the person name or done when finished")


# ask the user  to enter in a name appen to list 

while name !='done':
    name= input("Enter name : ")
    secert_user.append(name.title())
    print("\n")

#del the last element as it will always be the word 'Done'
del secert_user[-1]
#make a copy of the list 
secert_santa= secert_user.copy()

#loop throug the two list print out a randon element from the copy of the list 
for  su in secert_user:
    santa=secert_santa[random.randint(0,len(secert_santa)-1)]
  
    print(f"{santa} is {su}'s secert santa")
    secert_santa.remove(santa)






