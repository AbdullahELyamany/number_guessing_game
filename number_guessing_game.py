'''
Number Guessing Game
This game to guess a number between 1 and 100
-------------------------------------------------------------
Created by Abdullah Al-Yamani
'''

import random

attempts_list = []


def show_score():
  if not attempts_list:
      print('\n\033[;39;mThere is currently no high score, it\'s yours for the taking!\n')

  else:
      print(f'\n\033[;39;mThe current high score is {min(attempts_list)} attempts\n')


def start_game():
   attempts = 0
   rand_num = random.randint(1, 100)
   print('\033[;39;mHello traveler! Welcome to the game of guesses!')
   player_name = input('\033[;32;mWhat is your name? ')
   wanna_play = input(
       f'\033[;39;mHi, {player_name}, would you like to play the guessing game?'
       '\033[;32;m(Enter Yes/No): ')

   if wanna_play.lower() != 'yes' and wanna_play.lower() != 'y':
      print('\033[;36;mThat\'s cool, Thanks!')
      exit()
   else:
       show_score()

   while wanna_play.lower() == 'yes' or wanna_play.lower() == 'y':
       try:
           guess = int(input('\033[;32;mPick a number between 1 and 100: '))
           if guess < 1 or guess > 100:
               raise ValueError(
                   'Please guess a number within the given range')

           attempts += 1
           attempts_list.append(attempts)

           if guess == rand_num:
               print('\n\033[;36;mNice! You got it!')
               print(f'It took you {attempts} attempts')
               wanna_play = input(
                   '\n\033[;32;mWould you like to play again? (Enter Yes/No): ')
               if wanna_play.lower() != 'yes' and wanna_play.lower() != 'y' :
                   print('\033[;36;mThat\'s cool, have a good one!')
                   break
               else:
                   attempts = 0
                   rand_num = random.randint(1, 100)
                   show_score()
                   continue
           else:
               if guess > rand_num:
                   print('\n\033[;31;mIt\'s lower, Choose A Lower Number')
               elif guess < rand_num:
                   print('\n\033[;31;mIt\'s higher, Choose A Larger Number')

       except ValueError as err:
           print('\033[;31;mOh no!, that is not a valid value. Try again...')
           print(err)


if __name__ == '__main__':
   start_game()