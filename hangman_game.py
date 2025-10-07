'''
Author: Zikora 
Program title: HangShelly
Program description: This is a game of Hangman, but I called it "HangShelly" so it can be Madeira themed.

This is where you talk about...
- problems you faced and how you solved them
    +My biggest problem was trying to make a list with the letters that were incorrectly guessed so I could show them to the player. I had to do "if player input is not in the word and not in the incorrect guess list, append the playerinput into the incorrect guessed list"
    +I had trouble figuring out how to print the hangmans, but I used a list of lists (before you mentioned it in class)
        I also had to associate the letters_not_guessed scoer to the hangmans so I could just say hangmans[letters_not_guessed] instead of a bunch of if statements
    + For the underscores, I had to research and found out I can use len() and join() to replace the certain place with the player_input if it was in the word
    + I fixed the restart function by setting it up like the error_handling function and creating a list y_or_n

- what you're proud of
    - I'm proud of having the patience to do this
    - Making a funner game than blackjack
    - struggling less on this than the first PA1 because I learnt a lot since then
    - fixing the restart function because I struggled on that 
    - fixing the thigns I struggled on above

- what you'd change or add if you had more time
    + I would make the option after like 3 guesses to guess the word
    + I would do different levels of difficulty for the words (probably with a list of lists)
        I would do like guessing something with two words like "strawberries and cream"
    + I would create a dictionary so each word could be assigned a hint, because it is really hard right now to guess a word with all the different categories
    + I would use try except / find a way to because I didn't really know where to put it
    + I would work more on the error_handling. currently, it works, but not the way I want it to so when you don't type in a letter it
    prints the "Your answer:" but also prints the orignal input in main "Guess a letter:" so, the user would have to type the letter twice



Pledge: I have not given nor received external help on this assignment,
with the exception of the following sources:
- w3schools 
len(): https://www.w3schools.com/python/ref_func_len.asp
join(): https://www.w3schools.com/python/ref_string_join.asp
.lower(): https://www.w3schools.com/python/ref_string_lower.asp
import time: https://www.w3schools.com/Python/ref_module_time.asp
- geeks4geeks
list of lists: https://www.geeksforgeeks.org/python/python-list-of-lists/
- Hangmans
I took it from this https://www.fssnip.net/mO/title/Hangman

'''

#imports
import random
import time #because it's going to fast

#helper function
def error_handling(options =["yes", "no"]):
    print("Error! You must enter ", options)
    print("                                                           ")
    user_choice = input("Your answer: ").lower()
    while user_choice not in options:
        print("Error! You must enter a letter")
        print(letters)
        user_choice = input("Your answer: ").lower()
    return user_choice

#list of words
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
words = ["madeira", "shelly", "lucy", "snail", "escargot","cat", "dog", "lion", "tiger", "zebra", "horse", "sheep", "goat", "mouse", "rat",
"bear", "wolf", "fox", "deer", "eagle", "hawk", "owl", "crow", "swan", "duck",
"whale", "shark", "dolphin", "octopus", "crab", "lobster", "kangaroo", "panda", "giraffe", "crocodile",
"city", "village", "forest", "desert", "island", "ocean", "river", "mountain", "valley", "canyon",
"bridge", "castle", "temple", "palace", "pyramid", "tower", "harbor", "garden", "park", "jungle",
"star", "moon", "sun", "planet", "comet", "asteroid", "galaxy", "universe", "rocket", "orbit",
"telescope", "astronomy", "gravity", "satellite", "meteor", "nebula", "blackhole", "spaceship", "magnet", "triangle",
"rain", "snow", "wind", "storm", "cloud", "fog", "thunder", "lightning", "hurricane", "volcano",
"earthquake", "tsunami", "tornado", "sunrise", "sunset", "flower", "tree", "grass", "riverbank", "oasis",
"book", "game", "coin", "clock", "phone", "chair", "table", "pencil", "paper", "lamp",
"lantern", "mirror", "sword", "shield", "helmet", "crown", "diamond", "jewel", "fortune",
"labyrinth", "skeleton", "adventure", "mystery", "phantom", "potion", "puzzle", "treasure", "unicorn", "voyager",
"apple", "pear", "plum", "peach", "grape", "lemon", "lime", "mango", "melon", "guava",
"papaya", "banana", "orange", "cherry", "apricot", "fig", "kiwi", "berry", "olive", "date",
"coconut", "lychee", "durian", "avocado", "tomato", "pineapple", "pomegranate", "watermelon", "blueberry", "strawberry",
"raspberry", "cranberry", "blackberry", "mulberry", "tangerine", "nectarine", "passionfruit", "jackfruit", "dragonfruit", "starfruit"
] #I asked chatGPT for the words
y_or_n = ["y", "n"]


# hangman stages- took text prints from https://www.fssnip.net/mO/title/Hangman
#list of lists to store hangman stages https://www.geeksforgeeks.org/python/python-list-of-lists/
# had to put \\ because it kept showing an error?
hangmans = [[
    "____",
    "|/   |",
    "|   ",
    "|    ",
    "|    ",
    "|    ",
    "|    ",
    "|_____  ",
],
#testing hangman stages
#for line in hangman1:
    #print(line)
[
    "____",
    "|/   |",
    "|   \\_/",
    "|   (_)",
    "|    ",
    "|    ",
    "|    ",
    "|    ",
    "|_____  ",
],
[
    "____",
    "|/   |",
    "|   \\_/",
    "|   (_)",
    "|    |",
    "|    |",
    "|    ",
    "|    ",
    "|_____  ",
],
[
    "____",
    "|/   |",
    "|   \\_/",
    "|   (_)",
    "|   \\|",
    "|    |",
    "|    ",
    "|    ",
    "|_____  ",
],
[
    "____",
    "|/   |",
    "|   \\_/",
    "|   (_)",
    "|   \\|/",
    "|    |",
    "|    ",
    "|    ",
    "|_____  ",
],
[
    "____",
    "|/   |",
    "|   \\_/",
    "|   (_)",
    "|   \\|/",
    "|    |",
    "|   / ",
    "|    ",
    "|_____  ",
],
[
    "____",
    "|/   |",
    "|   \\_/",
    "|   (_)",
    "|   \\|/",
    "|    |",
    "|   / \\",
    "|    ",
    "|_____  ",
],
[
    "____",
    "|/   |",
    "|   \\_/",
    "|   (_)",
    "|   /|\\",
    "|    |",
    "|   | |",
    "|    ",
    "|_____  ",
]
]

#for styling
# from https://fsymbols.com/generators/
cool_letters = [
    "ＨＡＮＧＳＨＥＬＬＹ​", "𝕐𝕆𝕌 𝕎𝕀ℕ❕", "𝕐𝕆𝕌 𝕃𝕆𝕊𝕋 :("
]


#restart function
def restart(choices = ["yes", "no"]):
    print("___________________________________________________________")
    player_input = input("Do you want to play again? (y)es or (n)o: ").lower()
    while player_input not in choices:
        print("Invalid. Please enter ", choices, ".")
        player_input = input("Do you want to play again? (y)es or (n)o: ").lower()
    if player_input == "y":
        time.sleep(1)
        print("___________________________________________________________")
        print("                                                           ")
        print("                                                           ")
        print("                Restarting....")
        print("                                                           ")
        print("                                                           ")
        time.sleep(1)
        print("                Let's play again!")
        print("                                                           ")
        main()
    elif player_input == "n":
        time.sleep(0.5)
        print("                                                           ")
        print("Thanks for playing!")
        print("        __________________๑ï")
        print("        ꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷")

#main function
def main():
    #random word generator
    random_word = random.choice(words) #had to put it here so that it gives a new word each time
    # for underscors in random word
    hidden_word = []
    #len returns the number of items in an object and I need it to return the number of letters with underscores
    for i in range(len(random_word)):
        hidden_word.append("_")

    #to keep track of letters guessed + not guessed
    letters_guessed = []
    letters_not_guessed_list = []
    letters_not_guessed = 0

    #welcome message
    print("============================================================")
    print("         Hello, welcome to", cool_letters[0])
    for line in hangmans[7]:
        time.sleep(0.3)
        print("                   ", line) 
    print("============================================================")

    #do you know how to play?
    print("                                                           ")
    question = input("         Do you know how to play? (y)es or (n)o: ").lower()
    if question == "n":
        print("                                                           ")
        print("The objective of the game is to guess the word, one letter at a time.")
        time.sleep(2)
        print("You have 7 incorrect guesses before you lose the game.")
        time.sleep(2)
        print("Good luck!")
        time.sleep(1)
        print("============================================================")
        print("                                                           ")
        print("                                                           ")
        print("                Starting Game....")
        print("                                                           ")
        time.sleep(1)
    elif question == "y":
        time.sleep(0.5)
        print("                                                           ")
        print("Great! Let's start! ᯓ ๑ï")
        print("                                                           ")
        print("============================================================")
        time.sleep(1)
        print("                                                           ")
        print("                                                           ")
        print("                Starting Game....")
        print("                                                           ")
        time.sleep(1)
    else:
        error_handling(["y", "n"])

    
    #revealing hidden word
    print("                                                           ")
    print("____________________________________________________________")
    print("                                                           ")
    print("word: ", hidden_word)
    print("                                                           ")
    print("The word has", len(random_word), "letters.")
    print("                                                           ")
    for line in hangmans[0]:
        print(line)
    print("                                                           ")
    print("You have 7 guesses. Good luck!")
    print("                                                           ")
    print("____________________________________________________________")
    time.sleep(2)
    #print(random_word) #for testing purposes

    #game starts here basically
    while "_" in hidden_word:
        print("                                                           ")
        player_input = input("Guess a letter: ").lower()
        time.sleep(1)
        if player_input in random_word:
            if player_input in letters_guessed:
                print("!!________________________________________________________!!")
                print("You already guessed that letter! Try again!")
                print("!!________________________________________________________!!")
            else:
                for i in range(len(random_word)):
                    if random_word[i] == player_input: #if random word [letter] == player input
                        hidden_word[i] = player_input #replace place in hidden word with player_input
                letters_guessed.append(player_input)
                print("                                                           ")
                print("Good job! You guessed a letter!")
                time.sleep(1)
            # .join is to join the replace the underscore with the letter guessed, since underscore is a list random_word
            if "_" in hidden_word:
                print("word: ", ''.join(hidden_word))
                print("You have", 7 - letters_not_guessed, "guess(es) left.", "Reminder: the word has", len(random_word), "letters.")
                print("correct letters guessed so far: ", letters_guessed, " | incorrect letters guessed so far: ", letters_not_guessed_list)
            elif "_" not in hidden_word:
                break

        elif len(player_input) != 1 or player_input not in letters: #if player input is more than 1 letter or is not a letter
            error_handling(letters)
        
        else:
            if player_input not in random_word:
                if player_input in letters_not_guessed_list:
                    print("!!________________________________________________________!!")
                    print("You already guessed that letter! Try again!")
                    print("!!________________________________________________________!!")
                    time.sleep(1)
                else:
                    letters_not_guessed +=1
                    if player_input not in letters_not_guessed_list:
                        letters_not_guessed_list.append(player_input)
                    if letters_not_guessed != 7:
                        print("                                                           ")
                        print("The letter", player_input, "is not in the word.")
                        print("You have", 7 - letters_not_guessed, "guess(es) left.", "Reminder: the word has", len(random_word), "letters.")
                        print("correct letters guessed so far: ", letters_guessed, " | incorrect letters guessed so far: ", letters_not_guessed_list)
                    if letters_not_guessed == 7:
                        print("You have", 7 - letters_not_guessed, "guess(es) left.")
                        time.sleep(1.5)
                        break
            if letters_not_guessed == 7:
                time.sleep(1.5)
                break
            for line in hangmans[letters_not_guessed]:
                time.sleep(0.3)
                print(line)
            print("word: ", ''.join(hidden_word))

    #ending the game
    if "_" not in hidden_word:
        print("                                                           ")
        print("Congratulations, ", cool_letters[1], "! You guessed the word:", random_word)
        print("                                                           ")
        restart(y_or_n)
    else:
        print("____________________________________________________________")
        print("                                                           ")
        print("Sorry, ", cool_letters[2], "! The word was:", random_word)
        print("                                                           ")
        for line in hangmans[7]:  # final hangman stage
            time.sleep(0.3)
            print("                   ", line) 
        restart(y_or_n)

main()

