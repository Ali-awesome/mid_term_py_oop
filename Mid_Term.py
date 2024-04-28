import datetime
import random

class Star_Cinema:
    _hall_list = []
    def entry_hall(self,hall):
        self._hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no

    def get_hall_no(self):
        return self.__hall_no
    
    def __auditorium(self, row, col):
        seats = []
        for r in range(row):
            row_seats = []
            for c in range(col):
                row_seats.append('o')
            seats.append(row_seats)
        return seats

    def check_show_id(self, id):
        for show in self.__show_list:
            if show[0] == id:
                return True
        return False
    
    def entry_show(self, id, movie_name, time):
        self.__show_list.append((id, movie_name,time))
        self.__seats[id] = self.__auditorium(self.__rows, self.__cols)

    def book_seats(self, id, seats):
        for seat in seats:
            row, col = seat
            if row-1 >= self.__rows or col-1 >= self.__cols:
                print("Invalid seat number: This hall has", self.__rows, "Rows", "and", self.__cols, "Columns")
                print()
                return
            elif self.__seats[id][row-1][col-1] == 'x':
                print("Seat already booked for: Row", row, "Column", col)
                print("Please select another seat")
                print()
                return
            else:
                self.__seats[id][row-1][col-1] = 'x'
                print("Ticket:", ' '.join(f"Row {row}, Column {col}") + " is confirmed")
        print("Ticket(s) booked successfully!")
        for show in self.__show_list:
            if show[0] == id:
                print("Movie Name:", show[1])
                print("Time:", show[2])
        print("Hall:", self._hall_list[0].__hall_no)
        print()

    def view_show_list(self,hall_no):
        print(f"Shows for Hall {hall_no}:")
        for show in self.__show_list:
            print( "Show ID:", show[0],"|| Movie Name:", show[1],"|| Time:", show[2])

    def get_movie_name(self, id):
        for show in self.__show_list:
            if show[0] == id:
                return show[1]
            
    def remaining_seats(self, id):
        available_seats_count = 0
        for row in range(self.__rows):
            for col in range(self.__cols):
                if self.__seats[id][row][col] == 'o':
                    available_seats_count += 1
        return available_seats_count

    def view_available_seats(self, id):
        print("Total seats for show", self.get_movie_name(id),"is", self.__rows * self.__cols)
        print("Remaining seats for show", self.get_movie_name(id), "is", self.remaining_seats(id))
        print("X for already booked seats")
        for row in range(self.__rows):
            for col in range(self.__cols):
                print(self.__seats[id][row][col], end=' ')
            print()

def generate_random_datetime():
    day = random.randint(1, 28)
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    random_datetime = datetime.datetime(2024, 4, day, hour, minute, second)
    return random_datetime

hall1 = Hall(3, 5, "A10")
hall2 = Hall(5, 5, "B10")
cinema = Star_Cinema()
cinema.entry_hall(hall1)
cinema.entry_hall(hall2)
hall1.entry_show('123', "Kala Manush", generate_random_datetime())
hall1.entry_show('456', "Ajob Bedi", generate_random_datetime())
hall2.entry_show('500', "Gojob Beda", generate_random_datetime())
hall2.entry_show('511', "Manob Badur", generate_random_datetime())

while True:
    print("Options:")
    print("1. View all shows running")
    print("2. View available seats in a show")
    print("3. Book tickets in a show")
    print("4. Exit")
    print()
    choice = input("Enter your choice: ")

    if choice == '1':
        print()
        for hall in cinema._hall_list:
            hall.view_show_list(hall.get_hall_no())
            print()

    elif choice == '2':
        id = input("Enter the ID of the show: ")
        print()
        for hall in cinema._hall_list:
            if hall.check_show_id(id):
                hall.view_available_seats(id)
                print()
                break
            else:
                print("Invalid show ID.")
                print()

    elif choice == '3':
        id = input("Enter the ID of the show: ")
        for hall in cinema._hall_list:
            if hall.check_show_id(id):
                ticket_number = int(input("Enter Number of Tickets: "))
                seats = []
                for _ in range(ticket_number):
                    row = int(input("Enter Row Number: "))
                    col = int(input("Enter Column Number: "))
                    seats.append((row, col))
                print()
                hall.book_seats(id, seats)
                break
            else:
                print("Invalid show ID.")

    elif choice == '4':
        print("Exiting the program.")
        break
    
    else:
        print("Invalid choice. Please enter a valid option.")
        print()
