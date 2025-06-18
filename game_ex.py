import random

user_score = 0
computer_score = 0

while True:
    print("\n<--New Round--><--Game Start-->")

    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        user_choice = input("Enter your choice: ").lower()

    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1

    print("Result:", result)
    print(f"Score => You: {user_score} | Computer: {computer_score}")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
