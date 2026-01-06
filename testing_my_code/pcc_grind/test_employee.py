import pytest
from employee import Employee


@pytest.fixture
def employee_with_salary():
    return Employee('Ahad', 'Kin', 256000)


def test_get_default_raise(employee_with_salary):
    result = employee_with_salary.get_raise()

    assert result == 261000
    assert employee_with_salary.annual_salary == 261000


def test_get_custom_raise(employee_with_salary):
    result = employee_with_salary.get_raise(44000)

    assert result == 300000
    assert employee_with_salary.annual_salary == 300000


def test_get_raise_mutates_state(employee_with_salary):
    employee_with_salary.get_raise()
    employee_with_salary.get_raise()

    assert employee_with_salary.annual_salary == 266000
