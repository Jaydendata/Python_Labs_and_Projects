'''
Created on 30 Jul 2022
Jayden LI
'''

## Initialisation:
# Import modules needed for this game:
import random
import time

# Set a random answer (full number between 0 and 10 )
max_attempt_allowed = 3
number_range_begin = 1
number_range_end = 10

## Processing:
# Show invitation message:
print(
    f"Welcome to the guessing game, please guess a full number between {number_range_begin} and {number_range_end}, you only have {max_attempt_allowed} attemps!"
    )
time.sleep(2)

# Explain and invite typing a guess:
print(
    "\nWhat is your guessed full number?"
    )
time.sleep(1)      
guess = int(input(
    "Please type your guessed number here: "
    ))
time.sleep(1)

# Define the correct answer with a random number:
# correct_number = random.randint(number_range_begin,number_range_end)
correct_number = random.randint(number_range_begin,number_range_end)
attempt_count = 1

## Decisions:
# Use while loop to determine if the guess is right or wrong, show hints:
while guess != correct_number and attempt_count < max_attempt_allowed:
    time.sleep(1)
    if guess < correct_number:
        attempt_count += 1
        guess = int(input(
            f"That's low, attempt left: {max_attempt_allowed - attempt_count + 1}, try again: "
            ))
    else:
        attempt_count += 1
        guess = int(input(
            f"That's high, attempt left: {max_attempt_allowed - attempt_count + 1}, try again: "
            ))
time.sleep(1)

## Final output:
if guess == correct_number and attempt_count <= max_attempt_allowed:
    print(
    f"Congrats! the number is right: {correct_number}, you win with only {attempt_count} attempt(s)!"
    )
else:
    print(
        f"Unfortunately, you did not find the correct number after {max_attempt_allowed} attempts, you lost! The right answer is {correct_number}."
    )