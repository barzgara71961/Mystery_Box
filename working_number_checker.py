from tkinter import *
from functools import partial   # To prevent unwanted windows

import random


class Mystery:
    def __init__(self):

        # Formatting variables...

        background_color = "#68B684"

        # mystery box Main Screen GUT...
        self.Mystery_Box__frame = Frame(bg=background_color, width=900, height=900)
        self.Mystery_Box__frame.grid(padx=10, pady=10)  # padding in grey??

        # GUI to get starting balance and stakes
        self.starting_found = IntVar()
        self.starting_found.set(0)

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
                                          wrap=300, justify=LEFT,fg="black",bg=background_color)
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
        self.add_funds_button = Button(self.entry_button_frame,text="Add Funds", font="arial 10 bold",fg="black",
                                       bg="#95E06C", pady=7,
                                       command=self.check_funds)
        self.add_funds_button.grid(row=0, column=1, padx=5)

        self.money_button_frame = Frame(self.Mystery_Box__frame)
        self.money_button_frame.grid(row=4)

        # five dollar button (row 2 column 0 )
        self.five_dollar_button = Button(self.money_button_frame,
                                         text="Low $5",font="arial 10 bold", fg="black",
                                         bg="#95E06C",padx=12, pady=12,
                                         command=lambda: self.to_game(5))
        self.five_dollar_button.grid(row=0, column=1)

        # ten dollar button (row 2 column 0 )
        self.ten_dollar_button = Button(self.money_button_frame,
                                        text="Medium $10", font="arial 10 bold", fg="black",
                                        bg="#FF9933", padx=12, pady=12,
                                        command=lambda: self.to_game(10))
        self.ten_dollar_button.grid(row=0, column=2)

        # twenty dollar button (row 2 column 0 )
        self.twenty_dollar_button = Button(self.money_button_frame,
                                           text="High $20", font="arial 10 bold", fg="black",
                                           bg="#FF0000", padx=12, pady=12,
                                           command=lambda: self.to_game(20))
        self.twenty_dollar_button.grid(row=0, column=3)

        self.five_dollar_button.config(state=DISABLED)
        self.ten_dollar_button.config(state=DISABLED)
        self.twenty_dollar_button.config(state=DISABLED)

        self.help_export_frame = Frame(self.Mystery_Box__frame)
        self.help_export_frame.grid(row=5, pady=10)

        # help button (row 2 column 0 )
        self.help_button = Button(self.help_export_frame,text="How To Play",font="arial 10 bold",fg="black",
                                  bg="#95E06C", padx=12, pady=12,)
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
           self.starting_found.set(starting_balance)

    def to_game(self, stakes):
        starting_balance = self.money_amount_entry.get()

        Game(self, stakes, starting_balance)

        # hide start up window
        root.withdraw()


class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box")
    something = Mystery()
    root.mainloop()
