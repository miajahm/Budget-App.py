
# Wednsor Budget App 'Dashboard'

from datetime import datetime

# get the current hour
current_hour = datetime.now().hour

# determine the greeting
if 5 <= current_hour < 12:
    greeting = "Good morning"
elif 12 <= current_hour < 18:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"

def format_name(name):
    return " ".join(word.capitalize() for word in name.split())

user_name = input("Username:")
formatted_name = format_name(user_name)


print(f"{greeting}, {formatted_name}. Welcome to your dashboard!")

print("Enter your monthly income: $")
user_income = float(input())

expenses = [] # this is an empty list

while True:
    expense = float(input("Enter an expense: $"))
    expenses.append(expense)  # Add expense to list
    more_expenses = input("Do you have more expenses? y/n: ").lower() # Ask for more expenses
    if more_expenses != 'y':  # Exit loop if answer is not 'y'
     break

total_expenses = sum(expenses)
print()

