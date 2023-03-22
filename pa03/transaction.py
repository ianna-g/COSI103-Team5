# Rose
# TODO add functionality. I don't really understand what this class is meant to do so I'm going to go to office hours to ask.
# Feel free to change literally all of this!

import sqlite3
import sys
import os



class Transaction:

    def __init__(self, filename):
        self.filename = filename

    # TODO check that this is right.
    def runQuery(self, query, placeholder_values):
        # We want to edit the database that this object has the file name to
        con= sqlite3.connect(self.filename)
        cur = con.cursor() 
        cur.execute(query, placeholder_values)
        con.commit()
        con.close()
    
    def add_transaction(self, details):
        ''' Add transaction entry '''
        return self.runQuery("INSERT INTO transactions (amount, category, date, description) VALUES(?,?,?,?);", (details["amount"], details["category"], details["date"], details["description"]))

    def show_transactions(self):
        return self.runQuery("SELECT * FROM transactions;", ())