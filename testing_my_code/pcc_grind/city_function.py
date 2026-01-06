def capital_and_country(capital, country, population=''):
    if population:
        return f"{capital} {country} Total Population = {population}"
    else:
        return f"{capital} {country}"
