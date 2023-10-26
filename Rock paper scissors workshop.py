import tkinter as tk
import random

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle player's choice
def player_choice(choice):
    computer_choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(computer_choices)
    result = determine_winner(choice, computer_choice)

    result_label.config(text=f"Computer chose {computer_choice}. {result}")

# Create the main window
window = tk.Tk()
window.title("Rock, Paper, Scissors")

# Create a label to display the game result
result_label = tk.Label(window, text="", font=("Helvetica", 16))
result_label.pack()

# Create buttons for player's choices
rock_button = tk.Button(window, text="Rock", width=10, command=lambda: player_choice("Rock"))
paper_button = tk.Button(window, text="Paper", width=10, command=lambda: player_choice("Paper"))
scissors_button = tk.Button(window, text="Scissors", width=10, command=lambda: player_choice("Scissors"))

rock_button.pack()
paper_button.pack()
scissors_button.pack()

window.mainloop()
