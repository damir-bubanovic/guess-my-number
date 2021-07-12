import random
from rich.console import Console

console = Console()

attempts = 5
number = random.randrange(1, 10)
guess = 0

for attempt in range(attempts, 0, -1):
    guess = int(input(f'Guess what number am I thinking between 1 and 10?\n'))

    if guess < number:
        console.print(f'Wrong -> Too Low', style="yellow")
        print(f'You have {attempt} guesses left \n')
    elif guess > number:
        console.print(f'Wrong -> Too High', style="yellow")
        print(f'You have {attempt} guesses left \n')
    else:
        console.print(f'That \'s right the number is {guess}', style="bold green")
        break












# number = random.randrange(1,10)
# guess = 0

# while guess != number:
#   guess = int(input(f'Guess what number am I thinking between 1 and 10?'))
#   if guess < number:
#       print(f'Wrong Too Low')
#   elif guess > number:
#       print(f'Wrong Too High')

# print(f'That \'s right the number is {guess}')