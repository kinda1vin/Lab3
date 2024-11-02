import employee_info

employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
]

def test_get_employees_by_age_range():
    demo = employee_info.get_employees_by_age_range(30, 40)
    assert (demo == [{'name': 'Chloe', 'age': 35, 'department': 'Engineering', 'salary': 70000},
                    {'name': 'Mike', 'age': 32, 'department': 'Engineering', 'salary': 65000}] )
    
def test_calculate_average_salary():
    demo = employee_info.calculate_average_salary()
    assert (demo == 60166.666666666664)

def test_get_employees_by_dept():
    demo = employee_info.get_employees_by_dept('Sales')
    assert (demo == [{'name': 'John', 'age': 30, 'department': 'Sales', 'salary': 50000},
                    {'name': 'Peter', 'age': 40, 'department': 'Sales', 'salary': 60000}] )