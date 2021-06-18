import random
from pprint import pprint
import sys

#______begin coin flip game_____
class Coin_flip_game:
    
        def __init__(self):
            self.coins = 100
            self.round_count = 0
            self.coin_options = ["heads", "tails"]
            self.possible_answers = ["yes", "no"]

#common practice is to define "getters" (return status of variable, player should be able to do) 
#and "setters" (change a variable, often don't want players to be able to do this)      
        def get_coins(self):
            return self.coins
        
        def add_round(self):
            self.round_count += 1

        def get_round(self):
            return self.round_count
        
        def add_coins(self, new_amount):
            self.new_amount = self.wager
            self.coins += self.new_amount
            return self.coins

        def subtract_coins(self, new_amount):
            self.new_amount = self.wager
            self.coins -= self.new_amount
            return self.coins

#function to start a game        
        def start_game(self):
            self.answer = input("Would you like to play a game of chance? (yes/no) ")
            while self.answer not in self.possible_answers:
                print("invalid choice. ")
                self.answer = input("Would you like to play a game of chance? (yes/no) ")
            
            if self.answer == "yes":
                self.game_round()
            
            elif self.answer == "no":
                print("So long!")
                quit()

#function to initiate a coin flip        
        def flip(self):
            flip = random.choice(self.coin_options)
            return flip

#function to initiate a loaded flip:
        def loaded_flip(self):
            if self.guess == self.coin_options[0]:
                self.result = self.coin_options[1]
                return self.result
            elif self.guess == self.coin_options[1]:
                self.result = self.coin_options[0]
                return self.result

#function to run one entire coin flip, modify the coin amount, and count the number of rounds.
#if there are still coins, runs a function to start a new round         
        def game_round(self):
            
            print("You have {coin} coins".format(coin = self.coins))
            
            try:
                self.wager = int(input("How many coins will you wager? The table minimum is 10 coins. "))
                while self.wager < 10:
                    print("The table limit is 10. Please wager at least 10 coins.")
                    self.wager = int(input("How many coins will you wager? The table minimum is 10 coins. "))
            except ValueError:
                print("Please enter a number.")
                self.wager = int(input("How many coins will you wager? The table minimum is 10 coins. "))
                while self.wager < 10:
                    print("The table limit is 10. Please wager at least 10 coins.")
                    self.wager = int(input("How many coins will you wager? The table minimum is 10 coins. "))

            self.guess = input("Will you choose heads or tails? ")
            
            self.result = self.flip()
            
            while self.guess not in self.coin_options:
                print("Invalid choice.")
                self.guess = input("Will you choose heads or tails? ")
                
            if self.guess in self.coin_options:
                if self.guess == self.result:
                    self.add_coins(self.wager)
                else:
                    self.subtract_coins(self.wager)
            
            print("The coin landed on {result}!".format(result = str(self.result)))
            
            print("You now have {coin} coins".format(coin = self.coins))

                       
            self.count = self.add_round()

            self.check = self.coin_check()
            
            self.next = self.new_round()

#a function to start a new round            
        def new_round(self):
            answer1 = input("You have played " + str(self.round_count) + " rounds. Would you like to play again? (yes/no) ")

            while answer1 not in self.possible_answers:
                print("Invalid choice. ")
                answer1 = input("Would you like to play again? (yes/no) ")
            
            if answer1 == "yes":
                self.round_monitor()
                self.game_round()
            
            elif answer1 == "no":
                self.coin_check()
                print("Thanks for playing!")
                self.end_game()


#function to monitor round count and initiate losses after 5 rounds.
        def round_monitor(self):
            if self.round_count >= 5:
                self.losing_round()

#function to run a losing game round
        def losing_round(self):
            print("You have {coin} coins".format(coin = self.coins))
            
            try:
                self.wager = int(input("How many coins will you wager? The table minimum is 10 coins. "))
                while self.wager < 10:
                    print("The table limit is 10. Please wager at least 10 coins.")
                    self.wager = int(input("How many coins will you wager? The table minimum is 10 coins. "))
            except ValueError:
                print("Please enter a number.")
                self.wager = int(input("How many coins will you wager? The table minimum is 10 coins. "))

            self.guess = input("Will you choose heads or tails? ")
            
            self.result = self.loaded_flip()
            
            while self.guess not in self.coin_options:
                print("Invalid choice.")
                self.guess = input("Will you choose heads or tails? ")
                
            if self.guess in self.coin_options:
                if self.guess == self.result:
                    self.add_coins(self.wager)
                elif self.guess != self.result:
                    self.subtract_coins(self.wager)
            
            print("The coin landed on {result}!".format(result = str(self.result)))
            
            print("You now have {coin} coins".format(coin = self.coins))

                       
            self.count = self.add_round()

            self.check = self.coin_check()
            
            self.next = self.new_round()

#function to decide course of game based on count of coins.    
        def coin_check(self):
            marker_string = '''You are out of coins! We can issue you a marker so you can continue playing.\n Maybe you'll win your money back! Your luck has to turn eventually.\n
                Would you like to keep playing? (yes/no)
                '''
            if self.coins >= 500:
                print("You have {coin} coins! You've won the game. Thanks for playing!".format(coin = self.coins))
                self.end_game()

            #elif self.coins == 0:
            #    print("You are out of coins! Thanks for playing!")
            #    self.end_game()
 
            elif self.coins <= 0:
                answer2 = input(marker_string)
                if answer2 == "yes":
                    self.losing_round()

                elif answer2 == "no" and self.coins < 0:
                    self.bait_switch(1)
                
                elif answer2 == "no" and self.coins == 0:
                    print("You are out of coins! Thanks for playing!")
                    self.end_game() 

            elif self.coins <= -100:
                self.bait_switch(2)
       

#Function to open the path to the RPG
        def bait_switch(self, option):
            the_situation1 = '''Not so fast, friend! Your coin balance is negative, you owe money to the house. \n
            Don Corleone is a kind man, but he is not running a charity. How will you repay him? Choose a number.
                (1) Double or nothing?
                (2) Attempt to flee without repaying the debt
                (3) I'm really sorry, I just don't have the money. Is there some sort of arrangement that we can work out?
                '''
            
            the_situation2 = '''Wow, friend! You have dug yourself quite the hole here! \n
            Let's stop pretending that you're going win your way out. \n
            How will you repay Don Corleone? Choose a number.
                (2) Attempt to flee without repaying the debt
                (3) I'm really sorry, I just don't have the money. Is there some sort of arrangement that we can work out?
                '''
            
            possible_replies = ["1", "2", "3", "4"]
            if option == 1:
                answer3 = str(input(the_situation1))

            elif option == 2:
                answer3 = str(input(the_situation2))

            while answer3 not in possible_replies:
                answer3 = input('''Invalid choice. Please choose one of the following:
                        (1) Double or nothing?
                        (2) Attempt to flee without repaying the debt
                        (3) I'm really sorry, I just don't have the money. Is there some sort of arrangement that we can work out?''')

            if answer3 == "1":
                    self.double()
                    
            elif answer3 == "2":
                    self.flee()

            elif answer3 == "3":
                    self.other_options()


        def double(self):
            double_string = '''Ok, we can do double or nothing. If you win the toss, your debt is canceled. But if we win the toss, the debt is doubled.\n
            Will you choose heads or tails? '''
            answer4 = input(double_string)
            
            while answer4 not in self.coin_options:
                answer4 = input("Invalid choice. Please choose heads or tails.")
            
            if answer4 == "heads" or answer4 == "tails":
                self.coins = 2 * self.coins
                print("Oh no! You lost. You now owe {coins} coins.".format(coins = self.coins))
                self.bait_switch(2)
        
        
        def flee(self):
            print("option not finished yet.")
            self.end_game()
        
        def other_options(self):
            print("option also not finished yet.")
            self.end_game()
            

#function to end game        
        def end_game(self):
            quit()

new_game = Coin_flip_game()
new_game.start_game()


#___________begin RPG_________
class Main_char:

    def __init__(self, Chealth, Cstrength, Csneakiness, Cintelligence, Cname, Cdebt):
        self.name = Cname
        self.strength = Cstrength
        self.sneakiness = Csneakiness
        self.intelligence = Cintelligence
        self.health = Chealth
        self.debt = Cdebt

#getters and setters for the hero
    def getHealth(self):
        return self.health

    def setHealth(self):
        self.health = newHealth

    def getStrength(self):
        return self.strength

    def setStrength(self):
        self.health = newStrength

    def getSneak(self):
        return self.sneak

    def setSneak(self):
        self.sneak = newSneak

    def getIntel(self):
        return self.intel

    def setIntel(self):
        self.intel = newIntel

    def getName(self):
        return self.name

    def setName(self):
        self.name = newName

    def getDebt():
        return self.debt
        
    def setDebt():
        self.debt = newDebt

 #function to create your character
def createChar():
    create_choices = ["1", "2", "3"]
    print(''' Reluctantly, you have decided to join Don Corleone's crew to work off your debt.
     The next day, you report to the crew HR office to fill out the forms to begin managing your repayment 
     and to receive your benefits. After all, you don't get to be the top criminal organization in this city without 
     some corporate structure! ''')
    charName = str(input("Name? "))
    #ask the person to put address here but never store it- trigger admin asst. to warn the char not to give address,
    #these people are dangerous. Feel sympathy for admin, wonder if they are being extorted also.
    charAddress = str(input("Home address?")) 
    answer = str(input('''How do you prefer to resolve problems? Choose a number:
                        (1) With violence 
                        (2) Create a diversion and sneak away 
                        (3) Cleverly devise a solution
                        '''))
    while answer not in create_choices:
        print("Invalid selection, please try again.")
        answer = str(input('''How do you prefer to resolve problems? Choose a number:
                            (1) With violence 
                            (2) Create a diversion and sneak away 
                            (3) Implement a cleverly thought-out solution
                            '''))

    if answer == "1":
        charStrength = 6
        charSneak = 4
        charInt = 4
    
    elif answer == "2":
        charStrength = 5
        charSneak = 6
        charInt = 4

    elif answer == "3":
        charStrength = 4
        charSneak = 5
        charInt = 6        

    charDebt = 100 #self.coins (later will be able to pull this from coin flip game)
    print("Welcome to the crew, " + charName + ". You will be working for Don Corleone until you repay the " + str(charDebt) + ''' coins you owe.
    Here is your HR profile:''')

    return (charStrength, charSneak, charInt, charName, charDebt)

#you can create a long tuple which can be referred to by index in the future.
#char_data = createChar()

#character = Main_char(100, char_data[0], char_data[1], char_data[2], char_data[3], char_data[4])

#pprint(vars(character))

