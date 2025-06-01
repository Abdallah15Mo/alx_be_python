task = input("Enter your task: ")

# Prompt for priority with validation
while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ["high", "medium", "low"]:
        break
    print("Invalid priority. Please enter 'high', 'medium', or 'low'.")

# Prompt for time-bound with validation
while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    if time_bound in ["yes", "no"]:
        break
    print("Invalid input. Please enter 'yes' or 'no'.")

# Process priority with match case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"

# Customize reminder based on time sensitivity
if time_bound == "yes":
    reminder = "Reminder: " + reminder + " that requires immediate attention today!"
else:
    reminder = "Note: " + reminder + ". Consider completing it when you have free time."

print(reminder)
