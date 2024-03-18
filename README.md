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
