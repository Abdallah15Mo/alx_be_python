# daily_reminder.py

# Step 1: Get user input
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Step 2: Determine the base reminder using match-case
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task"
    case _:
        reminder = f"Reminder: '{task}' has an unknown priority"

# Step 3: Add time sensitivity if applicable
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Step 4: Print final customized reminder
print(reminder)
