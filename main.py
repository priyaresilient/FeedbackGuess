# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    def feedback_guess(x):
        low=1
        high=x
        guess_num=0
        feedback=''
        while(feedback!='c'):
            guess_num=random.randint(low,high)
            feedback=input(f'Is {guess_num} Too Low(L) Too High(H) or Correct(C)'.lower())
            if(feedback=='l'):
                low=guess_num+1
            elif(feedback=='h'):
                high=guess_num-1
        print('The computer guessed the number.')

feedback_guess(20)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
