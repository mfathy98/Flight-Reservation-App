from tkinter import *
import booking
import reservations

def open_home():
    global root
    root = Tk()
    root.title("FFly Reservations")
    root.geometry("900x600")

    Label(root, text="Welcome to FFly Reservations",
          font=("Arial", 20, "bold")).pack(pady=20)

    Button(root, text="Book Your Flight!",
           font=("Arial", 14),
           command=open_booking).pack(pady=10)
    
    Button(root, text="View Your Reservations",
           font=("Arial", 14),
           command=open_reservation).pack(pady=10)
    
    root.mainloop()

def open_booking():
    root.destroy()
    booking.open_page(on_back=open_home)   

def open_reservation():
    root.destroy()
    reservations.open_page(on_back=open_home)
