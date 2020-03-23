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

        # mystery box Heading (row 0)
        self.Mystery_Box_label = Label(self.Mystery_Box__frame,
                                       text="Mystery Box", font="arial 20 bold",
                                       fg="black", bg=background_color, padx=10, pady=10)
        self.Mystery_Box_label.grid(row=0, padx=5, pady=10)

        self.mystery_instructions = Label(self.Mystery_Box__frame,font="arial 10 italic",
                                          text="Please enter the amount of money you want to play with"
                                          "(a minimum of $5) in the box below. Remember that the profits "
                                          "are going to charity. Then choose the stakes. The higher the"
                                          "stake the high the stake the more profits you can make",
                                          wrap=300, justify=LEFT,fg="black",bg=background_color)
        self.mystery_instructions.grid(row=1)

        # Instruction row 1)

        # Entry box and button (row 2)

        self.entry_button_frame = Frame(self.Mystery_Box__frame, bg=background_color)
        self.entry_button_frame.grid(row=2)

        # Entry box (row 0 of entry button frame)
        self.money_amount_entry = Entry(self.entry_button_frame, width=20,
                                        font="arial 15 bold")
        self.money_amount_entry.grid(row=0, column=0)

        self.money_button_frame = Frame(self.Mystery_Box__frame)
        self.money_button_frame.grid(row=3)

        # five dollar button (row 2 column 0 )
        self.five_dollar_button = Button(self.money_button_frame,
                                         text="$5",font="arial 10 bold",fg="black",
                                         bg="#95E06C",padx=12, pady=12,
                                         command=lambda: self.to_game(5))
        self.five_dollar_button.grid(row=0, column=1)

        # ten dollar button (row 2 column 0 )
        self.ten_dollar_button = Button(self.money_button_frame,
                                         text="$10", font="arial 10 bold", fg="black",
                                         bg="#FF9933", padx=12, pady=12,
                                         command=lambda: self.to_game(10))
        self.ten_dollar_button.grid(row=0, column=2)

        # twenty dollar button (row 2 column 0 )
        self.twenty_dollar_button = Button(self.money_button_frame,
                                         text="$20", font="arial 10 bold", fg="black",
                                         bg="#FF0000", padx=12, pady=12,
                                         command=lambda: self.to_game(20))
        self.twenty_dollar_button.grid(row=0, column=3)

    def to_game(self, stakes):
        starting_balance = self.money_amount_entry.get()
        Game(self, stakes, starting_balance)

class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)
        background = "pink"

        # disable help button
        partner.five_dollar_button.config(state=DISABLED)
        partner.ten_dollar_button.config(state=DISABLED)
        partner.twenty_dollar_button.config(state=DISABLED)

        # Set up child window (ie: help box)
        self.game_box = Toplevel()

        # Set up GUI Frame
        self.game_frame = Frame(self.game_box, width=300, bg="#68B684")
        self.game_frame.grid(padx=10, pady=10)
        # Set up help heading (row 0)
        self.how_heading = Label(self.game_frame,
                                 text="help / instruction",
                                 font="arial 20 bold", bg="#68B684")
        self.how_heading.grid(row=0)
        # Help text (label, row 1)
        self.help_text = Label(self.game_frame,
                               text="Balance",
                               justify=LEFT, width=50, bg="#68B684", wrap=200,)
        self.help_text.grid(row=1)

        self.balan_diss_frame= Frame(self.game_frame, bg="#68B684")
        self.balan_diss_frame.grid(row=1)

        self.balance_btn = Button(self.balan_diss_frame, text="Balance", width=10, bg="#95E06C",
                                  font="arial 10 bold",
                                  command=partial)
        self.balance_btn.grid(row=1, column=0)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.balan_diss_frame, text="Dismiss", width=10, bg="red",
                                  font="arial 10 bold",
                                  command=partial(self.close_game, partner))
        self.dismiss_btn.grid(row=1, column=1)

    def close_game(self, partner):
        # Put help button back to normal
        partner.five_dollar_button.config(state=NORMAL)
        partner.ten_dollar_button.config(state=NORMAL)
        partner.twenty_dollar_button.config(state=NORMAL)
        self.game_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box")
    something = Mystery()
    root.mainloop()
