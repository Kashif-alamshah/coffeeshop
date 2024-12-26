class CoffeeShop:
    def __init__(self, coffee_price, sandwich_price):
        self.coffee_price = coffee_price
        self.sandwich_price = sandwich_price

    def calculate_total(self, wants_coffee, wants_sandwich):
        total = 0
        if wants_coffee:
            total += self.coffee_price
        if wants_sandwich:
            total += self.sandwich_price
        return total

    def process_order(self, customer_name, wants_coffee, wants_sandwich):
        print(f"Processing order for {customer_name}...")
        total = self.calculate_total(wants_coffee, wants_sandwich)
        print(f"Total to pay: ${total:.2f}")
        self.process_payment(total)

    def process_payment(self, amount):
        print(f"Payment of ${amount:.2f} processed. Thank you!")

    def update_menu(self, new_coffee_price, new_sandwich_price):
        self.coffee_price = new_coffee_price
        self.sandwich_price = new_sandwich_price
        print("Menu updated.")


def main():
    coffee_shop = CoffeeShop(4.0, 6.0)
    print("Welcome to the Coffee Shop Application")
    
    coffee_shop.process_order("Kashif", wants_coffee=True, wants_sandwich=False)
    
    coffee_shop.update_menu(5.0, 7.0)
    
    coffee_shop.process_order("Moula", wants_coffee=True, wants_sandwich=True)
    
    print("Thank you for visiting!")


if __name__ == "__main__":
    main()
