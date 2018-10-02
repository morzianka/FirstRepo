from common.Command import Command
import csv

class AddCommand(Command):
    user = {}

    def __init__(self, user):
        self.user = user

    def execute(self):
        with open(self.path, "a", newline="") as file:
            columns = ["Category", "Product", "Cost", "Date"]
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writerow(self.user)
        print("New row added: ", self.user)