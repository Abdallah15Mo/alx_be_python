# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    # Format: YYYY-MM-DD HH:MM:SS
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_date

def calculate_future_date(days_to_add):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    # Format: YYYY-MM-DD
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    return formatted_future_date

def main():
    current_datetime_str = display_current_datetime()
    print(f"Current date and time: {current_datetime_str}")

    while True:
        user_input = input("Enter the number of days to add to the current date: ").strip()
        if user_input.isdigit():
            days = int(user_input)
            future_date_str = calculate_future_date(days)
            print(f"Date after {days} days will be: {future_date_str}")
            break
        else:
            print("Invalid input. Please enter a valid integer number of days.")

if __name__ == "__main__":
    main()
