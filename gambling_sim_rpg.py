import random
#might use at some point, commented out for now:
#from pprint import pprint
import sys

class Coin_flip_game:
    
        def __init__(self):
            self.coins = 100
            self.coin_options = ["heads", "tails"]
            self.possible_answers1 = ["yes", "no"]
            self.possible_answers2 = ["yes", "no", "winnings", "flip results"]
            self.result_history = []
            self.flip_history = []
            self.finished_playing = False

#common practice is to define "getters" (return status of variable, player should be able to do) 
#and "setters" (change a variable, often don't want players to be able to do this)      
        def get_coins(self):
            return self.coins
        
        def get_result_history(self):
            return self.result_history

        def revise_result_hist(self, new_amount):
            self.result_history.append(new_amount)
        
        def revise_flip_history(self, new_result):
            self.flip_history.append(new_result)
        
        def get_flip_history(self):
            return self.flip_history
        
        def add_coins(self, new_amount):
            self.new_amount = self.wager
            self.coins += self.new_amount
            self.revise_result_hist(self.coins)
            return self.coins

        def subtract_coins(self, new_amount):
            self.new_amount = self.wager
            self.coins -= self.new_amount
            self.revise_result_hist(self.coins)
            return self.coins

#function to start a game        
        def start_game(self):
            self.answer = input("Would you like to play a game of chance? (yes/no) ")
            while self.answer.lower() not in self.possible_answers1:
                print("invalid choice. ")
                self.answer = input("Would you like to play a game of chance? (yes/no) ")
            
            if self.answer.lower().strip() == "yes":
                self.game_round()
            
            elif self.answer.lower() == "no":
                print("Goodbye!")

#function to initiate a coin flip        
        def flip(self):
            flip = random.choice(self.coin_options)
            return flip

#function to run one entire coin flip, modify the coin amount, flip records, and winnings history.
#if there are still coins, runs a function to start a new round         
        def game_round(self):
            print("You have {coin} coins".format(coin = self.coins))
            try:
                self.wager = int(input("How many coins will you wager? "))
            except ValueError:
                print("Please enter a number.")
                self.wager = int(input("How many coins will you wager? "))
            self.guess = input("Will you choose heads or tails? ")
            self.result = self.flip()
            self.store_history = self.revise_flip_history(self.result)
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
            self.check = self.coin_check()
            self.next = self.new_round()

#a function to start a new round            
        def new_round(self):
            answer = input("Would you like to play again or see your history? (yes/no/winnings/flip results) ")
            while answer.lower() not in self.possible_answers2:
                print("Invalid choice. ")
                answer = input("Would you like to play again or see your history? (yes/no/winnings/flip results) ")
            
            if answer.lower() == "yes":
                self.game_round()
            
            elif answer.lower() == "no":
                print("Thanks for playing!")
                
            elif answer.lower() == "winnings":
                print(self.get_result_history())
                next_round = self.new_round()
            
            elif answer.lower() == "flip results":
                print(self.get_flip_history())
                next_round = self.new_round()

#function to end game if coins are less than 0        
        def coin_check(self):
            if self.coins <= 0:
                print("You are out of coins! Thanks for playing!")
                sys.exit()
            else:
                pass
#function to end game- not needed?        
        def end_game(self):
            pass
            

class Main_char:

    def __init__(self, Cstrength, Csneakiness, Cintelligence, Cname, Chealth):
        self.name = Cname
        self.strength = Cstrength
        self.sneak = Csneakiness
        self.intel = Cintelligence
        self.name = Cname
        self.health = Chealth

#getters and setters for the hero
        def getHealth(self):
            return self.health

        def setHealth(self):
            self.health = newHealth






#new_game = Coin_flip_game()
#new_game.start_game()