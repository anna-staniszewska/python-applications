import numpy as np

class CinemaReservationSystem:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.seats = np.full((rows, cols), True)
        self.reservationUsers = {}

    def displaySeats(self):
        seatsDisplay = np.where(self.seats == True, "Free", self.seats)
        seatsDisplay = np.where(self.seats == False, "Taken", seatsDisplay)
        return f"Available seats:\n {seatsDisplay}"
    
    def makeReservation(self, row, col, user):
        if np.sum(self.seats) == 0:
            raise ValueError("There are no free seats for this event.")
        
        if user in self.reservationUsers:
            raise ValueError("You can only book 1 seat.")
        
        if col < 1 or col > self.cols or row < 1 or row > self.rows:
            raise ValueError("There is no seat with this row or column.")
        
        if self.seats[row - 1, col - 1] == False:
            raise ValueError("This seat is taken.")
        
        self.seats[row - 1, col - 1] = False
        self.reservationUsers[user] = [row, col]

        return "We have successfully made your reservation!"

    def cancelReservation(self, row, col, user):
        if user in self.reservationUsers:
            if self.reservationUsers[user] == [row, col]:
                self.seats[row - 1, col - 1] = True
            else:
                raise ValueError("Your seat that you want to cancel is different then the one you reserved.")
        else:
            raise ValueError("There is no seat taken by this user.")
        
        return "We have successfully cancelled your reservation!"


room = CinemaReservationSystem(7,10)
print("<Initial state>" + "\n" + room.displaySeats() + "\n")

# próby rezerwacji
try:
    print(room.makeReservation(1, 1, "Anna Staniszewska")) 
except ValueError as e:
    print(e)

try:
    print(room.makeReservation(2, 7, "Katarzyna Kisko"))

except ValueError as e:
    print(e)

try:
    print(room.makeReservation(1, 1, "Marcin Grześko"))
except ValueError as e:
    print(e)

try:  
    print(room.makeReservation(4, 10, "Grzegorz Małek"))  
except ValueError as e:
    print(e)

try:  
    print(room.makeReservation(6, 2, "Grzegorz Małek"))
except ValueError as e:
    print(e)

print("\n<After reservations>\n" + room.displaySeats() + "\n")

# próby anulacji
try:  
    print(room.cancelReservation(6, 2, "Grzegorz Małek"))  
except ValueError as e:
    print(e)

try:  
    print(room.cancelReservation(4, 10, "Grzegorz Małek"))  
except ValueError as e:
    print(e)

try:  
    print(room.cancelReservation(3, 9, "Wojciech Masny"))  
except ValueError as e:
    print(e)


print("\n<After cancellations>\n" + room.displaySeats())

