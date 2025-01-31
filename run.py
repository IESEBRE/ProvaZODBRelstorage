import transaction
from ZODB.config import databaseFromURL
from persistent import Persistent
path = "zodb_config.zcml"

db = databaseFromURL(path)

# Define a simple persistent class
class Employee(Persistent):
    def __init__(self, name, manager=None):
        self.name = name
        self.manager = manager

    def setName(self, name):
        self.name = name


    def getName(self):
        return self.name


# Load the database configuration
db = databaseFromURL('zodb_config.zcml')

# Open a connection to the database
connection = db.open()
root = connection.root()

# get the employees mapping, creating an empty mapping if
# necessary
print(root.get("employees"))
if not root.get("employees") != None:
    root["employees"] = {}
employees=root["employees"]


def listEmployees():
    if len(employees.values())==0:
        print ("There are no employees.")
        print ()
        return
    for employee in employees.values():
        print ("Name: %s" % employee.getName())
        if employee.manager is not None:
            print ("Manager's name: %s" % employee.manager.getName())
        print("")

def addEmployee(name, manager_name=None):
    if employees.get(name) !=  None:
        print ("There is already an employee with this name.")
        return
    if manager_name:
        try:
            manager=employees[manager_name]
        except KeyError:
            print()
            print ("No such manager")
            print()
            return
        employees[name]=Employee(name, manager)
    else:
        employees[name]=Employee(name)

    root['employees'] = employees  # reassign to change
    transaction.commit()
    print ("Employee %s added." % name)
    print()


if __name__=="__main__":
    while 1:
        choice=input("Press 'L' to list employees, 'A' to add an employee, or 'Q' to quit:")
        choice=choice.lower()
        if choice=="l":
            listEmployees()
        elif choice=="a":
            name=input("Employee name:")
            manager_name=input("Manager name:")
            addEmployee(name, manager_name)
        elif choice=="q":
            break

    # close database
    connection.close()
    db.close()