import random, os

def clear():
    if os.name == "nt": os.system('cls')
    elif os.name == "posix": os.system('clear')

def main():
    score_player = 0
    score_cpu = 0

    while True:
        choices = ["rock", "paper", "scissors"]
        choice_cpu = random.choice(choices)
        choice_player = input("Rock, paper or scissors? ")

        print(f"\nYou: {choice_player}\nCPU: {choice_cpu}")

        # outcomes
        if choice_player == choice_cpu:
            print("\nIt's a tie!\n")
        elif choice_player.lower() == "rock":
            if choice_cpu == "paper":
                score_cpu += 1
                print(f"\nCPU wins!\n\nYou: {score_player}\nCPU: {score_cpu}")
            if choice_cpu == "scissors":
                score_player += 1
                print(f"\nYou win!\n\nYou: {score_player}\nCPU: {score_cpu}")
        elif choice_player.lower() == "paper":
            if choice_cpu == "scissors":
                score_cpu += 1
                print(f"\nCPU wins!\n\nYou: {score_player}\nCPU: {score_cpu}")
            if choice_cpu == "rock":
                score_player += 1
                print(f"\nYou win!\n\nYou: {score_player}\nCPU: {score_cpu}")
        elif choice_player.lower() == "scissors":
            if choice_cpu == "rock":
                score_cpu += 1
                print(f"\nCPU wins!\n\nYou: {score_player}\nCPU: {score_cpu}")
            if choice_cpu == "paper":
                score_player += 1
                print(f"\nYou win!\n\nYou: {score_player}\nCPU: {score_cpu}")

        # play again?
        x = input("\nPlay again? [y/n]: ")
        clear()
        if x.lower() == "y" or x.lower() == " yes": 
            continue
        else:
            print(f"\rFinal score:\n\nYou: {score_player}\nCPU: {score_cpu}")
            if score_player > score_cpu: print("You win!")
            elif score_player == score_cpu: print("It's a tie!")
            else: print("CPU wins!")
            break

if __name__ == "__main__":
    main()