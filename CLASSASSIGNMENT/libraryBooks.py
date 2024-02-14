# a program to calculate the fine for overdue library book
from datetime import datetime

def calculate_days(days_overdue):
    if days_overdue == 7:
        charge_per_day = 20
        print(charge_per_day)
    elif days_overdue >= 8 and days_overdue <= 14:
        charge_per_day = 50
        print(charge_per_day)
    elif days_overdue >= 15:
        charge_per_day = 100
        print(charge_per_day)
    return charge_per_day * days_overdue

# Input return date and due date
return_date_str = input("Enter the return date (YYYY-MM-DD): ")
due_date_str = input("Enter the due date (YYYY-MM-DD): ")
book_ID = int(input("Enter the book ID :"))
# Convert input strings to datetime objects
return_date = datetime.strptime(return_date_str, "%Y-%m-%d")
due_date = datetime.strptime(due_date_str, "%Y-%m-%d")

days_overdue = (return_date - due_date).days
fine = days_overdue * calculate_days(days_overdue)

print(f"The fine for the overdue book is: ${fine:.2f}")