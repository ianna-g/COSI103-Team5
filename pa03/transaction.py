"""imports"""
import sqlite3
import os

def toDictTransactions(t):
    ''' t is a tuple (rowid, item #, amount, category, date, description)'''
    transaction = {'item #': t[0], 'amount': t[1],
    'category': t[2], 'date': t[3], 'description': t[4]}
    return transaction

def toDictCategories(c):
    ''' t is a tuple (rowid, item #, amount, category, date, description)'''
    category = { 'id': c[0], 'name': c[1] }
    return category

# Author: Rose
def toDictSumByDate(t):
    ''' t is a tuple (date, category, # of transactions, sum of transaction amounts)'''
    summary = {'date': t[0], 'category': t[1],
    '# of transactions': t[2], 'sum of transaction amounts': t[3]}
    return summary

# Author: Rose
def toDictSumByMonth(t):
    ''' t is a tuple (month, category, # of transactions, sum of transaction amounts)'''
    summary = {'month': t[0], 'category': t[1],
    '# of transactions': t[2], 'sum of transaction amounts': t[3]}
    return summary

# Author: Rose
def toDictSumByYear(t):
    ''' t is a tuple (year, category, # of transactions, sum of transaction amounts)'''
    summary = {'year': t[0], 'category': t[1],
    '# of transactions': t[2], 'sum of transaction amounts': t[3]}
    return summary

# Author: Ianna
def toDictSumByCategory(t):
    ''' t is a tuple (category, date, # of transactions, sum of transaction amounts)'''
    summary = {'category': t[0], 'date': t[1],
    '# of transactions': t[2], 'sum of transaction amounts': t[3]}
    return summary

class Transaction:
    """initializes a transaction object."""
    """filename should lead to the db file we want this transaction object to be linked to"""
    def __init__(self, filename):
        self.filename = filename
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, amount real,
                    category integer, date text, description text)''',())
        # This initializes an sql database that just has all of the categories for the main database
        self.runCategoryQuery('''CREATE TABLE IF NOT EXISTS categories
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, name text)''',())
    
    # Run this method if you want to query through the catagory table
    # Author: Rose
    def runCategoryQuery(self, query, tuple):
        """ return all of the categories as a list of dicts."""
        con= sqlite3.connect(os.getenv('HOME') + "/" + self.filename)
        cur = con.cursor()
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDictCategories(c) for c in tuples]

    # Run this method if you want to query through the main table
    def runQuery(self,query,tuple):
        ''' return all of the transactions as a list of dicts.'''
        con= sqlite3.connect(os.getenv('HOME') + "/" + self.filename)
        cur = con.cursor()
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDictTransactions(t) for t in tuples]
    
    # Used to print out sum by date
    # Author: Rose
    def runQuerySumByDate(self,query,tuple):
        """Used to print out sum by date"""
        con= sqlite3.connect(os.getenv('HOME') + "/" + self.filename)
        cur = con.cursor()
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDictSumByDate(t) for t in tuples]
    
    # Used to print out sum by month
    # Author: Rose
    def runQuerySumByMonth(self,query,tuple):
        """Used to print out sum by month"""
        con= sqlite3.connect(os.getenv('HOME') + "/" + self.filename)
        cur = con.cursor()
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        print([toDictSumByMonth(t) for t in tuples])
        return [toDictSumByMonth(t) for t in tuples]
    
    # Used to print out sum by year
    # Author: Rose
    def runQuerySumByYear(self,query,tuple):
        """Used to print out sum by year"""
        con= sqlite3.connect(os.getenv('HOME') + "/" + self.filename)
        cur = con.cursor()
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        print([toDictSumByYear(t) for t in tuples])
        return [toDictSumByYear(t) for t in tuples]
    
    # Used to print out sum by category
    # Author: Rose
    def runQuerySumByCategory(self,query,tuple):
        """Used to print out sum by category"""
        con= sqlite3.connect(os.getenv('HOME') + "/" + self.filename)
        cur = con.cursor()
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        print([toDictSumByCategory(t) for t in tuples])
        return [toDictSumByCategory(t) for t in tuples]
    
################## MinSung ####################
    def add_transaction(self, details):
        ''' Add transaction entry '''
        return self.runQuery("INSERT INTO transactions (amount, category, date, description) VALUES(?,?,?,?);", (details["amount"], details["category"], details["date"], details["description"]))
    
    def check_category_exists(self, category):
        """ Check if category already exists in categories table """
        con = sqlite3.connect(os.getenv('HOME') + "/" + self.filename)
        cur = con.cursor()
        cur.execute("SELECT * FROM categories WHERE name = ?", (category,))
        data = cur.fetchone()
        con.commit()
        con.close()
        if data is None:
            return False
        return True
        # exists = self.runQuery("SELECT EXISTS(SELECT 1 
        # FROM categories WHERE name= ? );", (category))
        # return exists
    
    def add_category(self, category):
        """ Add category entry to categories table """
        return self.runQuery("INSERT INTO categories (name) VALUES (?);", (category,))
###############################################

#################### Rose #####################
    def show_transactions(self):
        """Used to print out all of the transactions"""
        return self.runQuery("SELECT * FROM transactions;", ())
    
    def show_categories(self):
        """Used to print out all of the categories"""
        return self.runCategoryQuery("SELECT * FROM categories;", ())
    
    # Used to get the category name from the integer value
    def get_category(self, index):
        """Used to get the category name from the integer value"""
        con= sqlite3.connect(os.getenv('HOME') + "/" + self.filename)
        cur = con.cursor()
        cur.execute("SELECT DISTINCT name FROM categories WHERE id = ?", (index,))
        name = cur.fetchall()[0][0]
        con.commit()
        con.close()
        return name
###############################################

################## Ianna ######################

       # date format (YYYY-MM-DD)

    #extract the dates
    def sum_by_date(self):
        """ Prints summary of transactions by date """
        return self.runQuerySumByDate("SELECT date, category, COUNT(amount), SUM(amount) FROM transactions GROUP BY date;", ())
    
    #extract the months 
    def sum_by_month(self):
        """ Prints summary of transactions by month """
        return self.runQuerySumByMonth("SELECT strftime('%m', date) AS month, category, COUNT(amount), SUM(amount) FROM transactions GROUP BY month;", ())
    
    #extract the years 
    def sum_by_year(self):
        """ Prints summary of transactions by year """
        return self.runQuerySumByYear("SELECT strftime('%Y', date) as year, category, COUNT(amount), SUM(amount) FROM transactions GROUP BY year;", ())
    
    #based on the category return some data
    def sum_by_category(self):
        """ Prints summary of transactions by category """
        return self.runQuerySumByCategory("SELECT category, date, COUNT(amount), SUM(amount) FROM transactions GROUP BY category;", ())


######################Shaithea#########################
    # deletes a transaction
    def delete_transaction(self, item_number):
        """ Deletes a transaction of choice  """
        return self.runQuery("DELETE FROM transactions WHERE id = ?;", (item_number,))

    # modifies the category of a transaction
    def modify_category(self, item_number, newName):
        """ Modifies a category of choice  """
        return self.runQuery("UPDATE categories SET name = ? WHERE id = ?;", (newName, item_number))
