from tkinter import *
from tkinter import messagebox
import sqlite3, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, "ffly.db")

def _init_db():
    """Create DB file & table if not exist."""
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            flight_no TEXT NOT NULL,
            departure TEXT NOT NULL,
            destination TEXT NOT NULL,
            date TEXT NOT NULL,
            seat_no TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.commit()
    conn.close()

def open_page(on_back):
    _init_db()

    bk = Tk()
    bk.title("Booking Page")
    bk.geometry("900x600")

    form = Frame(bk)
    form.pack(pady=20)

    Label(form, text="Full Name:", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
    name_entry = Entry(form, width=35, borderwidth=2, font=("Arial", 12))
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    Label(form, text="Flight No:", font=("Arial", 14)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
    flight_entry = Entry(form, width=35, borderwidth=2, font=("Arial", 12))
    flight_entry.grid(row=1, column=1, padx=10, pady=10)

    Label(form, text="Departure:", font=("Arial", 14)).grid(row=2, column=0, padx=10, pady=10, sticky="e")
    dep_entry = Entry(form, width=35, borderwidth=2, font=("Arial", 12))
    dep_entry.grid(row=2, column=1, padx=10, pady=10)

    Label(form, text="Destination:", font=("Arial", 14)).grid(row=3, column=0, padx=10, pady=10, sticky="e")
    des_entry = Entry(form, width=35, borderwidth=2, font=("Arial", 12))
    des_entry.grid(row=3, column=1, padx=10, pady=10)

    Label(form, text="Date:", font=("Arial", 14)).grid(row=4, column=0, padx=10, pady=10, sticky="e")
    date_entry = Entry(form, width=35, borderwidth=2, font=("Arial", 12))
    date_entry.grid(row=4, column=1, padx=10, pady=10)

    Label(form, text="Seat No:", font=("Arial", 14)).grid(row=5, column=0, padx=10, pady=10, sticky="e")
    seat_entry = Entry(form, width=35, borderwidth=2, font=("Arial", 12))
    seat_entry.grid(row=5, column=1, padx=10, pady=10)

    def save_booking():
        data = {
            "full_name": name_entry.get().strip(),
            "flight_no": flight_entry.get().strip(),
            "departure": dep_entry.get().strip(),
            "destination": des_entry.get().strip(),
            "date": date_entry.get().strip(),
            "seat_no": seat_entry.get().strip(),
        }

        # تحقق بسيط
        if any(v == "" for v in data.values()):
            messagebox.showerror("Missing Data", "Please fill all fields.")
            return

        try:
            print("Saving to:", DB_FILE)  # Debug في الكونسول
            conn = sqlite3.connect(DB_FILE)
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO bookings (full_name, flight_no, departure, destination, date, seat_no)
                VALUES (:full_name, :flight_no, :departure, :destination, :date, :seat_no)
                """,
                data,
            )
            conn.commit()
            conn.close()
            messagebox.showinfo("Saved", "Booking saved successfully.")
            # امسح الحقول بعد الحفظ
            for e in (name_entry, flight_entry, dep_entry, des_entry, date_entry, seat_entry):
                e.delete(0, END)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save booking:\n{e}")

    btns = Frame(bk)
    btns.pack(pady=20)
    Button(btns, text="Save", font=("Arial", 14), width=16, command=save_booking).grid(row=0, column=0, padx=10)
    Button(btns, text="Back to Home", font=("Arial", 14), width=16,
           command=lambda: (bk.destroy(), on_back())).grid(row=0, column=1, padx=10)

    bk.mainloop()
