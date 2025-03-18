CampusLedger 📚
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CampusLedger is a student record and book management system designed for faculty members to efficiently add, manage, and track student records along with book borrowing details. It enables CRUD operations on both student records and book transactions, ensuring streamlined academic record-keeping.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Features
- User Authentication – Faculty can register, log in, and manage student records securely.
- Student Records Management – Add, view, update, and delete student details.
- Book Tracking – Record books borrowed by students with borrow and return dates.
- CRUD Operations – Perform create, read, update, and delete actions on both students and books.
- User-Friendly Interface – Simple and intuitive UI for efficient record management.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Tech Stack
- 🔹 Backend: Django (Python)
- 🔹 Frontend: HTML, CSS, Bootstrap
- 🔹 Database: MySQL
- 🔹 Authentication: Django's built-in user authentication

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Installation & Setup

Prerequisites:
- Ensure you have the following installed on your system:
  - Docker
  - Docker Compose

Clone the Repository:
```
git clone https://github.com/nikhitasathish1/CampusLedger.git
cd CampusLedger
```

Build and Start the Containers:
```
docker-compose up --build
```

Running Migrations:
- Once the containers are up, run migrations:
```
docker-compose exec web python manage.py migrate
```

Creating a Superuser:
```
docker-compose exec web python manage.py createsuperuser
```

Hosting it:
```
docker-compose exec web python manage.py runserver 0.0.0.0:8080
```

Login in:
```
http://localhost:8000
```

Stopping the Application:
```
docker-compose down
```
