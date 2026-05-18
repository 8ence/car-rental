# Car Rental System

A simple object-oriented car rental system written in Python.

## Project Overview

This application simulates a basic car rental company where users can:

- list available vehicles
- rent a vehicle for a selected date
- cancel existing rentals
- list current rentals

The project was created as an Object-Oriented Programming exam assignment.

---

# Features

## Vehicle Management

The system supports multiple vehicle types through inheritance:

- Passenger cars
- Trucks

## Rental Management

Users can:

- rent vehicles
- cancel rentals
- list all rentals

## Validation and Error Handling

The application includes:

- date format validation
- vehicle availability validation
- rental existence validation
- exception handling

---

# Technologies

- Python
- Object-Oriented Programming (OOP)
- Console-based UI
- Git & GitHub

---

# OOP Concepts Used

## Inheritance

```text
Vehicle
 ├── PassengerCar
 └── Truck
```

## Encapsulation

Private attributes are used throughout the project with getter methods.

## Abstraction

`Vehicle` is implemented as an abstract base class.

## Separation of Concerns

The project is separated into multiple layers:

```text
models/
services/
ui/
data/
```

---

# Project Structure

```text
src/
├── data/
│   └── seed_data.py
│
├── models/
│   ├── vehicle.py
│   ├── passenger_car.py
│   ├── truck.py
│   ├── rental.py
│   └── rental_company.py
│
├── services/
│   └── rental_service.py
│
└── ui/
    └── console_ui.py
```

---

# Initial Data

When the application starts:

- 3 vehicles are automatically loaded
- 4 rentals are automatically created

---

# How to Run

## 1. Clone repository

```bash
git clone <repository-url>
```

## 2. Open project

Open the project in PyCharm or VS Code.

## 3. Run application

```bash
python main.py
```

---

# Example Menu

```text
1. List vehicles
2. Rent vehicle
3. Cancel rental
4. List rentals
0. Exit
```

---

# Main Classes

| Class | Responsibility |
|---|---|
| `Vehicle` | Abstract base vehicle class |
| `PassengerCar` | Passenger vehicle implementation |
| `Truck` | Truck implementation |
| `Rental` | Stores rental information |
| `RentalCompany` | Stores vehicles and rentals |
| `RentalService` | Business logic layer |
| `ConsoleUI` | User interface |

---

# Author

Kővári Bence GDE 