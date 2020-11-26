#!/usr/bin/python
import createTables as PYSetup
import dbConnector as conn

# driver code
def main():
    #PYSetup.createDB()
    #PYSetup.createTables()
    try:
        db = conn.database()
        newUserID = db.addUser("Bob","notTelling","Bob@nottelling.com")
        print(newUserID)
    except:
        print("you must create the sqlite database file first before trying to access")
        print("if you got an error - it's because you [probably] didn't create the actual database file - bad you")
        print("uncomment the code on lines 7 & 8 then try running this main file again")
        print("IMPORTANT: once you've created the database file you need only do so once!")

if __name__ == '__main__':
    main()