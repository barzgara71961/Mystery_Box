def temp_convert(self, low):
    print(low)

    error = "#ffafaf"  # pale pink when a error

    # Retrieve amount entered into Entry field
    money_amount_entry = self.to_convert_entry.get()

    try:
        money_amount_entry = float(to_convert)
        has_error = "no"

        # Display answer
        if has_error == "no":
            self.converted_label.configure(text=answer, fg="blue")
            self.money_amount_entry.configure(bg="white")
        else:
            self.converted_label.configure(text=answer, fg="red")
            self.money_amount_entry.configure(bg=error)

        # Add Answer to list for history
        if has_error != "yes":
            self.all_calc_list.append(answer)
            self.five_dollar_button.config(state=NORMAL)

    except ValueError:
        self.converted_label.configure(text="enter a number", fg="red")
        self.to_convert_entry.configure(bg=error)