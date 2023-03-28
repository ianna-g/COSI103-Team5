"""class written by Ianna Gilbert. tests summarize commands"""
import transaction




my_dict = {"amount":30, "category" : 2,  "date": "2010-03-01", "description": "Items for picnic"}
my_dict1 = {"amount":50, "category" : 2,  "date": "2010-03-01", "description": "Items for picnic"}
my_dict2 = {"amount":4, "category" : 1,  "date": "2023-05-24", "description": "snacks"}
my_dict3 = {"amount":94, "category" : 1,  "date": "2023-12-24", "description": "snacks"}
my_dict4 = {"amount":200, "category" : 1,  "date": "2023-07-12", "description": "snacks"}
def test_sum_by_date():
    """tests sum_by_date()"""
    trans = transaction.Transaction("Test70")
    trans.add_transaction(my_dict)
    trans.add_transaction(my_dict2)
    expected = [{'date': '2010-03-01', 'category': 2,
                 '# of transactions': 1, 'sum of transaction amounts': 30.0},
                 {'date': '2023-05-24', 'category': 1, '# of transactions': 1,
                  'sum of transaction amounts': 4.0}]
    assert trans.sum_by_date() == expected

def test_sum_by_month():
    """tests sum_by_month"""
    trans = transaction.Transaction("Test71")
    trans.add_transaction(my_dict)
    trans.add_transaction(my_dict1)
    trans.add_transaction(my_dict2)
    expected = [{'month': '03', 'category': 2, '# of transactions': 2,
                 'sum of transaction amounts': 80.0},
                 {'month': '05', 'category': 1, '# of transactions': 1,
                  'sum of transaction amounts': 4.0}]
    assert trans.sum_by_month() == expected

def test_sum_by_year():
    """tests sum_by_year"""
    trans = transaction.Transaction("Test72")
    trans.add_transaction(my_dict)
    trans.add_transaction(my_dict1)
    trans.add_transaction(my_dict2)
    trans.add_transaction(my_dict3)
    trans.add_transaction(my_dict4)
    expected = [{'year': '2010', 'category': 2, '# of transactions': 2,
                 'sum of transaction amounts': 80.0},
                 {'year': '2023', 'category': 1, '# of transactions': 3,
                  'sum of transaction amounts': 298.0}]
    assert trans.sum_by_year() == expected

def test_sum_by_category():
    """tests sum_by_cater=gory"""
    trans = transaction.Transaction("Test73")
    trans.add_transaction(my_dict)
    trans.add_transaction(my_dict1)
    trans.add_transaction(my_dict2)
    expected = [ {'category': 1, 'date': '2023-05-24', '# of transactions': 1,
                  'sum of transaction amounts': 4.0},
                  {'category': 2, 'date': '2010-03-01', '# of transactions': 2,
                   'sum of transaction amounts': 80.0}]
    assert trans.sum_by_category() == expected
