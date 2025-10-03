
# Input monthly rent, utilities, internet, and number of roommates.
# Shows a monthly breakdown of total rent.
# Calculates per-person share (fair split).
# Includes a daily breakdown for better financial planning.
# Number of persons sharing the room

import calendar
import datetime

# Colors for terminal output
def green(text): return f"\033[92m{text}\033[0m"
def red(text): return f"\033[91m{text}\033[0m"
def yellow(text): return f"\033[93m{text}\033[0m"
def blue(text): return f"\033[94m{text}\033[0m"

def rent_calculator():
    print(blue("\n=== RENT CALCULATOR ==="))

    # Get inputs
    rent_amount = float(input("Enter your monthly rent amount: $"))
    roommates = int(input("Enter number of roommates (including you): "))

    utilities = float(input("Enter total utilities (water, electricity, etc.): $"))
    internet = float(input("Enter internet bill amount: $"))

    total_expense = rent_amount + utilities + internet
    per_person = total_expense / roommates

    print("\n" + yellow("------ Monthly Rent Breakdown ------"))
    print(f"Base Rent: {green(f'${rent_amount:.2f}')}")
    print(f"Utilities: {green(f'${utilities:.2f}')}")
    print(f"Internet: {green(f'${internet:.2f}')}")
    print(f"Total Rent + Bills: {green(f'${total_expense:.2f}')}")

    print("\n" + yellow("------ Per Person Share ------"))
    print(f"Each of the {roommates} roommates pays: {green(f'${per_person:.2f}')}")

    # Extra feature → Daily breakdown
    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    daily_rent = total_expense / days_in_month

    print("\n" + yellow("------ Daily Rent Breakdown ------"))
    print(f"Rent per day for the household: {blue(f'${daily_rent:.2f}')}")
    print(f"Rent per day per person: {blue(f'${daily_rent/roommates:.2f}')}")

    print(red("\nCalculation complete. Don't forget to pay on time!"))


if __name__ == "__main__":
    rent_calculator()