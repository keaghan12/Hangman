#This is the first game project I am working on myself. The comments were just me reminding myself what everything does so I could come back and understand if I needed to.


allLetters = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]#all acceptable letters to guess

z = 0
v = 0
validWord = True


wordToGuess = input("Type the word to guess into the console:")#creates a variable storing the word that is being guessed

while validWord:#confirms the word has no numbers or special characters. Asks for re-input if the word entered did.
    wordToGuess = wordToGuess.lower()
    listOfLetters = list(wordToGuess)  # splits the word into a list of letters
    invalidWord = False
    for i in range(len(listOfLetters)):
        if listOfLetters[i] not in allLetters:
            invalidWord = True
            break
        elif i == len(listOfLetters)-1:
            validWord = False
    if invalidWord == True:
        wordToGuess = input("Please do not use numbers or special characters. \nType the word to guess into the console:")

listGuessed = []
listOfWords = wordToGuess.split()#this splits the phrase inputted into a list of words. This is used to space the word output in the window.

spaceList = "c a tthiscanliterallysayanythingm" #I know this is really dumb but I don't know how to check if something is a space or not so I just made a space to reference
space = list(spaceList)#this just stores the space from the previous string as a value to reference.

outputListOfLetters = listOfLetters.copy()#creates a second list of letters that is identical to the first. This new list can be modified without losing the original data.
for n in range(len(listOfLetters)):
    outputListOfLetters[n] = "_"#this sets every value from the copy list to be an underscore by default (to show underscores in the front end before letters are guessed)

while z == 0:#needed a kill switch for the loop, didn't know how to end the entire function from within a nested loop.
    for i in range(26):#maximum of 26 letters could be included in the word. Loop can cycle up to once per letter.
        for m in range(len(listOfLetters)):#this runs through each of the characters in the word being guessed
            if listOfLetters[m] == space[1]:#checks if the value ^ is a space
                if v == 0:#another kill switch.
                    outputListOfLetters[m] = listOfLetters[m]#Replaces value with space if it is a space.
        wordPrinted = ''.join(outputListOfLetters)#converts list back to a string for convenience when printing.
        if v == 0:
            print(wordPrinted)
            letter = input("Guess a letter:")#introduces variable for the letter being guessed.
            letter = letter.lower()#makes it so that each letter must not be guessed twice, (cap/lowercase)
            if letter == wordToGuess: #At this point the variable could still be a string, this allows the user to guess the full word.
                wordPrinted = wordToGuess#if the guess is right, the front end list gets filled in.
                v+=1#ks operation
                z+=1
                if len(listOfWords) == 1:
                    print("You guessed the word! It was %s!" %(wordToGuess))
                else:
                    print("You guessed the phrase! It was %s!" %(wordToGuess))

        if letter in allLetters:#if the letter is contained in the list "all letters" -- this is just a list of every letter.
            if letter in listGuessed:
                if v == 0:
                    print("This letter was already guessed")
            else:
                listGuessed.append(letter)
            for j in range(len(listOfLetters)):#loops once per character in the phrase -- redundant I think.
                if listOfLetters[j] == letter:#checks if the letter at each index = the letter guessed.
                    outputListOfLetters[j] = letter#replaces front end letter in list.
                    wordPrinted = ''.join(outputListOfLetters)#compresses list back into string for front end.
                    if wordPrinted == wordToGuess:#checks if the whole word has been guessed yet.
                        if v == 0:
                            if len(listOfWords) == 1:
                                print("You guessed the word! It was %s!" %(wordToGuess))
                            else:
                                print("You guessed the phrase! It was %s!" %(wordToGuess))
                            z+=1
                            v+=1



        elif letter not in allLetters:#if the program makes it through the loop 26 times, the guessed character is not one of the 26 possible letters.
            if v == 0:
                print("Invalid letter.")
