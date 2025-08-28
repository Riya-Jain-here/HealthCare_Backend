# HEALTHCARE BACKEND System

A Django + Django REST Framework (DRF) backend for managing patients, doctors, and appointments. Users can register, log in, and manage patient-doctor records securely. Data is stored in PostgreSQL, and JWT is used for authentication.

Features:-

✅User Authentication

✅Register new users

✅Login and obtain JWT tokens

✅Patient Management

✅Add, view, update, and delete patients

✅Patients are linked to the authenticated user

✅Doctor Management

✅Add, view, update, and delete doctors

✅Patient-Doctor Mapping

✅Assign doctors to patients

✅Retrieve and remove doctor assignments

✅Secure APIs

✅JWT authentication protects sensitive endpoints

✅Validation and error handling included

Tech Stack:-
✅Backend: Django, Django REST Framework

✅Database: PostgreSQL

✅Authentication: JWT (via djangorestframework-simplejwt)

✅Environment variables: .env file for sensitive data (e.g., DB password)

Setup Instructions:-

Clone the repository~

->git clone <your-github-repo-link>

->cd HEALTHCARE_BACKEND

Create a virtual environment~

->python -m venv .venv

->source .venv/Scripts/activate    -Windows

 OR
 
source .venv/bin/activate         -Linux/Mac

Install required packages~

->pip install django djangorestframework psycopg2-binary djangorestframework-simplejwt python-dotenv

Set up PostgreSQL~

-Create a database (e.g., healthcare_db)

-Create a user with password

-Update .env file:

DB_NAME=healthcare_db

DB_USER=<your-db-username>

DB_PASSWORD=<your-db-password>

DB_HOST=localhost

DB_PORT=5432

Apply migrations~

->python manage.py makemigrations

->python manage.py migrate

Create a superuser~

->python manage.py createsuperuser

Run the development server~

->python manage.py runserver

✅Server will be available at http://127.0.0.1:8000/

API Endpoints:-

Authentication~

POST /api/auth/register/   – Register a new user

POST /api/auth/login/      – Obtain JWT token

POST /api/auth/refresh/    – Refresh JWT token

Patients~

POST /api/patients/        – Add new patient (JWT required)

GET /api/patients/         – Get all patients for logged-in user

GET /api/patients/<id>/    – Get details of a patient

PUT /api/patients/<id>/    – Update patient

DELETE /api/patients/<id>/ – Delete patient

Doctors~

POST /api/doctors/         – Add new doctor (JWT required)

GET /api/doctors/          – List all doctors

GET /api/doctors/<id>/     – Get doctor details

PUT /api/doctors/<id>/     – Update doctor

DELETE /api/doctors/<id>/  – Delete doctor

Patient-Doctor Mappings~

POST /api/mappings/                – Assign doctor to patient

GET /api/mappings/                 – List all mappings

GET /api/mappings/<patient_id>/    – Get all doctors assigned to a patient

DELETE /api/mappings/<id>/         – Remove a doctor from a patient

Note: In postman, include JWT token in Authorization header as:

-Authorization: Bearer <your-access-token> 

Testing:-

Use Postman to test all endpoints.

Verify user, patient, doctor, and mapping data in PostgreSQL via pgAdmin 4.
