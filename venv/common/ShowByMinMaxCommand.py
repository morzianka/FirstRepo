from common.Command import Command
import csv
import operator

class ShowByMinMaxCommand(Command):
    def __init__(self, desc):
        self.desc = desc

    def execute(self):
        with open(self.path, "r", newline="") as file:
            reader = csv.reader(file)
            minArray = []
            for row in reader:
                if(row[2] == "Cost"):
                    print(row[0], "\t", row[1], "\t", row[2], "\t", row[3])
                else:
                    minArray += [row]
            if self.desc == "yes":
                for row in sorted(minArray, key = lambda row: (float(row[2])), reverse=True):
                    print(row[0], "\t", row[1], "\t", row[2], "\t", row[3])
            else:
                for row in sorted(minArray, key = lambda row: (float(row[2]))):
                    print(row[0], "\t", row[1], "\t", row[2], "\t", row[3])


