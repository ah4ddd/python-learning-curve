import pytest
from employee import Employee

@pytest.fixture
def employee():
    salary_raise = Employee('Ahad', 'Kin', 256000)
    return salary_raise

def test_get_default_raise(employee):
    new_salary = employee.get_raise()
    assert new_salary == 261000
    assert employee.annual_salary == 261000

def test_custom_raise(employee):
    new_salary = employee.get_raise(44000)
    assert new_salary == 300000
    assert employee.annual_salary == 300000
