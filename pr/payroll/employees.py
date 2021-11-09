from abc import ABC, abstractmethod 

from payroll.productivity import(
    ManagerRole,
    SecretaryRole,
    SalesRole,
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
    def __init__(self, id, name, weekly_salary):
        SalaryPolicy.__init__(self, weekly_salary)
        super().__init__(id, name)

class SalesPerson(Employee, SalesRole, CommissionPolicy):
    def __init__(self, id, name, weekly_salary, commission):
        CommissionPolicy.__init__(self, weekly_salary, commission)
        super().__init__(id, name)

class FactoryWorker(Employee, FactoryRole, HourlyPolicy):
    def __init__(self, id, name, hours_worked, hour_rate):
        HourlyPolicy.__init__(self, hours_worked, hour_rate)
        super().__init__(id, name)

class TemporarySecretary(Employee, SecretaryRole, HourlyPolicy):
    def __init__(self, id, name, hours_worked, hour_rate):
        HourlyPolicy.__init__(self, hours_worked, hour_rate)
        super().__init__(id, name)