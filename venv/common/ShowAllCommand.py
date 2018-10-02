from common.Command import Command
import csv

class ShowAllCommand(Command):
    def execute(self):
         with open(self.path, "r", newline="") as file:
             reader = csv.reader(file)
             for row in reader:
                 print("{}|\t\t|{}|\t|{}|\t|{}".format(row[0].center(10), row[1].center(10), row[2].center(10), row[3].center(10)))


