from datetime import datetime
time = datetime.now() 

tables = []



class Table:
    def __init__(self, table_number):
        self.table_number = table_number
        self.table_occupied = False
        self.start_time = None
        self.end_time = None
        self.time_played = None
       
    

    def checkin(self):
        self.table_occupied = True
        self.start_time = datetime.now()
       
    

    def checkout(self):
        self.table_occupied = False
        self.end_time = datetime.now()
        
    def total_time(self):
        return self.end_time - self.start_time 

    def current_time(self):
        return datetime.now() - self.start_time 

def display_tables():
    for index in range(0 , len(tables)):
        table = tables[index]
        if table.table_occupied == False:
            print(f"Pool Table # {table.table_number} | Start time: {table.start_time} | End time: {table.end_time} | (Status- UNOCCUPIED")
        else:
            print(f"Pool Table # {table.table_number} | Start time: {table.start_time} | Current time played: {table.current_time()} | Status- OCCUPIED")

for index in range(1, 13):
    table_number = Table(index)
    tables.append(table_number)


choice = ""
while choice != 'q':
    print("---------University of Houston Pool Hall---------")
    print("Checkin table: Enter 1: ")
    print("Checkout table: Enter 2: ")
    print("View All Tables: Enter 3: ")
    print("To QUIT the app: Enter q")
    user_input =input("Enter Choice: ")
    if user_input == "1":
        display_tables()
        table = int(input("Please enter a pool table number to checkin: "))
        choice = tables[table - 1]
        choice.checkin()
        choice.current_time()
        
    if user_input == "q":
        break
    # choice = input("Press q to quit or any ket to continue: ") 
    if user_input == "2":
        display_tables()
        table = int(input("Please enter a pool table number to checkout: "))
        choice = tables[table - 1]
        choice.checkout()
      
    if user_input == "3":
        print(display_tables())
     








