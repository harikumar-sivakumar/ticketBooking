class ShowList:
    shows = []

    def createShow(self):
        name = input("\nEnter the show name: ").strip()
        if len([1 for show in self.shows if show.name == name]) == 0:
            self.shows.append(Show(name))
        else:
            print("Show already exists.")

    def soldDetails(self):
        if len(self.shows) > 0:
            print('\n' + '{:<20}'.format('Show Name') + '{:<9}'.format('Sold'))
            print('-' * 29)
            for show in self.shows:
                show.soldDetails()
        else:
            print("No shows.")

    def buyTickets(self):
        if len(self.shows) > 0:
            print('\n' + '{:<10}'.format('Show No.') + '{:<25}'.format('Show Name') + '{:<15}'.format('Available Seats'))
            print('-' * 50)
            for i,show in enumerate(self.shows):
                show.buyTicketsDetails(i)
            showSelected = input("Select show number (C to cancel): ").strip()
            if showSelected == 'c' or showSelected == 'C':
                print("Booking Cancelled.")
                return None
            try:
                showSelected = int(showSelected) - 1
                if showSelected not in range(0, len(self.shows)):
                    raise ValueError('Invalid input')
            except:
                print("Invalid input")
                return None
            self.shows[showSelected].buyTickets()
        else:
            print("No shows available.")

    def deleteShow(self):
        if len(self.shows) > 0:
            print('\n' + '{:<10}'.format('Show No.') + '{:<25}'.format('Show Name'))
            print('-' * 35)
            for i,show in enumerate(self.shows):
                show.deleteShowDetails(i)
            delete = input("Enter show number to delete (C to cancel): ").strip()
            if delete == 'c' or delete == 'C':
                print("Delete Cancelled.")
                return None
            try:
                delete = int(delete) - 1
                if delete in range(0, len(self.shows)):
                    self.shows.pop(delete)
                    print("Deleted successfully")
                else:
                    print("Invalid input.")
            except:
                print("Invalid input.")
        else:
            print("No shows.")


class Show:
    def __init__(self, name):
        self.name = name
        self.capacity = input("Enter the seating capacity: ").strip()
        while type(self.capacity) != int:
            try:
                self.capacity = int(self.capacity)
            except:
                self.capacity = input("Invalid input. Enter capacity as a number: ")
        self.availableSeats = self.capacity

    def buyTicketsDetails(self,i):
        print('{:<10}'.format(str(i + 1)) + '{:<25}'.format(self.name) + '{:<15}'.format(str(self.availableSeats)))

    def buyTickets(self):
        seatsSelected = input("Enter number of seats to book: ").strip()
        try:
            seatsSelected = int(seatsSelected)
        except:
            print("Invalid input")
            return None

        if self.availableSeats >= seatsSelected:
            self.availableSeats -= seatsSelected
            print(str(seatsSelected) + " ticket(s) booked successfully for the show " + self.name)
        else:
            print(str(seatsSelected) + " ticket(s) not available.")

    def soldDetails(self):
        print('{:<20}'.format(self.name) + '{:<4}'.format(str(self.capacity - self.availableSeats)))

    def deleteShowDetails(self,i):
        print('{:<10}'.format(str(i+1)) + '{:<25}'.format(self.name))


s = ShowList()
while True:
    action = input("\n1. Add new show. \n2. Delete show. \n3. Show sold tickets.\n4. Buy tickets.\n5. Quit. \n\nEnter your selection: ").strip()

    if action == '1':
        s.createShow()

    elif action == '2':
        s.deleteShow()

    elif action == '3':
        s.soldDetails()

    elif action == '4':
        s.buyTickets()

    elif action == '5' or action == 'q' or action == 'Q':
        break

    else:
        print("\nInvalid input.")