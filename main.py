from datetime import datetime

# Input start date and current date with error handling
while True:
    try:
        start_date_input = input("Enter the start date (YYYY-MM-DD): ")
        start_date = datetime.strptime(start_date_input, "%Y-%m-%d")
        break  # Exit the loop if the input is valid
    except ValueError:
        print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")

while True:
    try:
        end_date_input = input("Enter the end date (YYYY-MM-DD): ")
        end_date = datetime.strptime(end_date_input, "%Y-%m-%d")
        break  # Exit the loop if the input is valid
    except ValueError:
        print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")

# Calculate the total experience
if end_date >= start_date:
    total_days = (end_date - start_date).days
    total_years = total_days // 365
    total_months = (total_days % 365) // 30
    total_days = total_days % 30
else:
    print("End date cannot be before the start date.")
    exit(1)

# Output the total experience
print(f"Total Professional Experience: {total_years} years, {total_months} months, and {total_days} days.")
