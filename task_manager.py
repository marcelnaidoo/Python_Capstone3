# Import modules
from datetime import date, datetime
from os import path

# Get current day's date
today = date.today()

# Read users from text file
with open("user.txt", "r") as user_file:
    # Empty string to store the user file data in
    info = ""

    # Save everything in one line
    for line in user_file:
        info += line.strip() + " "

    # Remove commas and split string at spaces
    info = info.replace(",", "").split()


# Register user function
def reg_user():
    print("\n___________________ REGISTER NEW USER __________________________")

    # Loop continuously
    while True:
        # Boolean to check if a username exists
        correct_credentials = True  # True = username does not exist

        new_user = input("Enter new username: ")

        # Get the length of the info list
        length = len(info)

        for i in range(0, length):
            # Compare the input only with usernames, not the passwords
            if i % 2 == 0 and new_user == info[i]:
                print("\nUsername already exists. Enter a different username:")
                correct_credentials = False  # False = username exists
                break  # Break out of the for loop

        # If the username does not exist yet
        if correct_credentials:
            new_pass = input("Enter password for new user: ")
            compare = input("Confirm password:")

            # Check if the password entered twice are the same
            if new_pass != compare:
                print("\nPasswords don't match - user NOT added!")
                break  # End while loop
            else:
                # Append entered data to the end of the user file
                with open("user.txt", "a") as file:
                    file.write("\n" + new_user + ", " + new_pass)
                    print("\nNew user added.")
                    break  # End while loop

        return


# Add a task to a user
def add_task():
    print("\n__________________ ADD NEW TASK ___________________________")
    to_user = input("Username of the person the task should be added to: ")
    task_title = input("Title of the task: ")
    task_description = input("Describe the task: ")
    due_date = input("Due date of the task, Eg. 01 Jan 2020 : ")
    current_date = today.strftime("%d %b %Y")  # Output is: day + month abbreviation + year

    # Append the new task to the end of the tasks file
    with open("tasks.txt", "a") as task_file:
        task_file.write(
            "\n" + to_user + ", " + task_title + ", " + task_description + ", " + current_date + ", " + due_date + ", No")

        print("\nNew task added for " + to_user)
        return


# View all tasks in the file
def view_all():
    print("\n___________________ VIEW ALL TASKS _____________________________")

    num = 0  # To track the number of tasks for all users
    user_tasks = {}  # Empty dictionary to save tasks of all users

    # Open tasks.txt
    with open("tasks.txt", "r") as f:
        # Save tasks in a list
        task_file = f.readlines()

    # Length of task_file
    task_file_length = len(task_file)

    # Loop through task_file
    for i in range(task_file_length):
        task_data = task_file[i].strip().split(", ")
        num += 1  # Count how many tasks there are
        user_tasks[num] = task_data  # Assign task data to a number in the dictionary

    # Loop through and print dictionary
    for ind in user_tasks:
        print("TASK #: " + str(ind))
        print("Task Title: \t\t" + str(user_tasks[ind][1]))
        print("Task Description: \t" + str(user_tasks[ind][2]))
        print("Date Assigned: \t\t" + str(user_tasks[ind][3]))
        print("Due Date: \t\t\t" + str(user_tasks[ind][4]))
        print("Task Complete? \t\t" + str(user_tasks[ind][5]))
        print("")

    return


# View logged in user's tasks
def view_mine():
    print("\n___________ VIEW " + username.upper() + "'S TASKS ______________")

    num = 0  # To track the number of tasks for a certain user

    # Empty dictionary to save tasks of current user in
    user_tasks = {}

    # Empty list to save usernames to
    users = []

    # Open tasks.txt
    with open("tasks.txt", "r") as f:
        # Save tasks in a list
        task_file = f.readlines()

    # Open user.txt
    with open("user.txt", "r") as f:
        # Save users in a list
        for line in f:
            user_data = line.split(", ")
            users.append(user_data[0])

    # Length of task_file
    task_file_length = len(task_file)

    # Loop through task_file
    for i in range(task_file_length):
        task_data = task_file[i].strip().split(", ")
        num += 1  # Count how many tasks there are
        user_tasks[num] = task_data  # Assign task data to a number in the dictionary

    # Loop through and print dictionary
    for ind in user_tasks:
        # Print only current user's tasks
        if user_tasks[ind][0] == username:
            print("TASK #: " + str(ind))
            print("Task Title: \t\t" + str(user_tasks[ind][1]))
            print("Task Description: \t" + str(user_tasks[ind][2]))
            print("Date Assigned: \t\t" + str(user_tasks[ind][3]))
            print("Due Date: \t\t\t" + str(user_tasks[ind][4]))
            print("Task Complete? \t\t" + str(user_tasks[ind][5]))
            print("")

    # Ask user to choose a task
    select_task = int(input("Select a task#  (-1 for Main Menu): "))

    # Exit if -1 is entered
    if select_task == -1:
        return

    # The current user can only edit his/her own tasks
    elif select_task in user_tasks and user_tasks[select_task][0] == username:
        print("Task #" + str(select_task) + " Selected")

        # Continue asking input until something valid is entered
        while True:
            # Save user input is option variable
            option = input("Mark task as complete (C) or edit task (E)? ")

            # Mark the task as complete then exit the loop
            if option == "C" or option == "c":
                print("Task marked as complete.")
                user_tasks[select_task][5] = "Yes"
                break

            # Ask the user how to edit the task
            elif option == "E" or option == "e":

                # The task has to be incomplete to be editable
                if user_tasks[select_task][5] == "No":
                    # Save the user's input in the edit variable
                    edit = input("Change task to different user(T) or due date (D) of the task?")

                    if edit == "T" or edit == "t":

                        # Continue asking until a valid username is entered
                        while True:
                            change_user = input("Change task to which user? (-1 to exit)")

                            # Change the user if the username exists
                            if change_user in users:
                                user_tasks[select_task][0] = change_user
                                break

                            # Break the loop
                            elif change_user == "-1":
                                break

                            # Error message when an invalid username is entered
                            else:
                                print("User does not exist")

                    elif edit == "D" or edit == "d":
                        new_date = input("New due date (Eg. 01 Jan 2020): ")
                        user_tasks[select_task][4] = new_date

                    else:
                        print("Invalid input.")
                else:
                    print("Cannot edit completed tasks")

                break
            # Break loop if this is entered
            elif option == "X" or option == "x":
                break
            else:
                # Error message for wrong input
                print("Invalid input!! Enter a 'C', 'E' or 'X' to exit")

    else:
        # Error message
        print("Task not found!")

    # Open tasks file
    with open("tasks.txt", "w") as f:

        # Combine each dictionary value into one long string
        for key in user_tasks:
            f.write(", ".join(user_tasks[key]) + "\n")
        return


def generate_reports():
    # Open tasks.txt and save it in a list
    with open("tasks.txt", "r") as f:
        task_list = f.readlines()

    # Read user.txt and save it in a list
    with open("user.txt", "r") as f:
        user_list = f.readlines()

    # Total users
    total_users = len(user_list)

    # Empty user dictionary
    user_dict = {}  # Count a user's total tasks
    user_t_complete_dict = {}  # Count complete tasks
    user_t_overdue_dict = {}  # Count overdue and incomplete tasks
    user_percent_dict = {}  # Determine each user's % of tasks
    user_t_complete_percent_dict = {}  # Determine % completed tasks
    user_t_incomplete_percent_dict = {}  # Determine % incomplete tasks
    user_t_overdue_percent_dict = {}  # Determine % incomplete and overdue tasks

    # Variable to track completed tasks
    completed_tasks = 0

    # Variable to track overdue tasks
    overdue_tasks = 0

    # Determine total tasks
    total_tasks = len(task_list)

    # Create dictionary with usernames as keys and assign 0 to each value
    for i in range(total_users):
        user_data = user_list[i].strip().split(", ")

        user_dict[user_data[0]] = 1
        user_t_complete_dict[user_data[0]] = 0
        user_t_overdue_dict[user_data[0]] = 0

    # Loop through each task
    for i in range(total_tasks):
        # Split each line up at comma
        task_data = task_list[i].strip().split(", ")

        # Add one to user's total tasks
        user_dict[task_data[0]] += 1

        # Count completed tasks
        if task_data[-1] == "Yes":
            completed_tasks += 1
            user_t_complete_dict[task_data[0]] += 1

        # Convert task_data[i] date(string) to date
        task_due_date = datetime.strptime(task_data[-2], "%d %b %Y")

        # Get report's date
        report_date = datetime.today()

        # Check if tasks are incomplete and overdue
        if task_data[-1] == "No" and task_due_date < report_date:
            overdue_tasks += 1

            # Add as overdue to specific user
            user_t_overdue_dict[task_data[0]] += 1

    # Incomplete tasks
    incomplete_tasks = total_tasks - completed_tasks

    # Percentage values
    incom_percent = round(incomplete_tasks / total_tasks * 100)
    overdue_percent = round(overdue_tasks / total_tasks * 100)

    # Create TASK_OVERVIEW.TXT
    with open("task_overview.txt", "w") as f:
        f.write(
            "Total Tasks:       "   + str(total_tasks) +
            "\nCompleted Tasks:   " + str(completed_tasks) +
            "\nIncomplete Tasks: "  + str(incomplete_tasks) +
            "\nOverdue Tasks:     " + str(overdue_tasks) +
            "\nIncomplete (%):    " + str(incom_percent) +
            "\nOverdue (%):       " + str(overdue_percent))

    # Percentage total to each user
    for key in user_dict:
        user_percent_dict[key] = round((user_dict[key] - 1) / total_tasks * 100)
        user_t_complete_percent_dict[key] = round(user_t_complete_dict[key] / total_tasks * 100)
        user_t_incomplete_percent_dict[key] = round(((user_dict[key] - 1) - user_t_complete_dict[key]) / total_tasks * 100)
        user_t_overdue_percent_dict[key] = round(user_t_overdue_dict[key] / total_tasks * 100)

    # Create USER_OVERVIEW.TXT
    with open("user_overview.txt", "w") as f:
        f.write(
            "Total Users: \t" + str(total_users) +
            "\nTotal Tasks: \t" + str(total_tasks) +
            "\nTasks Assigned To Each User (%): \t" + str(user_percent_dict) +
            "\nTasks Completed By Each User (%): \t" + str(user_t_complete_percent_dict) +
            "\nEach User's Incomplete Tasks (%): \t" + str(user_t_incomplete_percent_dict) +
            "\nEach User's Overdue Tasks (%): \t\t" + str(user_t_overdue_percent_dict))

        return


def statistics():
    print("\n__________________STATISTICS __________________________")
    print("TASK OVERVIEW")

    # Open task_overview and display to screen
    with open("task_overview.txt", "r") as f:
        for line in f:
            print(line, end="")

    print("\n\nUSER OVERVIEW")

    # Open user_overview and display to screen
    with open("user_overview.txt", "r") as f:
        for line in f:
            print(line, end="")
        print("")

    return


print("\n_______________ LOGIN __________________________")

# Continue asking for input details until it is correct
while True:
    username = input("Enter username:")
    password = input("Enter password:")

    # Check if the username exists
    if username in info:
        index = info.index(username) + 1
        usr_password = info[index]

        # Check if the password matches the username
        if usr_password == password:
            print("\nSuccessful login.")
            break
        else:
            print("Incorrect username or password, Try again")

# Loop until 'e' is entered
while True:
    # Check if logged in as admin
    if username == "admin":
        print("\n_______________ LOGGED IN AS ADMIN ___________________")
        print("Please select one of the following options:")
        print("r - register user")
        print("a - add task")
        print("va - view all tasks")
        print("vm - view my tasks")
        print("gr - generate reports")
        print("s - statistics")
        print("e - exit")

        # Save the user's option as menu_option
        menu_option = input("")

        # Register a new user
        if menu_option == "r":
            reg_user()
        # Exit the program
        elif menu_option == "e":
            print("\nGOODBYE")
            break
        # Add a task
        elif menu_option == "a":
            add_task()
        # View all tasks
        elif menu_option == "va":
            view_all()
        # View current user's tasks
        elif menu_option == "vm":
            view_mine()
        # View statistics
        elif menu_option == "s":
            # If files were generated otherwise generate them
            if path.exists("task_overview.txt") and path.exists("user_overview.txt"):
                statistics()
            else:
                generate_reports()
                statistics()

        # Generate reports
        elif menu_option == "gr":
            print("\nGenerating....")
            generate_reports()
            print("Done.")
        else:
            # If anything other than the given options are entered, show an error
            print("\nInvalid input, Please try again")

    else:
        # Show menu options
        print("\n_________ LOGGED IN AS " + username.upper() + " ______________")
        print("Please select one of the following options:")
        print("a - add task")
        print("va - view all tasks")
        print("vm - view my tasks")
        print("e - exit")

        menu_option = input("")

        # Register a new user
        if menu_option == "e":
            print("\nGoodbye")
            break
        # Add a task
        elif menu_option == "a":
            add_task()
        # View all tasks
        elif menu_option == "va":
            view_all()
        # View current user's tasks
        elif menu_option == "vm":
            view_mine()
        else:
            # If anything other than the given options are entered, show an error
            print("\n Invalid input. Please try again")

