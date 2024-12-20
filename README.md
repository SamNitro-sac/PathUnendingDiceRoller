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

3. Follow the on-screen prompts to enter the simulation parameters. For example:
   ```
   Enter the number of dice rolled per roll: 4
   Enter the threshold for a success (1-10): 6
   Enter the drive multiplier for successes: 1.5
   Enter the number of rolls in one action: 8
   Enter the target number of successes: 16
   Enter the number of simulations to perform: 10000
   ```

4. The program will calculate and display:
   - The probability of achieving the target.
   - The average number of successes across all simulations.

---

## Example

Interactive input example:
```
Enter the number of dice rolled per roll: 4
Enter the threshold for a success (1-10): 6
Enter the drive multiplier for successes: 1.5
Enter the number of rolls in one action: 8
Enter the target number of successes: 16
Enter the number of simulations to perform: 10000
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

