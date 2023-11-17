class PrintCommand:
    def __init__(self, commands, descriptions):
        self.commands = commands
        self.descriptions = descriptions

    def printCommands(self):
        print("~" * 103)
        for command, description in self.descriptions.items():
            # Truncate the command if it is too long and adjust the spacing
            fixedLengthCommand = (command[:24]) if len(command) > 24 else command.ljust(25)
            fixedLengthDescription = (description[:65]) if len(description) > 69 else description.ljust(70)
            print(f"\ {fixedLengthCommand} -> {fixedLengthDescription} /")
        print("~" * 103)

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

            if userCommand in ('quit', 'Q'):
                print("Returning to main menu...")
                break
            elif not command_executed:
                print("Unknown command. Please try again.")

