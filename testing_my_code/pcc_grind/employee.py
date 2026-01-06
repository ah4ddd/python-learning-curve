class Employee:

    def __init__(self, first_name, last_name, annual_salary=0):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def get_raise(self,salary_raise=0):
        if salary_raise:
            self.annual_salary += salary_raise
        else:
            self.annual_salary += 5000

        return self.annual_salary

