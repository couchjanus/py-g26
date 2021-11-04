import payroll.payrollsystem as pr
import payroll.employees
import payroll.productivity

# solary_employee = pr.SalaryEmployee(1, 'John Smith', 1500)
# hourly_employee = pr.HourlyEmployee(2, 'John Doe', 40, 15)
# commission_employee = pr.CommissionEmployee(3, 'Mary Ann', 1000, 255)

manager = payroll.employees.Manager(1, 'John Smith', 5000)
secretary = payroll.employees.Secretary(2, 'John Doe', 1500)
saler = payroll.employees.SalesPerson(3, 'Mary Ann', 1000, 255)
worker = payroll.employees.FactoryWorker(4, 'Mary Poppins', 30, 55)

employees = [manager, secretary, saler, worker]
productivity_system = payroll.productivity.Productivity()
productivity_system.track(employees, 40)
payroll_system = pr.Payroll()
payroll_system.calculate_payroll(employees)