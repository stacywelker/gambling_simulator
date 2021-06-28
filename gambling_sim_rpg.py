import random
from pprint import pprint
import sys
from crime_RPG import *



#______begin coin flip game_____
class Coin_flip_game:
    
        def __init__(self):
            self.coins = 100
            self.round_count = 0
            self.coin_options = ["heads", "tails"]
            self.possible_answers = ["yes", "no"]
            self.RPG_running= False

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
        #function to end coin game


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

#helper function to only accept integers as input
        def int_only(self):
            user_input = input("How many coins will you wager? The table minimum is 10 coins. ")
            while user_input.isdigit()== False:
                user_input = input("Please enter a number greater or equal to 10.")
            return(int(user_input))

#function to run one entire coin flip, modify the coin amount, and count the number of rounds.
#if there are still coins, runs a function to start a new round         
        def game_round(self):

            print("You have {coin} coins".format(coin = self.coins))
            
            self.wager = self.int_only()
            while self.wager < 10:
                print("The table limit is 10, please wager at least 10 coins. ")
                self.wager = self.int_only()

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
            
            if self.RPG_running == False:
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

            self.wager = self.int_only()
            while self.wager < 10:
                print("The table limit is 10, please wager at least 10 coins. ")
                self.wager = self.int_only()

            self.guess = input("Will you choose heads or tails? ")
            while self.guess not in self.coin_options:
                print("Invalid choice.")
                self.guess = input("Will you choose heads or tails? ")
            
            self.result = self.loaded_flip()
                        
            if self.guess in self.coin_options:
                if self.guess == self.result:
                    self.add_coins(self.wager)

                elif self.guess != self.result:
                    self.subtract_coins(self.wager)
            
            print("The coin landed on {result}!".format(result = str(self.result)))
            
            print("You now have {coin} coins".format(coin = self.coins))

                       
            self.count = self.add_round()

            self.check = self.coin_check()
            
            if self.RPG_running == False:
                self.next = self.new_round()

            

#function to decide course of game based on count of coins.    
        def coin_check(self):
            marker_string = '''You are out of coins! We can issue you a marker so you can continue playing.\n Maybe you'll win your money back! Your luck has to turn eventually.\n
                Would you like to keep playing? (yes/no)
                '''
            if self.coins >= 500:
                print("You have {coin} coins! You've won the game. Thanks for playing!".format(coin = self.coins))
                self.end_game()
 
            elif self.coins <= 0:
                answer2 = input(marker_string)
                while answer2 not in self.possible_answers:
                    answer2 = input("Invalid choice. Would you like to keep playing with a marker? (yes/no)")

                if answer2 == "yes":
                    self.losing_round()

                elif answer2 == "no" and self.coins < 0:
                    self.bait_switch_1()
                
                elif answer2 == "no" and self.coins == 0:
                    print("You are out of coins! Thanks for playing!")
                    self.end_game() 

            elif self.coins <= -100:
                self.bait_switch_2()
      
        def start_RPG(self):
            self.RPG_running= True
            if self.RPG_running == True:
                print("RPG is running")
            char_data = createChar()
            character = Main_char(100, char_data[0], char_data[1], char_data[2], char_data[3], char_data[4])
            pprint(vars(character))

#Function to open the path to the RPG
#first is for if the player owes less than 100
        def bait_switch_1(self):
            the_situation1 = '''Not so fast, friend! Your coin balance is negative, you owe money to the house. \nDon Corleone is a kind man, but he is not running a charity. How will you repay him? Choose a number.
                (1) Double or nothing?
                (2) Attempt to flee without repaying the debt
                (3) I'm really sorry, I just don't have the money. Is there some sort of arrangement that we can work out?
                '''
            possible_replies_1 = ["1", "2", "3"]

            answer3 = input(the_situation1)
            while answer3 not in possible_replies_1:
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

#Second is for if player owes >100 or has already played double or nothing
        def bait_switch_2(self):        
            the_situation2 = '''Wow, friend! You have dug yourself quite the hole here! \nLet's stop pretending that you're going win your way out. \n
            How will you repay Don Corleone? Choose a number.
                (2) Attempt to flee without repaying the debt
                (3) I'm really sorry, I just don't have the money. Is there some sort of arrangement that we can work out?
                '''
            
            possible_replies_2 = ["2", "3"]
            
            answer3_2 = input(the_situation2)
                  
            while answer3_2 not in possible_replies_2:
                answer3_2 = input('''Invalid choice. Please choose one of the following:
                        (2) Attempt to flee without repaying the debt
                        (3) I'm really sorry, I just don't have the money. Is there some sort of arrangement that we can work out?''')

            if answer3_2 == "2":
                    self.flee()

            elif answer3_2 == "3":
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
                self.bait_switch_2()
        
        
        def flee(self):
            print('''You attempt to flee the gaming floor without replaying the debt. 
            You sprint for the double doors, taking a right turn into the hallway that leads out to the restaurant which serves as a front for the illegal gaming ring. 
            Frantically, you turn left, taking stairs two at a time. At the top of the stairs, you open a door which leads to the restaurant kitchen. You escape out the staff door of the kitchen.
            No one seems to be following you. You hail a cab and return to your apartment, legs trembling with fear the entire way. You close the door of you apartment behind you, breathing a sigh of relief.
            Surely you are safe now. Suddenly you hear the noise of movement in the living room. A tall, broad looking man walks out out of the living room, gun in hand. 
            ' "You didn't think you could escape payment that easily, did you?" ' He chuckles darkly. You back away until you hit the apartment door, heart pounding. 
            The man shoots the gun, but instead of the loud pop you were expecting, there is a sharp whoosh of compressed air, like from a paintball gun. 
            Confused, you clutch your shoulder, where a plastic tube has appeared, a needle connected to it and stuck into your skin through your shirt.
            ' "If you will not pay your debts honestly, we have other things of value to collect from you." ' The sound of your own breath in your ears becomes the roar of ocean waves.
            Warm blackness creeps in from the edges of your vision, your body recedes from your awareness. 
            The last thing you see is the man approaching you with what looks like a body bag as you fall to the ground. ''')
            print("Your organs have been harvested and sold to repay the debt! Your friends and family are distressed by your mysterious disappearance. They search for you fruitlessly for decades.")
            self.end_game()
        
        def other_options(self):
            print('''An arrangement, huh? I guess this is something we can do. You look like a fit, capable person. Maybe you can helps us with some... errands.
            Report to the gang HR office tomorrow and we'll get you started. Don't try to run. We know where you live and we know where your family lives.
            We'll be watching you.''')
            self.start_RPG()
            

#function to end game        
        def end_game(self):
            quit()


new_game = Coin_flip_game()

new_game.start_game()
