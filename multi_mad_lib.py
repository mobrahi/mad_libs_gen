import random
import time

def print_slow(text):
    """Print text with a typing effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def get_word(prompt):
    """Get a word from the user with validation"""
    while True:
        word = input(f"Enter a {prompt}: ").strip()
        if word:  # Check if input is not empty
            return word
        print("Please enter a word!")

def story1():
    """Funny story about a day at the beach"""
    print_slow("\n📖 STORY 1: A Day at the Beach 🏖️\n")
    
    # Get words from user
    adjective = get_word("funny adjective")
    noun = get_word("plural noun")
    verb = get_word("verb ending in -ing")
    animal = get_word("animal")
    food = get_word("type of food")
    celebrity = get_word("celebrity name")
    
    # Create the story
    story = f"""
    🌊 THE CRAZIEST BEACH DAY EVER! 🌊
    
    Last summer, I went to the beach with my {adjective} friends.
    We brought our {noun} to play in the sand.
    Suddenly, I saw a {animal} {verb} towards our stuff!
    
    It stole my {food} and ran away!
    Then {celebrity} appeared and chased the {animal} down the beach.
    
    Everyone started laughing so hard that water came out of their noses!
    It was the best beach day of my life!
    """
    
    return story

def story2():
    """Space adventure story"""
    print_slow("\n🚀 STORY 2: Space Adventure 🌟\n")
    
    # Get words from user
    color = get_word("color")
    noun1 = get_word("noun")
    noun2 = get_word("another noun")
    verb = get_word("verb")
    number = get_word("number")
    adjective = get_word("adjective")
    
    story = f"""
    🪐 MY SPACE ADVENTURE 🪐
    
    Mission Control: "Astronaut, report your status!"
    Me: "I see a {color} {noun1} floating in space!"
    
    Suddenly, aliens appeared riding on {noun2}!
    They wanted to {verb} with me, so I offered them {number} cookies.
    
    The aliens were so {adjective} that they became my friends forever!
    We had a dance party on the moon until morning.
    
    BEST. SPACE. MISSION. EVER.
    """
    
    return story

def story3():
    """Magical forest story"""
    print_slow("\n🧙 STORY 3: The Magic Forest 🌲\n")
    
    # Get words from user
    adjective1 = get_word("magical adjective")
    animal = get_word("animal")
    verb = get_word("verb")
    noun = get_word("noun")
    adjective2 = get_word("adjective")
    place = get_word("place")
    
    story = f"""
    🌟 THE MAGIC FOREST 🌟
    
    Deep in the {adjective1} forest, I met a talking {animal}.
    "Would you like to {verb} with me?" they asked.
    I nodded, and suddenly we were flying on a giant {noun}!
    
    We landed in {place}, where everything was made of candy.
    It was the most {adjective2} adventure I've ever had!
    
    The talking {animal} became my best friend forever.
    """
    
    return story

def display_story(story):
    """Display the completed story with formatting"""
    print("\n" + "="*50)
    print("🎭 YOUR MAD LIBS STORY 🎭")
    print("="*50)
    print_slow(story)
    print("="*50 + "\n")

def main():
    """Main game loop"""
    print("="*50)
    print("🎉 WELCOME TO MAD LIBS GENERATOR! 🎉")
    print("="*50)
    print("\nIn Mad Libs, you'll provide words to fill in the blanks,")
    print("and then we'll create a hilarious story using your words!\n")
    
    while True:
        # Show menu
        print("\n📚 CHOOSE A STORY:")
        print("1. 🌊 Crazy Beach Day")
        print("2. 🚀 Space Adventure")
        print("3. 🧙 Magic Forest")
        print("4. 🎲 Random Story")
        print("5. 👋 Exit")
        
        # Get user choice
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            story = story1()
            display_story(story)
        elif choice == "2":
            story = story2()
            display_story(story)
        elif choice == "3":
            story = story3()
            display_story(story)
        elif choice == "4":
            stories = [story1, story2, story3]
            random_story = random.choice(stories)
            story = random_story()
            display_story(story)
        elif choice == "5":
            print_slow("\n👋 Thanks for playing Mad Libs! Come back soon!\n")
            break
        else:
            print("\n❌ Invalid choice! Please enter 1-5.\n")
        
        # Ask if user wants to play again
        if choice != "5":
            again = input("\nWant to create another story? (yes/no): ").strip().lower()
            if again not in ['yes', 'y']:
                print_slow("\n👋 Thanks for playing! Goodbye!\n")
                break

# Run the game
if __name__ == "__main__":
    main()