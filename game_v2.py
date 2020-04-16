from tkinter import *
from functools import partial  # To prevent unwanted windows

import random


class Mystery:
    def __init__(self):

        # Formatting variables...
        background_color = "#68B684"

        # mystery box Main Screen GUT...
        self.Mystery_Box__frame = Frame(bg=background_color, width=900, height=900)
        self.Mystery_Box__frame.grid(padx=10, pady=10)  # padding in grey??

        # GUI to get starting balance and stakes
        self.starting_balance = IntVar()
        self.starting_balance.set(0)

        # mystery box Heading (row 0)
        self.Mystery_Box_label = Label(self.Mystery_Box__frame,
                                       text="Mystery Box", font="arial 20 bold",
                                       fg="black", bg=background_color, padx=10, pady=10)
        self.Mystery_Box_label.grid(row=0, padx=5, pady=10)

        # Instruction row 1)
        self.mystery_instructions = Label(self.Mystery_Box__frame, font="arial 10 italic",
                                          text="Please enter the amount of money you want to play with"
                                               "(a minimum of $5) in the box below. Remember that the profits "
                                               "are going to charity. Then choose the stakes. The higher the"
                                               "stake the high the stake the more profits you can make",
                                          wrap=300, justify=LEFT, fg="black", bg=background_color)
        self.mystery_instructions.grid(row=1)

        # Entry box and button (row 2)

        self.entry_button_frame = Frame(self.Mystery_Box__frame, bg=background_color)
        self.entry_button_frame.grid(row=2)

        # Error Label (row 3)
        self.amount_error_label = Label(self.Mystery_Box__frame, font="arial 10 italic",
                                        text="", bg=background_color)
        self.amount_error_label.grid(row=3)

        # Choice boxes... (row 4)

        # Entry box (row 0 of entry button frame)
        self.money_amount_entry = Entry(self.entry_button_frame, width=18,
                                        font="arial 15 bold")
        self.money_amount_entry.grid(row=0, column=0)

        # five dollar button (row 2 column 0 )
        self.add_funds_button = Button(self.entry_button_frame, text="Add Funds", font="arial 10 bold", fg="black",
                                       bg="#95E06C", pady=7,
                                       command=self.check_funds)
        self.add_funds_button.grid(row=0, column=1, padx=5)

        self.money_button_frame = Frame(self.Mystery_Box__frame)
        self.money_button_frame.grid(row=4)

        # five dollar button (row 2 column 0 )
        self.five_dollar_button = Button(self.money_button_frame,
                                         text="Low $5", font="arial 10 bold", fg="black",
                                         bg="#95E06C", padx=12, pady=12,
                                         command=lambda: self.to_game(1))
        self.five_dollar_button.grid(row=0, column=1)

        # ten dollar button (row 2 column 0 )
        self.ten_dollar_button = Button(self.money_button_frame,
                                        text="Medium $10", font="arial 10 bold", fg="black",
                                        bg="#FF9933", padx=12, pady=12,
                                        command=lambda: self.to_game(2))
        self.ten_dollar_button.grid(row=0, column=2)

        # twenty dollar button (row 2 column 0 )
        self.twenty_dollar_button = Button(self.money_button_frame,
                                           text="High $20", font="arial 10 bold", fg="black",
                                           bg="#FF0000", padx=12, pady=12,
                                           command=lambda: self.to_game(3))
        self.twenty_dollar_button.grid(row=0, column=3)

        self.five_dollar_button.config(state=DISABLED)
        self.ten_dollar_button.config(state=DISABLED)
        self.twenty_dollar_button.config(state=DISABLED)

        self.help_export_frame = Frame(self.Mystery_Box__frame)
        self.help_export_frame.grid(row=5, pady=10)

        # help button (row 2 column 0 )
        self.help_button = Button(self.help_export_frame, text="How To Play", font="arial 10 bold", fg="black",
                                  bg="#95E06C", padx=12, pady=12, )
        self.help_button.grid(row=0, column=2)

    def check_funds(self):
        starting_balance = self.money_amount_entry.get()

        # Set error background colour (and assum that there are no
        # error at the start
        error_back = "#ffafaf"
        has_error = "no"
        error_feedback = ""

        # change background to white (for testing purposes) ...
        self.money_amount_entry.config(bg="white")
        self.amount_error_label.config(text="")

        self.five_dollar_button.config(state=DISABLED)
        self.ten_dollar_button.config(state=DISABLED)
        self.twenty_dollar_button.config(state=DISABLED)

        def to_game(self, stakes):
            starting_balance = self.money_amount_entry.get()
            Game(self, stakes, starting_balance)

    def check_funds(self):
        starting_balance = self.money_amount_entry.get()

        # Set error background colour (and assum that there are no
        # error at the start
        error_back = "#ffafaf"
        has_error = "no"
        error_feedback = ""

        # change background to white (for testing purposes) ...
        self.money_amount_entry.config(bg="white")
        self.amount_error_label.config(text="")

        self.five_dollar_button.config(state=DISABLED)
        self.ten_dollar_button.config(state=DISABLED)
        self.twenty_dollar_button.config(state=DISABLED)

        try:
            starting_balance = int(starting_balance)

            if starting_balance < 5:
                has_error = "yes"
                error_feedback = "did you not read the instructions\n" \
                                 "a minimum of $5 "
            elif starting_balance > 50:
                has_error = "yes"
                error_feedback = "unfortunately I can't steal that much money"
            elif starting_balance >= 20:
                self.five_dollar_button.config(state=NORMAL)
                self.ten_dollar_button.config(state=NORMAL)
                self.twenty_dollar_button.config(state=NORMAL)
                error_feedback = "sorry you are too cheap"
            elif starting_balance >= 10:
                self.five_dollar_button.config(state=NORMAL)
                self.ten_dollar_button.config(state=NORMAL)
            elif starting_balance >= 5:
                self.five_dollar_button.config(state=NORMAL)


        except ValueError:
            has_error = "yes"
            error_feedback = "Please enter a dollar amount"

        if has_error == "yes":
            self.money_amount_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback)

        else:
            self.starting_balance.set(starting_balance)

    def to_game(self, stakes):
        starting_balance = self.money_amount_entry.get()
        print(starting_balance)

        Game(self, stakes, starting_balance)

        # hide start up window
        root.withdraw()


class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)

        background_color = "#68B684"

        # initialise variables
        self.balance = IntVar()
        # set starting balance to amount entered by user at start of game
        self.balance.set(starting_balance)

        # get value of stakes
        self.multiplier = IntVar()
        self.multiplier.set(stakes)

        # List for holding statistics
        self.round_stats_list = []

        # GUI setup
        self.game_box = Toplevel()

        # If user press cross at top, game quits
        self.game_box.protocol('WM_DELETE_WINDOW', self.to_quit)

        self.game_frame = Frame(self.game_box,bg=background_color)
        self.game_frame.grid()

        # Heading row
        self.heading_label = Label(self.game_frame, text="play...",
                                   font="Arial 24 bold", padx=10, pady=10,
                                   bg=background_color)
        self.heading_label.grid(row=0)

        # Instructions label
        self.Instructions_label = Label(self.game_frame, wrap=300, justify=LEFT,
                                        text="Press <enter> or click the 'open "
                                             "Boxes' button to reveal the "
                                             "contents of the mystery boxes.",
                                        font="arial 10" ,bg=background_color)
        self.Instructions_label.grid(row=1)

        # boxes go here
        box_text = "arial 15 bold"
        box_back = "#68B684"
        box_width = 5
        self.box_frame = Frame(self.game_frame)
        self.box_frame.grid(row=2)

        photo = PhotoImage(file="question.gif")

        self.prize1_label = Label(self.box_frame, text="?\n", font=box_text,
                                  image=photo, padx=10, pady=10)
        self.prize1_label.photo = photo
        self.prize1_label.grid(row=0, column=0)

        self.prize2_label = Label(self.box_frame, text="?\n", font=box_text,
                                  image=photo, padx=10, pady=10)
        self.prize2_label.photo = photo
        self.prize2_label.grid(row=0, column=1)

        self.prize3_label = Label(self.box_frame, text="?\n", font=box_text,
                                  image=photo, padx=10, pady=10)
        self.prize3_label.photo = photo
        self.prize3_label.grid(row=0, column=2)

        # Play button goes here
        self.play_btn = Button(self.game_frame, text="open boxes",
                               bg="yellow", font="arial 10 bold", width=20,
                               padx=10, pady=10, command=self.reveal_boxes)

        self.play_btn.focus()
        self.play_btn.bind('<Return>', lambda e: self.reveal_boxes())
        self.play_btn.grid(row=3)

        # balance label

        start_text = "Game cost: ${}\n""\nHow much" \
                     " will you win?".format(stakes * 5)

        self.balance_label = Label(self.game_frame, font="arial 12 bold", fg="black",
                                   text=start_text, justify=LEFT,bg=background_color)
        self.balance_label.grid(row=4, pady=10)

        # Help and Game Stats button
        self.help_export_frame = Frame(self.game_frame)
        self.help_export_frame.grid(row=5, pady=10)

        self.help_btn = Button(self.help_export_frame, text="Help / Rules",
                               font="arial 10 bold", bg="#95E06C", fg="black"
                               , padx=12, pady=12)
        self.help_btn.grid(row=0, column=0)

        self.stats_btn = Button(self.help_export_frame, text="Game stats...",
                                font="arial 10 bold", bg="#95E06C", fg="black"
                                , padx=12, pady=12)
        self.stats_btn.grid(row=0, column=1)

        self.quit_btn = Button(self.game_frame, text="Quit",
                               font="arial 10 bold", bg="#95E06C",
                               fg="black", padx=12, pady=12,
                               command=self.to_quit)
        self.quit_btn.grid(row=6)

    def reveal_boxes(self):
        # retrieve the balance from initial function
        current_balance = self.balance.get()
        stakes_multiplier = self.multiplier.get()

        round_winnings = 0
        prizes = []
        stats_prizes = []
        prize_list = []
        for item in range(0, 3):
            prize_num = random.randint(1, 100)

            if 0 < prize_num <= 5:
                prize = PhotoImage(file="gold_med.gif")
                prize = "gold\n(${})".format(5 * stakes_multiplier)
                back_color = "#FFD700"  # gold colour
                round_winnings += 5 * stakes_multiplier
            elif 6 < prize_num <= 20:
                prize = PhotoImage(file="silver_med.gif")
                prize = "sliver\n(${})".format(2 * stakes_multiplier)
                back_color = "#C0C0C0"  # silver colour
                round_winnings += 2 * stakes_multiplier
            elif 21 < prize_num <= 35:
                prize = PhotoImage(file="copper_med.gif")
                prize = "copper\n(${})".format(1 * stakes_multiplier)
                back_color = "#B87333"  # copper colour
                round_winnings += stakes_multiplier
            else:
                prize = PhotoImage(file="lead.gif")
                prize = "lead\n($0)"

            prizes.append(prize)
            stats_prizes.append(prize_list)

        photo1 = prizes[0]
        photo2 = prizes[1]
        photo3 = prizes[2]

        # Display prizes...
        self.prize1_label.config(image=photo1)
        self.prize1_label.photo = photo1
        self.prize2_label.config(image=photo2)
        self.prize2_label.photo = photo2
        self.prize3_label.config(image=photo3)
        self.prize3_label.photo = photo3

        # Deduct cost of game
        current_balance -= 5 * stakes_multiplier

        # Add winning
        current_balance += round_winnings

        # set balance to new balance
        self.balance.set(current_balance)

        balance_statement = "Game Cost: $ {}\nPayback: ${} \n" \
                            "Current Balance: ${}".format(5 * stakes_multiplier,
                                                          round_winnings,
                                                          current_balance)
        # Add round results to statistics list
        round_summary ="{} | {} | {} - Cost: ${} | " \
                       "Payback: ${} | Current Balance:" \
                       "${}".format(stats_prizes[0], stats_prizes[1],
                                    stats_prizes[2],
                                    5 * stakes_multiplier,round_winnings,
                                    current_balance)
        self.round_stats_list.append(round_summary)
        print(self.round_stats_list)


        # Edit label so user can see their balance
        self.balance_label.configure(text=balance_statement)

        if current_balance < 5 * stakes_multiplier:
            self.play_btn.config(state=DISABLED)
            self.game_box.focus()
            self.play_btn.config(text="Game Over")

            balance_statement = "Current Balance: ${}\n" \
                                "Your balance is too low. You can only quit " \
                                "or view your stats. sorry about that".format(current_balance)
            self.balance_label.config(fg="black", font="arial 10 bold",bg="#68B684",
                                      text=balance_statement)

    def to_quit(self):
        root.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box")
    something = Mystery()
    root.mainloop()
