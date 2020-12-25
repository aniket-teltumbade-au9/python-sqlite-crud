import sqlite3 as lite
from tabulate import tabulate
# functionality
class DatabaseManage(object):
    def __init__(self):
        global con
        try:
            con=lite.connect('courses.db')
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS course(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)")
        except Exception:
            print("Unable to create a db!")

    # create data
    def insert_data(self,data):
        try:
            with con:
                cur = con.cursor()
                cur.execute("INSERT INTO course(name,description, price, is_private) VALUES (?,?,?,?)", data)
                return True
        except Exception:
            return False
    
    # read data
    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM course")
                return cur.fetchall()
        except Exception:
            return False
    
    # delete data
    def delete_data(self,id):
        try:
            with con:
                cur = con.cursor()
                cur.execute("DELETE FROM course WHERE id = ?",[id])
                return True
        except Exception:
            return False
# interface
def main():
    print("*"*40,end="\n")
    print("\n:: COURSE MANAGEMENT ::\n")
    print("*"*40,end="\n")
    
    db=DatabaseManage()
    
    print("*"*40,end="\n")
    print("\n:: User Manual ::\n")
    print("*"*40,end="\n")

    print('1. Insert a new course' , end="\n")
    print('2. Show all courses' , end="\n")
    print('3. Delete a corse' , end="\n")
    print("*"*40,end="\n")
    print("\n")
    
    choice = input('\n Enter a choice: ')
    if choice == "1":
        name=input("\n Enter a course name: ")
        description=input("\n Enter a course description: ")
        price=input("\n Enter a course price: ")
        pvt=bool(input("\n Enter a course private (0/1): "))
        if db.insert_data([name,description,price,pvt]):
            print("Course was inserted successfully")
        else:
            print("OOPS Something went wrong")
    elif choice =="2":
        print("\n:: Course List ::")
        # print(db.fetch_data())
        print(tabulate(db.fetch_data(), headers=["ID","NAME","DESC","PRICE","PVT"], tablefmt="fancy_grid"))
    elif choice == "3":
        record_id = input("Enter the course ID::")
        if db.delete_data(record_id):
            print("Course Was Deleted Successfully")
        else:
            print("Sorry for inconvenience! Try Again")
    else:
        print("Enter valid option")
if __name__=="__main__":
    d="y"
    while(d=="y"):
        main()
        d=input("Enter \'y\' to continue:: ")
