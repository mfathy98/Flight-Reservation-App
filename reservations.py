# reservations.py
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3, os

# نفس مسار قاعدة البيانات المستخدم في booking.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, "ffly.db")

def _ensure_table():
    # للتأكد إن الجدول موجود حتى لو فتحت الصفحة مباشرة
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
    _ensure_table()

    res = Tk()
    res.title("Reservations")
    res.geometry("900x600")

    # ====== Title ======
    Label(res, text="Reservations List", font=("Arial", 20, "bold")).pack(pady=10)

    # ====== Table Frame (for Treeview + Scrollbar) ======
    table_frame = Frame(res)
    table_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

    cols = ("id", "full_name", "flight_no", "departure", "destination", "date", "seat_no", "created_at")
    tree = ttk.Treeview(table_frame, columns=cols, show="headings")
    tree.heading("id", text="ID")
    tree.heading("full_name", text="Full Name")
    tree.heading("flight_no", text="Flight No")
    tree.heading("departure", text="Departure")
    tree.heading("destination", text="Destination")
    tree.heading("date", text="Date")
    tree.heading("seat_no", text="Seat No")
    tree.heading("created_at", text="Created At")

    # أعرض أعمدة مقروءة
    tree.column("id", width=60, anchor=CENTER)
    tree.column("full_name", width=160)
    tree.column("flight_no", width=100, anchor=CENTER)
    tree.column("departure", width=120)
    tree.column("destination", width=120)
    tree.column("date", width=110, anchor=CENTER)
    tree.column("seat_no", width=90, anchor=CENTER)
    tree.column("created_at", width=150, anchor=CENTER)

    vsb = ttk.Scrollbar(table_frame, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=vsb.set)
    tree.grid(row=0, column=0, sticky="nsew")
    vsb.grid(row=0, column=1, sticky="ns")

    table_frame.rowconfigure(0, weight=1)
    table_frame.columnconfigure(0, weight=1)

    # ====== Helpers ======
    def load_data():
        tree.delete(*tree.get_children())
        conn = sqlite3.connect(DB_FILE)
        cur = conn.cursor()
        cur.execute("SELECT id, full_name, flight_no, departure, destination, date, seat_no, created_at "
                    "FROM bookings ORDER BY created_at DESC, id DESC")
        for row in cur.fetchall():
            tree.insert("", END, values=row)
        conn.close()

    def get_selected_id():
        sel = tree.selection()
        if not sel:
            return None
        values = tree.item(sel[0], "values")
        return values[0]  # id في أول عمود

    def on_delete():
        bid = get_selected_id()
        if not bid:
            messagebox.showwarning("Select row", "Please select a reservation to delete.")
            return
        if not messagebox.askyesno("Confirm Delete", f"Delete reservation ID {bid}?"):
            return
        try:
            conn = sqlite3.connect(DB_FILE)
            cur = conn.cursor()
            cur.execute("DELETE FROM bookings WHERE id = ?", (bid,))
            conn.commit()
            conn.close()
            load_data()
            messagebox.showinfo("Deleted", f"Reservation ID {bid} deleted.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete:\n{e}")

    def on_edit():
        bid = get_selected_id()
        if not bid:
            messagebox.showwarning("Select row", "Please select a reservation to edit.")
            return
        # GUI فقط: افتح صفحة تعديل من ملف خارجي edit_reservation.py
        try:
            import edit_reservation  # لازم تعمل الملف ده
            # أخفي صفحة الحجوزات مؤقتًا وافتح صفحة التعديل
            res.withdraw()
            # نمرر on_back يرجعنا ويعمل Refresh
            edit_reservation.open_page(
                booking_id=bid,
                on_back=lambda: (res.deiconify(), load_data())
            )
        except ModuleNotFoundError:
            messagebox.showinfo(
                "Edit",
                "Edit GUI placeholder.\nCreate 'edit_reservation.py' with open_page(booking_id, on_back)."
            )

    def on_double_click(event):
        on_edit()

    tree.bind("<Double-1>", on_double_click)

    # ====== Buttons ======
    btns = Frame(res)
    btns.pack(pady=10)

    Button(btns, text="Refresh", font=("Arial", 12), width=12, command=load_data).grid(row=0, column=0, padx=8)
    Button(btns, text="Edit", font=("Arial", 12), width=12, command=on_edit).grid(row=0, column=1, padx=8)
    Button(btns, text="Delete", font=("Arial", 12), width=12, command=on_delete).grid(row=0, column=2, padx=8)
    Button(btns, text="Back to Home", font=("Arial", 12), width=12,
           command=lambda: (res.destroy(), on_back())).grid(row=0, column=3, padx=8)

    # أول تحميل
    load_data()

    res.mainloop()
