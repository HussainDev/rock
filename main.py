
import random

def get_user_choice():
    shortcut_map = {
        'r': 'rock',
        'p': 'paper',
        's': 'scissors',
        'c': 'cheat'
    }

    while True:
        choice = input("Your move Rock/Paper/Scissor or (r/p/s): ").lower()
        if choice in shortcut_map:
            return shortcut_map[choice]
        elif choice in shortcut_map.values():
            return choice
        else:
            print("Invalid input. Please enter r, p, s, or full word.")

def get_computer_choice(user_choice, round_num, difficulty):
    if difficulty == "normal":
        return random.choice(["rock", "paper", "scissors"])
    elif difficulty == "skilled" and round_num % 4 == 0:
        return win_against(user_choice)
    elif difficulty == "warrior" and round_num % 2 == 0:
        return win_against(user_choice)
    else:
        return random.choice(["rock", "paper", "scissors"])

def win_against(choice):
    if choice == "rock":
        return "paper"
    elif choice == "paper":
        return "scissors"
    elif choice == "scissors":
        return "rock"
    else:
        return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "user"
    else:
        return "computer"

def play():
    print("\n 🎮 Welcome to Rock, Paper, Scissors! 🎮")
    print("\n Select difficulty level:  1. Normal -- 2. Skilled (pro) -- 3. Warrior (over-confident)")

    difficulty_map = {
        "1": "normal",
        "2": "skilled",
        "3": "warrior"
    }

    while True:
        difficulty_input = input("Enter 1, 2 or 3: ")
        if difficulty_input in difficulty_map:
            difficulty = difficulty_map[difficulty_input]
            break
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

    while True:
        try:
            target_score = int(input("Enter the number of points needed to win: "))
            if target_score > 0 and target_score<11:
                break
            else:
                print("Please enter a number greater than 0 upto 10.")
        except ValueError:
            print("Please enter a valid number.")

    print(f"\nGame starts! Difficulty: {difficulty.capitalize()}, First to {target_score} points wins.")

    user_score = 0
    computer_score = 0
    round_number = 0
    history = []

    while user_score < target_score and computer_score < target_score:
        round_number += 1
        print(f"\n--- Round {round_number} ---")
        user_input = get_user_choice()
        cheat_used = user_input == "cheat"

        if cheat_used:
            computer_choice = random.choice(["rock", "paper", "scissors"])
            user_choice = win_against(computer_choice)
        else:
            user_choice = user_input
            computer_choice = get_computer_choice(user_choice, round_number, difficulty)

        print(f"Computer chose: {computer_choice.capitalize()}")
        print(f"You chose: {user_choice.capitalize()}")

        result = determine_winner(user_choice, computer_choice)

        if result == "user":
            user_score += 1
            print("✅ You win this round! ✅")
        elif result == "computer":
            computer_score += 1
            print("❌ Computer wins this round! ❌")
        else:
            print("🤝 It's a tie! 🤝")

        history.append((round_number, user_choice, computer_choice, result))
        print(f"Score → You: {user_score} | Computer: {computer_score}")

    print("\n🏁 !Game Over! 🏁")
    if user_score == target_score:
        print("🎉 YOU WIN THE GAME! 🎉")
    else:
        print("💻 COMPUTER WINS THE GAME! 💻")

    # Return all relevant data for the menu
    return history, user_score, computer_score

def show_scoreboard(history):
    print("\n📊 Final Scoreboard:")
    for r, u, c, res in history:
        outcome = "Draw" if res == "tie" else ("You" if res == "user" else "Computer")
        print(f"Round {r}: You - {u.capitalize()} | Computer - {c.capitalize()} → {outcome}")

if __name__ == "__main__":
    while True:
        history, user_score, computer_score = play()
        while True:
            choice = input("\n CLICK 1 = Overall scoreboard -- --   2 = Replay -- --   Any other key to = Exit : ").strip()

            if choice == '1':
                show_scoreboard(history)
            elif choice == '2':
                break  # break inner loop to replay
            else:
                print("Thanks for playing! Goodbye! 👋  Have a nice TIME! \n")
                exit()
