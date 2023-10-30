# You can use this workspace to write and submit your adventure game project.
import time
import random


def print_pause(message):
    print(message)
    time.sleep(2)


def intro():
    print_pause("Your Country is experiencing economy instability")
    print_pause("Rumor has it that your Country's economy status will degrade significantly in the next 4 months")
    print_pause("A scholarship opportunity to study in a country almost the same level as your country came up which require you to leave the country before the economic degrading starts.")


def main_choice(items):
    choice = input("1. Accept the scholarship\n"
                   "2. Decide to stay in your country and hope things become better\n")
    if choice == '1':
        scholarship(items)
    elif choice == '2':
        patriot(items)
    else:
        main_choice(items)

def scholarship(items):
    print_pause("You got to a new country")
    print_pause("School begins")
    print_pause("You noticed the curriculum is way advanced for you and you find it difficult to cope")
    print_pause("Studying became hard. Then the unexpected came")
    print_pause("You were called in by the school Admins and they did an overview of your admission status and your school performance")
    print_pause("The result of the hearing resulted to the cancellation of your scholarship. So starting from next semester, you'll start paying tution fees.")
    Education(items)


def Education(items):
    choices = input("1. Accept the offer\n"
                    "2. Return back to your country\n")
    if choices == '1':
        Aftermath(items)
    elif choices == "2":
        Home(items)
    else:
        Education(items)


def Aftermath(items):
    print_pause("A new Session begins")
    print_pause("The new session was way too advanced than the previous session")
    print_pause("You were told to withdraw from the school.")
    play_again(items)

def Home(items):
    print_pause("You got back to your country")
    print_pause("living became tough since you don't have much money")
    print_pause("You met a friend of yours who suggested venturing into sport betting to make money.")
    Sports_Betting(items)

def Sports_Betting(items):
    betting = input("1. Accept the Idea\n"
                    "2. Ignore the Idea\n")
    
    if betting == "1":
        betting_firstoutcome(items)
    elif betting == "2":
        betting_secondoutcome(items)
    else:
        Sports_Betting(items)
    
hope = ("You won 10 million")

fate = ("You lost everything")

def betting_firstoutcome(items):
    outcome = [hope, fate]
    real_outcome = random.choice(outcome)
    print_pause(real_outcome)

    if real_outcome == hope:
        print_pause("You are rich")
        print_pause("Congratulations!!")
    else:
        print_pause("You now live on the streets.")
    
    play_again(items)

def betting_secondoutcome(items):
    print_pause("You met someone who helped you with the capital for a business.")
    print_pause("You became financially stable.")
    play_again(items)

def patriot(items):
    print_pause("You decided to learn a tech skill hoping to use that as a means of survival when the economy cones crashing.")
    print_pause("You streamline your tech skill choices to three but you have to learn just one.")
    Occupation(items)

def Occupation(items):
    print_pause("What skill would you choose?")
    Occupation_choices = input("1. Full Stack Developer\n"
                               "2. Data Analyst\n"
                               "3. Graphics Designer\n")
    
    if Occupation_choices == "2":
        Occupation_success(items)
    elif Occupation_choices == "1" or "3":
        Occupation_setback(items)
    else:
        Occupation(items)

def Occupation_success(items):
    print_pause("You got a high paying full-time Job as a data analyst")
    print_pause("The economy instability subdue and went back to normal")
    play_again(items)

def Occupation_setback(items):
    print_pause("Things didn't go well after learning the skill")
    print_pause("The economy instability hit you and you ended up on the streets")
    play_again(items)

def play_again(items):
    print_pause("Do you want to play again?")
    again = input("1. Yes\n"
                  "2. No\n")
    if again == '1':
        show()
    elif again == '2':
        print_pause("Okay. See you again!")
    else:
        play_again(items)

def show():
    items = []
    intro()
    main_choice(items)


if __name__ == "__main__":
    show()
