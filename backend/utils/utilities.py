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

