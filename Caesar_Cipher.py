def caesar_cipher(text, shift, mode):
    result = ""
    # Loop through every single letter the user typed
    for char in text:
        # Check if it's an alphabetical letter
        if char.isalpha():
            # Figure out the math to shift the letter
            shift_amount = shift if mode == "encrypt" else -shift
            start = ord('a') if char.islower() else ord('A')

            # Shift the letter and wrap around the alphabet
            new_char = chr((ord(char) - start + shift_amount) % 26 + start)
            result += new_char
        else:
            # If it's a space or punctuation, leave it alone
            result += char
    return result


# --- This is the User Interface part ---
print("Welcome to the Caesar Cipher!")
# Get input from the user
user_text = input("Type your message: ")
user_shift = int(input("Enter a shift number (e.g., 3): "))
user_mode = input("Type 'encrypt' or 'decrypt': ").lower()

# Run the function and print the result
final_message = caesar_cipher(user_text, user_shift, user_mode)
print("Your final message is:", final_message)