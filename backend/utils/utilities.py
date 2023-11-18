class PrintCommand:
    def __init__(self, commands, descriptions, lenwave=130, lenCommand=60, lenDescipt=75):
        self.commands = commands
        self.descriptions = descriptions
        self.lenwave = lenwave
        self.lenCommand = lenCommand
        self.lenDescipt = lenDescipt

    def printCommands(self):
        print("~" * self.lenwave)
        for command, description in self.descriptions.items():
            # Truncate the command if it is too long and adjust the spacing
            fixedLengthCommand = (command[:self.lenCommand]) if len(command) > self.lenCommand else command.ljust(self.lenCommand)
            fixedLengthDescription = (description[:self.lenDescipt]) if len(description) > self.lenDescipt else description.ljust(self.lenDescipt)
            print(f"\ {fixedLengthCommand} -> {fixedLengthDescription} /")
        print("~" * self.lenwave)

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

