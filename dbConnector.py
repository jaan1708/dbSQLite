#!/usr/bin/python
import sqlite3

class database(object):
    def __init__(self):
        self.__dbConn = None
        # connection settings - these might change 
        # to a mysql or postgress database
        # these would really be in an external file
        self.__databaseName = 'SQLite_Python.db' # this is name of the mysql file name

        # try and connect to the named db
        try:        
            sqliteConnection = sqlite3.connect(self.__databaseName)
            self.__dbConn = sqliteConnection
        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
        finally:
            pass

    def __del__(self):
          # destructor - close the connection
          if (self.__dbConn):
              self.__dbConn.close()
              
    def addUser(self, username, pwd, email):
        # connect to db and insert a new user
        try:
            with self.__dbConn:
                cur = self.__dbConn.cursor()
                query = "INSERT INTO GAMEUSER (username, pwd, email) VALUES (?, ?, ?);" # using ? means sql injection attack is prevented
                cur.execute(query, (username, pwd, email,))
                self.__dbConn.commit()
                last_row_id = cur.lastrowid
                # return the id of the new user - this will be the autoincremented id from the db
                return last_row_id

        except sqlite3.IntegrityError as error:
            print("error:", error)
            self.__dbConn.rollback() # don't commit the transaction
            return -1

    def getUser(self, id):
        query = "SELECT ID, username, email FROM GAMEUSER WHERE ID = ?;"
        try:
            with self.__dbConn:
                self.__dbConn.row_factory = sqlite3.Row # this will give a dictionary with the keys as the column names
                cur = self.__dbConn.cursor() # create a cursor object using the dbconnection
                cur.execute(query, (id,)) # execute query
                rows = cur.fetchone()
                return rows
        except sqlite3.IntegrityError:
            print("error")
            return None
