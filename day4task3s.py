# shopping_cart.py

# -----------------------------
# ammu Shopping Cart System
# -----------------------------

# Predefined product catalog (id: (name, price))
PRODUCTS = {
    1: ("carrot", 30.0),
    2: ("tomato", 10.0),
    3: ("Milk", 45.0),
    4: ("Bread", 25.0),
    5: ("Eggs (Dozen)", 60.0),
    6:("choclate",25)
}

# Shopping cart dictionary (id: quantity)
cart = {}

def display_products():
    """Display available products."""
    print("\nAvailable Products:")
    print("-" * 40)
    for pid, (name, price) in PRODUCTS.items():
        print(f"{pid}. {name} - ₹{price:.2f}")
    print("-" * 40)

def add_to_cart():
    """Add a product to the cart."""
    try:
        pid = int(input("Enter product ID to add: "))
        if pid not in PRODUCTS:
            print(" Invalid product ID.")
            return
        qty = int(input("Enter quantity: "))
        if qty <= 0:
            print(" Quantity must be positive.")
            return
        cart[pid] = cart.get(pid, 0) + qty
        print(f" Added {qty} x {PRODUCTS[pid][0]} to cart.")
    except ValueError:
        print("Please enter valid numbers.")

def remove_from_cart():
    """Remove a product from the cart."""
    try:
        pid = int(input("Enter product ID to remove: "))
        if pid not in cart:
            print(" Product not in cart.")
            return
        qty = int(input("Enter quantity to remove: "))
        if qty <= 0:
            print(" Quantity must be positive.")
            return
        if qty >= cart[pid]:
            del cart[pid]
            print("️ Product removed from cart.")
        else:
            cart[pid] -= qty
            print(f" Removed {qty} from {PRODUCTS[pid][0]}.")
    except ValueError:
        print(" Please enter valid numbers.")

def view_cart():
    """Display cart contents."""
    if not cart:
        print("\n Your cart is empty.")
        return
    print("\nYour Cart:")
    print("-" * 40)
    total = 0
    for pid, qty in cart.items():
        name, price = PRODUCTS[pid]
        subtotal = price * qty
        total += subtotal
        print(f"{name} x {qty} = ₹{subtotal:.2f}")
    print("-" * 40)
    print(f"Total: ₹{total:.2f}")

def checkout():
    """Checkout and display final bill."""
    if not cart:
        print(" Your cart is empty. Nothing to checkout.")
        return
    view_cart()
    print("\n Processing payment...")
    print("Payment successful. Thank you for shopping!")
    cart.clear()

def main():
    """Main menu loop."""
    while True:
        print("\n=== Shopping Cart Menu ===")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")
        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            display_products()
        elif choice == "2":
            display_products()
            add_to_cart()
        elif choice == "3":
            view_cart()
            remove_from_cart()
        elif choice == "4":
            view_cart()
        elif choice == "5":
            checkout()
        elif choice == "6":
            print(" Goodbye!")
            break
        else:
            print(" Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
