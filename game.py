from tkinter import *
from functools import partial   # To prevent unwanted windows

import random


class Mystery:
    def __init__(self, parent):

        # Formatting variables...
        background_color = "#68B684"

        # mystery box Main Screen GUT...
        self.start_frame = Frame(bg=background_color, width=900, height=900)
        self.start_frame.grid(padx=10, pady=10)  # padding in grey??

        # five dollar button (row 2 column 0 )
        self.push_btn = Button(self.start_frame,
                               text="push",font="arial 10 bold",fg="black",
                               bg="#95E06C",padx=12, pady=12,
                               command=lambda: self.to_game())
        self.push_btn.grid(row=0, column=1)

    def to_game(self):

        starting_balance = 50
        stakes = 2

        Game(self, stakes, starting_balance)

        self.start_frame.destroy()


class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)


        # initialise variables
        self.balance = IntVar()
        # set starting balance to amount entered by user at start of game
        self.balance.set(starting_balance)

        # get value of stakes
        self.multiplier = IntVar()
        self.multiplier.set(stakes)

        # GUI setup
        self.game_box = Toplevel()

        # If user press cross at top, game quits
        self.game_box.protocol('WM_DELETE_WINDOW', self.to_quit)

        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Heading row
        self.heading_label = Label(self.game_frame, text="play...",
                                   font="Arial 24 bold", padx=10, pady=10)
        self.heading_label.grid(row=0)

        # Instructions label
        self.Instructions_label = Label(self.game_frame, wrap=300, justify=LEFT,
                                        text="Press <enter> or click the 'open "
                                             "Boxes' button to reveal the "
                                             "contents of the mystery boxes.",
                                        font="arial 10")
        self.Instructions_label.grid(row=1)

        # boxes go here
        box_text = "arial 15 bold"
        box_back = "#68B684"
        box_width = 5
        self.box_frame = Frame(self.game_frame)
        self.box_frame.grid(row=2)

        self.prize1_label = Label(self.box_frame, text="?\n", font=box_text,
                                  bg=box_back, width=box_width, padx=10, pady=10)
        self.prize1_label.grid(row=0, column=0, padx=10)

        self.prize2_label = Label(self.box_frame, text="?\n", font=box_text,
                                  bg=box_back, width=box_width, padx=10, pady=10)
        self.prize2_label.grid(row=0, column=1, padx=10)

        self.prize3_label = Label(self.box_frame, text="?\n", font=box_text,
                                  bg=box_back, width=box_width, padx=10, pady=10)
        self.prize3_label.grid(row=0, column=2, padx=10)

        # Play button goes here
        self.play_btn = Button(self.game_frame, text="open boxes",
                               bg="yellow", font="arial 10 bold", width=20,
                               padx=10, pady=10, command=self.reveal_boxes)

        self.play_btn.focus()
        self.play_btn.bind('<Return>', lambda e: self.reveal_boxes())
        self.play_btn.grid(row=3)

        # balance label

        start_text = "Game cost: ${}\n""\nHow much"\
                    "will you win?".format(stakes * 5)

        self.balance_label = Label(self.game_frame, font="arial 12 bold", fg="green",
                                   text=start_text,justify=LEFT)
        self.balance_label.grid(row=4, pady=10)

        # Help and Game Stats button
        self.help_export_frame = Frame(self.game_frame)
        self.help_export_frame.grid(row=5,pady=10)

        self.help_btn= Button(self.help_export_frame, text="Help / Rules",
                              font="arial 10 bold", bg="#808080", fg="white")
        self.help_btn.grid(row=0, column=0, padx=2)

        self.stats_btn = Button(self.help_export_frame, text="Game stats...",
                              font ="arial 10 bold", bg="#808080", fg="white")
        self.stats_btn.grid(row=0, column=1, padx=2)


        self.quit_btn = Button(self.game_frame, text="Quit",
                              font ="arial 10 bold", bg="#808080", fg="white",
                               command=self.to_quit)
        self.quit_btn.grid(row=6, padx=2)


    def reveal_boxes(self):
        # retrieve the balance from initial function
        current_balance = self.balance.get()
        stakes_multiplier = self.multiplier.get()

        round_winnings = 0
        prizes = []
        background = []
        for item in range(0,3):
            prize_num = random.randint(1,100)

            if 0 < prize_num <= 5:
                prize = "gold\n(${})".format(5 * stakes_multiplier)
                back_color = "#FFD700"  # gold colour
                round_winnings += 5 * stakes_multiplier
            elif 6 < prize_num <= 20:
                prize = "sliver\n(${})".format(2 * stakes_multiplier)
                back_color = "#C0C0C0" # silver colour
                round_winnings += 2 * stakes_multiplier
            elif 21 < prize_num <= 50:
                prize = "copper\n(${})".format(1 * stakes_multiplier)
                back_color = "#B87333" # copper colour
                round_winnings += stakes_multiplier
            else:
                prize = "lead\n($0)"
                back_color = "#6D6A65" # lead colour

            prizes.append(prize)
            background.append(back_color)

        # Display prizes...
        self.prize1_label.config(text=prizes[0], bg=background[0])
        self.prize2_label.config(text=prizes[1], bg=background[1])
        self.prize3_label.config(text=prizes[2], bg=background[2])

        # Deduct cost of game
        current_balance -= 5 * stakes_multiplier

        # Add winning
        current_balance += round_winnings

        # set balance to new balance
        self.balance.set(current_balance)

        balance_statement = "Game Cost: $ {}\nPayback: ${} \n" \
                            "Current Balance: ${}".format(5* stakes_multiplier,
                                                          round_winnings,
                                                          current_balance)

        # Edit label so user can see their balance
        self.balance_label.configure(text=balance_statement)

        if current_balance<5 * stakes_multiplier:
            self.play_btn.config(state=DISABLED)
            self.game_box.focus()
            self.play_btn.config(text="Game Over")

            balance_statement = "Currrent Balance: ${}\n" \
                                "Your balance is too low. You can only quit " \
                                "or view your stats. sorry about that".format(current_balance)
            self.balance_label.config(fg="black", font="arial 10 bold",
                                      text=balance_statement)

    def to_quit(self):
        root.destroy()



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box")
    something = Mystery(root)
    root.mainloop()

