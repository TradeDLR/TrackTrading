class PrintCommand:
    def __init__(self, commands, descriptions):
        self.commands = commands
        self.descriptions = descriptions

    def printCommands(self):
        print("*" * 103)
        for command, description in self.descriptions.items():
            # Truncate the command if it is too long and adjust the spacing
            fixedLengthCommand = (command[:24]) if len(command) > 24 else command.ljust(25)
            fixedLengthDescription = (description[:65]) if len(description) > 69 else description.ljust(70)
            print(f"* {fixedLengthCommand} -> {fixedLengthDescription} *")
        print("*" * 103)

    def userInput(self):
        while True:
            self.printCommands()
            userCommand = input("Enter command: ").lower()
            if userCommand == 'quit':
                break
            if userCommand in self.commands:
                self.commands[userCommand]()
            else:
                print("Unknown command. Please try again.")

    def quit(self):
        print("Goodbye")
        exit()