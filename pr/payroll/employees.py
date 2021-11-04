from abc import ABC, abstractmethod 

from payroll.productivity import(
    ManagerRole,
    SecretaryRole,
    SalerRole,
    FactoryRole
)
from payroll.payrollsystem import(
    SalaryPolicy,
    HourlyPolicy,
    CommissionPolicy
)
class Employee():
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
    
class Manager(Employee, ManagerRole, SalaryPolicy):
    def __init__(self, id, name, weekly_salary) -> None:
        SalaryPolicy.__init__(self, weekly_salary)
        super().__init__(id, name)
    
    
class Secretary(Employee, SecretaryRole, SalaryPolicy):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours doing office paperwork.')
            
class SalesPerson(CommissionEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours on the phone.')
            
class FactoryWorker(HourlyEmployee):
    def work(self, hours):
        print(f'{self.name} manufactures gadgets for {hours} hours.')
        
class TemporarySecretary(Secretary, HourlyEmployee):
    def __init__(self, id, name, hours_worked, hour_rate) -> None:
        HourlyEmployee.__init__(id, name, hours_worked, hour_rate)
    def calculate_payroll(self):
        return HourlyEmployee.calculate_payroll(self)