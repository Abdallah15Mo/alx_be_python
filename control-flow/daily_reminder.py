# Final corrected version matching the test regex:

# Step 1: Get user input
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Step 2: Build base reminder using match-case
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority"

# Step 3: Add time-sensitive note
if time_bound == "yes":
    message += " that requires immediate attention today!"

# Step 4: Print final customized reminder (exact format required by autograder)
print(f"Reminder: {message}")
