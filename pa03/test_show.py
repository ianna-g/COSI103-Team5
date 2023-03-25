import pytest
from transaction import *

def test_show_transaction():
    expected = "[]"
    t_trans = Transaction("abc123")
    assert t_trans.show_transactions().__str__() == expected
    t_trans.add_transaction({ 'amount': 10, 'category': 1, 'date': '2023-03-25', 'description': 'testing123' })
    expected = "[{'item #': 1, 'amount': 10.0, 'category': 1, 'date': '2023-03-25', 'description': 'testing123'}]"
    assert t_trans.show_transactions().__str__() == expected