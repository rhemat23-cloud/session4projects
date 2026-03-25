# Unique Store Visitor Counter using Python Set

def main():
    visitors = set()  # Stores unique visitor names
    print("=== Store Visitor Counter ===")
    print("Type 'exit' to stop entering names.\n")

    while True:
        name = input("Enter visitor name: ").strip()

        # Exit condition
        if name.lower() == "exit":
            break

        # Validate input
        if not name:
            print(" Name cannot be empty. Try again.")
            continue

        # Normalize name for uniqueness (case-insensitive)
        normalized_name = name.lower()

        if normalized_name in visitors:
            print(f"'{name}' already counted as a visitor.")
        else:
            visitors.add(normalized_name)
            print(f" '{name}' added to visitor list.")

    # Final output
    print("\n=== Visitor Summary ===")
    print(f"Total unique visitors: {len(visitors)}")
    print("Visitor names:")
    for v in sorted(visitors):
        print(f"- {v.capitalize()}")

if __name__ == "__main__":
    main()
