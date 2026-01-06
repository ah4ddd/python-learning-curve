from city_function import capital_and_country

def test_capital_and_country():
    results = capital_and_country('Stockholm', 'Sweden', '10.7 million')
    assert results == 'Stockholm Sweden Total Population = 10.7 million'
