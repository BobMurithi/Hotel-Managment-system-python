class hotelfarecal:
    def __init__(self):
        self.room_rent = 0
        self.restaurant_bill = 0
        self.laundry_bill = 0
        self.game_bill = 0
        self.service_charge = 1800
        self.name = ""
        self.address = ""
        self.check_in_date = ""
        self.check_out_date = ""
        self.room_number = 101

    def inputdata(self):
        self.name = input("\nEnter your name: ")
        self.address = input("Enter your address: ")
        self.check_in_date = input("Enter your check-in date: ")
        self.check_out_date = input("Enter your check-out date: ")
        print("Your room number:", self.room_number)

    def roomrent(self):
        print("\nWe have the following rooms for you:")
        print("1. Room type A ----> Rs 6000 per night")
        print("2. Room type B ----> Rs 5000 per night")
        print("3. Room type C ----> Rs 4000 per night")
        print("4. Room type D ----> Rs 3000 per night")

        room_choice = int(input("Enter your room type (1-4): "))
        nights = int(input("Enter the number of nights: "))

        room_rates = {1: 6000, 2: 5000, 3: 4000, 4: 3000}
        room_names = {
            1: "A",
            2: "B",
            3: "C",
            4: "D",
        }

        if room_choice not in room_rates:
            print("Please choose a valid room type.")
            return
        if nights < 1:
            print("Please enter at least one night.")
            return

        print("You have opted for room type", room_names[room_choice])
        self.room_rent = room_rates[room_choice] * nights
        print("Your room rent is Rs", self.room_rent)

    def restaurentbill(self):
        print("\n***** RESTAURANT MENU *****")
        print("1. Water ----> Rs 20")
        print("2. Tea ----> Rs 10")
        print("3. Breakfast combo ----> Rs 150")
        print("4. Exit")

        menu_prices = {1: 20, 2: 10, 3: 150}
        while True:
            choice = int(input("Enter your choice: "))
            if choice == 4:
                break
            if choice not in menu_prices:
                print("Invalid option.")
                continue

            quantity = int(input("Enter the quantity: "))
            if quantity < 1:
                print("Quantity must be at least 1.")
                continue
            self.restaurant_bill += menu_prices[choice] * quantity

        print("Total food cost is Rs", self.restaurant_bill)

    def laundrybill(self):
        print("\n***** LAUNDRY MENU *****")
        print("1. Shorts ----> Rs 3")
        print("2. Trousers ----> Rs 4")
        print("3. Shirt ----> Rs 5")
        print("4. Jeans ----> Rs 6")
        print("5. Girls suit ----> Rs 8")
        print("6. Exit")

        menu_prices = {1: 3, 2: 4, 3: 5, 4: 6, 5: 8}
        while True:
            choice = int(input("Enter your choice: "))
            if choice == 6:
                break
            if choice not in menu_prices:
                print("Invalid option.")
                continue

            quantity = int(input("Enter the quantity: "))
            if quantity < 1:
                print("Quantity must be at least 1.")
                continue
            self.laundry_bill += menu_prices[choice] * quantity

        print("Total laundry cost is Rs", self.laundry_bill)

    def gamebill(self):
        print("\n***** GAME MENU *****")
        print("1. Table tennis ----> Rs 60 per hour")
        print("2. Bowling ----> Rs 80 per hour")
        print("3. Snooker ----> Rs 70 per hour")
        print("4. Video games ----> Rs 90 per hour")
        print("5. Pool ----> Rs 50 per hour")
        print("6. Exit")

        menu_prices = {1: 60, 2: 80, 3: 70, 4: 90, 5: 50}
        while True:
            choice = int(input("Enter your choice: "))
            if choice == 6:
                break
            if choice not in menu_prices:
                print("Invalid option.")
                continue

            hours = int(input("Enter the number of hours: "))
            if hours < 1:
                print("Hours must be at least 1.")
                continue
            self.game_bill += menu_prices[choice] * hours

        print("Total game bill is Rs", self.game_bill)

    def display(self):
        subtotal = (
            self.room_rent
            + self.restaurant_bill
            + self.laundry_bill
            + self.game_bill
        )
        grand_total = subtotal + self.service_charge

        print("\n***** HOTEL BILL *****")
        print("Customer details:")
        print("Customer name:", self.name)
        print("Customer address:", self.address)
        print("Check-in date:", self.check_in_date)
        print("Check-out date:", self.check_out_date)
        print("Room number:", self.room_number)
        print("Room rent:", self.room_rent)
        print("Food bill:", self.restaurant_bill)
        print("Laundry bill:", self.laundry_bill)
        print("Game bill:", self.game_bill)
        print("Subtotal bill:", subtotal)
        print("Additional service charges:", self.service_charge)
        print("Grand total bill:", grand_total)


def main():
    print("\n\n***** WELCOME TO HEWING HOTEL *****\n")
    hotel = hotelfarecal()

    while True:
        print("\n1. Enter customer data")
        print("2. Calculate room rent")
        print("3. Calculate restaurant bill")
        print("4. Calculate laundry bill")
        print("5. Calculate game bill")
        print("6. Show total cost")
        print("7. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            hotel.inputdata()
        elif choice == 2:
            hotel.roomrent()
        elif choice == 3:
            hotel.restaurentbill()
        elif choice == 4:
            hotel.laundrybill()
        elif choice == 5:
            hotel.gamebill()
        elif choice == 6:
            hotel.display()
        elif choice == 7:
            print("Thank you. Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
