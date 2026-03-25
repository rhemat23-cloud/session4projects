# String Formatting Utility

# Step 1: Take inputs
name = input("Enter your name: ")
product = input("Enter the product name: ")

# Step 2: Create a formatted sentence using f-string
sentence = f"Hello {name}, your product '{product}' is ready for pickup!"
print("\nFormatted Sentence:")
print(sentence)

# Step 3: Show padded output
print("\nPadded Output Examples:")
print(f"Left aligned  : {sentence.ljust(60, '-')}")
print(f"Right aligned : {sentence.rjust(60, '-')}")
print(f"Center aligned: {sentence.center(60, '-')}")
