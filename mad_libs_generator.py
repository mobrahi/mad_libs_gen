# Simple Mad Libs Generator - Beginner Version

print("=" * 40)
print("   WELCOME TO MAD LIBS GAME!")
print("=" * 40)

# Get words from the user
print("\nGive me some words, and I'll make a silly story!\n")

color = input("Enter a color: ")
animal = input("Enter an animal: ")
verb = input("Enter a verb (action word): ")
food = input("Enter a type of food: ")
friend = input("Enter a friend's name: ")

# Create the story using the words
story = f"""
One day, a {color} {animal} was walking through the park.
Suddenly, it started to {verb} very fast!
"I'm hungry!" said the {animal}.
So it ate a giant {food} in one bite.
Just then, {friend} showed up and said,
"That's my {food}! Oh well, let's share!"
They became best friends and ate {food} together every day.
"""

# Display the story
print("\n" + "=" * 40)
print("   YOUR SILLY STORY!")
print("=" * 40)
print(story)
print("=" * 40)