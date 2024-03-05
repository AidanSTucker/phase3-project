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
1. Fork and clone the repository
2. install the dependencies with pipenv install, then open a shell with pipenv shell
3. Navigate to the lib directory, then run python lib/cli.py to run the CLI
4. Enjoy!
