import random
import os
numb_of_tries=0
max_attempts=10
high_score=[]


#### MAKES SURE USER INPUTS CORRECT NON NEGATIVE INTEGER BETWEEN 1-10
def user_input_integer():
    global user_answer
    ####user_answer=int(input("please enter a whole number  "))
    try:
        user_answer=int(input("\nPlease enter a whole number  "))
    except ValueError:
      print("\n Don't forget to type a digit ")
      return user_input_integer()
    while user_answer > 10 or user_answer<0:
      print("\nyou must input whole positive number between 1 - 10 ")
      return user_input_integer()


####MAKES SURE USER INPUTS CORRECT NAME (STRINGS) NOT NUMBERS AND GREETS
def user_input_string():
    user_name=input("\nEnter your name A-Z    ")
    while user_name.isdigit():
        print("\nYou must use letters ")
        return user_input_string()
        break
    print("\nHello {}, you are playing the guessing game  ".format(user_name))


####ASKS USER IF THEY WANT TO PLAY AGAIN AND MAKES SURE THEY ANSWER Y OR N
####PRINTS OUT HIGH SCORE (MEANING LOWEST TRY GUESS)

def if_user_wants_more():
    more_play=input("\nDo you want to play again Y/N  ")
    more_play=more_play.lower()
    if more_play == "y":
        print("\n NEW GAME !!!\nThe highest score (minimum attempts used) is {}.\n**GOOD LUCK***".format(min(high_score)))
        start_game()

    elif print("\nYou must choose either Y(YES) or N(EXIT)"):

      return if_user_wants_more()
    else:
      if more_play=="n":

        print("\n Game finished. Have a great day   ")
        os._exit(1)


###GAME
def start_game():
    answer=random.randint(1,10)
    numb_of_tries=0
    max_attempts=10

    user_input_string()
    while numb_of_tries < max_attempts:
        numb_of_tries+=1
        if numb_of_tries>=max_attempts:
            print("\nSorry, you used all attempts ")
            if_user_wants_more()
            break

        user_input_integer()
        if user_answer>answer:
            print("\n TRY LOWER ! ")
        elif user_answer< answer:
            print("\nTRY HIGHER !     ")
        else:
            print("\nCongrats, it took you   {}   tries   ".format(numb_of_tries))
            high_score.append(numb_of_tries)
            if_user_wants_more()
if __name__ == '__main__':
  start_game()
