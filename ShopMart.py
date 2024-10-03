class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def display_info(self):
        print(f"{self.name}: ${self.price:.2f}, Quantity: {self.quantity}")

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.order_history = []

    def add_order(self, order):
        self.order_history.append(order)

    def display_info(self):
        print(f"Customer Name: {self.name}")
        print(f"Email: {self.email}")
        print("Order History:")
        for order in self.order_history:
            print(f"   {order}")

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def checkout(self, customer):
        order = f"{customer.name}'s Order:"
        total_price = 0
        for product in self.products:
            order += f"\n   {product.name}: ${product.price:.2f}"
            total_price += product.price
            product.update_quantity(product.quantity - 1)
        order += f"\nTotal: ${total_price:.2f}"
        customer.add_order(order)
        self.products = []

def process_order(product, quantity):
    try:
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        if quantity > product.quantity:
            raise ValueError("Insufficient product quantity.")
        product.quantity -= quantity
        print(f"Order processed: {quantity} {product.name}(s)")
    except ValueError as ve:
        print(f"Error: {ve}")

def save_to_file(filename, content):
    with open(filename, "a") as file:
        file.write(content + "\n")

def load_from_file(filename):
    data = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            data.append(line.strip())
    return data

def generate_sales_report(customers):
    total_revenue = 0
    products_sold = {}
    for customer in customers:
        for order in customer.order_history:
            lines = order.split("\n")
            total_price = float(lines[-1].split(": $")[1])
            total_revenue += total_price
            for line in lines[1:-1]:
                product_name = line.split(": $")[0]
                if product_name in products_sold:
                    products_sold[product_name] += 1
                else:
                    products_sold[product_name] = 1
    print("Sales Report:")
    print(f"Total Revenue: ${total_revenue:.2f}")
    print("Most Popular Products:")
    for product, quantity in products_sold.items():
        print(f"   {product}: {quantity} sold")

def main():
    products = []
    customers = []

    while True:
        print("\nE-Commerce Management System")
        print("1. Add Product")
        print("2. Add Customer")
        print("3. Process Order")
        print("4. Generate Sales Report")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            products.append(Product(name, price, quantity))
            print("Product added successfully.")

        elif choice == 2:
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            customers.append(Customer(name, email))
            print("Customer added successfully.")

        elif choice == 3:
            customer_name = input("Enter customer name: ")
            product_name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            customer = next((c for c in customers if c.name == customer_name), None)
            product = next((p for p in products if p.name == product_name), None)
            if customer and product:
                cart = Cart()
                cart.add_product(product)
                cart.checkout(customer)
                print("Order processed successfully.")
            else:
                print("Customer or product not found.")

        elif choice == 4:
            generate_sales_report(customers)

        elif choice == 5:
            break

if __name__ == "__main__":
    main()
