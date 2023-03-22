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
    def runQuery(self,query):
        # We want to edit the database that this object has the file name to
        con= sqlite3.connect(os.getenv('HOME')+self.filename)
        cur = con.cursor() 
        cur.execute(query)
        con.commit()
        con.close()