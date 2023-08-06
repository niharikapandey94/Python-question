employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
emp1={
    'name':employees[0]
}
emp2={
    'name':employees[1]
}
emp1.update(defaults)
print(emp1)
emp2.update(defaults)
print(emp2)
