from common.Command import Command
import csv

class ShowByCategoryCommand(Command):
    def __init__(self, category):
        self.category = category

    def execute(self):
        with open(self.path, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if(row[0] == self.category):
                    print(row[0], "\t", row[1], "\t", row[2], "\t", row[3])