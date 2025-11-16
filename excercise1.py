Introduction:

This program calculates a person's age using a fixed birthdate without requiring user input. It also converts the given date into European (dd/mm/yyyy) format.

from datetime import datetime

def calculate_age_no_input():
    try:
        # Set birth date directly here (mm/dd/yyyy)
        birth_input = "07/14/2003"   # ← Change this value as needed

        # Validate and convert to date object
        try:
            birth_date = datetime.strptime(birth_input, "%m/%d/%Y")
        except ValueError:
            print(" Invalid date format! Please use mm/dd/yyyy and ensure it's a real date.")
            return

        # Calculate age
        today = datetime.today()
        age = today.year - birth_date.year

        # Adjust if birthday hasn't happened yet this year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        print(f" Your current age is: {age} years")

        # Convert to European format (dd/mm/yyyy)
        euro_format = birth_date.strftime("%d/%m/%Y")
        print(f" Birth date in European format: {euro_format}")

    except Exception as e:
        print("⚠ Unexpected error:", e)


# Run the program
calculate_age_no_input()

Conclusion:

The program successfully determines the current age and displays the birthdate in another format, making age calculation simple and error-free.