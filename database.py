import sqlite3, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, "flights.db")

def get_conn():
    return sqlite3.connect(DB_FILE)

def init_db():
    conn = get_conn()
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

def insert_booking(data):
    conn = get_conn()
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

def fetch_all_bookings():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, full_name, flight_no, departure, destination, date, seat_no, created_at "
        "FROM bookings ORDER BY created_at DESC, id DESC"
    )
    rows = cur.fetchall()
    conn.close()
    return rows

def fetch_booking(bid):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, full_name, flight_no, departure, destination, date, seat_no FROM bookings WHERE id = ?",
        (bid,),
    )
    row = cur.fetchone()
    conn.close()
    return row

def delete_booking(bid):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM bookings WHERE id = ?", (bid,))
    conn.commit()
    conn.close()

def update_booking(data):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        """
        UPDATE bookings
           SET full_name=:full_name,
               flight_no=:flight_no,
               departure=:departure,
               destination=:destination,
               date=:date,
               seat_no=:seat_no
         WHERE id=:id
        """,
        data,
    )
    conn.commit()
    conn.close()
