try:
    tasks = int(input("Enter number of project tasks: "))
    print(f"You have {tasks} tasks to manage in the ProjectManagementSystem.")
except ValueError:
    print("Invalid input! Please enter a number.")