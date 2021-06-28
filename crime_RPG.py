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

    def getDebt(self):
        return self.debt
        
    def setDebt(self):
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
