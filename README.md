# airlinebooking_165915
Airline booking system

Airline Booking System API

This project is a simplified airline booking system built using Django and Django Rest Framework (DRF). The API supports CRUD operations for flights and passengers, including relationships between the Features

CRUD operations for Flights and Passengers.
Relationship: A Passenger is associated with exactly one Flight; a Flight can have multiple Passengers.
Built-in validation for unique fields
Prerequisites

Python 3.8+
Django 4.0+
Django Rest Framework 3.14+
how to set up and run the project

Clone the repository: git clone https://github.com/your-username/airline_booking_165915.git cd airline_booking_165915 Create a virtual environment:
2.create a virtual environment python -m venv env source env/bin/activate # Linux/Mac env\Scripts\activate # Windows Install dependencies:

3.install dependancies pip install -r requirements.txt

4.Apply database migrations: python manage.py makemigrations python manage.py migrate

5.Run the development server: python manage.py runserver

6.Access the API:Flights: http://127.0.0.1:8000/api/flights/ Passengers: http://127.0.0.1:8000/api/passengers/

Models Below are is the representation of the models Flight Field ,Type, Description flight_number ,CharField, Unique identifier for the flight. departure ,DateTimeField ,Date and time of departure. arrival ,DateTimeField, Date and time of arrival. origin ,CharField ,Origin airport. destination, CharField, Destination airport. capacity ,IntegerField ,Total number of seats available. Passenger Field ,Type, Description first_name ,CharField, Passenger's first name. last_name ,CharField ,Passenger's last name. email ,EmailField, Unique email address. phone_number ,CharField, Contact number. flight ,ForeignKey ,The flight the passenger is booked on. API Endpoints Flights GET /api/flights/: List all flights. POST /api/flights/: Create a new flight. GET /api/flights/{id}/: Retrieve a single flight by ID. PUT /api/flights/{id}/: Update a flight. DELETE /api/flights/{id}/: Delete a flight. Passengers GET /api/passengers/: List all passengers. POST /api/passengers/: Create a new passenger. GET /api/passengers/{id}/: Retrieve a single passenger by ID. PUT /api/passengers/{id}/: Update a passenger. DELETE /api/passengers/{id}/: Delete a passenger. Notable Design Decisions Django Rest Framework: Used for rapid API development. Pagination: Not implemented but could be added for list endpoints. Validation: Unique fields are validated at the model level. Scalability: Designed with modularity to accommodate future enhancements.
