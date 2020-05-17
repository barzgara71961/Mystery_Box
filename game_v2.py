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
                                  bg="#95E06C", padx=12, pady=12,command=self.how_to_play )
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

    def how_to_play(self):
        print("you need help")
        get_help = How_to_play(self)
        #get_help.help_text.configure(text="i really dont want to write something long out")


class How_to_play:
    def __init__(self, partner):
        background = "#68B684"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Set up child window (ie: help box)
        self.help_box = Toplevel()

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()
        # Set up help heading (row 0)
        self.how_heading = Label(self.help_frame,
                                 text="how to play ",
                                 font="arial 20 bold",bg=background)
        self.how_heading.grid(row=0)
        # Help text (label, row 1)
        self.help_text = Label(self.help_frame,
                               text="i really dont want to write something long out",
                               justify=LEFT,width=50, bg=background,wrap=200)
        self.help_text.grid(column=0,row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame,text="Dismiss",padx=12, pady=12,bg="red",
                                  font="arial 10 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        starting_balance = int(starting_balance)

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
        self.game_stats_list = [starting_balance, starting_balance]

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
                               , padx=12, pady=12,command=self.help_rule)
        self.help_btn.grid(row=0, column=0)

        self.stats_btn = Button(self.help_export_frame, text="Game stats...",
                                font="arial 10 bold", bg="#95E06C", fg="black", padx=12, pady=12,
                                command=lambda: self.to_stats(self.round_stats_list, self.game_stats_list))
        self.stats_btn.grid(row=0, column=1)

        self.quit_btn = Button(self.game_frame, text="Quit",
                               font="arial 10 bold", bg="#95E06C",
                               fg="black", padx=12, pady=12,
                               command=self.to_quit)
        self.quit_btn.grid(row=6)

    def help_rule(self):
        print("you need help")
        get_help_rule = Help_rules(self)

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
                prize_list = "gold\n(${})".format(5 * stakes_multiplier)
                back_color = "#FFD700"  # gold colour
                round_winnings += 5 * stakes_multiplier
            elif 6 < prize_num <= 20:
                prize = PhotoImage(file="silver_med.gif")
                prize_list = "sliver\n(${})".format(2 * stakes_multiplier)
                back_color = "#C0C0C0"  # silver colour
                round_winnings += 2 * stakes_multiplier
            elif 21 < prize_num <= 35:
                prize = PhotoImage(file="copper_med.gif")
                prize_list = "copper\n(${})".format(1 * stakes_multiplier)
                back_color = "#B87333"  # copper colour
                round_winnings += stakes_multiplier
            else:
                prize = PhotoImage(file="lead.gif")
                prize_list = "lead\n($0)"

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

        # update game_stats_list with current balance (replace item in
        # position 1 with current balance)
        self.game_stats_list[1]= current_balance

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

    def to_stats(self, game_history, game_stats):
        GameStats(self, game_history, game_stats)


class Help_rules:
    def __init__(self, partner):
        background = "#68B684"

        # disable help button
        partner.help_btn.config(state=DISABLED)

        # Set up child window (ie: help box)
        self.help_box = Toplevel()

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()
        # Set up help heading (row 0)
        self.how_heading = Label(self.help_frame,
                                 text="how to play ",
                                 font="arial 20 bold",bg=background)
        self.how_heading.grid(row=0)
        # Help text (label, row 1)
        self.help_text = Label(self.help_frame,
                               text="i really dont want to write something long out",
                               justify=LEFT,width=50, bg=background,wrap=200)
        self.help_text.grid(column=0,row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame,text="Dismiss",padx=12, pady=12,bg="red",
                                  font="arial 10 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal
        partner.help_btn.config(state=NORMAL)   # Changed to normal so help button becomes available again.
        self.help_box.destroy()

class GameStats:
    def __init__(self, partner, game_history, game_stats):

        # print(game_history)
        print("Game Stats: ", game_stats)

        # disable help button
        # Commented out by GK because it is in the wrong place.
        # partner.stats_btn.config(state=DISABLED)

        heading = "arial 10 bold"
        content = "arial 10"

        # set up child window
        self.stats_box = Toplevel()

        # if user press cross at top, close help and releases help button
        # self.stats_box.protocol('WM_DELETE_WINDOW', partner(self.close_stats, partner))

        # set up GUI frame
        self.stats_frame = Frame(self.stats_box)
        self.stats_frame.grid()

        # Set up heading
        self.stats_heading_label = Label(self.stats_frame, text="Game Statistic",
                                         font="arial 15 bold")
        self.stats_heading_label.grid(row=0)

        # to export
        self.export_instructions = Label(self.stats_frame,
                                         text="here are your game stats."
                                         "please use the export button to"
                                         "access the result of each "
                                         "round that you played", wrap=200,
                                         font="arial 10 italic",
                                         justify=LEFT, fg="black")
        self.export_instructions.grid(row=1)

        # Starting balance
        self.details_frame = Frame(self.stats_frame)
        self.details_frame.grid(row=2)

        # starting balance

        self.start_balance_label = Label(self.details_frame,
                                         text="starting balance:", font=heading,
                                         anchor="e")
        self.start_balance_label.grid(row=0, column=0)

        self.start_balance_value_label = Label(self.details_frame, font=content,
                                               text="${}".format(game_stats[0]),anchor="w")
        self.start_balance_value_label.grid(row=0,column=1)

        # current balance
        self.current_balance_label = Label(self.details_frame,
                                           text="Current Balance:", font=heading,
                                           anchor="e")
        self.current_balance_label.grid(row=1, column=0)

        self.current_balance_value_label = Label(self.details_frame, font=content,
                                                 text="$()".format(game_stats[1]),anchor="w")
        self.current_balance_value_label.grid(row=1, column=1)

        if game_stats[1] > game_stats[0]:
            win_loss = "Amount won:"
            amount = game_stats[1] - game_stats[0]
            win_loss_fg = "green"
        else:
            win_loss = "Amount loss:"
            amount = game_stats[0] - game_stats[1]
            win_loss_fg = "#660000"

        # Amount won/ loss
        self.wind_loss_label = Label(self.details_frame,
                                    text=win_loss, font=heading, anchor="e")
        self.wind_loss_label.grid(row=2, column=0)

        self.wind_loss_value_label = Label(self.details_frame, font=content,
                                           text="${}".format(amount),
                                           fg=win_loss_fg, anchor="w")
        self.wind_loss_value_label.grid(row=2, column=1)

        # rounds played
        self.games_played_label = Label(self.details_frame,
                                        text="round played:", font=heading,
                                        anchor="e")
        self.games_played_label.grid(row=4, column=0)

        self.games_played_value_label = Label(self.details_frame, font=content,
                                              text=len(game_history), anchor="w")
        self.games_played_value_label.grid(row=4, column=2)
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box")
    something = Mystery()
    root.mainloop()
