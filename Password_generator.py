# Password Generator
import random
import string

def list_of_pass():
    lowercase = list(string.ascii_lowercase)      
    uppercase = list(string.ascii_uppercase)     
    digits = list(string.digits)                  
    special_characters = list(string.punctuation) 
    lst = lowercase + uppercase + digits + special_characters
    return lst

def password(length):
    lst1 = list_of_pass()
    random.shuffle(lst1)            
    passcode = random.choices(lst1, k=length)  
    print("Your password: ", ''.join(passcode))  

print("WELCOME TO PASSWORD GENERATOR!")
length = int(input("Enter length of the password to be generated: "))
password(length)

while True:
    ch = input("Do you want any more passwords? (y/n): ")
    if ch == 'y' or ch == 'Y':
        length = int(input("Enter length of the password to be generated: "))
        password(length)
    else:
        print("THANK YOU!")
        break
