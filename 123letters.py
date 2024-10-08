#TheEnd

print("This is the letter counter APP =D")

#Get user input
name = input("\nWhat is your name: ").title().strip()
print("Hello, " + name + "!")

print("I will count the number of times that a specific letter accurs in a message.")
message = input("\nPlease enter a message: ")
letter = input("which letter would you like to count the occurrences of: ")

#Standardize the format
message = message.lower()
letter = letter.lower()

letter_count = message.count(letter)
print("\n" + name + ", you have " + str(letter_count) + " "
+ letter + "'s in your message^^")


