import random

def dice(num_dice, threshold):
    """
    Simulates rolling a number of dice and counts successes.
    - Success: roll >= threshold
    - Penalty: roll == 1 (removes one success if > 0)
    - Explosive: roll == 10 (adds an extra roll)

    Args:
    - num_dice (int): Number of dice to roll.
    - threshold (int): Minimum roll value to count as a success.

    Returns:
    - int: Total number of successes.
    """
    successes = 0
    for _ in range(num_dice):
        roll = random.randint(1, 10)
        if roll >= threshold:
            successes += 1
        elif roll == 1 and successes > 0:
            successes -= 1
        elif roll == 10:
            successes += dice(1, threshold)  # Recursive call for explosive dice
    return successes

def simulate_action(num_dice, threshold, drive, rolls, target, num_simulations):
    """
    Simulates multiple actions and calculates the probability of success and average successes.

    Args:
    - num_dice (int): Number of dice rolled per action.
    - threshold (int): Minimum roll value to count as a success.
    - drive (float): Multiplier applied to total successes.
    - rolls (int): Number of rolls in each action.
    - target (int): Minimum number of successes required to succeed.
    - num_simulations (int): Number of simulations to perform.

    Returns:
    - float: Probability of achieving the target as a percentage.
    - float: Average number of successes over all simulations.
    """
    successful_simulations = 0
    total_successes_sum = 0

    for _ in range(num_simulations):
        total_successes = 0
        for _ in range(rolls):
            total_successes += round(dice(num_dice, threshold) * drive)
        total_successes_sum += total_successes
        if total_successes >= target:
            successful_simulations += 1

    average_successes = total_successes_sum / num_simulations
    probability = (successful_simulations / num_simulations) * 100

    return probability, average_successes

def main():
    print("Welcome to the Dice-Based Probability Simulator!")
    
    # User inputs
    num_dice = int(input("Enter the number of dice rolled per roll: "))
    threshold = int(input("Enter the threshold for a success (1-10): "))
    drive = float(input("Enter the drive multiplier for successes: "))
    rolls = int(input("Enter the number of rolls in one action: "))
    target = int(input("Enter the target number of successes: "))
    num_simulations = int(input("Enter the number of simulations to perform: "))
    
    print("\nSimulating...\n")
    
    # Perform simulation
    probability, average_successes = simulate_action(num_dice, threshold, drive, rolls, target, num_simulations)
    
    # Results
    print(f"Probability of success: {probability:.2f}%")
    print(f"Average number of successes: {average_successes:.2f}")

if __name__ == "__main__":
    main()
