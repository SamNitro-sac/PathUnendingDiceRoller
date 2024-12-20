import tkinter as tk
import random
import pygame

# Initialize pygame mixer for audio
pygame.mixer.init()

def play_sound(file):
    """Plays a sound file."""
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def dice(num_dice, threshold):
    successes = 0
    for _ in range(num_dice):
        roll = random.randint(1, 10)
        if roll >= threshold:
            successes += 1
        elif roll == 1 and successes > 0:
            successes -= 1
        elif roll == 10:
            successes += dice(1, threshold)
    return successes

def simulate_action(num_dice, threshold, drive, rolls, target, num_simulations):
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

def run_simulation():
    try:
        num_dice = int(entry_num_dice.get())
        threshold = int(entry_threshold.get())
        drive = float(entry_drive.get())
        rolls = int(entry_rolls.get())
        target = int(entry_target.get())
        num_simulations = int(entry_simulations.get())

        probability, average_successes = simulate_action(
            num_dice, threshold, drive, rolls, target, num_simulations
        )

        # Update the result label
        result_label.config(text=f"Probability of success: {probability:.2f}%\n"
                                 f"Average number of successes: {average_successes:.2f}",
                            fg="white")

        # Play sound based on probability
        if probability < 50:
            play_sound("nelson.mp3")  # Replace with the actual file path
        else:
            play_sound("yes.mp3")  # Replace with the actual file path

    except ValueError:
        result_label.config(text="Error: Please enter valid numbers for all fields.",
                            fg="red")

# Create the main window
root = tk.Tk()
root.title("Dice-Based Probability Simulator")
root.configure(bg="#3e2723")

# Title label
title_label = tk.Label(root, text="Dice-Based Probability Simulator", font=("Papyrus", 16, "bold"),
                       bg="#3e2723", fg="#FFD700")
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Input fields
field_bg = "#5d4037"
field_fg = "white"
tk.Label(root, text="Number of Dice:", font=("Arial", 12), bg="#3e2723", fg="white").grid(row=1, column=0, sticky="e")
entry_num_dice = tk.Entry(root, bg=field_bg, fg=field_fg)
entry_num_dice.grid(row=1, column=1, pady=5)

tk.Label(root, text="Threshold (1-10):", font=("Arial", 12), bg="#3e2723", fg="white").grid(row=2, column=0, sticky="e")
entry_threshold = tk.Entry(root, bg=field_bg, fg=field_fg)
entry_threshold.grid(row=2, column=1, pady=5)

tk.Label(root, text="Drive Multiplier:", font=("Arial", 12), bg="#3e2723", fg="white").grid(row=3, column=0, sticky="e")
entry_drive = tk.Entry(root, bg=field_bg, fg=field_fg)
entry_drive.grid(row=3, column=1, pady=5)

tk.Label(root, text="Number of Rolls:", font=("Arial", 12), bg="#3e2723", fg="white").grid(row=4, column=0, sticky="e")
entry_rolls = tk.Entry(root, bg=field_bg, fg=field_fg)
entry_rolls.grid(row=4, column=1, pady=5)

tk.Label(root, text="Target Successes:", font=("Arial", 12), bg="#3e2723", fg="white").grid(row=5, column=0, sticky="e")
entry_target = tk.Entry(root, bg=field_bg, fg=field_fg)
entry_target.grid(row=5, column=1, pady=5)

tk.Label(root, text="Number of Simulations:", font=("Arial", 12), bg="#3e2723", fg="white").grid(row=6, column=0, sticky="e")
entry_simulations = tk.Entry(root, bg=field_bg, fg=field_fg)
entry_simulations.grid(row=6, column=1, pady=5)
entry_simulations.insert(0, "10000")  # Default value

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#3e2723", fg="white", justify="left")
result_label.grid(row=8, column=0, columnspan=2, pady=10)

# Run button
btn_run = tk.Button(root, text="Run Simulation", font=("Arial", 12), bg="#FFD700", fg="#3e2723", command=run_simulation)
btn_run.grid(row=7, column=0, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()
