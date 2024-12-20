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

---

## Usage

### Requirements
- Python 3.x
- No additional libraries are required (uses Python's built-in modules).

### Running the Program

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/dice-simulator.git
   cd dice-simulator
   ```

2. Run the program:
   ```bash
   python dice_simulator.py
   ```

3. Edit the parameters in the script to suit your needs (e.g., number of dice, threshold, drive multiplier, rolls, target, and simulations).

---

## Example

```python
num_dice = 4       # Number of dice rolled per roll
threshold = 6      # Minimum roll value to succeed
drive = 1.5        # Multiplier for successes
rolls = 8          # Number of rolls in one action
target = 16        # Minimum successes needed
num_simulations = 10000  # Number of simulations
```

Output:
```
Probability of success: 78.52%
Average number of successes: 18.34
```

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

---

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request with improvements or new features.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments
- Inspired by mechanics from tabletop RPGs and custom dice systems.

