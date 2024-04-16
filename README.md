## **Blackjack Game**

### Overview

This Python script simulates a simple blackjack game where the player competes against the dealer to achieve a hand value as close to 21 as possible without exceeding it. The game follows standard blackjack rules, with Aces counted as 1 or 11, face cards (J, Q, K) counted as 10, and numeric cards counted at face value.

### Features

1. **Hit or Stand:** Players are prompted to decide whether to draw an additional card ("hit") or end their turn ("stand").
2. **Player Turn:** The player starts the game by receiving two initial cards and can continue to draw additional cards until they choose to stand or their hand value exceeds 21.
3. **Dealer Turn:** After the player stands, the dealer draws cards until their hand value is at least 17.
4. **Outcome Determination:** The player wins if their hand value is higher than the dealer's and does not exceed 21. Otherwise, the player loses.

### Usage

1. Run the script in a Python environment.
2. Follow the prompts to input player decisions during the game:
    - Enter 'Y' or 'y' to draw another card (hit).
    - Enter 'N' or 'n' to end the player's turn (stand).
3. The script will display the current status of the player's and dealer's hands, as well as the outcome of the game.
