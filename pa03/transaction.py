"""imports"""
import sqlite3
import os

def to_dict_transactions(trans):
    ''' t is a tuple (rowid, item #, amount, category, date, description)'''
    transaction = {'item #': trans[0], 'amount': trans[1],
    'category': trans[2], 'date': trans[3], 'description': trans[4]}
    return transaction

def to_dict_categories(cat):
    ''' t is a tuple (rowid, item #, amount, category, date, description)'''
    category = { 'id': cat[0], 'name': cat[1] }
    return category

# Author: Rose
def to_dict_sum_by_date(trans):
    ''' t is a tuple (date, category, # of transactions, sum of transaction amounts)'''
    summary = {'date': trans[0], 'category': trans[1],
    '# of transactions': trans[2], 'sum of transaction amounts': trans[3]}
    return summary

# Author: Rose
def to_dict_sum_by_month(trans):
    ''' t is a tuple (month, category, # of transactions, sum of transaction amounts)'''
    summary = {'month': trans[0], 'category': trans[1],
    '# of transactions': trans[2], 'sum of transaction amounts': trans[3]}
    return summary

# Author: Rose
def to_dict_sum_by_year(trans):
    ''' t is a tuple (year, category, # of transactions, sum of transaction amounts)'''
    summary = {'year': trans[0], 'category': trans[1],
    '# of transactions': trans[2], 'sum of transaction amounts': trans[3]}
    return summary

# Author: Ianna
def to_dict_sum_by_category(trans):
    ''' t is a tuple (category, date, # of transactions, sum of transaction amounts)'''
    summary = {'category': trans[0], 'date': trans[1],
    '# of transactions': trans[2], 'sum of transaction amounts': trans[3]}
    return summary

class Transaction:
    """initializes a transaction object. filename should lead to the db
    file we want this transaction object to be linked to"""
    def __init__(self, filename):
        self.filename = filename
        self.run_query('''CREATE TABLE IF NOT EXISTS transactions
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, amount real,
                    category integer, date text, description text)''',())
        # This initializes an sql database that just has all of the categories for the main database
        self.run_category_query('''CREATE TABLE IF NOT EXISTS categories
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, name text)''',())

    # Run this method if you want to query through the catagory table
    # Author: Rose
    def run_category_query(self, query, trans):
        """ return all of the categories as a list of dicts."""
        con= sqlite3.connect(os.getenv('HOME') + "/" + self.filename)
        cur = con.cursor()
        cur.execute(query,trans)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [to_dict_categories(c) for c in tuples]

    # Run this method if you want to query through the main table
    def run_query(self,query,trans):
        ''' return all of the transactions as a list of dicts.'''
        con= sqlite3.connect(os.getenv('HOME') + "/" + self.filename)
        cur = con.cursor()
        cur.execute(query,trans)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [to_dict_transactions(t) for t in tuples]

    # Used to print out sum by date
    # Author: Rose
    def run_query_sum_by_date(self,query,trans):
        """Used to print out sum by date"""
        con= sqlite3.connect(os.getenv('HOME') + "/" + self.filename)
        cur = con.cursor()
        cur.execute(query,trans)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [to_dict_sum_by_date(t) for t in tuples]

    # Used to print out sum by month
    # Author: Rose
    def run_query_sum_by_month(self,query,trans):
        """Used to print out sum by month"""
        con= sqlite3.connect(os.getenv('HOME') + "/" + self.filename)
        cur = con.cursor()
        cur.execute(query,trans)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [to_dict_sum_by_month(t) for t in tuples]

    # Used to print out sum by year
    # Author: Rose
    def run_query_sum_by_year(self,query,trans):
        """Used to print out sum by year"""
        con= sqlite3.connect(os.getenv('HOME') + "/" + self.filename)
        cur = con.cursor()
        cur.execute(query,trans)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [to_dict_sum_by_year(t) for t in tuples]

    # Used to print out sum by category
    # Author: Rose
    def run_query_sum_by_category(self,query,trans):
        """Used to print out sum by category"""
        con= sqlite3.connect(os.getenv('HOME') + "/" + self.filename)
        cur = con.cursor()
        cur.execute(query,trans)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [to_dict_sum_by_category(t) for t in tuples]

################## MinSung ####################
    def add_transaction(self, details):
        ''' Add transaction entry '''
        return self.run_query("""INSERT INTO transactions (amount, category, date, description)
          VALUES(?,?,?,?);""",(details["amount"], details["category"],
                               details["date"], details["description"]))

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
        # exists = self.run_query("SELECT EXISTS(SELECT 1
        # FROM categories WHERE name= ? );", (category))
        # return exists

    def check_transaction_exists(self, transaction_index):
        """ Check if transaction exists in table """
        con = sqlite3.connect(os.getenv('HOME') + "/" + self.filename)
        cur = con.cursor()
        cur.execute("SELECT * FROM transactions WHERE id = ?", (transaction_index,))
        data = cur.fetchone()
        con.commit()
        con.close()
        if data is None:
            return False
        return True

    def add_category(self, category):
        """ Add category entry to categories table """
        return self.run_query("INSERT INTO categories (name) VALUES (?);", (category,))
###############################################

#################### Rose #####################
    def show_transactions(self):
        """Used to print out all of the transactions"""
        return self.run_query("SELECT * FROM transactions;", ())

    def show_categories(self):
        """Used to print out all of the categories"""
        return self.run_category_query("SELECT * FROM categories;", ())

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
        return self.run_query_sum_by_date("""SELECT date, category, COUNT(amount), SUM(amount)
        FROM transactions GROUP BY date;""", ())

    #extract the months
    def sum_by_month(self):
        """ Prints summary of transactions by month """
        return self.run_query_sum_by_month("""SELECT strftime('%m', date) AS month, category,
        COUNT(amount), SUM(amount) FROM transactions GROUP BY month;""", ())

    #extract the years
    def sum_by_year(self):
        """ Prints summary of transactions by year """
        return self.run_query_sum_by_year("""SELECT strftime('%Y', date) as year, category,
        COUNT(amount), SUM(amount) FROM transactions GROUP BY year;""", ())

    #based on the category return some data
    def sum_by_category(self):
        """ Prints summary of transactions by category """
        return self.run_query_sum_by_category("""SELECT category, date, COUNT(amount), SUM(amount)
        FROM transactions GROUP BY category;""", ())


######################Shaithea#########################
    # deletes a transaction
    def delete_transaction(self, item_number):
        """ Deletes a transaction of choice  """
        return self.run_query("DELETE FROM transactions WHERE id = ?;", (item_number,))

    # modifies the category of a transaction
    def modify_category(self, item_number, new_name):
        """ Modifies a category of choice  """
        return self.run_query("UPDATE categories SET name = ? WHERE id = ?;",
                              (new_name, item_number))
