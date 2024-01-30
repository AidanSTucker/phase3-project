This README should serve as a template for your own- go through the important files in your project and describe what they do. Each file that you edit (you can ignore your Alembic files) should get at least a paragraph. Each function should get a small blurb.

You should descibe your actual CLI script first, and with a good level of detail. The rest should be ordered by importance to the user. (Probably functions next, then models.)

Screenshots and links to resources that you used throughout are also useful to users and collaborators, but a little more syntactically complicated. Only add these in if you're feeling comfortable with Markdown.

# Phase 3 Project - Task Workflow Program

## What It Does
My project is a CLI program that functions as a "app" to create, delete, and manage users and tasks. It's main purposes is to create, assign, and complete tasks within a company. As a user you can see which tasks are assigned to you, along with it's unique id, description, estimated time to complete, foreign key (points to user that it's assigned to), and the department the task belongs to. if a user has a task that belongs to them, it would like something like this:

ID: 1
Department: Marketing
Description: Create high funnel non-brand campaign for new client
Time To Complete: Estimated 1 hour and 15 minutes
user_id = 2

Each prospectibe user also has three characteristics; id, name, and department. 

ID: 2
Name: David Smith
Department: Marketing

As a user you have the ability to do the following actions:
0. Exit the program
1. View all tasks
2. View all users
3. View tasks by department
4. View users by department
5. Add new task
6. Delete task
7. Add new user
8. Delete user
9. Find task by id
10. Find user by id

## How It Works