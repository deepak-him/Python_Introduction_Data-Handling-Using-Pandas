# Define a class for Product
class Product:
    # Constructor for Product class, initializes name, price, and quantity
    def __init__(self, name, price, quantity):


    # Method to update the quantity of a product
    def update_quantity(self, new_quantity):


    # Method to display product information
    def display_info(self):


# Define a class for Customer
class Customer:
    # Constructor for Customer class, initializes name, email, and order_history
    def __init__(self, name, email):

        self.order_history = []

    # Method to add an order to a customer's order history
    def add_order(self, order):
        self.order_history.append(order)

    # Method to display customer information
    def display_info(self):
        print(f"Customer Name: {self.name}")
        print(f"Email: {self.email}")
        print("Order History:")
        for order in self.order_history:
            print(f"   {order}")

# Define a class for Cart
class Cart:
    # Constructor for Cart class, initializes products as an empty list
    def __init__(self):
        self.products = []

    # Method to add a product to the cart
    def add_product(self, product):


    # Method to process a checkout and create an order
    def checkout(self, customer):

        
        
        
        
        
        customer.add_order(order)
        self.products = []

# Function to process an order
def process_order(product, quantity):
    try:
        # Check if quantity is not positive
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        # Check if there is insufficient product quantity
        if quantity > product.quantity:
            raise ValueError("Insufficient product quantity.")
        # Update product quantity and print order processed message
        product.quantity -= quantity
        print(f"Order processed: {quantity} {product.name}(s)")
    except ValueError as ve:
        # Handle ValueError and print an error message
        print(f"Error: {ve}")

# Function to save content to a file
def save_to_file(filename, content):
    # Open the file in append mode and write content to it
    with open(filename, "a") as file:
        file.write(content + "\n")

# Function to load content from a file
def load_from_file(filename):
    data = []
    # Open the file in read mode, read lines, and append them to data
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            data.append(line.strip())
    return data

# Function to generate a sales report
def generate_sales_report(customers):
    total_revenue = 0
    products_sold = {}
    # Iterate over customers and their order history
    for customer in customers:
        for order in customer.order_history:
            lines = order.split("\n")
            total_price = float(lines[-1].split(": $")[1])
            total_revenue += total_price
            # Iterate over order lines and track product sales
            for line in lines[1:-1]:
                product_name = line.split(": $")[0]
                if product_name in products_sold:
                    products_sold[product_name] += 1
                else:
                    products_sold[product_name] = 1
    # Print the sales report
    print("Sales Report:")
    print(f"Total Revenue: ${total_revenue:.2f}")
    print("Most Popular Products:")
    for product, quantity in products_sold.items():
        print(f"   {product}: {quantity} sold")

# Main program
def main():
    products = []  # List to store product objects
    customers = []  # List to store customer objects

    while True:
        print("\nE-Commerce Management System")
        print("1. Add Product")
        print("2. Add Customer")
        print("3. Process Order")
        print("4. Generate Sales Report")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Prompt user to enter product details and create a Product object
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            # write your code here
            print("Product added successfully.")

        elif choice == 2:
            # Prompt user to enter customer details and create a Customer object
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            # write your code here
            print("Customer added successfully.")

        elif choice == 3:
            # Process an order by updating product quantity and creating an order for a customer
            customer_name = input("Enter customer name: ")
            product_name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            # write your code here

        elif choice == 4:
            # Generate and display a sales report
            # write your code here

        elif choice == 5:
            # Exit the program
            break

if __name__ == "__main__":
    main()
