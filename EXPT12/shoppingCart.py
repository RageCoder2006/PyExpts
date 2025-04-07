class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ₹{self.price} (Stock: {self.quantity})"


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if product.quantity >= quantity:
            if product.name in self.items:
                self.items[product.name]["quantity"] += quantity
            else:
                self.items[product.name] = {
                    "product": product,
                    "price": product.price,
                    "quantity": quantity
                }
            product.quantity -= quantity
            print(f"Added {quantity} {product.name}(s) to cart.")
        else:
            print(f"Only {product.quantity} {product.name}(s) left in stock.")

    def remove_item(self, product, quantity):
        if product.name in self.items:
            if self.items[product.name]["quantity"] >= quantity:
                self.items[product.name]["quantity"] -= quantity
                product.quantity += quantity
                if self.items[product.name]["quantity"] == 0:
                    del self.items[product.name]
                print(f"Removed {quantity} {product.name}(s) from cart.")
            else:
                print(f"Only {self.items[product.name]['quantity']} {product.name}(s) in cart.")
        else:
            print(f"{product.name} is not in the cart.")

    def calculate_total(self):
        total = 0
        for item in self.items.values():
            total += item["price"] * item["quantity"]
        return total

    def display_cart(self):
        if not self.items:
            print("Cart is empty.")
        else:
            print("\nShopping Cart:")
            for name, item in self.items.items():
                print(f"{name} x {item['quantity']} - ₹{item['price'] * item['quantity']}")
            print(f"Total: ₹{self.calculate_total()}")


class User:
    def __init__(self, name):
        self.name = name
        self.cart = ShoppingCart()

    def checkout(self):
        if self.cart.items:
            print(f"\n{self.name}, your total bill is: ₹{self.cart.calculate_total()}")
            self.cart = ShoppingCart()
            print("Checkout successful!")
        else:
            print("Cart is empty. Nothing to checkout.")


products = [
    Product("Pencil", 10, 5),
    Product("Pen", 50, 10),
    Product("Eraser", 20, 15),
    Product("Sharpener", 2, 10),
    Product("Scale", 5, 20),
    Product("Notebook", 20, 30)
]

user1 = User("Rishit")

while True:
    print("\n==== Shopping Menu ====")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. Remove from Cart")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        print("\nAvailable Products:")
        for i, p in enumerate(products):
            print(f"{i + 1}. {p}")
    elif choice == "2":
        product_no = int(input("Enter product number to add: ")) - 1
        qty = int(input("Enter quantity: "))
        if 0 <= product_no < len(products):
            user1.cart.add_item(products[product_no], qty)
        else:
            print("Invalid product number.")
    elif choice == "3":
        product_no = int(input("Enter product number to remove: ")) - 1
        qty = int(input("Enter quantity to remove: "))
        if 0 <= product_no < len(products):
            user1.cart.remove_item(products[product_no], qty)
        else:
            print("Invalid product number.")
    elif choice == "4":
        user1.cart.display_cart()
    elif choice == "5":
        user1.checkout()
    elif choice == "6":
        print("Thanks for shopping. Goodbye!")
        break
    else:
        print("Invalid choice. Please select from 1 to 6.")
