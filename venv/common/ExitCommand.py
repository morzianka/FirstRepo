from common.Command import Command

class ExitCommand(Command):
    def execute(self):
        print("GoodBye!")