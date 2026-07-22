# MoonWalk Restaurant Management System

MoonWalk is a backend restaurant management system built using Flask and SQLAlchemy.

It simulates how restaurants manage incoming orders, assign chefs, process cooking automatically, and support multiple restaurant branches.

---

# Features

- Multi Restaurant Support
- Chef Management
- Menu Management
- Order Management
- Automatic Chef Assignment
- Waiting Queue
- Kitchen Scheduler
- Automatic Order Completion
- Estimated Preparation Time
- REST APIs
- SQLAlchemy ORM
- Service Layer Architecture

---

# Tech Stack

- Python 3
- Flask
- Flask-SQLAlchemy
- APScheduler
- SQLite (Development)

---

# Project Structure

```
MoonWalk/

│

├── app/

│   ├── models/

│   ├── routes/

│   ├── services/

│   ├── config.py

│   ├── scheduler.py

│   ├── seed.py

│   └── __init__.py

│

├── tests/

├── app.py

├── requirements.txt

└── README.md
```

---

# Database Design

Restaurant

↓

Chef

↓

Menu

↓

Order

---

# Order Workflow

Customer

↓

Create Order

↓

Check Menu

↓

Available Chef?

↓

YES -------------------- NO

↓

Assign Chef         Waiting Queue

↓

Cooking

↓

Kitchen Scheduler

↓

Completed

↓

Chef Available Again

↓

Assign Next Waiting Order

---

# API Endpoints

## Home

GET /

Returns application status.

---

## Create Order

POST /orders

Request

```json
{
    "customer_name": "Sajal",
    "dish": "Pizza",
    "quantity": 2,
    "restaurant_id": 1
}
```

---

## Complete Order

PUT /orders/<id>/complete

Marks an order as completed.

---

# Running the Project

Create virtual environment

```
python -m venv venv
```
venv\Scripts\activate.ps1
```
Install dependencies
```
pip install -r requirements.txt
```
Run
```
python app.py
```

---

# Seed Database

Run

```python
seed_data()
```

to populate

- Restaurants
- Chefs
- Menu Items

---

# Current Features

- Restaurant Management
- Chef Assignment
- Queue Management
- Kitchen Processing
- Scheduler
- Waiting Time Calculation
- Multi Restaurant Support

---

---

# Learning Objectives

This project was built to practice:

- Flask
- SQLAlchemy
- REST APIs
- OOP
- Service Layer Architecture
- Scheduling
- Backend Design
- Multi-Tenant Architecture

---

# Author

Developed by Sajal Tiwari as part of the MoonWalk Backend Engineering Learning Project.