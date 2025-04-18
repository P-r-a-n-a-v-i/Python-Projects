import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("welcome to password generator")
no_letters = int(input("how many letters do you want in password? "))
no_numbers = int(input("how many numbers do you want in password? "))
no_symbols = int(input("how many symbols do you want in password? "))

password_l = []
for char in range(0,no_letters):
   password_l.append(random.choice(letters))
for char in range(0,no_numbers):
   password_l.append(random.choice(numbers))
for char in range(0,no_symbols):
   password_l.append(random.choice(symbols))   

print(password_l)
random.shuffle(password_l)
print(password_l)

password = ""
for char in password_l:
  password += char
print(password)  
