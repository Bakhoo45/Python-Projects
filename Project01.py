#Madlib game
#This is a simple madlib game where the user can input words to create a story.
print("Welcome to the Madlib game!")
print("Please enter the following words:")

adjective1 = input("Adjective: ")
adjective2 = input("Another Adjective: ")
noun1 = input("Noun: ")
noun2 = input("Another Noun: ")
verb1 = input("Verb: ")
verb2 = input("Another Verb: ")

story = f"Once upon a time, there was a {adjective1} {noun1} that loved to {verb1}. " \
        f"One day, it met a {adjective2} {noun2} and they decided to {verb2} together."

print("\nHere is your story:")
print(story)
