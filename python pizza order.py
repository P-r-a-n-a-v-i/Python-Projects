print("Welcome to Python Pizza Deliveries!")
pizza_size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
if pizza_size == "L" :
   bill += 12
   print("you have to pay 12$")
elif pizza_size == "M" :
  bill += 10
  print("you have to pay 10$")
elif pizza_size == "S":
  bill += 5
  print(" you have to pay 5$")
else:
  bill += 0  
if pepperoni == "Y":
    if pizza_size == "S":
       bill += 4
    else:
       bill += 6

if extra_cheese == "Y":
    bill += 2
print(f"your total bill is : ${bill} ")



     

