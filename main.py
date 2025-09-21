from database import init_db
import home

def main():
    init_db()
    home.open_home()

if __name__ == "__main__":
    main()
