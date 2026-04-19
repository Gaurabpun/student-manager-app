# Student Manager Web App (Flask)

A web-based Student Management System built using Flask and MySQL.  
This application allows users to perform CRUD operations (Create, Read, Update, Delete) on student records through a simple and clean interface.

---

## Features

- Add new students  
- View all students  
- Edit student details  
- Delete student records  
- Flash messages for user feedback  
- Organized backend with database configuration separation  

---

## Tech Stack

- Backend: Python (Flask)  
- Database: MySQL  
- Frontend: HTML, CSS, Jinja2 Templates  

---

## Project Structure

```
student-manager-flask/
│
├── app.py
├── db_config.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── templates/
│   ├── index.html
│   ├── students.html
│   ├── add_student.html
│   └── edit_student.html
│
├── static/
│   └── style.css
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/student-manager-flask.git
cd student-manager-flask
```

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup MySQL database

Create a database:

```sql
CREATE DATABASE student_db;
USE student_db;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    major VARCHAR(100) NOT NULL
);
```

Update your database credentials inside `db_config.py`.

---

### 5. Run the application

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## Future Improvements

- Add search and filtering functionality  
- Improve UI/UX with better styling  
- Add authentication (login/signup)  
- Deploy the application online  

---

## Author

Gaurab Pun