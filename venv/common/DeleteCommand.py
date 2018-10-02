from common.Command import Command

class DeleteCommand(Command):
    def execute(self):
        # opening the file with w+ mode truncates the file
        f = open(self.path, "w+")
        print("File cleared")