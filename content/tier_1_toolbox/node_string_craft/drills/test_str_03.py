import pytest
import active_lab

def test_replace_student_name():
    assert active_lab.replace_student_name("Hello Leonidas") == "Hello Justin"
    assert active_lab.replace_student_name("Leonidas is coding") == "Justin is coding"
