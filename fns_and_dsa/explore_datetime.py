# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    # Format: YYYY-MM-DD HH:MM:SS
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date(days_to_add):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    # Format: YYYY-MM-DD
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Date after {days_to_add} days will be: {formatted_future_date}")

def main():
    display_current_datetime()

    while True:
        user_input = input("Enter number of days to add to the current date: ").strip()
        if user_input.isdigit():
            days = int(user_input)
            calculate_future_date(days)
            break
        else:
            print("Invalid input. Please enter a valid integer number of days.")

if __name__ == "__main__":
    main()
