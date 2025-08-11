#class for bus , what does bus should have 

class Bus:
    # this class is for bus here we define what Bus should has 

    def __init__(self , route ,seats , price , bus_id  ):
        #Route mean the path of bus , seats mean the chair that you take 
        # it on bus for seat, price is 
      # that you pay for our trip,nus od is the bus you use that id like plat
        self.route = route
        self.seats = seats
        self.price = price 
        self.bus_id = bus_id 

        self.booked = 0
        self.passenger = []

    # info about bus 
    def Show_bus_info(self):
        print(f"Route : {self.route} Seats : {self.seats} booked : {self.booked} Price : {self.price}") 

    # how to book seats 
    def book_seats(self,name):
         if self.booked < self.seats:
          self.booked += 1
          self.passenger.append(name)
          print(f"Seats booked for {name} Ticket price is {self.price}")
         else:
            print("no Seats avalibles please wait fo next bus ")

    def Cencel_booking(self,name):
        if name in self.passenger:
            self.passenger.remove(name)  
            self.booked -= 1
            print(f"booking  for {name} has been canceled ") 

        else:
            print(f"we didnt find at the name of {name } in our system .") 

# class for system of bus 

class Bus_system:
    def __init__(self):
        self.buses = []

    # i add herew a new bus 
    def add_bus(self , route ,seats , price , bus_id ):
        self.buses.append(Bus(route ,seats , price , bus_id ))
        print(f"added new bus added id is{bus_id} ")

    #show all bus we have 

    def Show_bus(self):
        for indx,bus in enumerate(self.buses , 1 ):
            print(f"{indx}. ", end="")
            bus.Show_bus_info()

    # book a new seat for passsenger on bus 
    def book_bus_seat(self,index,name):
        if 0<= index < len(self.buses):
            self.buses[index].book_seats(name)

        else:

            print("Invalid bus selection .")

    def delete_bus_by_id(self, bus_id):
        for bus in self.buses:
            if bus_id == bus.bus_id:
                self.buses.remove(bus)
                print(f"Bus with id {bus_id} has been deleted from our system .")

                return
        print("Bus not found with the id provided . please try againg or check the id .")

    def find_bus_by_id(self,bus_id):
        for bus in self.buses:
            if bus.bus_id == bus_id:
                return bus 
        return None 
    

# main menu for bus 

def main():
    system = Bus_system()

    while True:
        print("\n1. Add bus")
        print("2. Show buses")
        print("3. Book seat")
        print("4. Cancel booking")
        print("5. Delete bus by ID")
        print("6. Exit")

        choice = input("Select: ")

        if choice == "1":
            route = input("Route: ")
            seats = int(input("Seats: "))
            price = float(input("Price: "))
            bus_id = input("Bus ID: ")
            system.add_bus(route, seats, price, bus_id)

        elif choice == "2":
            system.Show_bus()

        elif choice == "3":
            index = int(input("Bus index (starting from 0): "))
            name = input("Passenger name: ")
            system.book_bus_seat(index, name)

        elif choice == "4":
            bus_id = input("Bus ID: ")
            bus = system.find_bus_by_id(bus_id)
            if bus:
                name = input("Passenger name to cancel: ")
                bus.Cencel_booking(name)
            else:
                print("Bus not found.")

        elif choice == "5":
            bus_id = input("Bus ID: ")
            system.delete_bus_by_id(bus_id)

        elif choice == "6":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()      

        