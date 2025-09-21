# Flight Reservation App

A simple desktop application built with **Python (Tkinter + SQLite)** for booking and managing flight reservations.

---

##  How to Run the App

### Option 1 — Run from Python source code
1. Make sure you have **Python 3.8+** installed.
2. Clone or download this repository.
3. Open a terminal in the project folder.
4. Run:
   ```bash
   python main.py


### Option 2 — If you don’t want to install Python:

Download the latest main.exe from the dist/ folder (or from the release ZIP if provided).

Double-click main.exe to start the application.

A SQLite database file flights.db will be created automatically in the same folder if it does not exist.

## Features

- Book Flights: Add a reservation (Name, Flight No, Departure, Destination, Date, Seat No).
- View Reservations: List all bookings in a table.
- Edit Reservations: Double-click or select and edit.
- Delete Reservations: Remove selected booking.
- All data is stored in flights.db (SQLite).

## Project Structure

Flight-Reservation-App/
├─ main.py # Entry point of the app
├─ home.py # Home screen
├─ booking.py # Booking page
├─ reservations.py # Reservation list page
├─ edit_reservation.py # Edit reservation page
├─ database.py # Database connection & queries
├─ flights.db # SQLite database (auto-created)
└─ README.md # This file


## Notes

- On Windows: use the .exe file if provided.
- On Linux/macOS: run `python3 main.py`.
- To reset the app, delete `flights.db` (this will remove all bookings).
