import payroll.payrollsystem as pr
import payroll.employees
import payroll.productivity

manager = payroll.employees.Manager(1, 'Mary Poppins', 3000)
secretary = payroll.employees.Secretary(2, 'John Smith', 1500)
sales_guy = payroll.employees.SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worker = payroll.employees.FactoryWorker(4, 'Jane Doe', 40, 15)
temporary_secretary = payroll.employees.TemporarySecretary(5, 'Robin Williams', 40, 9)

employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
    temporary_secretary,
]

productivity_system = payroll.productivity.Productivity()
productivity_system.track(employees, 40)
payroll_system = pr.Payroll()
payroll_system.calculate_payroll(employees)