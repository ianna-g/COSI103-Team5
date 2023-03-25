# test for each method in Transaction class
from transaction import *
t_trans = Transaction("testdatabase123")
print(t_trans.show_transactions())
t_trans.add_transaction({ 'amount': 10, 'category': 1, 'date': '2023-03-25', 'description': 'testing123' })
print(t_trans.show_transactions())