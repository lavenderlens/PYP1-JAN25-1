# Part 2 Loops
# In this exercise you will create a number guess game. It will prompt the user to guess the
# magic number between 1 and 10. If the user guesses correctly, it will print a winner
# message and exit. If the user guesses incorrectly, he/she will be prompted again. The user
# will be given three go's after which, if he/she has not guessed correctly the script will
# print a loser message.
# 1. Create a script named loops_exercise.py.
# 2. Import the random module as follows:
# import random
# 3. Declare and assign a variable that produces a random number in the range 1-10, as follows:
# magic_number = random.randint(1, 10)
# 4. Code a loop that iterates three times.
# 5. Inside the loop…
# a. Prompt the user to input a guess and capture it in a variable named
# user_guess.
# b. If the user's guess equals the magic number, print a winner message to the
# console and break out of the loop.
# c. If the user's guess does not equal the magic number, print an appropriate
# message, e.g. too low or too high.
# 6. If the loop exits normally, the user has not guessed correctly so print a suitable
# consolation message to the console.