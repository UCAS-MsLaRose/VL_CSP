#VL, Hangman 
import random 

#Create a list of 10 words on a seperate txt file

# create another file holds win/loss counts 

# Use split(",") on the content of the words txt document to create your list of words

#Pull win and lose totals from the other txt file and save them as 2 seperate variables 

#Build the hangman game

# save the correct word as a varaible random.choice(name of the list)
# number of wrong guesses
# What letters have been guessed 


# Function to display the hangman (Needs number of wrong guesses)
"""_______
   |     |
   |     O
   |    /|\\
   |    / \\
   |_________
"""

# Function to show the letters and spaces (The correct word, letters that have been guessed)
# loop over the corect word
    # varible for display word (starts as an empty string)
    #check if letter has been guessed
        #then add the letter to the display word
    # if they haven't guessed the letter 
        # add an underscore to the display word 
 #return the finished display word (outside of the loop)


 # Main game loop (while True)
    # call function to show hangman
    # print function call to show display word
    # create variable and ask user to guess a letter
    # add the letter to list of guessed letters
    # check if not letter in word:
        # increase incorrect guesses
    # check if display word is same as the word
        # Tell user they won!
        #increase win total
        #ask if they want to play again
            #reset random word, rest wrong guess count
    #check to see if they lost (if thay have 6 wrong guesses)
        #Tell them they lost
        #tell them what the word was
        #Increase the lost count
        #ask if they want to play again
                    #reset random word, rest wrong guess count