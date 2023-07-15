import os
os.system("cls")
# Get input from the user
name = input("Enter a name: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")

# Create the story using f-strings
story = f"Once upon a time, there was a person named {name}. {name} found a {noun} and decided to {verb} it. It was a {adjective} experience."

# Print the story
print(story)
