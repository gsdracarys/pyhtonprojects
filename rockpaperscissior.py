# Rock paper scissior between computer and user
import random
import sys

def main():
    user_option = input("Please make a selection \n1. Rock \n2. Paper \n3. Scissor\n\n")
    if type(user_option) != int or user_option > 3:
        print("Wrong Value !!")
        sys.exit()
    user_selection_set = {1:"Rock",2:"Paper",3:"Scissor"}
    user_selection_value = user_selection_set[user_option]
    bot_selection = bot_selection_random()
    print("You have selected " + format(user_selection_value) +" \nBot has selected " + format(bot_selection))

    if user_selection_value == bot_selection:
        print("Its a tie !! Play again")
        sys.exit()


    if winner(bot_selection, user_selection_value) == bot_selection:
        print("Darn !! Bot Wins")
    else:
        print("Yayy !! You Win!!")

def bot_selection_random():
    rps_list = ['Rock','Paper','Scissor']
    selection = random.choice(rps_list)
    return selection

def winner(user1,user2):
    if user1 == "Rock":
        if user2 == "Paper":
            return user2
        else:
            return user1
    elif user1 == "Scissor":
        if user2 == "Rock":
            return user2
        else:
            return user1
    else:
        if user2 == "Scissor":
            return user2
        else:
            return user1



if __name__ == "__main__":
    main()