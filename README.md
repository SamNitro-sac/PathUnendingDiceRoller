# Dice-Based Probability Simulator

This program simulates dice rolls and calculates the probability of achieving a target number of successes in a tabletop role-playing game (RPG) or similar scenarios. It also computes the average number of successes produced by an action.

---

## Features
- Simulates multiple dice rolls with custom rules:
  - **Success:** Rolls greater than or equal to a threshold.
  - **Penalty:** Rolls of `1` remove one success (if any exist).
  - **Explosive Dice:** Rolls of `10` generate an additional roll.
- Applies a **drive multiplier** to successes.
- Supports actions with multiple rolls and calculates:
  - Probability of achieving or exceeding a target number of successes.
  - Average number of successes per action.
- **Interactive GUI** with themed design inspired by tabletop RPGs.
- Plays sounds based on the probability of success:
  - A "Nelson ha-ha" sound for probabilities below 50%.
  - A "Yes!" sound for probabilities 50% or higher.

---

## Usage

### Requirements
- Python 3.x
- The following Python libraries:
  - `pygame` for playing sounds. Install it using:
    ```bash
    pip install pygame
    ```

### Running the Program

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/dice-simulator.git
   cd dice-simulator
   ```

2. Ensure you have Python 3.x installed. If not, download and install it from [python.org](https://www.python.org/).

3. Install the required library:
   ```bash
   pip install pygame
   ```

4. Run the program:
   ```bash
   python dice_simulator.py
   ```

5. Use the graphical interface to enter your parameters:
   - **Number of Dice**: The number of dice rolled per roll.
   - **Threshold**: Minimum roll value to count as a success (1-10).
   - **Drive Multiplier**: Multiplier applied to total successes.
   - **Number of Rolls**: Number of rolls in one action.
   - **Target Successes**: Minimum successes needed to succeed.
   - **Number of Simulations**: Total number of simulations to perform (default: 10000).

6. Click "Run Simulation" to see the results displayed in the GUI. Depending on the probability:
   - If the probability is below 50%, you will hear the "Nelson ha-ha" sound.
   - If the probability is 50% or higher, you will hear the "Yes!" sound.

---

## Example

Interactive input example in the GUI:
- Enter the following parameters:
  - **Number of Dice:** 4
  - **Threshold:** 6
  - **Drive Multiplier:** 1.5
  - **Number of Rolls:** 8
  - **Target Successes:** 16
  - **Number of Simulations:** 10000

Output displayed in the GUI:
```
Probability of success: 78.52%
Average number of successes: 18.34
```

If the probability is below 50%, you will hear a "ha-ha" sound. Otherwise, you will hear "Yes!".

---

## Functions

### `dice(num_dice, threshold)`
Simulates rolling `num_dice` and counts the number of successes according to the rules:
- Rolls >= `threshold` are successes.
- Rolls of `1` remove one success.
- Rolls of `10` trigger additional rolls.

### `simulate_action(num_dice, threshold, drive, rolls, target, num_simulations)`
Simulates multiple actions and calculates:
- Probability of achieving the target number of successes.
- Average number of successes across all simulations.

Arguments:
- `num_dice`: Number of dice rolled per roll.
- `threshold`: Minimum roll value to count as a success.
- `drive`: Multiplier applied to the total number of successes.
- `rolls`: Number of rolls in one action.
- `target`: Minimum successes needed to succeed.
- `num_simulations`: Total number of simulations to perform.

Returns:
- `probability`: Probability of achieving the target (percentage).
- `average_successes`: Average number of successes per action.

### `play_sound(file)`
Plays a sound file using `pygame`.

Arguments:
- `file`: Path to the sound file to play.

---

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request with improvements or new features.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments
- Inspired by mechanics from tabletop RPGs and custom dice systems.
- Sounds are inspired by common pop culture references.

