class PrintCommand:
    def __init__(self, commands, descriptions):
        self.commands = commands
        self.descriptions = descriptions

    def printCommands(self):
        longest_command_length = 0
        longest_description_length = 0

        for command, description in self.descriptions.items():
            longest_command_length = max(longest_command_length, len(command))
            longest_description_length = max(longest_description_length, len(description))
        longest_command_length += 4
        longest_description_length += 4

        # 5 additional characters for "->" and additional 1 space from the beginning.
        wave_length = longest_command_length + longest_description_length + 5

        print(' ' + "~" * wave_length)
        for command, description in self.descriptions.items():
            # Adjust the command and description to have even spacing and a tab (4 spaces)
            formatted_command = command.ljust(longest_command_length)
            formatted_description = description.ljust(longest_description_length)
            print(f"\ {formatted_command} -> {formatted_description}/")
        print(' ' + "~" * wave_length)


    def userInput(self):
        while True:
            self.printCommands()
            userCommand = input("Enter command: ")

            command_executed = False
            for key in self.commands:
                if userCommand in key:  # Since all keys are tuples, this check is sufficient
                    self.commands[key]()
                    command_executed = True
                    break

            if userCommand in ('quit', 'Q', 'q'):
                print("Returning to main menu...")
                break
            elif not command_executed:
                print("Unknown command. Please try again.")


    """
    Prompts the user to enter a cryptocurrency coin symbol (e.g., ETH, ARB) and validates 
    the input.
    Returns:
        str or None: Returns the valid coin symbol as a string if a valid input is provided. 
                     Returns None if the user enters 'q' to quit the input process.
    """
    def coinInput(self, method):
        while True:
            coin = str(input("Enter coin (or q to quit): ").upper())
            if coin == "Q":
                return None
            if method(coin) is not None:
                return coin
            else:
                print(f"{coin} is not a valid coin. Please try again.")


    """
    Prompts the user to input a value and validates it against a set of allowed choices.
    Args:
        prompt (str): The prompt message to display to the user.
        validChoices (list of str or int): A list of valid input choices.
    Returns:
        str or int or None: The valid user input matching one of the validChoices.
                            Returns None if the user chooses to exit with 'Q'.
    """
    def getValidInput(self, prompt, validChoices):
        while True:
            userInput = input(prompt).upper()
            if userInput == "Q":
                return None

            if all(isinstance(choice, int) for choice in validChoices):
                try:
                    userInput = int(userInput)
                except ValueError:
                    pass  # Continue to the next iteration if conversion fails

            if userInput in validChoices:
                return userInput
            print(f"Invalid input. Please enter one of {validChoices}.")


    """
    Get the quantity of the coin or the price of the coin,
    and quote order quantity. 
    """
    def getFloatInput(self, prompt):
        while True:
            user_input = input(prompt)
            if user_input.upper() == "Q":
                return None  # Signal to exit
            try:
                return float(user_input)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

