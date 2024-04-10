# Phase 3 Project - Task Workflow Program

## What It Does
My project is a CLI program that functions as a "app" to create, delete, and manage users and tasks. It's main purposes is to create, assign, and complete tasks within a company. As a user you can see which tasks are assigned to you, along with it's unique id, description, estimated time to complete, and the foreign key (points to user that it's assigned to). if a user has a task that belongs to them, it would like something like this:

ID: 1
Description: Create high funnel non-brand campaign for new client
Time To Complete: Estimated 1 hour and 15 minutes
user_id = 2

Each prospectibe user also has three characteristics; id, name, and department. 

ID: 2
Name: David Smith
Department: Marketing

This project itself is an accurate representation of what a workflow program might look like in a fully remote company. throughout the company, there are things called "projects", which consist of different pre-made tasks for each department. Everytime you onboard a new client, or have to do something new for them, you would create a new project and send those premade tasks out to your department members. 

The tasks you find in specific projects will be identical for all members. For example, if you onboard a new client, here is the tasks each department / member should expect to receive:

HR: close out / complete project (when done)
Sales: submit signed proposal from client into docusign
Marketing: created new ad account OR update monthly offer
Management: create new project and send out tasks

Knowing that if I am working in the Marketing department I should only expect to see 2-3 different types of tasks, I know if i look up my tasks with the title "create ad account", I will see all the new clients who still need to have their account made. Non-managerial users are also capable of assigning themself a task, which could be useful in the case that you had to go back and fix something you did wrong in a previous task. That would serve as a "reminder task" to go back and fix that / edit it. 

Only Managers are able to create / assign & delete new tasks to other users, as well as hiring and firing new users. If you imagine you are an employee using this CLI, you would be using it to simply view your active tasks that you need to work on, and mark them as complete when done so others can know your progress. The extra functionality to view your teammates by department, view all tasks, etc, are all extraneous and just additional features that all apps offer that most people hardly ever use. The CLI could easily be improved to have tasks auto sent out when a new project is created, add a message to the managers inbox when a task is completed, and send alerts to complete an overdue task. 

## Features
Task Management: Create, assign, view, and delete tasks.
User Management: Add, view, and delete users.
Search Functionality: Find tasks and users by name / title.
Database Integration: Data is stored in a SQLite database (company.db).

## File Structure
lib/: Contains the main application code.
cli.py: Entry point for the CLI application. Handles user interaction and menu display.
helpers.py: Contains helper functions for database operations and other functionalities.
lib/db/: Contains database models and connections.
task.py: Defines the Task model.
user.py: Defines the User model.
Pipfile: Specifies project dependencies.
company.db: SQLite database file.
README.md: Project documentation.

## Classes & Database Models
User and Task Classes: Defined in user.py and task.py respectively.
Define class attributes such as ID, name, department, description, and estimated time to complete.
Database Models: Corresponding to User and Task classes. Define database tables and their relationships.

## Instructions For Running The CLI

As always start by forking and cloning this repository, then opening it in your terminal window / navigating to its directory. Install the dependencies with pipenv install, then open a shell with pipenv shell.

The first real step involves seeding your database, since initially there will be none. Seeding the database involves re-creating the initial "users" and "task" tables, from then you can create all of your employees and begin assigning / completing tasks. 
To initialize the database tables required for the project, follow these steps:

1. Navigate to the Project Directory: Open a terminal or command prompt and navigate to the directory where the project files are located.

2. Ensure SQLite is Installed: Ensure that SQLite is installed on your system. If not, you can download and install it from the SQLite website.

3. Run the Seed File: Execute the seed.py script to create the database tables. You can do this by running the following command:

```
$ python lib/db/seed.py
```

This will execute the Python script and create the necessary tables in the company.db database file.

4. Verify Table Creation: Once the script has finished running, you can verify that the tables have been created by checking the company.db file using an SQLite database browser or by querying the tables using SQLite command-line tools.

5. Ready to Use: With the tables created, you can now proceed to run the main application or interact with the database as needed. Navigate to the lib directory, then run python lib/cli.py to run the CLI. (Note: you'll need to create a few employees and different tasks before you can utilize most of the menu functions, since there is no existing data in the tables!)

Enjoy.
