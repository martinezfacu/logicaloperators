print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("Well, you can ride :D ")
else:
  print("Oh sorry, you can't ride D: ")
  
age = int(input("What is your age? "))

if age < 12:
  bill += 3
  print(f"Child tickets costs ${bill+3}")
elif age <= 18:
  bill =+ 7
  print(f"Teenagers tickets ${bill}")
elif age > 18 and age < 45 :
  bill += 12
  print(f"Adult tickets ${bill}")
if age >= 45 and age <= 55:
  bill += 0
  print("The tickets are free.")
  
photos = str(input("Do you want photos? Yes or No. "))
bill += 1
if photos == "Yes":
  print(f"Okay, the final price is ${bill}")
else:
  print(f"Okay, the final price is ${bill}")
