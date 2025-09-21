from tkinter import *
from tkinter import messagebox
from database import fetch_booking, update_booking

def open_page(booking_id, on_back, master=None):
    row = fetch_booking(booking_id)
    if not row:
        messagebox.showerror("Not found", f"Reservation ID {booking_id} not found.")
        on_back()
        return

    win = Toplevel(master) if master else Tk()
    win.title(f"Edit Reservation #{booking_id}")
    win.geometry("900x600")

    form = Frame(win)
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

    Label(form, text="Date (YYYY-MM-DD):", font=("Arial", 14)).grid(row=4, column=0, padx=10, pady=10, sticky="e")
    date_entry = Entry(form, width=35, borderwidth=2, font=("Arial", 12))
    date_entry.grid(row=4, column=1, padx=10, pady=10)

    Label(form, text="Seat No:", font=("Arial", 14)).grid(row=5, column=0, padx=10, pady=10, sticky="e")
    seat_entry = Entry(form, width=35, borderwidth=2, font=("Arial", 12))
    seat_entry.grid(row=5, column=1, padx=10, pady=10)

    _, full_name, flight_no, departure, destination, date, seat_no = row
    name_entry.insert(0, full_name)
    flight_entry.insert(0, flight_no)
    dep_entry.insert(0, departure)
    des_entry.insert(0, destination)
    date_entry.insert(0, date)
    seat_entry.insert(0, seat_no)

    def save_changes():
        data = {
            "full_name": name_entry.get().strip(),
            "flight_no": flight_entry.get().strip(),
            "departure": dep_entry.get().strip(),
            "destination": des_entry.get().strip(),
            "date": date_entry.get().strip(),
            "seat_no": seat_entry.get().strip(),
            "id": booking_id
        }
        if any(v == "" for k, v in data.items() if k != "id"):
            messagebox.showerror("Missing Data", "Please fill all fields.")
            return
        try:
            update_booking(data)
            messagebox.showinfo("Saved", "Changes saved successfully.")
            win.destroy()
            on_back()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save changes:\n{e}")

    btns = Frame(win)
    btns.pack(pady=20)
    Button(btns, text="Save Changes", font=("Arial", 14), width=16, command=save_changes).grid(row=0, column=0, padx=10)
    Button(btns, text="Back", font=("Arial", 14), width=16,
           command=lambda: (win.destroy(), on_back())).grid(row=0, column=1, padx=10)

    if not master:
        win.mainloop()
