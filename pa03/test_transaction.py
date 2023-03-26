# test for each method in Transaction class
from transaction import *
t_trans = Transaction("testdatabase123")
print(t_trans.show_transactions())
t_trans.add_transaction({ 'amount': 10, 'category': 1, 'date': '2023-03-25', 'description': 'testing123' })
print(t_trans.show_transactions())

def test_delete_transaction(self):
    self.transaction.add_transaction(1, 20, "Test", "2020-01-01", "Testing transaction")
    self.transaction.delete_transaction(1)
    self.assertEqual(self.transaction.show_transactions(), [])

def test_modify_category(self):
    self.transaction.add_transaction(1, 20, "Test", "2020-01-01", "Testing transaction")   
    self.transaction.modify_category("Test", "Modified")
    expected = [(1, 20, "Modified", "2020-01-01", "Testing transaction")]
    actual = self.transaction.show_transactions()
    self.assertEqual(actual, expected)
    
def test_sum_by_date(self):
    self.transaction.add_transaction(30, 2,  "2010-03-01", "Items for picnic")  
    self.transaction.add_transaction(4, 1,  "2023-05-24", "snack item")  
    expected = "[{'date': '2010-03-01', 'category': 2,  'COUNT(amount)': 1, 'SUM(amount)': 30.0}, {'date': '2023-05-24', 'category': 1,  'COUNT(amount)': 1, 'SUM(amount)': 4.0}]"
    assert self.transaction.test_sum_by_date().__str__() == expected

def test_sum_by_month(self):
    self.transaction.add_transaction(30, 2,  "2010-03-01", "Items for picnic")  
    self.transaction.add_transaction(50, 2,  "2010-03-01", "Items for picnic")  
    self.transaction.add_transaction(4, 1,  "2023-05-24", "snack item")  
    expected = "[{'month': 03, 'category': 2, 'COUNT(amount)': 2, 'SUM(amount)': 80.0}, {'month': 05, 'category': 1, 'COUNT(amount)': 1, 'SUM(amount)': 4.0}]"
    assert self.transaction.test_sum_by_month().__str__() == expected

def test_sum_by_year(self):
    self.transaction.add_transaction(30, 2,  "2010-03-01", "Items for picnic")  
    self.transaction.add_transaction(50, 2,  "2010-09-01", "Items for outing")  
    self.transaction.add_transaction(94, 1,  "2023-12-24", "snack item")  
    self.transaction.add_transaction(40, 1,  "2023-05-20", "snack item")  
    self.transaction.add_transaction(200, 1,  "2023-07-24", "snack item")  
    expected = "[{'year': 2010, 'category': 2, 'COUNT(amount)': 2,  'SUM(amount)': 80.0}, {'item #': 2, ''year': 2023, 'category': 1, 'COUNT(amount)': 3,  'SUM(amount)': 334.0}]"
    assert self.transaction.test_sum_by_year().__str__() == expected

def test_sum_by_category(self):
    self.transaction.add_transaction(30, 2,  "2010-03-01", "Items for picnic")  
    self.transaction.add_transaction(4, 1,  "2023-05-24", "snack item")  
    expected = "[{'category': 2, 'date': '2010-03-01', 'COUNT(amount)': 1, 'SUM(amount)': 30.0}, {'category': 1, 'date': '2023-05-24', 'COUNT(amount)': 1, 'SUM(amount)': 4.0}]"
    assert self.transaction.test_sum_by_category().__str__() == expected



