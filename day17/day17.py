class Employee:
    def __init__(self, name, age, salary):
        self.nama = name
        self.umur = age
        self.gaji = salary
    
    def set_name(self, name):
        self.nama = name

    def set_age(self, age):
        self.umur = age

    def set_salary(self, salary):  # Corrected method name
        self.gaji = salary

    def get_name(self):
        return self.nama
    
    def get_age(self):
        return self.umur
    
    def get_salary(self):
        return self.gaji
    
def update_employee(employee):
    name = input("Masukkan nama: ")
    age = int(input("Masukkan umur: "))
    salary = float(input("Masukkan gaji: "))

    employee.set_name(name)
    employee.set_age(age)
    employee.set_salary(salary)

employee = Employee("", 0, 0)
update_employee(employee)

print("\nUpdate Employee Info: ")
print("Employee Name:", employee.get_name())
print("Employee Age: ", employee.get_age())
print("Employee Salary: ", employee.get_salary())