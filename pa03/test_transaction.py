# test for each method in Transaction class
from transaction import *
t_trans = Transaction("testdatabase123")
print(t_trans.show_transactions())
t_trans.add_transaction({ 'amount': 10, 'category': 1, 'date': '2023-03-25', 'description': 'testing123' })
print(t_trans.show_transactions())

def test_delete_transaction(self)
    self.transaction.add_transaction(1, 20, "Test", "2020-01-01", "Testing transaction")
    self.transaction.delete_transaction(1)
    self.assertEqual(self.transaction.show_transactions(), [])

def test_modify_category(self)
    self.transaction.add_transaction(1, 20, "Test", "2020-01-01", "Testing transaction")   
    self.transaction.modify_category("Test", "Modified")
    expected = [(1, 20, "Modified", "2020-01-01", "Testing transaction")]
    actual = self.transaction.show_transactions()
    self.assertEqual(actual, expected)