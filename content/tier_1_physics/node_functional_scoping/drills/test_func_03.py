import pytest
import active_lab

def test_default_args():
    list1 = active_lab.add_token_safe('hello')
    assert list1 == ['hello']
    
    list2 = active_lab.add_token_safe('world')
    assert list2 == ['world'], "list2 contained 'hello'. You fell into the mutable default argument trap!"
