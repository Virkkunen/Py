import random, time

def main():
    num_dice = int(input("How many dice? "))
    num_dice_display = num_dice
    dice_faces = int(input("How many faces? "))
    rolls = []
    
    while num_dice:
        rolls.append(random.randint(1, dice_faces))
        num_dice -= 1

    rolls_total = sum(rolls)
    print(f"\nRolled {num_dice_display}d{dice_faces}: {rolls}\nTotal: {rolls_total}")

if __name__ == "__main__":
    main()
    