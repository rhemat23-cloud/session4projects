# Number Utility Tool in Python

def convert_number(num):
    """Convert number to binary, octal, and hexadecimal."""
    return {
        "binary": bin(num),
        "octal": oct(num),
        "hexadecimal": hex(num)
    }

def format_with_commas(num):
    """Format large numbers with commas."""
    return f"{num:,}"

def scientific_notation(num):
    """Return number in scientific notation."""
    return f"{num:.6e}"  # 6 decimal places

def main():
    try:
        # Input from user
        user_input = input("Enter an integer: ").strip()
        
        # Validate integer input
        if not user_input.lstrip('-').isdigit():
            raise ValueError("Invalid input. Please enter a valid integer.")
        
        num = int(user_input)

        # Perform conversions
        conversions = convert_number(num)
        formatted = format_with_commas(num)
        sci_notation = scientific_notation(num)

        # Display results
        print("\n--- Number Utility Tool ---")
        print(f"Original Number: {num}")
        print(f"Binary: {conversions['binary']}")
        print(f"Octal: {conversions['octal']}")
        print(f"Hexadecimal: {conversions['hexadecimal']}")
        print(f"Formatted with commas: {formatted}")
        print(f"Scientific Notation: {sci_notation}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
