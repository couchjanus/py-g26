class Payroll:
    def calculate_payroll(self, employees):
        print('Calculateing Payroll')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}')
            print()
            
            
class SalaryPolicy:
    def __init__(self, weekly_salary) -> None:
        self.weekly_salary = weekly_salary
    
    def calculate_payroll(self):
        return self.weekly_salary

class HourlyPolicy:
    def __init__(self, hours_worked, hour_rate) -> None:

        self.hours_worked = hours_worked
        self.hour_rate = hour_rate
        
    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate
    
class CommissionPolicy(SalaryPolicy):
    def __init__(self, weekly_salary, commission) -> None:
        super().__init__(weekly_salary)
        self.commission = commission
            
    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return self.commission + fixed