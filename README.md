# PYTHON_capstone3
Create a task manager program for a small business to keep track of assignments given to each worker.


	Create a task manager program for a small business to keep track of assignments
	given to each worker, the date issued and date due, task description, and an
	indication if task is complete or not. Data stored/retrieved from file "tasks.txt".

	Program must allow users to login with a matching username/password combination
	that has been stored, and display an error message if username/password incorrect.
	Combinations stored and retrieved from file "user.txt".

	After login, menu of options must be displayed for user registration, add task,
	view all tasks, view tasks assigned to user specifically and exit. Each option must
	perform the function indicated by its name.

	Format the program to restrict menu options: only the username admin must be allowed
	to register users.
	Additionally, admin must have a new menu option to display statistics

login:
	
	have user enter a username, then enter a password.
		check if username/password combination appears in "user.txt" file
		if both appear in combination continue to menu
		if one or both do not match, print error message
			

Functions:
	
	register user:
		Only allow admin user to access this option
			use an if statement to check if user is admin upon login
			if result false, display error message if user attempts to add a new user
		prompt user for a new username, password and confirm password
			check that username doesn't exist already, print error message if it does
			check that password and confirmed password match, print error message if not
			write username/password combination to file "user.txt"
	
	
	add task:
		prompt user for username to which the task is assigned
			check that user exists within "user.txt" file
			if not, display error message and prompt again
		prompt user for task title
		prompt user for task description
		prompt user for task due date
		Write task to file "tasks.txt", defaulting completed to "No" and date assigned to current date
			import module datetime
			use input today = datetime.date.today()
				for formatting, use today.strftime(%x). output result will formatted to local version
				otherwise, use today.strftime(%d %b %Y) to output as dd mmm yyyy

	
	view all tasks:
		display each task in an easy to ready format

	
	view my tasks:
		display only tasks assigned to logged in user in an easy to read format

		
	generate reports:
		option must be added to menu selection - gr as selector
		Output must generate 2 files:
			task_overview.txt must contain
				Total number of tasks generated
				Total number of completed tasks
				Total number of uncompleted tasks
				Total number of overdue, uncompleted tasks
				Percentage of tasks incomplete
				Percentage of tasks overdue
			user_overview.txt must contain
				Total number of registered users
				Total number of tasks generated
				for each user:
					Total number of tasks assigned to user
					Percentage of total tasks assigned to user
					Percentage of those tasks completed
					Percentage to still complete
					Percentage overdue and incomplete

	
	display statistics:
		New source of data to be task_overview.txt and user_overview.txt
		Files above must be generated if not present
		Look into checking when last files were updated
		Ask user if they would like to update the files prior to proceeding
