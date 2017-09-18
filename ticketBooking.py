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
                print('{:<20}'.format(show.name) + '{:<4}'.format(str(show.capacity - show.availableSeats)))
        else:
            print("No shows.")

    def buyTickets(self):
        if len(s.shows) > 0:
            print('\n' + '{:<10}'.format('Show No.') + '{:<25}'.format('Show Name') + '{:<15}'.format('Available Seats'))
            print('-' * 50)
            for i,show in enumerate(self.shows):
                print('{:<10}'.format(str(i+1)) + '{:<25}'.format(show.name) + '{:<15}'.format(str(show.availableSeats)))

            showSelected = input("Select show number: ").strip()
            try:
                showSelected = int(showSelected) - 1
                if showSelected not in range(0, len(self.shows)):
                    raise ValueError('invalid input')
            except:
                print("Invalid input")
                return None

            seatsSelected = input("Enter number of seats to book: ").strip()
            try:
                seatsSelected = int(seatsSelected)
            except:
                print("Invalid input")
                return None

            if s.shows[showSelected].availableSeats >= seatsSelected:
                s.shows[showSelected].availableSeats -= seatsSelected
                print(str(seatsSelected) + " ticket(s) booked successfully for the show " + s.shows[showSelected].name)
            else:
                print(str(seatsSelected) + " ticket(s) not available.")

        else:
            print("No shows available.")

    def deleteShow(self):
        if len(self.shows) > 0:
            print('\n' + '{:<10}'.format('Show No.') + '{:<25}'.format('Show Name'))
            print('-' * 35)
            for i,show in enumerate(self.shows):
                print('{:<10}'.format(str(i+1)) + '{:<25}'.format(show.name))
            delete = input("Enter show number to delete: ").strip()
            if type(delete) != int:
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