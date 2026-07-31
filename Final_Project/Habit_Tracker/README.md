
Habit Tracker

Video Demo  https://youtu.be/o7BkjOP8AVEr

⸻

Description

Habit Tracker is a simple web-based application built with Flask and SQLite that allows users to create and manage daily habits. The purpose of this project is to demonstrate understanding of backend development, routing, database integration, and dynamic HTML rendering using Python and Flask.

This application allows users to add habits and view them in a structured list format. All habits are stored in a SQLite database, ensuring that data persists even after the server is restarted.

⸻

Features
	•	Add new habits through a form
	•	Store habits in a SQLite database
	•	Display all saved habits dynamically
	•	Persistent data storage
	•	Simple and clean interface

⸻

Technologies Used
	•	Python – Core programming language
	•	Flask – Web framework for handling routes and requests
	•	SQLite – Database for storing habit data
	•	HTML – Frontend structure
	•	CS50 SQL Library – Simplified database interaction

⸻

File Structure

project/
│
├── app.py
├── habits.db
├── README.md
└── templates/
  └── index.html

⸻

How It Works

The application uses Flask to handle HTTP requests. When a user visits the homepage (”/”), the application retrieves all habits from the database and renders them using an HTML template.

When a user submits the form to add a new habit:
	1.	The form sends a POST request to the server.
	2.	The server reads the input value from the request.
	3.	The habit is inserted into the SQLite database.
	4.	The user is redirected back to the homepage.
	5.	The updated list of habits is displayed.

The SQLite database contains a table named habits with the following structure:
	•	id – Integer (Primary Key, Auto Increment)
	•	name – Text (Not Null)

This ensures each habit is uniquely identified and properly stored.

⸻

Design Decisions

This project was intentionally kept simple and focused on core backend concepts rather than complex UI design. The goal was to demonstrate:
	•	Understanding of Flask routing
	•	Proper use of POST and GET methods
	•	Database creation and querying
	•	Template rendering
	•	Clean project structure

The interface is minimal to keep the focus on functionality and logic rather than styling.

⸻

Future Improvements

If expanded further, this application could include:
	•	User authentication
	•	Habit completion tracking
	•	Delete and edit functionality
	•	Progress statistics
	•	Improved styling with CSS
	•	Mobile-friendly responsive design

⸻

Conclusion

This Habit Tracker project demonstrates the integration of Python, Flask, and SQLite to create a functional web application with persistent data storage. It reflects understanding of backend development concepts and server-client interaction.

The project serves as a foundation for building more advanced productivity or tracking applications in the future.
