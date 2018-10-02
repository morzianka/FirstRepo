from common import AddCommand,Command,DeleteCommand,ShowAllCommand,\
    ShowByCategoryCommand,ShowByMinMaxCommand,ShowForDateCommand,ExitCommand
import datetime

def askOperation():
    print("1 - ADD\n" +
        "2 - SHOW ALL\n" +
        "3 - SHOW FOR DATE\n" +
        "4 - SHOW BY CATEGORY\n" +
        "5 - SHOW BY MIN MAX\n" +
        "6 - DELETE\n" +
        "0 - EXIT");
    operationNum = int(input("What would you like to do?"));
    command = None
    if (operationNum == 1):
        command = AddCommand.AddCommand(
            user = {"Category":input("Category:"), "Product":input("Product:"), "Cost":float(input("Cost:")), "Date":input("Date:")})
    if (operationNum == 2):
        command = ShowAllCommand.ShowAllCommand()
    if (operationNum == 3):
        try:
            date = datetime.datetime.strptime(input("Date in format YYYY-MM-DD:"), "%Y-%m-%d")
        except:
            print("Wrong data format")
            return -1
        command = ShowForDateCommand.ShowForDateCommand(date)
    if (operationNum == 4):
        command = ShowByCategoryCommand.ShowByCategoryCommand(input("Category:"))
    if (operationNum == 5):
        command = ShowByMinMaxCommand.ShowByMinMaxCommand(input("Sort descending(yes/no)?:"))
    if (operationNum == 6):
        command = DeleteCommand.DeleteCommand()
    if (operationNum == 0):
        command = ExitCommand.ExitCommand()
    command.execute()
    return operationNum

print("Hello")
operationNum = None
while(operationNum != 0):
    operationNum = askOperation()

