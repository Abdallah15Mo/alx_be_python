def main():
    # Prompt for user input
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Process task based on priority using match-case
    match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a high priority task"
        case "medium":
            reminder = f"Reminder: '{task}' is a medium priority task"
        case "low":
            reminder = f"Note: '{task}' is a low priority task"
        case _:
            print("Invalid priority entered. Please choose from high, medium, or low.")
            return

    # Append message based on time sensitivity
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    elif time_bound == "no":
        if priority == "low":
            reminder += ". Consider completing it when you have free time."
        else:
            reminder += "."
    else:
        print("Invalid input for time-bound. Please enter 'yes' or 'no'.")
        return

    # Output the final reminder
    print("\n" + reminder)

if __name__ == "__main__":
    main()
