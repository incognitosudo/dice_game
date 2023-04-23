import random
import tkinter as tk

high_score = 0


def dice_game():
    global high_score
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    total_score = roll1 + roll2
    message = f"First roll: {roll1} \nSecond roll: {roll2} \ntotal score: {total_score}. \n"
    if total_score > high_score:
        high_score = total_score
        message += f"Congratulations! Your new high score is: {high_score} \n"
    else:
        message += f"Current high score: {high_score}.\n"
    message_label.config(text=message)


def leave_game():
    root.destroy()


root = tk.Tk()
root.title("Dice Game")
root.geometry("300x200")  # sets window size
root.configure(bg="black")  # sets background color to black


roll_button = tk.Button(root, text="Roll Dice",
                        command=dice_game, fg="green", bg="black")
roll_button.pack()

leave_button = tk.Button(root, text="Leave Game",
                         command=leave_game, fg="green", bg="black")
leave_button.pack()

message_label = tk.Label(
    root, text="Welcome to the Dice Game!", fg="green", bg="black")  # sets text green and bg black
message_label.pack()

root.mainloop()
