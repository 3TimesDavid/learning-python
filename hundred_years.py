from datetime import date

name = input("Enter name: ")
age = int(input("Enter age or birth year: "))

user_rest_age = 100 - age
current_date = date.today()
current_year = current_date.year

if age == 0:
    print(f"Hi, you indicated 0. In case the baby is not 1 year yet, try to indicate for example 0,5 if he is 6 mounth.")

elif age == 100:
    print(f"Hi {name}, congratulations! You are already 100 years old!")

elif age <= 100:
    print(f"Hi {name}, you will be 100 years old in {current_year + user_rest_age}.")

elif age >= 100:
    print(f"Hi {name} you already passed 100 years, that is incredible! Congratulations!.")

elif age >= 1800:
    print(f"Hi {name}, you will be 100 years old in {age + 100}.")

else:
    print("Not valid input. Try again.")






