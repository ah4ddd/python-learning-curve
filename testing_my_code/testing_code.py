from name_function import get_full_name

def test_first_last_name():
    """Does 'Ahad Khan' work?"""
    full_name = get_full_name('Ahad', 'Khan')
    assert full_name == 'Ahad Khan'
