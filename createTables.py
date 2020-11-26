#!/usr/bin/python
import sqlite3

def createTables():
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Database created and Successfully Connected to SQLite")
        sqlite_create_table_query  =   '''CREATE TABLE GAMEUSER 
                                        (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                                        username CHAR(50) NOT NULL,
                                        pwd CHAR(50) NOT NULL,
                                        email TEXT NOT NULL UNIQUE);'''
        cursor.execute(sqlite_create_table_query)
        sqliteConnection.commit()
        print("SQLite table GAMEUSER created")
        cursor.close()

    except sqlite3.Error as error:
        print("Error", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")


def createDB():
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Database created and Successfully Connected to SQLite")
        sqlite_select_Query = "select sqlite_version();"
        cursor.execute(sqlite_select_Query)
        record = cursor.fetchall()
        print("SQLite Database Version is: ", record)
        cursor.close()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")