from common.Command import Command
import csv
import datetime

class ShowForDateCommand(Command):
    def __init__(self, date):
        self.date = date

    def execute(self):
        with open(self.path, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if (row[3] == str(self.date).replace(" 00:00:00", "")):
                    print(row)