import random
from graphics import *

def create_window():
    
    window = GraphWin("Hangman!", 500, 500)

    def print_menu():
        print ("-------------------------------------------------------------------------------------------------------------------------------------------")
        print("                                         Hi Welcome to our Hangman Game!                            ")
        print("                  In this game your task will be to guess the correct word before your man is complete")
        print("                        We will give you a hint... all of our words will be related to CS65")
        print ("-------------------------------------------------------------------------------------------------------------------------------------------")
        print("Steps of our game:")
        print("1) Enter a letter you think is correct")
        print("2) If your letter is correct it will appear in the shell, for example if you guessed the letter 'a'  it will print _ a _ _ _ _")
        print("3) If your letter is wrong a body part will appear on your new window")
        print("4) You will get 6 opportunities to guess the word and keep your man alive")
        print("Click start to begin your game")
        print("--------------------------------------------------------------------------------------------------------------------------------------------")
        return None

    print_menu()

    def start_screen():
    
        text_point = Point(250, 250)
    
        text = Text(text_point, "Read Instructions then Click Anywhere on Window")
    
        text.draw(window)
    
        mouse_point = window.getMouse()
    
        if mouse_point:
            text.undraw()
   
        return window

    new_window = start_screen()


    def create_hang():
    
        point1 = Point(250, 125)
        point2 = Point(250, 300)
    
        my_line    = Line(point1, point2)
        my_line.setFill("black")
    
        point3 = Point(250, 125)   # first coord = where line goes
        point4 = Point(190, 125)   
    
        my_line2   = Line(point3, point4)
        my_line2.setFill("black")
    
        point5 = Point(290, 300)
        point6 = Point(210, 300)
    
        my_line3   = Line(point5, point6)
        my_line3.setFill("black")
    
        point7 = Point(190, 140)
        point8 = Point(190, 125)
    
        my_line4   = Line(point7, point8)
        my_line4.setFill("black")
    
        my_line.draw(window)
        my_line2.draw(window)
        my_line3.draw(window)
        my_line4.draw(window)
    
        return window


    def create_head():
    
        cir_center = Point(190, 160)
        cir_radius = 20
        my_cir     = Circle(cir_center, cir_radius)
        my_cir.setFill("blue")
    
        my_cir.draw(window)
    
        return window

    def create_body():
    
        point9 = Point(190, 150)
        point10 = Point(190, 240)
    
        my_body    = Line(point9, point10)
        my_body.setFill("blue")
    
        my_body.draw(window)
    
        return window

    def create_leftleg():
    
        point11 = Point(170, 260)
        point12 = Point(190, 239)
    
        my_leg1 = Line(point11, point12)
        my_leg1.setFill("blue")
    
        my_leg1.draw(window)
    
        return window

    def create_rightleg():
    
        point13 = Point(210, 260)
        point14 = Point(190, 239)
    
        my_leg2    = Line(point13, point14)
        my_leg2.setFill("blue")
    
        my_leg2.draw(window)
        
        return window

    def create_leftarm():
    
        point15 = Point(170, 220)
        point16 = Point(190, 195)
    
        my_arm1    = Line(point15, point16)
        my_arm1.setFill("blue")
    
        my_arm1.draw(window)
    
        return window

    def create_rightarm():
    
        point15 = Point(210, 220)
        point16 = Point(190, 195)
    
        my_arm2 = Line(point15, point16)
        my_arm2.setFill("blue")
    
        my_arm2.draw(window)
    
        return window

    def getRandomWord():
        word = str(random.choice(open("cs_word.txt").read().split()))
        return word


    def displayBoard(missedLetters, correctLetters, secretWord):
        if len(missedLetters) == 0:
            create_hang()
        elif len(missedLetters) == 1:
            create_head()
        elif len(missedLetters) == 2:
            create_body()
        elif len(missedLetters) == 3:
            create_leftarm()
        elif len(missedLetters) == 4:
            create_rightarm()
        elif len(missedLetters) == 5:
            create_leftleg()
        elif len(missedLetters) == 6:
            create_rightleg()
        

        print('Missed Letters:', end=' ')
        for letter in missedLetters:
            print(letter, end=' ')
        print("\n")

        blanks = '_' * len(secretWord)

        for i in range(len(secretWord)):  # replace blanks with correctly guessed letters
            if secretWord[i] in correctLetters:
                blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

        for letter in blanks:  # show the secret word with spaces in between each letter
            print(letter, end=' ')
        print("\n")


    def getGuess(alreadyGuessed):
        while True:
            guess = input('Guess a letter: ')
            guess = guess.lower()
            if len(guess) != 1:
                print('Please enter a single letter.')
            elif guess in alreadyGuessed:
                print('You have already guessed that letter. Choose again.')
            elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                print('Please enter a LETTER.')
            else:
                return guess


    def playAgain():
        return input("\nDo you want to play again? ").lower().startswith('y')



    missedLetters = ''
    correctLetters = ''
    secretWord = getRandomWord()
    gameIsDone = False

    while True:
        displayBoard(missedLetters, correctLetters, secretWord)

        guess = getGuess(missedLetters + correctLetters)

        if guess in secretWord:
            correctLetters = correctLetters + guess

            foundAllLetters = True
            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetters:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('\nYes! The secret word is "' +
                      secretWord + '"! You have won!')
                
                rectangle_point1 = Point(0,0)
                rectangle_point2 = Point(500,500)
    
                rectangle = Rectangle(rectangle_point1, rectangle_point2)
                rectangle.setFill("green")
                rectangle.draw(window)
                
                text_point2 = Point(250, 250)
                text2 = Text(text_point2, "YOU WON! :)")
                text2.draw(window)
                
                gameIsDone = True
        else:
            missedLetters = missedLetters + guess

            if len(missedLetters) == 6:
                displayBoard(missedLetters, correctLetters, secretWord)
                print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' +
                      str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
                rectangle_point1 = Point(0,0)
                rectangle_point2 = Point(500,500)
    
                rectangle = Rectangle(rectangle_point1, rectangle_point2)
                rectangle.setFill("red")
                rectangle.draw(window)
                
                text_point2 = Point(250, 250)
                text2 = Text(text_point2, "YOU DIED! :(")
                text2.draw(window)
                
                gameIsDone = True
                

        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord = getRandomWord()
                window.close()
                create_window()
            else:
                break

create_window()