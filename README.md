Student Study Manager

Student Study Manager is a menu-driven Python application built to help students manage their study subjects and track the number of hours studied for each subject.
This project focuses on strengthening core programming fundamentals such as logic building, modular coding, and file handling.
Features:
Add new study subjects
Prevent duplicate subject entries
Log study hours for existing subjects
Validate user inputs (empty values, invalid hours)
View total study progress for each subject
Persistent data storage using text files
Clean and modular project structure

Tech Stack:
Programming Language: Python
Concepts Used:
Functions
Loops and conditional statements
File handling
Input validation
Modular programming

Tools:
VS Code
GitHub

Project Structure:

Student_Study_Manager
│
├── main.py (Entry point of the application)
├── study_manager.py (Core logic for managing subjects and study hours)
├── file_handler.py (Handles file read/write operations)
│
├── data
│ ├── subjects.txt (Stores subject names)
│ └── study_log.txt (Stores study hours data)
│
├── README.md
├── requirements.txt
└── .gitignore

Prerequisites & Setup:
Make sure you have Python installed (3.8+ recommended).
From the project root, create the data folder and empty files if they don't exist:
mkdir data
type NUL > data\subjects.txt (Windows) or touch data/subjects.txt (Linux/Mac)
type NUL > data\study_log.txt (Windows) or touch data/study_log.txt (Linux/Mac)
(Optional) Add a .gitignore with:
pycache/
*.pyc

How to Run the Project:
Clone the repository
git clone https://github.com/Arpitawork24/Student_Study_Manager.git

Navigate to the project directory
cd Student_Study_Manager

Run the program
python main.py

Sample Usage:
Student Study Manager

1. Add Subject
2. Log Study Hours
3. View Progress
4. Exit

Example Flow:

Enter your choice: 1
Enter subject name: Python
Subject added successfully.

Enter your choice: 2
Enter subject name: Python
Enter study hours: 2
Study hours logged successfully.

Enter your choice: 3

Study Progress
Python : 2.0 hours

Learning Outcomes
Through this project, I gained hands-on experience with:
Designing a menu-driven CLI application
Managing control flow across multiple Python files
Reading from and writing to files for data persistence
Validating user input to avoid runtime errors
Writing clean, structured, and maintainable Python code
Debugging and incremental development

Future Improvements
Add date-wise tracking of study hours
Display weekly or monthly study summaries
Export progress reports
Add a GUI or web-based interface
Integrate a database instead of text files

Author:
Arpita Sutariya
Second-year Computer Science Engineering student
GitHub: https://github.com/Arpitawork24
LinkedIn: https://www.linkedin.com/in/arpita-sutariya-3181b6314

This project represents my learning journey in Python and my focus on building strong programming fundamentals.
