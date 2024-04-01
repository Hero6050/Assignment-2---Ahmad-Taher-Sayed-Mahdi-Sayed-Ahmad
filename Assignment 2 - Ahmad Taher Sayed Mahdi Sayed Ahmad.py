# Create a class for the museum
# This will hold the locations, arts, and events all in one place
class Museum:
    '''This class has the ticket pricing, locations, events, and the art in the museum.'''
    def __init__(self):
        # Here we define the ticket price and create locations to host events and house arts
        # You can change the ticket price here, added in the constructor above,
        # or change it using setter function.
        self.__ticketPrice = 63.0
        # The classes Location will help creating new locations if needed in the future
        self.__permGal = Location ()
        self.__exhHall = Location ()
        self.__outSpace = Location ()

        # allEvents holds every available events
        # allArts holds every art in the museum even ones in storage.
        self.__allEvents = []
        self.__allArts = []

    # Setter/getter for ticket price
    def getTicketPrice(self):
        return self.__ticketPrice
    def setTicketPrice(self, price):
        self.__ticketPrice = price

    # Functions to add, remove, and get art from a location
    def addArtPerm(self, art):
        # This function is for adding art to permGalArt
        # It won't add the art piece if it is already there
        # It also makes sure art is in allArts
        self.addArt(art)
        self.__permGal.addArtLoc(art)
        # This updates the location of the art
        art.setLocation("Permanent Gallery")
    def removeArtPerm(self, art):
        # This function is for removing art from permGalArt
        self.__permGal.removeArtLoc(art)
        art.setLocation("Storage")
    def getPermGalArt(self):
        # This returns the art in permGal
        return self.__permGal.getArtLoc()

    def addArtExh(self, art):
        # This adds art to the exhibition hall
        self.addArt(art)
        self.__exhHall.addArtLoc(art)
        art.setLocation("Exhibition Hall")
    def removeArtExh(self, art):
        # This removes art from exhibition hall
        self.__exhHall.removeArtLoc(art)
        art.setLocation("Storage")
    def getExhHallArt(self):
        # Returns art in exhibition hall
        return self.__exhHall.getArtLoc()

    def addArtOut(self, art):
        # This adds art to outdoor space
        self.addArt(art)
        self.__outSpace.addArtLoc(art)
        art.setLocation("Outdoor Space")
    def removeArtOut(self, art):
        # This removes art from outdoor space
        self.__outSpace.removeArtLoc(art)
        art.setLocation("Storage")
    def getOutSpaceArt(self):
        # This returns all the art in outdoor space
        return self.__outSpace.getArtLoc()

    def addArt(self, art):
        # This adds art to allArts
        # This functions checks if it is available
        # We don't have to check before calling it
        if art not in self.__allArts:
            self.__allArts.append(art)
            art.setLocation("Storage")
            return True
        return False
    def removeArt(self, art):
        # This removes art from the museum
        # Because if art is not in allArts it shouldn't be in the museum
        if art in self.__allArts:
            self.__allArts.remove(art)
            self.removeArtPerm(art)
            self.removeArtExh(art)
            self.removeArtOut(art)
            art.setLocation("N/A")
            return True
        return False
    def getArts(self):
        # This returns every art piece in the museum
        # including in storage
        return self.__allArts


    # Functions to add, remove, and get events from a location
    def addEventPerm (self, event):
        # This adds an event to permGal
        # This also ensures that the event is available in the list of events
        self.addEvent(event)
        self.__permGal.addEventLoc(event)
        # Tours don't have a specific location
        if not isinstance(event, Tour):
            event.setLocation("Permanent Gallery")
    def removeEventPerm (self, event):
        # This removes an event from permGal
        # The reason this does not remove the event from allEvents
        # Is because an event can be temporarily be unavailable.
        self.__permGal.removeEventLoc(event)
        # Tours don't have locations so we ignore them here
        if not isinstance(event, Tour):
            event.setLocation("Unavailable")
    def getPermEvents(self):
        # Returns all the events in permGal
        return self.__permGal.getEventsLoc()

    def addEventExh(self, event):
        # This adds an event to the exhibition hall and all events list
        self.addEvent(event)
        self.__exhHall.addEventLoc(event)
        # Tours don't have locations so we ignore them here
        if not isinstance(event, Tour):
            event.setLocation("Exhibition Hall")
    def removeEventExh(self, event):
        # This removes an event from exhibition hall
        self.__exhHall.removeEventLoc(event)
        # Tours don't have locations so we ignore them here
        if not isinstance(event, Tour):
            event.setLocation("Unavailable")
    def getExhHallEvents(self):
        # Returns all the event in exhibition halls
        return self.__exhHall.getEventsLoc()

    def addEventOut(self, event):
        # Adds an event to the outdoor space and the all events list
        self.addEvent(event)
        self.__outSpace.addEventLoc(event)
        # Tours don't have locations so we ignore them here
        if not isinstance(event, Tour):
            event.setLocation("Outdoor Space")
    def removeEventOut(self, event):
        # Removes an event from the outdoor space
        self.__outSpace.removeEventLoc(event)
        # Tours don't have locations so we ignore them here
        if not isinstance(event, Tour):
            event.setLocation("Unavailable")
    def getOutSpaceEvents(self):
        # Returns all the events in the outdoor space
        return self.__outSpace.getEventsLoc()

    def addEvent(self, event):
        # Adds the event to the list of all events
        if event not in self.__allEvents:
            self.__allEvents.append(event)
            return True
        return False
    def removeEvent(self, event):
        # Removes an event entirely from the museum
        if event in self.__allEvents:
            self.__allEvents.remove(event)
            self.removeEventPerm(event)
            self.removeEventExh(event)
            self.removeEventOut(event)
            return True
        return False
    def getEvents(self):
        # Returns all the events available.
        return self.__allEvents

    # This function allows us to sell tickets
    def sellTicket(self, visitor, event):
        # First we check if the event is available or not
        if event in self.getEvents():
            # Here if the visitor is a child (below 18) or a senior (above 60)
            # They get a free ticket, however, we check if they have their ID first
            if not 18 <= visitor.getAge() <= 60 and visitor.getID() != None:
                price = 0.0
            #Teachers and students get free tickets too
            elif visitor.getOccupation() == "Teacher" or visitor.getOccupation == "Student" and visitor.getID() != None:
                price = 0.0
            else:
                # special events have their unique price
                # If it is not a unique event we set the normal price
                if not isinstance(event, Sp_Event):
                    price = self.getTicketPrice()
                    # Here we take into account groups (tour)
                    if isinstance(event, Tour):
                        # Here apply the discount for a group
                        price = price * 0.5
                else:
                    price = event.getTicketPrice()

            # Here we apply 5% VAT and sell the ticket
            price += (0.05 * price)

            # We check if the user can pay or not. If they can't, we end the interaction.
            if visitor.getMoney() >= price:
                # Here we add the visitor to the tour if the event is a tour
                if isinstance(event, Tour):
                    event.addGroupMember(visitor)

                # Here we take money from the visitor
                visitor.setMoney((visitor.getMoney() - price))

                # Here we create the ticket and give it to the user
                ticket = Ticket(owner=visitor, event=event, price=price)
                visitor.addTicket(ticket)

                # Here we print the receipt and give it to the user
                receipt = [f"Receipt of ticket to {visitor.getName()}, with price of {price}. Transaction was confirmed.",
                           f"Ticket to event: {event.getName()}"]
                print (receipt)
                visitor.addReceipt(receipt)
                return True
        return False


    # Functions to display location details.
    def displayPermGal(self):
        # Display the information of permGal
        print (f"Permanent Gallery")
        print (f"Art in permanent gallery: ")
        self.__permGal.displayArts()
        print (f"Events in permanent gallery: ")
        self.__permGal.displayEvents()
    def displayExhHall(self):
        # Display the information of exhibition hall
        print (f"Exhibition Hall")
        print (f"Art in the exhibition hall: ")
        self.__exhHall.displayArts()
        print (f"Events in the exhibition hall: ")
        self.__exhHall.displayEvents()
    def displayOutSpace(self):
        # Display the information of outdoor space
        print (f"Outdoor Space")
        print (f"Art in outdoor space: ")
        self.__outSpace.displayArts()
        print (f"Events in outdoor space: ")
        self.__outSpace.displayEvents()

    # To display arts in the museum
    def displayArts(self):
        # Notice that this is a polymorphic function
        # It displays all the art for the museum
        # But in the context of location
        # It only displays the art in that location
        print (f"All art in the museum: ")
        for art in self.__allArts:
            art.displayArt()
            print("")

    # To display every event in the museum
    def displayEvents(self):
        # This is a polymorphic function too
        # It displays all the event in the museum here
        print ("All events in the museum: ")
        for event in self.__allEvents:
            event.displayEvent()

    # To display museum details
    def displayMuseum(self):
        # This displays every information the museum has
        # ONLY FOR CUSTOMERS, so we don't display unavailable art or events
        # For all arts and events use the two functions above.
        print (f"Ticket price (18 <= age <= 60, before VAT): {self.getTicketPrice()} AED")
        print (f"Ticket price (18 > age, 60 < age, teachers, and students): FREE")
        print (f"50% off original price in groups\n")
        self.displayPermGal()
        self.displayExhHall()
        self.displayOutSpace()


# Create a class for locations to hold arts and events
# This class will help creating location, adding, removing,
# , and getting arts or events a lot easier in the main class Museum
# It helps simplify the process and lessen spaghetti code
class Location:
    '''This class holds the events and arts a location has'''
    # Here we construct the object
    def __init__(self):
        self.__arts = []
        self.__events = []

    # Functions to add, remove, and get art
    def addArtLoc(self, art):
        # This adds art to the location
        if art not in self.__arts:
            self.__arts.append(art)
            return True
        return False
    def removeArtLoc(self, art):
        # This removes art from the location
        if art in self.__arts:
            self.__arts.remove(art)
            return True
        return False
    def getArtLoc(self):
        # This returns the art in the location
        return self.__arts

    # Functions to add, remove, and get events
    def addEventLoc(self, event):
        # This adds an event to the location
        if event not in self.__events:
            self.__events.append(event)
            return True
        return False
    def removeEventLoc(self, event):
        # This remove an event from the location
        if event in self.__events:
            self.__events.remove(event)
            return True
        return False
    def getEventsLoc(self):
        # This returns the events in the location
        return self.__events

    # This function displays the location's information
    def displayArts(self):
        # This one is for the art in the location
        for art in self.__arts:
            print(f"Title: {art.getTitle()}")
            print(f"Author: {art.getArtist()}")
            print(f"Date of Creation: {art.getDoC()}\n")

    def displayEvents(self):
        # This is a polymorphic function
        # It is for displaying the events in the location
        for event in self.__events:
            event.displayEvent()


# Create a class for events
class Event:
    '''Event is a general class for events such as exhibitions, tours, and special events'''
    # Here we construct the object
    def __init__(self, name, duration, location):
        self.__name = name
        self.__duration = duration
        self.__location = location
        self.__type = None

    # Setter/Getter functions
    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    def setDuration(self, duration):
        self.__duration = duration
    def getDuration(self):
        return self.__duration
    def setLocation(self, location):
        self.__location = location
    def getLocation(self):
        return self.__location
    def setType(self, type):
        # Although this will not need to be changed, you can change it if you wished to.
        self.__type = type
    def getType(self):
        return self.__type

    def displayEvent(self):
        # Displays the event.
        print(f"Event name: {self.getName()}")
        print(f"Location: {self.getLocation()} ")
        print(f"Duration: {self.getDuration()}\n")


# Create a class for exhibitions
# This class inherits the class Event
# This is because they share attributes with other events
class Exhibition(Event):
    '''This class has details for exhibitions like the theme and featured art'''
    # Here we construct the object
    def __init__(self, name, duration, theme):
        super().__init__(name, duration, location = None)
        self.setType("Exhibition")
        self.__theme = theme

    # Setter/Getter functions
    def setTheme(self, theme):
        self.__theme = theme
    def getTheme(self):
        return self.__theme

    # To display Exhibition detail
    def displayEvent(self):
        # This is a polymorphic function
        print (f"Event name: {self.getName()}")
        print (f"Type: {self.getType()}")
        print (f"Theme: {self.getTheme()}")
        print (f"Location: {self.getLocation()} ")
        print (f"Duration: {self.getDuration()}\n")


# Create a class for tours
# This class inherits the class Event
# This is because they share attributes with other events
class Tour(Event):
    '''This class has the group, date, and the guide of a tour'''
    # Here we create the object
    def __init__(self, name, duration, date, guide, group):
        # A tour has some attributes of an event but does not have a location
        # As it is a tour of the museum
        super().__init__(name, duration, location = None)
        self.__date = date
        self.setType("Tour")
        self.__guide = guide
        self.__groupMembers = group

        #Here we update the guide's info
        guide.setTour(self)
        guide.updateGroup()

    # Setter/getter functions
    def setDate(self, date):
        self.__date = date
    def getDate(self):
        return self.__date
    def setGuide(self, guide):
        # This sets a new guide and updates their tour and group.
        # Here we update the old guide's info
        self.__guide.setTour (None)
        self.__guide.updateGroup()

        # Here we set the new guide and update their info
        self.__guide = guide
        guide.setTour(self)
        guide.updateGroup()
    def getGuide(self):
        return self.__guide

    # To add, remove, and get visitors in the group
    def addGroupMember(self, member):
        # Here we make sure there is enough room for a new member first.
        if len(self.__groupMembers) < 40 and member not in self.__groupMembers:
            # We add the member then update their status and the guide's info
            self.__groupMembers.append(member)
            self.__guide.addMember(member)
            member.setGroup(self)
            return True
        return False
    def removeGroupMember(self, member):
        if member in self.__groupMembers:
            # We remove the member then update their status and the guide's info
            self.__groupMembers.remove(member)
            self.__guide.removeMember(member)
            member.setGroup(None)
    def getGroupMembers(self):
        return self.__groupMembers

    # To display all group member
    def displayGroupMembers(self):
        for member in self.getGroupMembers():
            member.displaVisitor()

    # To display tour details
    def displayEvent(self):
        # This is a polymorphic function
        print(f"Event name: {self.getName()}")
        print(f"Type: {self.getType()}")
        print(f"Date: {self.getDate()}")
        print(f"Guide: {self.__guide.getName()}")
        print(f"Groups size: {len(self.__groupMembers)}")
        if 15 <= len(self.__groupMembers) <= 40:
            print(f"Status: Ready")
        else:
            print(f"Status: Not ready")
        print(f"Expected duration: {self.getDuration()}\n")


# Create a class for special events
# This class inherits the class Event
# This is because they share attributes with other events
class Sp_Event(Event):
    '''This class has the purpose of the special event and other details'''
    # Here we create the object
    def __init__(self, name, duration, purpose, price):
        super().__init__(name, duration, location = None)
        self.setType("Special Event")
        self.__purpose = purpose
        self.__ticketPrice = price

    # Setter/Getter functions
    def setPurpose(self, purpose):
        self.__purpose = purpose
    def getPurpose(self):
        return self.__purpose
    def setTicketPrice(self, price):
        self.__ticketPrice = price
    def getTicketPrice(self):
        return self.__ticketPrice

    def displayEvent(self):
        # This is a polymorphic function
        print(f"Event name: {self.getName()}")
        print(f"Type: {self.getType()}")
        print(f"Purpose: {self.getPurpose()}")
        print(f"Ticket price: {self.getTicketPrice()} AED")
        print(f"Location: {self.getLocation()} ")
        print(f"Duration: {self.getDuration()}\n")


# Create a class to represent art pieces
class Art:
    '''Here we set the requirements for an art piece which will be inherited by more specific categories'''
    # Here we create the object
    def __init__(self, title, artist, dateOfCreation, history):
        self.__title = title
        self.__artist = artist
        self.__dateOfCreation = dateOfCreation
        self.__history = history
        self.__location = None

    # Setter/Getter functions
    def setTitle(self, title):
        self.__title = title
    def getTitle(self):
        return self.__title
    def setArtist(self, artist):
        self.__artist = artist
    def getArtist(self):
        return self.__artist
    def setDoC(self, dateOfCreation):
        self.__dateOfCreation = dateOfCreation
    def getDoC(self):
        return self.__dateOfCreation
    def setHistory(self, history):
        self.__history = history
    def getHistory(self):
        return self.__history
    def setLocation(self, location):
        self.__location = location
    def getLocation(self):
        return self.__location

    # To display art details
    def displayArt(self):
        print(f"Title: {self.getTitle()}")
        print(f"Author: {self.getArtist()}")
        print(f"Date of Creation: {self.getDoC()}")
        print(f"Historical significance: {self.getHistory()}")
        print(f"Location: {self.getLocation()}")


# Create a class for tickets
class Ticket:
    '''This class will hold the detail of the exhibition, tour, or special event'''
    # Here we create the object
    def __init__(self, owner, event, price):
        self.__owner = owner
        self.__event = event
        self.__eventName = event.getName()
        self.__type = event.getType()
        self.__duration = event.getDuration()
        self.__ticketPrice = price

        # Although every ticket has the same details,
        # details will vary depending on the type of event
        # This will make sure no error occurs.
        if not isinstance(event, Tour):
            self.__location = event.getLocation()
            self.__guide = None
            self.__date = "N/A"
            if isinstance(event, Sp_Event):
                self.__purpose = event.getPurpose()
            else:
                self.__purpose = None
        else:
            self.__location = None
            self.__guide = event.getGuide()
            self.__date = event.getDate()
            self.__purpose = None

    # Setter/Getter functions
    def setOwner(self, owner):
        self.__owner = owner
    def getOwner(self):
        return self.__owner
    def setEvent(self, event):
        self.__event = event
    def getEvent(self):
        return self.__event
    def setEventName(self, eventName):
        self.__eventName = eventName
    def getEventName(self):
        return self.__eventName
    def setType(self, type):
        self.__type = type
    def getType(self):
        return self.__type
    def setDuration(self, duration):
        self.__duration = duration
    def getDuration(self):
        return self.__duration
    def setTicketPrice(self, price):
        self.__ticketPrice = price
    def getTicketPrice(self):
        return self.__ticketPrice
    def setLocation(self, location):
        self.__location = location
    def getLocation(self):
        return self.__location
    def setGuide(self, guide):
        self.__guide = guide
    def getGuide(self):
        return self.__guide
    def setDate(self, date):
        self.__date = date
    def getDate(self):
        return self.__date
    def setPurpose(self, purpose):
        self.__purpose = purpose
    def getPurpose(self):
        return self.__purpose

    # To display the ticket to the user
    def displayTicket(self):
        print(f"Ticket owner: {self.getOwner().getName()}")
        print(f"Event: {self.getEventName()}")
        print(f"Event type: {self.getType()}")
        print(f"Ticket price: {self.getTicketPrice()}")
        print(f"Guide: {self.getGuide().getName()}")
        print(f"Date: {self.getDate()}")
        print(f"Purpose: {self.getPurpose()}")
        print(f"Location: {self.getLocation()}")
        print(f"Duration: {self.getDuration()}\n")


# Create a class to represent a person
class Person:
    '''This class will have age, name, occupation, money, and national ID of an individual'''
    # Here we create the object
    def __init__(self, name, age, occupation, money, ID):
        self.__name = name
        self.__age = age
        self.__occupation = occupation
        self.__money = money
        self.__ID = ID

    # Setter/Getter functions
    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    def setAge(self, age):
        self.__age = age
    def getAge(self):
        return self.__age
    def setOccupation(self, occupation):
        self.__occupation = occupation
    def getOccupation(self):
        return self.__occupation
    def setMoney(self, money):
        self.__money = money
    def getMoney(self):
        return self.__money
    def setID(self, ID):
        self.__ID = ID
    def getID(self):
        return self.__ID

    # To display person details
    def displayPerson(self):
        print(f"Name: {self.getName()}")
        print(f"Age: {self.getAge()}")
        print(f"National ID: {self.getID()}")
        print(f"Occupation: {self.getOccupation()}")
        print(f"Money: {self.getMoney()}")


# Create a class to represent a guide
# This class inherits from the class Person
# Because it share attributes with that class.
class Guide(Person):
    '''This class will have the group and the event the guide is assigned to'''
    def __init__(self, name, age, money, ID, tour = None):
        # A guide will have an assigned Tour
        # and an assigned group.
        super().__init__(name = name, age = age, occupation = "Guide", money = money, ID = ID)
        self.__tour = tour
        # To make sure no error occurs if we create a guide before a tour
        if tour == None:
            self.__group = []
        else:
            # Here we update the tour's guide
            tour.setGuide(self)
            self.__group = tour.getGroupMembers()

    # Setter/Getter functions
    def setTour(self, tour):
        self.__tour = tour
    def getTour(self):
        return self.__tour

    # To add, remove, and get group members
    def addMember(self, member):
        if member not in self.__group:
            self.__group.append(member)
            return True
        return False
    def removeMember(self, member):
        if member in self.__group:
            self.__group.remove(member)
            return True
        return False
    def getGroup(self):
        return self.__group

    # This function allows for quick update when changing guides/tours
    def updateGroup(self):
        if self.__tour != None:
            self.__group = self.__tour.getGroupMembers()
            return True
        self.__group = []

    # To display guide information
    def displayGuide(self):
        super().displayPerson()
        # To make sure no error occurs when no tour is assigned
        # When the guide is assigned a tour we will print the tour's info
        # Otherwise we say that they are not assigned a group or a tour
        if self.__tour != None:
            print(f"Assigned tour: {self.__tour.getName()}")
            print(f"Assigned group: ")
            if self.__group == []:
                print(f"Currently no member is assigned")
            else:
                for member in self.__group:
                    member.displayPerson()
                    print("")
        else:
            print(f"Assigned tour: None")
            print(f"Assigned group: None")


# Create a class to represent visitors
# This class inherits from the class Person
# Because it shares attributes with that class
class Visitor(Person):
    '''This class will hold the tickets, bill, and group of the visitor'''
    def __init__(self, name, age, occupation, money, ID, group):
        super().__init__(name, age, occupation, money, ID)
        self.__tickets = []
        self.__group = group
        self.__receipts = []

    # Setter/Getter functions
    def setGroup(self, group):
        self.__group = group
    def getGroup(self):
        return self.__group

    # Functions to add, remove, and get tickets/receipts
    def addTicket(self, ticket):
        if ticket not in self.__tickets:
            self.__tickets.append(ticket)
            return True
        return False
    def removeTicket(self, ticket):
        if ticket in self.__tickets:
            self.__tickets.remove(ticket)
            return True
        return False
    def getTickets(self):
        return self.__tickets
    def addReceipt(self, receipt):
        if receipt not in self.__receipts:
            self.__receipts.append(receipt)
            return True
        return False
    def removeReceipt(self, receipt):
        if receipt in self.__receipts:
            self.__receipts.remove(receipt)
            return True
        return False
    def getReceipts(self):
        return self.__receipts

    # For visitors to buy tickets
    def purchaseTicket(self, event, museum):
        museum.sellTicket(self, event)

    # To visitor details
    def displayVisitor(self):
        super().displayPerson()
        print(f"Tickets: ")
        for ticket in self.__tickets:
            ticket.displayTicket()
        if self.__group != None:
            print(f"Group: {self.__group.getName()}")
        else:
            print(f"Group: None")
        print(f"Receipts: ")
        for receipt in self.__receipts:
            print (receipt)
        print("")




print ("Test Cases:")
# Creating a museum and an art piece
museum1 = Museum()
art1 = Art("Mona Lisa", "Leonardo Da Vinci", 1503, "The best known work of art in the word")

print ("Checking the art piece: ")
art1.displayArt()

# Creating a new event
print("")
exhibition1 = Exhibition("Famous Arts", "2 Hours", "Iconic Arts")
print ("Checking the event: ")
exhibition1.displayEvent()


# Adding the art piece and event to the permanent gallery
print(f"\n")
print(f"Permanent Gallery before adding art piece and event:")
museum1.displayPermGal()
museum1.addArtPerm(art1)
museum1.addEventPerm(exhibition1)
print("")
print("Permanent Gallery after adding art piece and event:")
museum1.displayPermGal()


print("")
print("Art piece after adding to permanent gallery: ")
art1.displayArt()


# Creating a guide and a tour
print(f"\n")
guide1 = Guide("Ahmad", 22, 29000.0, "2312341")
print ("Guide before creating a tour:")
guide1.displayGuide()
print("")
print ("Guide after creating a tour:")
tour1 = Tour("The Ahmad Experience", "1.5 hours", "2/04/2024", guide1, [])
guide1.displayGuide()
print("")
print("Tour details before adding members: ")
tour1.displayEvent()

# Tour needs to be added to the museum for users to interact with it
museum1.addEvent(tour1)

# Creating a visitor and purchasing a ticket to the tour
print(f"\n")
print ("Visitor before tour:")
visitor1 = Visitor("Andrew", 37, "Businessman", 50000.0, "6251", None)
visitor1.displayVisitor()
print ("")
print ("Visitor after tour (purchasing ticket):")
visitor1.purchaseTicket(tour1, museum1)
visitor1.displayVisitor()

print("")
print("Tour after adding members: ")
tour1.displayEvent()
print("Guide after adding members: ")
guide1.displayGuide()

# Opening special event and free tickets
print(f"\n")
special1 = Sp_Event("Music", "4 hours", "Musical Concert", 100)
# Adding the event to outdoor space
museum1.addEventOut(special1)
# Adding some art and add to outdoor space
art2 = Art("IDK", "Me", 2024, "Something")
museum1.addArtOut(art2)
# Create two visitors one who will get a free ticket another who will have to pay
visitor2 = Visitor("Andrew2", 37, "Teacher", 50000.0, "432414", None)
visitor3 = Visitor("Ahmad", 19, "Other than student", 200, "2313", None)
# Make them purchase the ticket
print ("Here the receipts show that free tickets work because Anderw2 was a teacher")
print ("Special events having unique prices seem to work here as well")
visitor2.purchaseTicket(special1, museum1)
visitor3.purchaseTicket(special1, museum1)

# Displaying the final museum
print(f"\n")
museum1.displayMuseum()
museum1.displayEvents()
museum1.displayArts()

# Testing removing an art and removing an event
print("")
print("Museum after removing two events and one art piece: ")
# We will keep the art piece in storage just in on display
museum1.removeArtPerm(art2)
# We will remove the exhibition permanently
museum1.removeEvent(exhibition1)
# We will remove the special event from one location and make it unavailable.
museum1.removeEventOut(special1)
museum1.displayMuseum()
museum1.displayEvents()
museum1.displayArts()

# Everything works as intended
print ("As you can see, the art is in storage now as intended.")
print ("We can also see that the exhibition is completely gone, while the special event is unavailable.")