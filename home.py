from tkinter import *
import booking
import reservations
#define the window, define the buttons, it's style and functionality 
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


#this is what happens when you press on book btn 
#destroys the home window and calling the open_page function inside the booking file 
#passing on_back variable as a parameter and make it point at open_home
#the parameter now is used insde the function in booking.py 
    #Button(bk, text="Back to Home", bk for booking (aka root)
        #    font=("Arial", 14),
        #    command=lambda: (bk.destroy(), on_back())).pack(pady=20)
        # the button go back now waants to take the on_back paramter so we used lambda to allow the command to take - 
        # -paramteres for functions 
        # now the function of the button destroy() the current window 
        # then passing the paramter to it ( which points to a function inside home.py)
        # same goes for open_reservation()
        
def open_booking():
    root.destroy()
    booking.open_page(on_back=open_home)   

def open_reservation():
    root.destroy()
    reservations.open_page(on_back=open_home)

if __name__ == "__main__":
    open_home()
